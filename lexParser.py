import re

tokens = \
    {
        'CREATE': 'KEYWORD',
        'DATABASE': 'KEYWORD',
        'INTO': 'KEYWORD',
        'USE': 'KEYWORD',
        'TABLE': 'KEYWORD',
        'INSERT': 'KEYWORD',
        'SELECT': 'KEYWORD',
        'FROM': 'KEYWORD',
        'ORDER': 'KEYWORD',
        'BY': 'KEYWORD',
        'WHERE': 'KEYWORD',
        'UPDATE': 'KEYWORD',
        'SET': 'KEYWORD',
        'DELETE': 'KEYWORD',
        'TRUNCATE': 'KEYWORD'
    }
specialTokens = \
    {
        '(': 'SPECIAL_SYMBOL',
        ')': 'SPECIAL_SYMBOL',
        '<=': 'SPECIAL_SYMBOL',
        '>=': 'SPECIAL_SYMBOL',
        '=': 'SPECIAL_SYMBOL',
        '>': 'SPECIAL_SYMBOL',
        '<': 'SPECIAL_SYMBOL',
        ',': 'SPECIAL_SYMBOL',
        '*': 'SPECIAL_SYMBOL',
        ';': 'SPECIAL_SYMBOL'
    }
types = \
    {
        'INT': 'TYPE',
        'VARCHAR': 'TYPE',
        'CHAR': 'TYPE',
        'DATE': 'TYPE',
        'FLOAT': 'TYPE',
        'DOUBLE': 'TYPE',
        'BOOLEAN': 'TYPE',
        'STRING': 'TYPE'
    }


def isToken(text: str) -> tuple:
    entry = text
    text = text.upper()
    token = 'INVALID_TOKEN'
    if text in tokens:
        token = (entry, tokens[text])
    elif text in specialTokens:
        token = (entry, specialTokens[text])
    elif text in types:
        token = (entry, types[text])
    elif re.match(r'[a-zA-Z]+', text):
        token = (entry, 'ID')
    elif text[0] == '"' and text[-1] == '"' and len(text) > 1:
        token = (entry, 'VALUE')
    elif re.match(r'[0-9]+(.[0-9]+)?', text):
        token = (entry, 'VALUE')
    return token


def lexParser(text: str) -> list:
    identifiedTokens = []
    actual = ''
    for char in text:
        if char != ' ':
            if char in specialTokens:
                if actual != '':
                    identifiedTokens.append(isToken(actual))
                identifiedTokens.append(isToken(char))
                actual = ''
            else:
                actual += char
        else:
            if actual != '':
                identifiedTokens.append(isToken(actual))
            actual = ''
    if actual != '':
        identifiedTokens.append(isToken(actual))
    return identifiedTokens


class Token:
    def __init__(self, text: str, type: str):
        self.text = text
        self.type = type


class Lexer:
    def __init__(self, text: str):
        self.tokens = lexParser(text)
        self.position = 0

    def nextToken(self) -> Token:
        if self.position < len(self.tokens):
            self.position += 1
            return Token(self.tokens[self.position - 1][0], self.tokens[self.position - 1][1])
        else:
            return Token('', '')


if __name__ == '__main__':
    lexer = Lexer('INSERT INTO jogadores (nome, idade, CPF) VALUES (josicreuson, 1900, 00000000011);')
    print(lexer.nextToken())
    print(lexer.nextToken())
    print(lexer.nextToken())
    print(lexer.nextToken())

