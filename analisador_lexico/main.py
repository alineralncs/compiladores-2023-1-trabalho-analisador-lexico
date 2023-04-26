from scanner import Scanner
from scanner import *


if __name__ == '__main__':
    file_code_font = 'code_font.c'

    scanner = Scanner(file_code_font)
    tokens, errors = scanner.analyse()

    print("\nTokens Válidos \n")
    for token in tokens:
        print('<{}, {}>'.format(token[0], token[1]))

    # print("\nTokens Inválidos: \n")
    # for error in errors:
    #     print(errors[error])
