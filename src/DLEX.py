__author__ = 'Nathan Hernandez'

import ply.lex as lex
import ply.yacc as yacc


class Lexer:
    # List of token names.
    tokens = (
        'OPCODE',
        # 'REGISTER',
        # 'DECIMAL',
        # 'OCTAL',
        # 'HEXADECIMAL',
        # 'DIRECTIVE',
        # 'LABEL',
        # 'COMMA',
    )

    # precedence = ()

    def __init__(self):
        lex.lex(module=self)
        lex.input("test data")
        print(lex.token())
        pass

    # Regular expression rules for simple tokens
    def t_OPCODE(t):
        r'\+'
