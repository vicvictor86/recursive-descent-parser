# Generated from D:/Programming/Universidade/Compiladores/RecursiveDescentParser\sqlGrammar.g4 by ANTLR 4.12.0
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
        4,1,33,9,2,0,7,0,1,0,5,0,4,8,0,10,0,12,0,7,9,0,1,0,0,0,1,0,0,1,1,
        0,1,28,8,0,5,1,0,0,0,2,4,7,0,0,0,3,2,1,0,0,0,4,7,1,0,0,0,5,3,1,0,
        0,0,5,6,1,0,0,0,6,1,1,0,0,0,7,5,1,0,0,0,1,5
    ]

class sqlGrammarParser ( Parser ):

    grammarFileName = "sqlGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'CREATE'", "'DATABASE'", "'INTO'", "'USE'", 
                     "'TABLE'", "'INSERT'", "'SELECT'", "'FROM'", "'ORDER'", 
                     "'BY'", "'WHERE'", "'UPDATE'", "'SET'", "'DELETE'", 
                     "'TRUNCATE'", "'('", "')'", "'<='", "'>='", "'='", 
                     "'>'", "'<'", "','", "'*'", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "TYPE", "VALUE", "ID", "STRING", 
                      "NUM", "INT", "FLOAT", "WS" ]

    RULE_start = 0

    ruleNames =  [ "start" ]

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
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    TYPE=26
    VALUE=27
    ID=28
    STRING=29
    NUM=30
    INT=31
    FLOAT=32
    WS=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(sqlGrammarParser.TYPE)
            else:
                return self.getToken(sqlGrammarParser.TYPE, i)

        def VALUE(self, i:int=None):
            if i is None:
                return self.getTokens(sqlGrammarParser.VALUE)
            else:
                return self.getToken(sqlGrammarParser.VALUE, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(sqlGrammarParser.ID)
            else:
                return self.getToken(sqlGrammarParser.ID, i)

        def getRuleIndex(self):
            return sqlGrammarParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = sqlGrammarParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 5
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 536870910) != 0):
                self.state = 2
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 536870910) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 7
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





