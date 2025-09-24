# Generated from Modificado.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ModificadoParser import ModificadoParser
else:
    from ModificadoParser import ModificadoParser

# This class defines a complete listener for a parse tree produced by ModificadoParser.
class ModificadoListener(ParseTreeListener):

    # Enter a parse tree produced by ModificadoParser#prog.
    def enterProg(self, ctx:ModificadoParser.ProgContext):
        pass

    # Exit a parse tree produced by ModificadoParser#prog.
    def exitProg(self, ctx:ModificadoParser.ProgContext):
        pass


    # Enter a parse tree produced by ModificadoParser#printExpr.
    def enterPrintExpr(self, ctx:ModificadoParser.PrintExprContext):
        pass

    # Exit a parse tree produced by ModificadoParser#printExpr.
    def exitPrintExpr(self, ctx:ModificadoParser.PrintExprContext):
        pass


    # Enter a parse tree produced by ModificadoParser#Modo.
    def enterModo(self, ctx:ModificadoParser.ModoContext):
        pass

    # Exit a parse tree produced by ModificadoParser#Modo.
    def exitModo(self, ctx:ModificadoParser.ModoContext):
        pass


    # Enter a parse tree produced by ModificadoParser#blank.
    def enterBlank(self, ctx:ModificadoParser.BlankContext):
        pass

    # Exit a parse tree produced by ModificadoParser#blank.
    def exitBlank(self, ctx:ModificadoParser.BlankContext):
        pass


    # Enter a parse tree produced by ModificadoParser#MulDiv.
    def enterMulDiv(self, ctx:ModificadoParser.MulDivContext):
        pass

    # Exit a parse tree produced by ModificadoParser#MulDiv.
    def exitMulDiv(self, ctx:ModificadoParser.MulDivContext):
        pass


    # Enter a parse tree produced by ModificadoParser#Toterm.
    def enterToterm(self, ctx:ModificadoParser.TotermContext):
        pass

    # Exit a parse tree produced by ModificadoParser#Toterm.
    def exitToterm(self, ctx:ModificadoParser.TotermContext):
        pass


    # Enter a parse tree produced by ModificadoParser#AddSub.
    def enterAddSub(self, ctx:ModificadoParser.AddSubContext):
        pass

    # Exit a parse tree produced by ModificadoParser#AddSub.
    def exitAddSub(self, ctx:ModificadoParser.AddSubContext):
        pass


    # Enter a parse tree produced by ModificadoParser#Tofactor.
    def enterTofactor(self, ctx:ModificadoParser.TofactorContext):
        pass

    # Exit a parse tree produced by ModificadoParser#Tofactor.
    def exitTofactor(self, ctx:ModificadoParser.TofactorContext):
        pass


    # Enter a parse tree produced by ModificadoParser#parens.
    def enterParens(self, ctx:ModificadoParser.ParensContext):
        pass

    # Exit a parse tree produced by ModificadoParser#parens.
    def exitParens(self, ctx:ModificadoParser.ParensContext):
        pass


    # Enter a parse tree produced by ModificadoParser#Log.
    def enterLog(self, ctx:ModificadoParser.LogContext):
        pass

    # Exit a parse tree produced by ModificadoParser#Log.
    def exitLog(self, ctx:ModificadoParser.LogContext):
        pass


    # Enter a parse tree produced by ModificadoParser#Raiz.
    def enterRaiz(self, ctx:ModificadoParser.RaizContext):
        pass

    # Exit a parse tree produced by ModificadoParser#Raiz.
    def exitRaiz(self, ctx:ModificadoParser.RaizContext):
        pass


    # Enter a parse tree produced by ModificadoParser#Factor.
    def enterFactor(self, ctx:ModificadoParser.FactorContext):
        pass

    # Exit a parse tree produced by ModificadoParser#Factor.
    def exitFactor(self, ctx:ModificadoParser.FactorContext):
        pass


    # Enter a parse tree produced by ModificadoParser#id.
    def enterId(self, ctx:ModificadoParser.IdContext):
        pass

    # Exit a parse tree produced by ModificadoParser#id.
    def exitId(self, ctx:ModificadoParser.IdContext):
        pass


    # Enter a parse tree produced by ModificadoParser#SinCosTan.
    def enterSinCosTan(self, ctx:ModificadoParser.SinCosTanContext):
        pass

    # Exit a parse tree produced by ModificadoParser#SinCosTan.
    def exitSinCosTan(self, ctx:ModificadoParser.SinCosTanContext):
        pass


    # Enter a parse tree produced by ModificadoParser#int.
    def enterInt(self, ctx:ModificadoParser.IntContext):
        pass

    # Exit a parse tree produced by ModificadoParser#int.
    def exitInt(self, ctx:ModificadoParser.IntContext):
        pass



del ModificadoParser