# Generated from D:/Programming/Universidade/Compiladores/RecursiveDescentParser\sqlGrammar.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .sqlGrammarParser import sqlGrammarParser
else:
    from sqlGrammarParser import sqlGrammarParser

# This class defines a complete generic visitor for a parse tree produced by sqlGrammarParser.

class sqlGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by sqlGrammarParser#start.
    def visitStart(self, ctx:sqlGrammarParser.StartContext):
        return self.visitChildren(ctx)



del sqlGrammarParser