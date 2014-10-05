__author__ = 'Nathan Hernandez'

import sys
# from Rtype import Rtype
# from Jtype import Jtype
from src.Instruction import Instruction
# from Dlexer import Lexer
# import ply.yacc as yacc
# import ply.lex as lex
from src.Dlexer import Lexer
from src.Encoder import Encoder

# from calc import MyLexer


def main():
    data = 'add R1, R2, R3\nmovf R23, R31\nnop\nlabel1: j label1\n'

    file = open('inputs/jump.dlx', 'r')
    # print(sys.argv[1])
    # file = open(sys.argv[1], 'r')
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
    print("==========")

    for instruction in instructions:
        # if instruction.isItype():
        # print(instruction.opcode() + " ITYPE")
        # elif instruction.isJtype():
        #     print(instruction.opcode() + " JTYPE")
        # elif instruction.isRtype():
        #     print(instruction.opcode() + " RTYPE")
        print(instruction.__class__)
        # instruction.encode()
        print()
    print("==========")

    encoder = Encoder(instructions)
    encoder.encode()
    print("==========")

    for label in encoder.labels:
        print(label + " : " + hex(encoder.labels[label]))


if __name__ == "__main__":
    main()