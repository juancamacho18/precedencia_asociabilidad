# Generated from Modificado.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,18,69,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,0,
        11,0,12,0,13,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,23,8,1,1,2,1,2,1,2,
        1,2,1,2,3,2,30,8,2,1,3,1,3,1,3,1,3,1,3,3,3,37,8,3,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,3,4,60,8,4,1,4,1,4,5,4,64,8,4,10,4,12,4,67,9,4,1,4,0,1,8,5,
        0,2,4,6,8,0,4,1,0,11,12,1,0,13,14,1,0,4,5,1,0,7,9,74,0,11,1,0,0,
        0,2,22,1,0,0,0,4,29,1,0,0,0,6,36,1,0,0,0,8,59,1,0,0,0,10,12,3,2,
        1,0,11,10,1,0,0,0,12,13,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,1,
        1,0,0,0,15,16,3,4,2,0,16,17,5,17,0,0,17,23,1,0,0,0,18,19,5,1,0,0,
        19,20,5,15,0,0,20,23,5,17,0,0,21,23,5,17,0,0,22,15,1,0,0,0,22,18,
        1,0,0,0,22,21,1,0,0,0,23,3,1,0,0,0,24,25,3,6,3,0,25,26,7,0,0,0,26,
        27,3,4,2,0,27,30,1,0,0,0,28,30,3,6,3,0,29,24,1,0,0,0,29,28,1,0,0,
        0,30,5,1,0,0,0,31,32,3,8,4,0,32,33,7,1,0,0,33,34,3,6,3,0,34,37,1,
        0,0,0,35,37,3,8,4,0,36,31,1,0,0,0,36,35,1,0,0,0,37,7,1,0,0,0,38,
        39,6,4,-1,0,39,40,5,2,0,0,40,41,3,4,2,0,41,42,5,3,0,0,42,60,1,0,
        0,0,43,44,7,2,0,0,44,45,5,6,0,0,45,46,3,4,2,0,46,47,5,3,0,0,47,60,
        1,0,0,0,48,49,7,3,0,0,49,50,5,6,0,0,50,51,3,4,2,0,51,52,5,3,0,0,
        52,60,1,0,0,0,53,60,5,16,0,0,54,60,5,15,0,0,55,56,5,6,0,0,56,57,
        3,4,2,0,57,58,5,3,0,0,58,60,1,0,0,0,59,38,1,0,0,0,59,43,1,0,0,0,
        59,48,1,0,0,0,59,53,1,0,0,0,59,54,1,0,0,0,59,55,1,0,0,0,60,65,1,
        0,0,0,61,62,10,4,0,0,62,64,5,10,0,0,63,61,1,0,0,0,64,67,1,0,0,0,
        65,63,1,0,0,0,65,66,1,0,0,0,66,9,1,0,0,0,67,65,1,0,0,0,6,13,22,29,
        36,59,65
    ]

