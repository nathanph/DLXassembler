__author__ = 'Nathan Hernandez'

import sys
# from Rtype import Rtype
# from Jtype import Jtype
from Instruction import Instruction
from Dlexer import Lexer
import ply.yacc as yacc
import ply.lex as lex
from Dlexer import Lexer

from calc import MyLexer


def main():
    data = 'label2: jalr R0, label3, 4\njalr test test 0x45\nnop\n.asciiz "This is a string! Hello world!"'

    file = open('inputs/data.dlx', 'r')
    data = file.read()
    print(data)
    print()

    lexer = Lexer()
    # lexer.test(data)
    lexer.input(data)

    tokens = []
    instructions = []

    # Generate instructions from tokens.
    while True:
        tok = lexer.token()
        if not tok:
            break
        if tok.type != 'EOL':
            tokens.append(tok)
        else:
            print(tokens)
            instructions.append(Instruction(tokens.copy()))
            tokens.clear()
    # instructions.append(Instruction(tokens.copy()))
    print(tokens)



    for instruction in instructions:
        # if instruction.isItype():
        #     print(instruction.opcode() + " ITYPE")
        # elif instruction.isJtype():
        #     print(instruction.opcode() + " JTYPE")
        # elif instruction.isRtype():
        #     print(instruction.opcode() + " RTYPE")
        print(instruction.__class__)
        instruction.encode()
        print()


if __name__ == "__main__":
    main()