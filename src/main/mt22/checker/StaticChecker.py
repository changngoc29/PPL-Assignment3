from Visitor import Visitor
from AST import *
from StaticError import *


class Utils:
    def lookup(name, o):
        for scope in o:
            if name in scope:
                return scope[name]
        return None

    def import_special_func():
        special_dict = {
            "readInteger": FunctionType(IntegerType(), [], None, {}, True),
            "printInteger": FunctionType(VoidType(), [IntegerType()], None, {}, True),
            "readFloat": FunctionType(FloatType(), [], None, {}, True),
            "writeFloat": FunctionType(VoidType(), [FloatType()], None, {}, True),
            "readBoolean": FunctionType(BooleanType(), [], None, {}, True),
            "printBoolean": FunctionType(VoidType(), [BooleanType()], None, {}, True),
            "readString": FunctionType(StringType(), [], None, {}, True),
            "printString": FunctionType(VoidType(), [StringType()], None, {}, True),
            "super": FunctionType(VoidType(), [], None, {}, True),
            "preventDefault": FunctionType(VoidType(), [], None, {}, True),
        }
        return special_dict

    def show_dict(o):
        print("--------------------Start")
        for scope in o:
            print("<<<")
            for key, value in scope.items():
                print(key, value)
            print(">>>")
        print("--------------------End")


class FunctionType:
    def __init__(
        self, return_typ, params, inherit, inherit_params=None, is_declared=False
    ):
        self.return_typ = return_typ
        self.params = params
        self.inherit = inherit
        self.inherit_params = inherit_params
        self.is_declared = is_declared

    def __str__(self):
        return "FunctionType({}, {}, {}, {})".format(
            str(self.return_typ),
            str(self.params),
            str(self.inherit),
            str(self.inherit_params),
        )


