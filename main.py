from lexParser import Lexer

def recursiveDescentParser(text):
    lexer = Lexer(text)

    token = lexer.nextToken()
    print(token)
    if token.text == "CREATE":
        token = lexer.nextToken()
        if token.text == "DATABASE":
            token = lexer.nextToken()
            if token.type == "ID":
                if lexer.nextToken().text == ";":
                    return True
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
                        return True
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
                return True
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
                    return True
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
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                elif token.text == "WHERE":
                    return recognizeWhere(token, lexer)
                elif token.text == ";":
                    return True

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
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    print(recursiveDescentParser('DELETE FROM jogadores WHERE nome = "amarildo"'))