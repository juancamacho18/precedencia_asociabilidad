import sys
from antlr4 import *
from ModificadoLexer import ModificadoLexer
from ModificadoParser import ModificadoParser
from EvalVisitor import EvalVisitor

if __name__=='__main__':
    Input=FileStream(sys.argv[1])
    lexer=ModificadoLexer(Input)
    tokens=CommonTokenStream(lexer)
    parser=ModificadoParser(tokens)
    tree=parser.prog()

    Eval=EvalVisitor()
    Eval.visit(tree)