class StaticChecker(Visitor):
    is_in_loop = False
    curr_func = None

    def __init__(self, ast):
        self.ast = ast

    def check(self):
        return self.visitProgram(self.ast, [{}])

    def handle_block(self, ctx, o, param_dict=None, inherited=None, func_name=None):
        if param_dict:
            local_o = param_dict + o
        else:
            local_o = [{}] + o
        if inherited:
            if len(inherited.params) != 0:
                if len(ctx.body) == 0:
                    raise InvalidStatementInFunction(func_name)
                else:
                    first_stmt = ctx.body[0]
                    if type(first_stmt) is not CallStmt:
                        raise InvalidStatementInFunction(func_name)
                    if type(first_stmt) is CallStmt and len(inherited.params) != 0:
                        if first_stmt.name not in ["preventDefault", "super"]:
                            raise InvalidStatementInFunction(func_name)
                        if first_stmt.name == "super":
                            args_typs = [
                                self.visit(arg, local_o) for arg in first_stmt.args
                            ]
                            if len(args_typs) != len(inherited.params):
                                raise InvalidStatementInFunction(func_name)
                            for i in range(len(args_typs)):
                                if type(args_typs[i]) is not type(inherited.params[i]):
                                    raise InvalidStatementInFunction(func_name)

        stmtlist = self.visit(ctx, local_o)
        con_br = self.check_continue_break(stmtlist)
        if not StaticChecker.is_in_loop and con_br:
            raise MustInLoop(con_br)
        o = local_o[1:]
        return stmtlist

    def handle_return_stmt(self, typ, return_stmt):
        if type(StaticChecker.curr_func.return_typ) is AutoType:
            StaticChecker.curr_func.return_typ = typ
        elif type(typ) is not type(StaticChecker.curr_func.return_typ):
            raise TypeMismatchInStatement(return_stmt)

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
                type(rtyp) is IntegerType and type(ltyp) is IntegerType
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
        if type(typ) is FunctionType:
            raise TypeMismatchInExpression(ctx)
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
        root_typ = self.visit(ctx.explist[0], o)

        for i in range(1, len(ctx.explist)):
            exp_typ = self.visit(ctx.explist[i], o)
            # check type in explist
            if type(root_typ) is not type(exp_typ):
                raise IllegalArrayLiteral(ctx)
            # check with ArrayType
            if type(root_typ) is ArrayType:
                # check typ and len of ArrayType
                if type(root_typ.typ) is not type(exp_typ.typ):
                    raise IllegalArrayLiteral(ctx)
                if len(root_typ.dimensions) != len(exp_typ.dimensions):
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
            if type(typ.params[i]) is AutoType:
                typ.params[i] = args[i]
            elif type(args[i]) is not type(typ.params[i]):
                if not (
                    type(args[i]) is IntegerType and type(typ.params[i]) is FloatType
                ):
                    raise TypeMismatchInExpression(ctx)
        return typ.return_typ

    def visitAssignStmt(self, ctx, o):
        rtyp = self.visit(ctx.rhs, o)
        ltyp = self.visit(ctx.lhs, o)
        if type(ltyp) in [FunctionType, ArrayType]:
            raise TypeMismatchInStatement(ctx)

        if type(rtyp) is not AutoType:
            if type(rtyp) is not type(ltyp):
                if type(ltyp) is not FloatType or type(rtyp) is not IntegerType:
                    raise TypeMismatchInStatement(ctx)
        else:
            rtyp = Utils.lookup(ctx.rhs.name, o)
            rtyp.return_typ = ltyp
            if type(rtyp.return_typ) is not type(ltyp):
                if (
                    type(ltyp) is not FloatType
                    or type(rtyp.return_typ) is not IntegerType
                ):
                    raise TypeMismatchInStatement(ctx)
        return ltyp

    def visitBlockStmt(self, ctx, o):
        return_count = 0
        for stmt in ctx.body:
            if type(stmt) is ReturnStmt and return_count == 0:
                return_count += 1
                typ = self.visit(stmt, o)
                self.handle_return_stmt(typ, stmt)

            else:
                self.visit(stmt, o)
        return ctx.body

    def visitIfStmt(self, ctx, o):
        cond_typ = self.visit(ctx.cond, o)
        if type(cond_typ) is not BooleanType:
            raise TypeMismatchInStatement(ctx)

        if type(ctx.tstmt) is BlockStmt:
            self.handle_block(ctx.tstmt, o)
        elif type(ctx.tstmt) is ReturnStmt:
            typ = self.visit(ctx.tstmt, o)
            self.handle_return_stmt(typ, ctx.tstmt)

        if type(ctx.fstmt) is BlockStmt:
            self.handle_block(ctx.fstmt, o)
        elif type(ctx.fstmt) is ReturnStmt:
            typ = self.visit(ctx.fstmt, o)
            self.handle_return_stmt(typ, ctx.fstmt)

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
        if type(ctx.stmt) is ReturnStmt:
            typ = self.visit(ctx.stmt, o)
            self.handle_return_stmt(typ, ctx.stmt)
        elif type(ctx.stmt) is BlockStmt:
            StaticChecker.is_in_loop = True
            self.handle_block(ctx.stmt, o)
            StaticChecker.is_in_loop = False

    def visitWhileStmt(self, ctx, o):
        cond_typ = self.visit(ctx.cond, o)
        if type(cond_typ) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        if type(ctx.stmt) is ReturnStmt:
            typ = self.visit(ctx.stmt, o)
            self.handle_return_stmt(typ, ctx.stmt)
        elif type(ctx.stmt) is BlockStmt:
            StaticChecker.is_in_loop = True
            self.handle_block(ctx.stmt, o)
            StaticChecker.is_in_loop = False

    def visitDoWhileStmt(self, ctx, o):
        cond_typ = self.visit(ctx.cond, o)
        if type(cond_typ) is not BooleanType:
            raise TypeMismatchInStatement(ctx)
        StaticChecker.is_in_loop = True
        self.handle_block(ctx.stmt, o)
        StaticChecker.is_in_loop = False

    def visitBreakStmt(self, ctx, o):
        return BreakStmt()

    def visitContinueStmt(self, ctx, o):
        return ContinueStmt()

    def visitReturnStmt(self, ctx, o):
        return_typ = self.visit(ctx.expr, o)
        return return_typ

    def visitCallStmt(self, ctx, o):
        typ = Utils.lookup(ctx.name, o)
        if type(typ) is not FunctionType:
            raise Undeclared(Function(), ctx.name)
        args = [self.visit(arg, o) for arg in ctx.args]
        if ctx.name == "super":
            return typ.return_typ
        if len(args) != len(typ.params):
            raise TypeMismatchInStatement(ctx)
        for i in range(len(args)):
            if type(args[i]) is not type(typ.params[i]):
                raise TypeMismatchInStatement(ctx)
        return typ.return_typ

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
            elif type(init_typ) is AutoType:
                Utils.lookup(ctx.init.name, o).return_typ = ctx.typ
            # check type between ctx and init
            elif type(init_typ) is not type(ctx.typ):
                if not (type(ctx.typ) is FloatType and type(init_typ) is IntegerType):
                    raise TypeMismatchInVarDecl(ctx)
            # check for case ArrayType
            elif type(init_typ) is ArrayType:
                # check type + length of ctx array and init array
                if type(ctx.typ.typ) is not type(init_typ.typ):
                    if type(ctx.typ.typ) is AutoType:
                        ctx.typ.typ = init_typ.typ
                    else:
                        raise TypeMismatchInVarDecl(ctx)
                if len(ctx.typ.dimensions) != len(init_typ.dimensions):
                    raise TypeMismatchInVarDecl(ctx)
                # check dimensions between init and ctx
                for i in range(len(ctx.typ.dimensions)):
                    if ctx.typ.dimensions[i] != init_typ.dimensions[i]:
                        raise TypeMismatchInVarDecl(ctx)
        o[0][ctx.name] = ctx.typ

    def visitParamDecl(self, ctx, o):
        pass

    def visitFuncDecl(self, ctx, o):
        # check name
        if o[0][ctx.name].is_declared:
            raise Redeclared(Function(), ctx.name)

        # inherit
        inherit_params = None
        inherited = None
        if ctx.inherit:
            inherited = Utils.lookup(ctx.inherit, o)
            if not inherited:
                raise Undeclared(Function(), ctx.inherit)
            inherit_params = inherited.inherit_params
        # check params
        local_dict = [{}]
        for param in ctx.params:
            if inherit_params:
                if param.name in inherit_params:
                    raise Invalid(Parameter(), param.name)
            if param.name in local_dict[0]:
                raise Redeclared(Parameter(), param.name)
            local_dict[0][param.name] = param.typ
        # merge inherit_params and local_dict
        if inherit_params:
            local_dict[0].update(inherit_params)
        StaticChecker.curr_func = o[0][ctx.name]
        self.handle_block(ctx.body, o, local_dict, inherited, ctx.name)
        StaticChecker.curr_func = None
        o[0][ctx.name].is_declared = True

    def visitProgram(self, ctx, o):
        o.append(Utils.import_special_func())
        entry_point = False
        for decl in ctx.decls:
            # record func basically
            if type(decl) is FuncDecl:
                param_types = []
                inherit_dict = {}
                for param in decl.params:
                    param_types.append(param.typ)
                    if param.inherit:
                        inherit_dict[param.name] = param.typ
                if len(inherit_dict) != 0:
                    o[0][decl.name] = FunctionType(
                        decl.return_type, param_types, decl.inherit, inherit_dict
                    )
                else:
                    o[0][decl.name] = FunctionType(
                        decl.return_type, param_types, decl.inherit
                    )
            # check if main() existed
            if (
                (type(decl) is FuncDecl)
                and (decl.name == "main")
                and (type(decl.return_type) is VoidType)
                and (len(decl.params) == 0)
            ):
                entry_point = True
        [self.visit(decl, o) for decl in ctx.decls]
        if not entry_point:
            raise NoEntryPoint()
        Utils.show_dict(o)
        return [str(ctx)]
