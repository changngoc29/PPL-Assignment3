# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decllist.
    def visitDecllist(self, ctx:MT22Parser.DecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl.
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardeclnoinit.
    def visitVardeclnoinit(self, ctx:MT22Parser.VardeclnoinitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardeclinit.
    def visitVardeclinit(self, ctx:MT22Parser.VardeclinitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramlist.
    def visitParamlist(self, ctx:MT22Parser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#params.
    def visitParams(self, ctx:MT22Parser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param.
    def visitParam(self, ctx:MT22Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#functyp.
    def visitFunctyp(self, ctx:MT22Parser.FunctypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relationalExpr.
    def visitRelationalExpr(self, ctx:MT22Parser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relationalOpt.
    def visitRelationalOpt(self, ctx:MT22Parser.RelationalOptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logicalExpr.
    def visitLogicalExpr(self, ctx:MT22Parser.LogicalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logicalOpt.
    def visitLogicalOpt(self, ctx:MT22Parser.LogicalOptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#addExpr.
    def visitAddExpr(self, ctx:MT22Parser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#addOpt.
    def visitAddOpt(self, ctx:MT22Parser.AddOptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#multiExpr.
    def visitMultiExpr(self, ctx:MT22Parser.MultiExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#multiOpt.
    def visitMultiOpt(self, ctx:MT22Parser.MultiOptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#unaryLogicalExpr.
    def visitUnaryLogicalExpr(self, ctx:MT22Parser.UnaryLogicalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#signExpr.
    def visitSignExpr(self, ctx:MT22Parser.SignExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#indexOptExpr.
    def visitIndexOptExpr(self, ctx:MT22Parser.IndexOptExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#subexpr.
    def visitSubexpr(self, ctx:MT22Parser.SubexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callexpr.
    def visitCallexpr(self, ctx:MT22Parser.CallexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignstmt.
    def visitAssignstmt(self, ctx:MT22Parser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ifstmt.
    def visitIfstmt(self, ctx:MT22Parser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#forstmt.
    def visitForstmt(self, ctx:MT22Parser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#whilestmt.
    def visitWhilestmt(self, ctx:MT22Parser.WhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dowhilestmt.
    def visitDowhilestmt(self, ctx:MT22Parser.DowhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#breakstmt.
    def visitBreakstmt(self, ctx:MT22Parser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continuestmt.
    def visitContinuestmt(self, ctx:MT22Parser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#returnstmt.
    def visitReturnstmt(self, ctx:MT22Parser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callstmt.
    def visitCallstmt(self, ctx:MT22Parser.CallstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockstmt.
    def visitBlockstmt(self, ctx:MT22Parser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockstmtbody.
    def visitBlockstmtbody(self, ctx:MT22Parser.BlockstmtbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#declandstmts.
    def visitDeclandstmts(self, ctx:MT22Parser.DeclandstmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#declandstmt.
    def visitDeclandstmt(self, ctx:MT22Parser.DeclandstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#scalarvar.
    def visitScalarvar(self, ctx:MT22Parser.ScalarvarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#nonullexprlist.
    def visitNonullexprlist(self, ctx:MT22Parser.NonullexprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#nullexprlist.
    def visitNullexprlist(self, ctx:MT22Parser.NullexprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typ.
    def visitTyp(self, ctx:MT22Parser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraytyp.
    def visitArraytyp(self, ctx:MT22Parser.ArraytypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#intList.
    def visitIntList(self, ctx:MT22Parser.IntListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#intandexpr.
    def visitIntandexpr(self, ctx:MT22Parser.IntandexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#alllit.
    def visitAlllit(self, ctx:MT22Parser.AlllitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayLit.
    def visitArrayLit(self, ctx:MT22Parser.ArrayLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayElements.
    def visitArrayElements(self, ctx:MT22Parser.ArrayElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#alllits.
    def visitAlllits(self, ctx:MT22Parser.AlllitsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#specialFunc.
    def visitSpecialFunc(self, ctx:MT22Parser.SpecialFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readInt.
    def visitReadInt(self, ctx:MT22Parser.ReadIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printInt.
    def visitPrintInt(self, ctx:MT22Parser.PrintIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readFloat.
    def visitReadFloat(self, ctx:MT22Parser.ReadFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#writeFloat.
    def visitWriteFloat(self, ctx:MT22Parser.WriteFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readBoolean.
    def visitReadBoolean(self, ctx:MT22Parser.ReadBooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printBoolean.
    def visitPrintBoolean(self, ctx:MT22Parser.PrintBooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readString.
    def visitReadString(self, ctx:MT22Parser.ReadStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printString.
    def visitPrintString(self, ctx:MT22Parser.PrintStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#superFunc.
    def visitSuperFunc(self, ctx:MT22Parser.SuperFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#preventDefault.
    def visitPreventDefault(self, ctx:MT22Parser.PreventDefaultContext):
        return self.visitChildren(ctx)



del MT22Parser