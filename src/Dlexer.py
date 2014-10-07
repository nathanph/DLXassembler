__author__ = 'Nathan Hernandez'

import ply.lex as lex


class Lexer:
    # Dictonary of reserved words. Technically all registers and opcodes would exist within this dictionary, but I
    # instead use states to accomplish proper token detection.
    # reserved = {}

    # Tuple of states.
    states = (
        # Searches for labels after OPCODE.
        ('label', 'inclusive'),
    )

    # List of token names.
    tokens = [
        'OPCODE',
        'REGISTER',
        'FP_REGISTER',
        'FLOAT',
        'DECIMAL',
        'OCTAL',
        'HEXADECIMAL',
        'DIRECTIVE',
        'LABEL',
        'LABEL_DECLARATION',
        'COMMA',
        'COMMENT',
        'LPAREN',
        'RPAREN',
        'EOL',
        'STRING',
    ]

    # Precedence of tokens.
    # precedence = ()

    # Regular expression rules for simple tokens.
    t_COMMA = r'\,'
    t_COMMENT = r';.*'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'

    # Regular expression for registers.
    # Note: ANY must be used, otherwise when the label state is entered the LABEL token will be recognized before the
    # REGISTER token.
    # TODO:: Report this as a bug. REGISTER should still be recognized first because it's declared before LABEL.
    def t_ANY_REGISTER(self, t):
        r'\b[Rr]([0-9]|[1-2][0-9]|3[0-1])\b'
        t.value = int(t.value[1:])
        return t

    # Regular expression for floating point registers.
    def t_ANY_FP_REGISTER(self, t):
        r'\b[Ff]([0-9]|[1-2][0-9]|3[0-1])\b'
        t.value = int(t.value[1:])
        return t

    # Regular expression for label declaration
    def t_LABEL_DECLARATION(self, t):
        r'[a-zA-Z][a-zA-Z0-9]*:'
        t.value = t.value[:-1]
        return t

    # Regular expression for labels.
    def t_label_LABEL(self, t):
        r'[a-zA-Z][a-zA-Z0-9]*'
        # t.type = self.reserved.get(t.value,'LABEL')
        return t

    # Regular expression for opcodes.
    def t_OPCODE(self, t):
        r'[a-zA-Z][a-zA-Z0-9]*'
        t.lexer.begin('label')
        return t

    # Regular expression for directives.
    def t_DIRECTIVE(self, t):
        r'(\.[a-zA-Z]+) '
        return t

    # Regular expression for floats.
    def t_FLOAT(self, t):
        r'[\-]{0,1}\d*\.\d*'
        return t

    # Regular expression for decimals.
    def t_DECIMAL(self, t):
        r'[\-]{0,1}\b([0-9]|[1-9][0-9]*)\b'
        return t

    # Regular expression for octals.
    def t_OCTAL(self, t):
        r'[\-]{0,1}\b0[1-7][0-7]*\b'
        return t

    # Regular expression for hexadecimals.
    def t_HEXADECIMAL(self, t):
        r'[\-]{0,1}0x[0-9a-fA-F]+'
        return t

    # Regular expression for strings.
    def t_STRING(self, t):
        r'".*?"'
        t.value = t.value[1:-1]
        return t

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        t.lexer.begin('INITIAL')
        t.type = 'EOL'
        return t

    # A string containing ignored characters (spaces, tabs, and commas).
    t_ignore = ' \t,'

    # Error handling rule.
    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer.
    def __init__(self):
        self.lexer = lex.lex(module=self)

    def token(self):
        return self.lexer.token()

    def input(self, data):
        self.lexer.input(data)

    # Test lexer input.
    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)
