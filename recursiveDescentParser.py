from lexParser import Lexer

def recursiveDescentParser(lexer: Lexer) -> bool:
    token = lexer.nextToken()
    if token.text.upper() == "CREATE":
        token = lexer.nextToken()
        if token.text.upper() == "DATABASE":
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
        elif token.text.upper() == "TABLE":
            token = lexer.nextToken()
            if token.type == "ID":
                token = lexer.nextToken()
                if token.text.upper() == "(":
                    token = lexer.nextToken()

                    while token.text != ")":
                        if token.type == "ID":
                            token = lexer.nextToken()

                            if token.type == "TYPE":
                                token = lexer.nextToken()

                                if token.text.upper() == ",":
                                    token = lexer.nextToken()

                                    continue
                                elif token.text.upper() == ")":
                                    break
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False

                    token = lexer.nextToken()

                    if token.text.upper() == ";":
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
    elif token.text.upper() == "USE":
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
    elif token.text.upper() == "UPDATE":
        token = lexer.nextToken()
        if token.type == "ID":
            token = lexer.nextToken()
            if token.text.upper() == "SET":
                token = lexer.nextToken()
                if token.type == "ID":
                    token = lexer.nextToken()
                    if token.text.upper() == "=":
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
    elif token.text.upper() == "SELECT":
        return recognizeSelect(token, lexer)
    elif token.text.upper() == "DELETE":
        token = lexer.nextToken()
        if token.text.upper() == "FROM":
            token = lexer.nextToken()
            if token.type == "ID":
                token = lexer.nextToken()
                if token.text.upper() == "WHERE":
                    return recognizeWhere(token, lexer)
            else:
                return False
        else:
            return False
    elif token.text.upper() == "TRUNCATE":
        token = lexer.nextToken()
        if token.text.upper() == "TABLE":
            token = lexer.nextToken()
            if token.type == "ID":
                token = lexer.nextToken()

                if token.text.upper() == ";":
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
    elif token.text.upper() == "INSERT":
        token = lexer.nextToken()
        if token.text.upper() == "INTO":
            token = lexer.nextToken()
            if token.type == "ID":
                token = lexer.nextToken()

                if token.text.upper() == "(":
                    token = lexer.nextToken()

                    while token.text != ")":
                        if token.type == "ID":
                            token = lexer.nextToken()

                            if token.text.upper() == ",":
                                token = lexer.nextToken()

                                continue
                            elif token.text.upper() == ")":
                                break
                            else:
                                return False
                        else:
                            return False

                    token = lexer.nextToken()

                    if token.text.upper() == "VALUES":
                        token = lexer.nextToken()
                        if token.text.upper() == "(":
                            token = lexer.nextToken()

                            while token.text != ")":
                                if token.type == "VALUE":
                                    token = lexer.nextToken()

                                    if token.text.upper() == ",":
                                        token = lexer.nextToken()

                                        continue
                                    elif token.text.upper() == ")":
                                        break
                                    else:
                                        return False
                                else:
                                    return False

                            token = lexer.nextToken()

                            if token.text.upper() == ";":
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
    elif token.text.upper() == "":
        return True
    elif token.text.upper() == ";":
        return True
    else:
        return False


def recognizeWhere(token, lexer):
    if token.text.upper() == "WHERE":
        token = lexer.nextToken()
        if token.type == "ID":
            token = lexer.nextToken()
            if token.text.upper() == "=" or token.text.upper() == ">" or token.text.upper() == "<" or token.text.upper() == ">=" or token.text.upper() == "<=" or token.text.upper() == "!=":
                token = lexer.nextToken()
                if token.type == "VALUE":
                    token = lexer.nextToken()

                    if token.text.upper() == ";":
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
    if token.text.upper() == "FROM":
        token = lexer.nextToken()
        if token.type == "ID":
            return True
        else:
            return False
    else:
        return False


def recognizeSelect(token, lexer):
    if token.text.upper() == "SELECT":
        token = lexer.nextToken()
        if token.text.upper() == "*":
            token = lexer.nextToken()

            if recognizeFrom(token, lexer):
                token = lexer.nextToken()

                if token.text.upper() == "ORDER":
                    token = lexer.nextToken()
                    if token.text.upper() == "BY":
                        token = lexer.nextToken()
                        if token.type == "ID":
                            token = lexer.nextToken()

                            if token.text.upper() == ";":
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
                elif token.text.upper() == "WHERE":
                    return recognizeWhere(token, lexer)
                elif token.text.upper() == ";":
                    if recursiveDescentParser(lexer):
                        return True
                    else:
                        return False

                return False
        while token.text != "FROM":
            if token.type == "ID":
                token = lexer.nextToken()
                if token.text.upper() == ",":
                    token = lexer.nextToken()
                elif token.text.upper() == "FROM":
                    break
                else:
                    return False
            else:
                return False
        if token.text.upper() == "FROM":
            token = lexer.nextToken()
            if token.type == "ID":
                token = lexer.nextToken()

                if token.text.upper() == ";":
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
    lexer = Lexer('create DATABASE jogadores;' +
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