class ModificadoParser ( Parser ):

    grammarFileName = "Modificado.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'modo='", "'Sqrt('", "')'", "'ln'", "'log'", 
                     "'('", "'sin'", "'cos'", "'tan'", "'!'", "'*'", "'/'", 
                     "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "MUL", "DIV", 
                      "ADD", "SUB", "ID", "INT", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2
    RULE_term = 3
    RULE_fact = 4

    ruleNames =  [ "prog", "stat", "expr", "term", "fact" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    MUL=11
    DIV=12
    ADD=13
    SUB=14
    ID=15
    INT=16
    NEWLINE=17
    WS=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ModificadoParser.StatContext)
            else:
                return self.getTypedRuleContext(ModificadoParser.StatContext,i)


        def getRuleIndex(self):
            return ModificadoParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = ModificadoParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.stat()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 230390) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ModificadoParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlankContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ModificadoParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(ModificadoParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlank" ):
                listener.enterBlank(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlank" ):
                listener.exitBlank(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlank" ):
                return visitor.visitBlank(self)
            else:
                return visitor.visitChildren(self)


    class ModoContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ModificadoParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ModificadoParser.ID, 0)
        def NEWLINE(self):
            return self.getToken(ModificadoParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModo" ):
                listener.enterModo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModo" ):
                listener.exitModo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModo" ):
                return visitor.visitModo(self)
            else:
                return visitor.visitChildren(self)


    class PrintExprContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ModificadoParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ModificadoParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(ModificadoParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpr" ):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = ModificadoParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 4, 5, 6, 7, 8, 9, 15, 16]:
                localctx = ModificadoParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.expr()
                self.state = 16
                self.match(ModificadoParser.NEWLINE)
                pass
            elif token in [1]:
                localctx = ModificadoParser.ModoContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.match(ModificadoParser.T__0)
                self.state = 19
                self.match(ModificadoParser.ID)
                self.state = 20
                self.match(ModificadoParser.NEWLINE)
                pass
            elif token in [17]:
                localctx = ModificadoParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 21
                self.match(ModificadoParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ModificadoParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ModificadoParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(ModificadoParser.TermContext,0)

        def expr(self):
            return self.getTypedRuleContext(ModificadoParser.ExprContext,0)

        def MUL(self):
            return self.getToken(ModificadoParser.MUL, 0)
        def DIV(self):
            return self.getToken(ModificadoParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class TotermContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ModificadoParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(ModificadoParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToterm" ):
                listener.enterToterm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToterm" ):
                listener.exitToterm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToterm" ):
                return visitor.visitToterm(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = ModificadoParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = ModificadoParser.MulDivContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.term()
                self.state = 25
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==11 or _la==12):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 26
                self.expr()
                pass

            elif la_ == 2:
                localctx = ModificadoParser.TotermContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.term()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ModificadoParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TofactorContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ModificadoParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def fact(self):
            return self.getTypedRuleContext(ModificadoParser.FactContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTofactor" ):
                listener.enterTofactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTofactor" ):
                listener.exitTofactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTofactor" ):
                return visitor.visitTofactor(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ModificadoParser.TermContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def fact(self):
            return self.getTypedRuleContext(ModificadoParser.FactContext,0)

        def term(self):
            return self.getTypedRuleContext(ModificadoParser.TermContext,0)

        def ADD(self):
            return self.getToken(ModificadoParser.ADD, 0)
        def SUB(self):
            return self.getToken(ModificadoParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)



    def term(self):

        localctx = ModificadoParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.state = 36
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = ModificadoParser.AddSubContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.fact(0)
                self.state = 32
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 33
                self.term()
                pass

            elif la_ == 2:
                localctx = ModificadoParser.TofactorContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.fact(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ModificadoParser.RULE_fact

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParensContext(FactContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ModificadoParser.FactContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ModificadoParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class LogContext(FactContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ModificadoParser.FactContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ModificadoParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLog" ):
                listener.enterLog(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLog" ):
                listener.exitLog(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLog" ):
                return visitor.visitLog(self)
            else:
                return visitor.visitChildren(self)


    class RaizContext(FactContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ModificadoParser.FactContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ModificadoParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRaiz" ):
                listener.enterRaiz(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRaiz" ):
                listener.exitRaiz(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRaiz" ):
                return visitor.visitRaiz(self)
            else:
                return visitor.visitChildren(self)


    class FactorContext(FactContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ModificadoParser.FactContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def fact(self):
            return self.getTypedRuleContext(ModificadoParser.FactContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(FactContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ModificadoParser.FactContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ModificadoParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class SinCosTanContext(FactContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ModificadoParser.FactContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ModificadoParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSinCosTan" ):
                listener.enterSinCosTan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSinCosTan" ):
                listener.exitSinCosTan(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSinCosTan" ):
                return visitor.visitSinCosTan(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(FactContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ModificadoParser.FactContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ModificadoParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def fact(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ModificadoParser.FactContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_fact, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = ModificadoParser.RaizContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 39
                self.match(ModificadoParser.T__1)
                self.state = 40
                self.expr()
                self.state = 41
                self.match(ModificadoParser.T__2)
                pass
            elif token in [4, 5]:
                localctx = ModificadoParser.LogContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 43
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==4 or _la==5):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 44
                self.match(ModificadoParser.T__5)
                self.state = 45
                self.expr()
                self.state = 46
                self.match(ModificadoParser.T__2)
                pass
            elif token in [7, 8, 9]:
                localctx = ModificadoParser.SinCosTanContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 48
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 49
                self.match(ModificadoParser.T__5)
                self.state = 50
                self.expr()
                self.state = 51
                self.match(ModificadoParser.T__2)
                pass
            elif token in [16]:
                localctx = ModificadoParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 53
                self.match(ModificadoParser.INT)
                pass
            elif token in [15]:
                localctx = ModificadoParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 54
                self.match(ModificadoParser.ID)
                pass
            elif token in [6]:
                localctx = ModificadoParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 55
                self.match(ModificadoParser.T__5)
                self.state = 56
                self.expr()
                self.state = 57
                self.match(ModificadoParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 65
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ModificadoParser.FactorContext(self, ModificadoParser.FactContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_fact)
                    self.state = 61
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 62
                    self.match(ModificadoParser.T__9) 
                self.state = 67
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.fact_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def fact_sempred(self, localctx:FactContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         




