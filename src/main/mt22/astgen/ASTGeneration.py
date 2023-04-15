from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *


class ASTGeneration(MT22Visitor):
    # program
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program(self.visit(ctx.decllist()))

    # decllist
    def visitDecllist(self, ctx: MT22Parser.DecllistContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.decl())
        return self.visit(ctx.decl()) + self.visit(ctx.decllist())

    # decl
    def visitDecl(self, ctx: MT22Parser.DeclContext):
        return self.visit(ctx.vardecl()) if ctx.vardecl() else self.visit(ctx.funcdecl())

    # vardecl
    def visitVardecl(self, ctx: MT22Parser.VardeclContext):
        return self.visit(ctx.vardeclnoinit()) if ctx.vardeclnoinit() else self.visit(ctx.vardeclinit())

    # vardeclnoinit
    def visitVardeclnoinit(self, ctx: MT22Parser.VardeclnoinitContext):
        return [VarDecl(x, self.visit(ctx.typ())) for x in self.visit(ctx.idlist())]

    # vardeclinit
    arrayIdVarDeclInit = []
    arrayExprVarDeclInit = []

    def visitVardeclinit(self, ctx: MT22Parser.VardeclinitContext):
        if ctx.typ():
            self.arrayIdVarDeclInit += [ctx.ID().getText()]
            self.arrayExprVarDeclInit += [self.visit(ctx.expr())]

            arrayIdVarDeclInit = self.arrayIdVarDeclInit
            arrayExprVarDeclInit = self.arrayExprVarDeclInit[::-1]

            assocArray = list(zip(arrayIdVarDeclInit, arrayExprVarDeclInit))

            self.arrayIdVarDeclInit.clear()
            self.arrayExprVarDeclInit.clear()

            return [VarDecl(x[0], self.visit(ctx.typ()), x[1]) for x in assocArray]
        self.arrayIdVarDeclInit += [ctx.ID().getText()]
        self.arrayExprVarDeclInit += [self.visit(ctx.expr())]
        return self.visit(ctx.vardeclinit())

    # funcdecl: ID COLON FUNCTION functyp LB paramlist RB (INHERIT ID)? blockstmt;
    def visitFuncdecl(self, ctx: MT22Parser.FuncdeclContext):
        if ctx.INHERIT():
            return [FuncDecl(ctx.ID(0).getText(), self.visit(ctx.functyp()), self.visit(ctx.paramlist()), ctx.ID(1).getText(), self.visit(ctx.blockstmt()))]
        return [FuncDecl(ctx.ID(0).getText(), self.visit(ctx.functyp()), self.visit(ctx.paramlist()), None, self.visit(ctx.blockstmt()))]

    # paramlist: params | ;
    def visitParamlist(self, ctx: MT22Parser.ParamlistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.params())

    # params: param CM params | param;
    def visitParams(self, ctx: MT22Parser.ParamsContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.param())]
        return [self.visit(ctx.param())] + self.visit(ctx.params())

    # param: INHERIT? OUT? ID COLON typ;
    def visitParam(self, ctx: MT22Parser.ParamContext):
        out = True if ctx.OUT() else False
        inherit = True if ctx.INHERIT() else False
        return ParamDecl(ctx.ID().getText(), self.visit(ctx.typ()), out, inherit)

    # functyp: typ | VOID ;
    def visitFunctyp(self, ctx: MT22Parser.FunctypContext):
        if ctx.typ():
            return self.visit(ctx.typ())
        return VoidType()

    # EXPRESSION
    # expr
    def visitExpr(self, ctx: MT22Parser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.relationalExpr(0))
        return BinExpr(ctx.CONCATOP().getText(), self.visit(ctx.relationalExpr(0)), self.visit(ctx.relationalExpr(1)))

    # relationalExpr
    def visitRelationalExpr(self, ctx: MT22Parser.RelationalExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.logicalExpr(0))
        return BinExpr(self.visit(ctx.relationalOpt()), self.visit(ctx.logicalExpr(0)), self.visit(ctx.logicalExpr(1)))

    # relationalOpt
    def visitRelationalOpt(self, ctx: MT22Parser.RelationalOptContext):
        if ctx.EQCOP():
            return ctx.EQCOP().getText()
        elif ctx.NOTEQOP():
            return ctx.NOTEQOP().getText()
        elif ctx.SMOP():
            return ctx.SMOP().getText()
        elif ctx.GTOP():
            return ctx.GTOP().getText()
        elif ctx.SMEOP():
            return ctx.SMEOP().getText()
        return ctx.GTEOP().getText()

    # logicalExpr
    def visitLogicalExpr(self, ctx: MT22Parser.LogicalExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.addExpr())
        return BinExpr(self.visit(ctx.logicalOpt()), self.visit(ctx.logicalExpr()), self.visit(ctx.addExpr()))

    # logicalOpt
    def visitLogicalOpt(self, ctx: MT22Parser.LogicalOptContext):
        if ctx.ANDOP():
            return ctx.ANDOP().getText()
        return ctx.OROP().getText()

    # addExpr
    def visitAddExpr(self, ctx: MT22Parser.AddExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.multiExpr())
        return BinExpr(self.visit(ctx.addOpt()), self.visit(ctx.addExpr()), self.visit(ctx.multiExpr()))

    # addOpt
    def visitAddOpt(self, ctx: MT22Parser.AddOptContext):
        return ctx.ADDOP().getText() if ctx.ADDOP() else ctx.SUBOP().getText()

    # multiExpr
    def visitMultiExpr(self, ctx: MT22Parser.MultiExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.unaryLogicalExpr())
        return BinExpr(self.visit(ctx.multiOpt()), self.visit(ctx.multiExpr()), self.visit(ctx.unaryLogicalExpr()))

    # multiOpt
    def visitMultiOpt(self, ctx: MT22Parser.MultiOptContext):
        if ctx.MULOP():
            return ctx.MULOP().getText()
        elif ctx.DIVOP():
            return ctx.DIVOP().getText()
        return ctx.MODOP().getText()

    # logicalExpr
    def visitUnaryLogicalExpr(self, ctx: MT22Parser.UnaryLogicalExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.signExpr())
        return UnExpr(ctx.NOTOP().getText(), self.visit(ctx.unaryLogicalExpr()))

    # signExpr
    def visitSignExpr(self, ctx: MT22Parser.SignExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.indexOptExpr())
        return UnExpr(ctx.SUBOP().getText(), self.visit(ctx.signExpr()))

    # indexOptExpr
    def visitIndexOptExpr(self, ctx: MT22Parser.IndexOptExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.subexpr())
        # ID LS nonnullexprlist RS
        return ArrayCell(ctx.ID().getText(), self.visit(ctx.nonullexprlist()))

    # subexpr
    def visitSubexpr(self, ctx: MT22Parser.SubexprContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.alllit():
            return self.visit(ctx.alllit())
        elif ctx.expr():
            return self.visit(ctx.expr())
        return self.visit(ctx.callexpr())

    # callexpr
    def visitCallexpr(self, ctx: MT22Parser.CallexprContext):
        if ctx.ID():
            return FuncCall(ctx.ID().getText(), self.visit(ctx.nullexprlist()))
        return FuncCall(self.visit(ctx.specialFunc()), self.visit(ctx.nullexprlist()))

    # STMT
    # stmt
    def visitStmt(self, ctx: MT22Parser.StmtContext):
        if ctx.assignstmt():
            return self.visit(ctx.assignstmt())
        elif ctx.ifstmt():
            return self.visit(ctx.ifstmt())
        elif ctx.forstmt():
            return self.visit(ctx.forstmt())
        elif ctx.whilestmt():
            return self.visit(ctx.whilestmt())
        elif ctx.dowhilestmt():
            return self.visit(ctx.dowhilestmt())
        elif ctx.breakstmt():
            return self.visit(ctx.breakstmt())
        elif ctx.continuestmt():
            return self.visit(ctx.continuestmt())
        elif ctx.returnstmt():
            return self.visit(ctx.returnstmt())
        elif ctx.callstmt():
            return self.visit(ctx.callstmt())
        return self.visit(ctx.blockstmt())

    # assignstmt: scalarvar EQ expr SM;
    def visitAssignstmt(self, ctx: MT22Parser.AssignstmtContext):
        return AssignStmt(self.visit(ctx.scalarvar()), self.visit(ctx.expr()))

    # ifstmt: IF LB expr RB stmt (ELSE stmt)? ;
    def visitIfstmt(self, ctx: MT22Parser.IfstmtContext):
        if ctx.ELSE():
            return IfStmt(self.visit(ctx.expr()), self.visit(ctx.stmt(0)), self.visit(ctx.stmt(1)))
        return IfStmt(self.visit(ctx.expr()), self.visit(ctx.stmt(0)))

    # forstmt: FOR LB scalarvar EQ expr CM expr CM expr RB stmt;
    def visitForstmt(self, ctx: MT22Parser.ForstmtContext):
        return ForStmt(AssignStmt(self.visit(ctx.scalarvar()), self.visit(ctx.expr(0))), self.visit(ctx.expr(1)), self.visit(ctx.expr(2)), self.visit(ctx.stmt()))

    # whilestmt: WHILE LB expr RB stmt;
    def visitWhilestmt(self, ctx: MT22Parser.WhilestmtContext):
        return WhileStmt(self.visit(ctx.expr()), self.visit(ctx.stmt()))

    # dowhilestmt: DO blockstmt WHILE LB expr RB SM;;
    def visitDowhilestmt(self, ctx: MT22Parser.DowhilestmtContext):
        return DoWhileStmt(self.visit(ctx.expr()), self.visit(ctx.blockstmt()))

    # breakstmt: BREAK SM;
    def visitBreakstmt(self, ctx: MT22Parser.BreakstmtContext):
        return BreakStmt()

    # continuestmt: CONTINUE SM;
    def visitContinuestmt(self, ctx: MT22Parser.ContinuestmtContext):
        return ContinueStmt()

    # returnstmt: RETURN expr? SEMI;
    def visitReturnstmt(self, ctx: MT22Parser.ReturnstmtContext):
        if ctx.expr():
            return ReturnStmt(self.visit(ctx.expr()))
        return ReturnStmt()

    # callstmt: (ID | specialFunc) LB nullexprlist RB SM;
    def visitCallstmt(self, ctx: MT22Parser.CallstmtContext):
        if ctx.ID():
            return CallStmt(ctx.ID().getText(), self.visit(ctx.nullexprlist()))
        # speicalFunc
        return CallStmt(self.visit(ctx.specialFunc()), self.visit(ctx.nullexprlist()))

    # blockstmt
    # blockstmt: LP blockstmtbody RP;
    def visitBlockstmt(self, ctx: MT22Parser.BlockstmtContext):
        return self.visit(ctx.blockstmtbody())

    # blockstmtbody: declandstmts | ;
    def visitBlockstmtbody(self, ctx: MT22Parser.BlockstmtbodyContext):
        if ctx.getChildCount() == 0:
            return BlockStmt([])
        return BlockStmt(self.visit(ctx.declandstmts()))

    # declandstmts: declandstmt declandstmts | declandstmt;
    def visitDeclandstmts(self, ctx: MT22Parser.DeclandstmtsContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.declandstmt())
        return self.visit(ctx.declandstmt()) + self.visit(ctx.declandstmts())

    # declandstmt: decl | stmt;
    def visitDeclandstmt(self, ctx: MT22Parser.DeclandstmtContext):
        if ctx.decl():
            return self.visit(ctx.decl())
        return [self.visit(ctx.stmt())]

    # scalarvar: ID | (ID LS nonullexprlist RS);
    def visitScalarvar(self, ctx: MT22Parser.ScalarvarContext):
        if ctx.getChildCount() == 1:
            return Id(ctx.ID().getText())
        return ArrayCell(ctx.ID().getText(), self.visit(ctx.nonullexprlist()))

    # STMTLIST & EXPRLIST
    # nonullexprlist: expr CM nonullexprlist | expr;
    def visitNonullexprlist(self, ctx: MT22Parser.NonullexprlistContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.nonullexprlist())

    # nullexprlist: nonullexprlist | ;
    def visitNullexprlist(self, ctx: MT22Parser.NullexprlistContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.nonullexprlist())

    # IDLIST & TYP
    # idlist
    def visitIdlist(self, ctx: MT22Parser.IdlistContext):
        if ctx.getChildCount() == 1:
            return [ctx.ID().getText()]
        return [ctx.ID().getText()] + self.visit(ctx.idlist())

    # typ
    def visitTyp(self, ctx: MT22Parser.TypContext):
        if ctx.INT():
            return IntegerType()
        elif ctx.FLOAT():
            return FloatType()
        elif ctx.STRING():
            return StringType()
        elif ctx.BOOLEAN():
            return BooleanType()
        elif ctx.AUTO():
            return AutoType()
        return self.visit(ctx.arraytyp())

    # arrayTyp
    def visitArraytyp(self, ctx: MT22Parser.ArraytypContext):
        return ArrayType(self.visit(ctx.intList()), self.visit(ctx.typ()))

    # intList
    def visitIntList(self, ctx: MT22Parser.IntListContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.intandexpr())]
        return [self.visit(ctx.intandexpr())] + self.visit(ctx.intList())

    # intandexpr
    def visitIntandexpr(self, ctx: MT22Parser.IntandexprContext):
        if ctx.INTLIT():
            return int(ctx.INTLIT().getText())
        return self.visit(ctx.expr())

    # alllit: INTLIT | STRINGLIT | FLOATLIT | TRUE | FALSE | arrayLit;
    def visitAlllit(self, ctx: MT22Parser.AlllitContext):
        if ctx.INTLIT():
            return IntegerLit(int(ctx.INTLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLit(ctx.STRINGLIT().getText())
        elif ctx.FLOATLIT():
            lit = ctx.FLOATLIT().getText()
            if lit[0] == '.':
                lit = '0'+lit
            return FloatLit(float(lit))
        elif ctx.TRUE() or ctx.FALSE():
            return BooleanLit(True if ctx.TRUE() else False)
        return self.visit(ctx.arrayLit())

    # arrayLit: LP arrayElements RP;
    def visitArrayLit(self, ctx: MT22Parser.ArrayLitContext):
        return ArrayLit(self.visit(ctx.arrayElements()))

    # arrayElements: alllits | ;
    def visitArrayElements(self, ctx: MT22Parser.ArrayElementsContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.alllits())

    def visitAlllits(self, ctx: MT22Parser.AlllitsContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.alllits())

    # SPECIAL FUNCTIONS
    def visitSpecialFunc(self, ctx: MT22Parser.SpecialFuncContext):
        if ctx.readInt():
            return self.visit(ctx.readInt())
        elif ctx.printInt():
            return self.visit(ctx.printInt())
        elif ctx.readFloat():
            return self.visit(ctx.readFloat())
        elif ctx.writeFloat():
            return self.visit(ctx.writeFloat())
        elif ctx.readBoolean():
            return self.visit(ctx.readBoolean())
        elif ctx.printBoolean():
            return self.visit(ctx.printBoolean())
        elif ctx.readString():
            return self.visit(ctx.readString())
        elif ctx.printString():
            return self.visit(ctx.printString())
        elif ctx.superFunc():
            return self.visit(ctx.superFunc())
        return self.visit(ctx.preventDefault())

    def visitReadInt(self, ctx: MT22Parser.ReadIntContext):
        return "readInteger"

    def visitPrintInt(self, ctx: MT22Parser.PrintIntContext):
        return "printInteger"

    def visitReadFloat(self, ctx: MT22Parser.ReadFloatContext):
        return "readFloat"

    def visitWriteFloat(self, ctx: MT22Parser.WriteFloatContext):
        return "writeFloat"

    def visitReadBoolean(self, ctx: MT22Parser.ReadBooleanContext):
        return "readBoolean"

    def visitPrintBoolean(self, ctx: MT22Parser.PrintBooleanContext):
        return "printBoolean"

    def visitReadString(self, ctx: MT22Parser.ReadStringContext):
        return "readString"

    def visitPrintString(self, ctx: MT22Parser.PrintStringContext):
        return "printString"

    def visitSuperFunc(self, ctx: MT22Parser.SuperFuncContext):
        return "super"

    def visitPreventDefault(self, ctx: MT22Parser.PreventDefaultContext):
        return "preventDefault"
