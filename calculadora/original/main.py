import sys
from antlr4 import *
from OriginalLexer import OriginalLexer
from OriginalParser import OriginalParser
from EvalVisitor import EvalVisitor

if __name__=='__main__':
    Input=FileStream(sys.argv[1])
    lexer=OriginalLexer(Input)
    tokens=CommonTokenStream(lexer)
    parser=OriginalParser(tokens)
    tree=parser.prog()

    Eval=EvalVisitor()
    Eval.visit(tree)
