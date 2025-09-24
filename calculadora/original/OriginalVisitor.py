# Generated from Original.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .OriginalParser import OriginalParser
else:
    from OriginalParser import OriginalParser

# This class defines a complete generic visitor for a parse tree produced by OriginalParser.

class OriginalVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by OriginalParser#prog.
    def visitProg(self, ctx:OriginalParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OriginalParser#printExpr.
    def visitPrintExpr(self, ctx:OriginalParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OriginalParser#Modo.
    def visitModo(self, ctx:OriginalParser.ModoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OriginalParser#blank.
    def visitBlank(self, ctx:OriginalParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OriginalParser#AddSub.
    def visitAddSub(self, ctx:OriginalParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OriginalParser#Toterm.
    def visitToterm(self, ctx:OriginalParser.TotermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OriginalParser#Tofactor.
    def visitTofactor(self, ctx:OriginalParser.TofactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OriginalParser#MulDiv.
    def visitMulDiv(self, ctx:OriginalParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OriginalParser#parens.
    def visitParens(self, ctx:OriginalParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OriginalParser#Log.
    def visitLog(self, ctx:OriginalParser.LogContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OriginalParser#Raiz.
    def visitRaiz(self, ctx:OriginalParser.RaizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OriginalParser#Factor.
    def visitFactor(self, ctx:OriginalParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OriginalParser#id.
    def visitId(self, ctx:OriginalParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OriginalParser#SinCosTan.
    def visitSinCosTan(self, ctx:OriginalParser.SinCosTanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OriginalParser#int.
    def visitInt(self, ctx:OriginalParser.IntContext):
        return self.visitChildren(ctx)



del OriginalParser