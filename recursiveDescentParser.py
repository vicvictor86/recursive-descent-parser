from lexParser import Lexer

def recursiveDescentParser(lexer: Lexer) -> bool:
    token = lexer.nextToken()
    if token.text == "CREATE":
        token = lexer.nextToken()
        if token.text == "DATABASE":
            token = lexer.nextToken()
            if token.type == "ID":
                if lexer.nextToken().text == ";":
                    if recursiveDescentParser(lexer):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        elif token.text == "TABLE":
            token = lexer.nextToken()
            if token.type == "ID":
                token = lexer.nextToken()
                if token.text == "(":
                    token = lexer.nextToken()

                    while token.text != ")":
                        if token.type == "ID":
                            token = lexer.nextToken()

                            if token.type == "TYPE":
                                token = lexer.nextToken()

                                if token.text == ",":
                                    token = lexer.nextToken()

                                    continue
                                elif token.text == ")":
                                    break
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    token = lexer.nextToken()

                    if token.text == ";":
                        if recursiveDescentParser(lexer):
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    elif token.text == "USE":
        token = lexer.nextToken()
        if token.type == "ID":
            if lexer.nextToken().text == ";":
                if recursiveDescentParser(lexer):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    elif token.text == "UPDATE":
        token = lexer.nextToken()
        if token.type == "ID":
            token = lexer.nextToken()
            if token.text == "SET":
                token = lexer.nextToken()
                if token.type == "ID":
                    token = lexer.nextToken()
                    if token.text == "=":
                        token = lexer.nextToken()
                        if token.type == "VALUE":
                            token = lexer.nextToken()

                            return recognizeWhere(token, lexer)
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    elif token.text == "SELECT":
        return recognizeSelect(token, lexer)
    elif token.text == "DELETE":
        token = lexer.nextToken()
        if token.text == "FROM":
            token = lexer.nextToken()
            if token.type == "ID":
                token = lexer.nextToken()
                if token.text == "WHERE":
                    return recognizeWhere(token, lexer)
            else:
                return False
        else:
            return False
    elif token.text == "TRUNCATE":
        token = lexer.nextToken()
        if token.text == "TABLE":
            token = lexer.nextToken()
            if token.type == "ID":
                token = lexer.nextToken()

                if token.text == ";":
                    if recursiveDescentParser(lexer):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    elif token.text == "INSERT":
        token = lexer.nextToken()
        if token.text == "INTO":
            token = lexer.nextToken()
            if token.type == "ID":
                token = lexer.nextToken()

                if token.text == "(":
                    token = lexer.nextToken()

                    while token.text != ")":
                        if token.type == "ID":
                            token = lexer.nextToken()

                            if token.text == ",":
                                token = lexer.nextToken()

                                continue
                            elif token.text == ")":
                                break
                            else:
                                return False
                        else:
                            return False

                    token = lexer.nextToken()

                    if token.text == "VALUES":
                        token = lexer.nextToken()
                        if token.text == "(":
                            token = lexer.nextToken()

                            while token.text != ")":
                                if token.type == "VALUE":
                                    token = lexer.nextToken()

                                    if token.text == ",":
                                        token = lexer.nextToken()

                                        continue
                                    elif token.text == ")":
                                        break
                                    else:
                                        return False
                                else:
                                    return False

                            token = lexer.nextToken()

                            if token.text == ";":
                                if recursiveDescentParser(lexer):
                                    return True
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
            else:
                return False
        else:
            return False
    elif token.text == "":
        return True
    else:
        return False


def recognizeWhere(token, lexer):
    if token.text == "WHERE":
        token = lexer.nextToken()
        if token.type == "ID":
            token = lexer.nextToken()
            if token.text == "=" or token.text == ">" or token.text == "<" or token.text == ">=" or token.text == "<=" or token.text == "!=":
                token = lexer.nextToken()
                if token.type == "VALUE":
                    token = lexer.nextToken()

                    if token.text == ";":
                        if recursiveDescentParser(lexer):
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def recognizeFrom(token, lexer):
    if token.text == "FROM":
        token = lexer.nextToken()
        if token.type == "ID":
            return True
        else:
            return False
    else:
        return False


def recognizeSelect(token, lexer):
    if token.text == "SELECT":
        token = lexer.nextToken()
        if token.text == "*":
            token = lexer.nextToken()

            if recognizeFrom(token, lexer):
                token = lexer.nextToken()

                if token.text == "ORDER":
                    token = lexer.nextToken()
                    if token.text == "BY":
                        token = lexer.nextToken()
                        if token.type == "ID":
                            token = lexer.nextToken()

                            if token.text == ";":
                                if recursiveDescentParser(lexer):
                                    return True
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                elif token.text == "WHERE":
                    return recognizeWhere(token, lexer)
                elif token.text == ";":
                    if recursiveDescentParser(lexer):
                        return True
                    else:
                        return False

                return False
        while token.text != "FROM":
            if token.type == "ID":
                token = lexer.nextToken()
                if token.text == ",":
                    token = lexer.nextToken()
                elif token.text == "FROM":
                    break
                else:
                    return False
            else:
                return False
        if token.text == "FROM":
            token = lexer.nextToken()
            if token.type == "ID":
                token = lexer.nextToken()

                if token.text == ";":
                    if recursiveDescentParser(lexer):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    lexer = Lexer('CREATE DATABASE jogadores;' +
                                       'USE jogadores;' +
                                       'CREATE TABLE jogadores (nome string, idade int, CPF int);' +
                                       'INSERT INTO jogadores (nome, idade, CPF) VALUES ("josicreuson", 1900, 00000000011);' +
                                       'SELECT * FROM jogadores;' +
                                       'SELECT nome, idade FROM jogadores;' +
                                       'SELECT * FROM jogadores ORDER BY nome;' +
                                       'SELECT * FROM jogadores WHERE idade > 9023;' +
                                       'UPDATE jogadores SET nome = "josicreuson" WHERE nome = "victor";' +
                                       'DELETE FROM jogadores WHERE nome = "amarildo";TRUNCATE TABLE jogadores;')
    print(recursiveDescentParser(lexer))
    print(lexer.tokens)
