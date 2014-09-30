__author__ = 'Nathan Hernandez'

import ply.lex as lex


class Lexer:
    # List of token names.
    tokens = (
        'OPCODE',
        'REGISTER',
        'DECIMAL',
        'OCTAL',
        'HEXADECIMAL',
        'DIRECTIVE',
        'LABEL',
        'COMMA',
        'COMMENT',
        'LPAREN',
        'RPAREN',
    )
    # Precedence of tokens.
    # precedence = ()

    # Regular expression rules for simple tokens.
    t_COMMA = r'\,'
    t_COMMENT = r';.*'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'

    def t_LABEL(self, t):
        r'[a-zA-Z][a-zA-Z0-9]*:'
        t.value = t.value[:-1]
        return t

    def t_REGISTER(self, t):
        r'\b[Rr]([0-9]|[1-2][0-9]|3[0-1])\b'
        t.value = int(t.value[1:])
        return t

    def t_OPCODE(self, t):
        r'[a-zA-Z][a-zA-Z0-9]+'
        return t

    def t_DECIMAL(self, t):
        r'\b([0-9]|[1-9][0-9]*)\b'
        return t

    def t_OCTAL(self, t):
        r'\b0[1-7][0-7]*\b'
        return t

    def t_HEXADECIMAL(self, t):
        r'0x[0-9a-fA-F]+'
        return t

    def t_DIRECTIVE(self, t):
        r'(\.[a-zA-Z]+) '
        return t

    # A string containing ignored characters (spaces, tabs, newlines, and commas)
    t_ignore = ' \t\n,'

    # Error handling rule
    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer
    def __init__(self):
        self.lexer = lex.lex(module=self)

    # Test output
    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok: break
            print(tok)

            # Regular expression rules for simple tokens
            # def t_OPCODE(t):
            # r'\+'
