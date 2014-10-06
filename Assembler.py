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
    DEBUG = True

    data = 'add R1, R2, R3\nmovf R23, R31\nnop\nlabel1: j label1\n'

    fileName = "inputs/double1"

    if len(sys.argv) > 1:
        fileName = sys.argv[1][:-4]
        DEBUG=False

    file = open(fileName+'.dlx', 'r')

    data = file.read()
    file.close()
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
            if DEBUG:
                print(tokens)
            if(len(tokens)>0):
                instructions.append(Instruction(tokens.copy()))
            tokens.clear()
    # instructions.append(Instruction(tokens.copy()))
    if DEBUG:
        print("==========")

    for instruction in instructions:
        # if instruction.isItype():
        # print(instruction.opcode() + " ITYPE")
        # elif instruction.isJtype():
        #     print(instruction.opcode() + " JTYPE")
        # elif instruction.isRtype():
        #     print(instruction.opcode() + " RTYPE")
        if DEBUG:
            print(instruction.__class__)
            # instruction.encode()
            print()
    if DEBUG:
        print("==========")

    encoder = Encoder(instructions)
    encoding = encoder.encode()

    if DEBUG:
        print(encoding)



    if not DEBUG:
        file = open(fileName+'.hex', 'w')
        file.write(encoding)
        file.close()

    if DEBUG:
        print("==========")

    if DEBUG:
        for label in encoder.labels:
            print(label + " : " + hex(encoder.labels[label]))


if __name__ == "__main__":
    main()