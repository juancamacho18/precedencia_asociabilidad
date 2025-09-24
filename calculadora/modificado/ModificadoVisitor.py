# Generated from Modificado.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ModificadoParser import ModificadoParser
else:
    from ModificadoParser import ModificadoParser

# This class defines a complete generic visitor for a parse tree produced by ModificadoParser.

class ModificadoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ModificadoParser#prog.
    def visitProg(self, ctx:ModificadoParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModificadoParser#printExpr.
    def visitPrintExpr(self, ctx:ModificadoParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModificadoParser#Modo.
    def visitModo(self, ctx:ModificadoParser.ModoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModificadoParser#blank.
    def visitBlank(self, ctx:ModificadoParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModificadoParser#MulDiv.
    def visitMulDiv(self, ctx:ModificadoParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModificadoParser#Toterm.
    def visitToterm(self, ctx:ModificadoParser.TotermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModificadoParser#AddSub.
    def visitAddSub(self, ctx:ModificadoParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModificadoParser#Tofactor.
    def visitTofactor(self, ctx:ModificadoParser.TofactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModificadoParser#parens.
    def visitParens(self, ctx:ModificadoParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModificadoParser#Log.
    def visitLog(self, ctx:ModificadoParser.LogContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModificadoParser#Raiz.
    def visitRaiz(self, ctx:ModificadoParser.RaizContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModificadoParser#Factor.
    def visitFactor(self, ctx:ModificadoParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModificadoParser#id.
    def visitId(self, ctx:ModificadoParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModificadoParser#SinCosTan.
    def visitSinCosTan(self, ctx:ModificadoParser.SinCosTanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ModificadoParser#int.
    def visitInt(self, ctx:ModificadoParser.IntContext):
        return self.visitChildren(ctx)



del ModificadoParser