from Visitor import Visitor
from AST import *
from StaticError import *


class Utils:
    def lookup(name, o):
        for scope in o:
            if name in scope:
                return scope[name]
        return None

    def show_dict(o):
        for scope in o:
            print("<<<")
            for key, value in scope.items():
                print(key, value)
            print(">>>")


class FunctionType:
    def __init__(self, return_typ, params, inherit):
        self.return_typ = return_typ
        self.params = params
        self.inherit = inherit

    def __str__(self):
        return "FunctionType({}, {}, {})".format(
            str(self.return_typ), str(self.params), str(self.inherit)
        )


class StaticChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visitProgram(self.ast, [{}])

    def handle_block(self, case, ctx, o, params=None):
        local_o = [{}] + o
        stmtlist = self.visit(ctx, local_o)
        con_br = self.check_continue_break(stmtlist)
        if case in ["IF"] and con_br:
            raise MustInLoop(con_br)
        o = local_o[1:]
        return stmtlist

    def check_continue_break(self, liststmt):
        for stmt in liststmt:
            if type(stmt) is BreakStmt:
                return stmt
            if type(stmt) is ContinueStmt:
                return stmt
        return None

    def visitIntegerType(self, ctx, o):
        pass

    def visitFloatType(self, ctx, o):
        pass

    def visitBooleanType(self, ctx, o):
        pass

    def visitStringType(self, ctx, o):
        pass

    def visitArrayType(self, ctx, o):
        pass

    def visitAutoType(self, ctx, o):
        pass

    def visitVoidType(self, ctx, o):
        pass

    def visitBinExpr(self, ctx, o):
        rtyp = self.visit(ctx.right, o)
        ltyp = self.visit(ctx.left, o)

        if ctx.op in ["+", "-", "*", "/"]:
            if type(rtyp) is IntegerType and type(ltyp) is IntegerType:
                return IntegerType()
            elif type(rtyp) is IntegerType and type(ltyp) is FloatType:
                return FloatType()
            elif type(rtyp) is FloatType and type(ltyp) is IntegerType:
                return FloatType()
            elif type(rtyp) is FloatType and type(ltyp) is FloatType:
                return FloatType()

        elif ctx.op == "%":
            if type(rtyp) is IntegerType and type(ltyp) is IntegerType:
                return IntegerType()

        elif ctx.op in ["||", "&&"]:
            if type(rtyp) is BooleanType and type(ltyp) is BooleanType:
                return BooleanType()

        elif ctx.op == "::":
            if type(rtyp) is StringType and type(ltyp) is StringType:
                return StringType()

        elif ctx.op in ["==", "!="]:
            if (type(rtyp) is BooleanType and type(ltyp) is BooleanType) or (
                type(rtyp) is IntType and type(ltyp) is IntType
            ):
                return BooleanType()

        elif ctx.op in ["<", ">", "<=", ">="]:
            if (type(rtyp) is FloatType or type(rtyp) is IntegerType) and (
                type(ltyp) is FloatType or type(ltyp) is IntegerType
            ):
                return BooleanType()
        raise TypeMismatchInExpression(ctx)

    def visitUnExpr(self, ctx, o):
        typ = self.visit(ctx.val, o)
        if ctx.op == "-":
            if type(typ) is IntegerType or type(typ) is FloatType:
                return typ

        elif ctx.op == "!":
            if type(typ) is BooleanType:
                return typ

        else:
            raise TypeMismatchInExpression(ctx)

    def visitId(self, ctx, o):
        typ = Utils.lookup(ctx.name, o)
        if not typ:
            raise Undeclared(Identifier(), ctx.name)
        return typ

    def visitArrayCell(self, ctx, o):
        typ = Utils.lookup(ctx.name, o)
        if not typ:
            raise Undeclared(Identifier(), ctx.name)
        # if cannot find the name in the "o" (not solved)
        if not typ:
            raise Undeclared(Identifier(), ctx.name)
        # check if the typ is not ArrayType
        if type(typ) is not ArrayType:
            raise TypeMismatchInExpression(ctx)
        # check len(cell)
        if len(ctx.cell) > len(typ.dimensions):
            raise TypeMismatchInExpression(ctx)
        for i in range(len(ctx.cell)):
            expr_typ = self.visit(ctx.cell[i], o)
            # check cell is integer list
            if type(expr_typ) is not IntegerType:
                raise TypeMismatchInExpression(ctx)
            # check range NOT CHECKED
        # return type: not ArrayType
        if len(ctx.cell) == len(typ.dimensions):
            return typ.typ
        # return type: ArrayType
        if len(ctx.cell) < len(typ.dimensions):
            return ArrayType(typ.dimensions[len(ctx.cell) :], typ.typ)

    def visitIntegerLit(self, ctx, o):
        return IntegerType()

    def visitFloatLit(self, ctx, o):
        return FloatType()

    def visitStringLit(self, ctx, o):
        return StringType()

    def visitBooleanLit(self, ctx, o):
        return BooleanType()

    def visitArrayLit(self, ctx, o):
        dimensions = [len(ctx.explist)]
        # check for empty array (not need)
        if len(ctx.explist) == 0:
            return ArrayType([0], AutoType())
        root_typ = self.visit(ctx.explist[0], o)

        for i in range(1, len(ctx.explist)):
            exp_typ = self.visit(ctx.explist[i], o)
            # check type in explist
            if type(root_typ) is not type(exp_typ):
                raise IllegalArrayLiteral(ctx)
            # check with ArrayType
            if type(root_typ) is ArrayType:
                # check typ and len of ArrayType
                if type(root_typ.typ) is not type(exp_typ.typ) or len(
                    root_typ.dimensions
                ) != len(exp_typ.dimensions):
                    raise IllegalArrayLiteral(ctx)
                # check num of element in ArrayType
                for i in range(len(root_typ.dimensions)):
                    if root_typ.dimensions[i] != exp_typ.dimensions[i]:
                        raise IllegalArrayLiteral(ctx)
        if type(root_typ) is ArrayType:
            dimensions += root_typ.dimensions
        return_typ = root_typ.typ if type(root_typ) is ArrayType else root_typ
        return ArrayType(dimensions, return_typ)

    def visitFuncCall(self, ctx, o):
        typ = Utils.lookup(ctx.name, o)
        if type(typ) is not FunctionType:
            raise Undeclared(Function(), ctx.name)
        if type(typ.return_typ) is VoidType:
            raise TypeMismatchInExpression(ctx)
        args = [self.visit(arg, o) for arg in ctx.args]
        if len(args) != len(typ.params):
            raise TypeMismatchInExpression(ctx)
        for i in range(len(args)):
            if type(args[i]) is not type(typ.params[i]):
                raise TypeMismatchInExpression(ctx)
        return typ.return_typ

    def visitAssignStmt(self, ctx, o):
        rtyp = self.visit(ctx.rhs, o)
        ltyp = self.visit(ctx.lhs, o)
        if type(ltyp) in [FunctionType, ArrayType]:
            raise TypeMismatchInStatement(ctx)

        if type(rtyp) is not FunctionType:
            if type(rtyp) is not type(ltyp):
                raise TypeMismatchInStatement(ctx)
        else:
            if type(rtyp.return_typ) is AutoType:
                rtyp.return_typ = ltyp
            elif type(rtyp.return_typ) is not type(ltyp):
                raise TypeMismatchInStatement(ctx)
        return ltyp

    def visitBlockStmt(self, ctx, o):
        # inherit NOT DONE
        [self.visit(x, o) for x in ctx.body]
        return ctx.body

    def visitIfStmt(self, ctx, o):
        cond_typ = self.visit(ctx.cond, o)
        if type(cond_typ) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        if type(ctx.tstmt) is BlockStmt:
            self.handle_block("IF", ctx.tstmt, o)
        if type(ctx.fstmt) is BlockStmt:
            self.handle_block("IF", ctx.fstmt, o)

    def visitForStmt(self, ctx, o):
        init_typ = self.visit(ctx.init, o)
        cond_typ = self.visit(ctx.cond, o)
        upd_typ = self.visit(ctx.upd, o)
        if (
            type(init_typ) is not IntegerType
            or type(cond_typ) is not BooleanType
            or type(upd_typ) is not IntegerType
        ):
            raise TypeMismatchInStatement(ctx)
        if type(ctx.stmt) is BlockStmt:
            self.handle_block("FOR", ctx.stmt, o)

    def visitWhileStmt(self, ctx, o):
        cond_typ = self.visit(ctx.cond, o)
        if type(cond_typ) is not Boolean:
            raise TypeMismatchInStatement(ctx)
        if type(ctx.stmt) is BlockStmt:
            self.handle_block("WHILE", ctx.stmt, o)

    def visitDoWhileStmt(self, ctx, o):
        pass

    def visitBreakStmt(self, ctx, o):
        return BreakStmt()

    def visitContinueStmt(self, ctx, o):
        return ContinueStmt()

    def visitReturnStmt(self, ctx, o):
        pass

    def visitCallStmt(self, ctx, o):
        pass

    def visitVarDecl(self, ctx, o):
        if ctx.name in o[0]:
            raise Redeclared(Variable(), ctx.name)
        # check AutoType() have init() ?
        if (type(ctx.typ) is AutoType) and (not ctx.init):
            raise Invalid(Variable(), ctx.name)
        if ctx.init:
            init_typ = self.visit(ctx.init, o)
            if type(ctx.typ) is AutoType:
                ctx.typ = init_typ
            # check type between ctx and init
            elif type(init_typ) is not type(ctx.typ):
                raise TypeMismatchInVarDecl(ctx)
            # check for case ArrayType
            elif type(init_typ) is ArrayType:
                # check type + length of ctx array and init array
                if type(ctx.typ.typ) is not type(init_typ.typ) or len(
                    ctx.typ.dimensions
                ) != len(init_typ.dimensions):
                    raise TypeMismatchInVarDecl(ctx)
                # check dimensions between init and ctx
                for i in range(len(ctx.typ.dimensions)):
                    if ctx.typ.dimensions[i] != init_typ.dimensions[i]:
                        raise TypeMismatchInVarDecl(ctx)
        o[0][ctx.name] = ctx.typ

    def visitParamDecl(self, ctx, o):
        # inherit NOT CHECKED
        # out NOT CHECKED
        # check redeclared
        if ctx.name in o[0]:
            raise Redeclared(Parameter(), ctx.name)
        o[0][ctx.name] = ctx.typ
        return ctx.typ

    def visitFuncDecl(self, ctx, o):
        # check name
        if Utils.lookup(ctx.name, o):
            raise Redeclared(Function(), ctx.name)
        # inherit NOT CHECKED
        # auto return NOT CHECKED
        local_o = [{}] + o
        params = [self.visit(decl, local_o) for decl in ctx.params]
        self.visit(ctx.body, local_o)
        o = local_o[1:]
        o[0][ctx.name] = FunctionType(ctx.return_type, params, ctx.inherit)

    def visitProgram(self, ctx, o):
        entry_point = False
        for decl in ctx.decls:
            # check if main() existed
            if (
                (type(decl) is FuncDecl)
                and (decl.name == "main")
                and (type(decl.return_type) is VoidType)
                and (len(decl.params) == 0)
            ):
                entry_point = True
        if not entry_point:
            raise NoEntryPoint()
        [self.visit(decl, o) for decl in ctx.decls]
        return [str(ctx)]


# Notes:
# Functions inherit and invoke can be declared after its use (not done)
# Check inherit of function and handle inherit parameter (not done)
# When use a function as a variable -> type mismatch or undeclared ???
# auto function inference (done)
# inherit function first stmt (not done) ?
