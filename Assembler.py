__author__ = 'Nathan Hernandez'

import sys
from Rtype import Rtype
from Jtype import Jtype
from Dlexer import Lexer
import ply.yacc as yacc
import ply.lex as lex
from Dlexer import Lexer

from calc import MyLexer


def main():
    # rTest = Rtype("nop", 0, 0)
    # jTest = Jtype("j", 2)
    # print(sys.argv)
    # print(rTest)
    # print(jTest)
    data = "add R0, 5(r1)"
    # lexer = Lexer()
    # l = MyLexer()
    # l.build()
    # l.test("3 + 4")
    file = open('inputs/intShift.dlx', 'r')
    # data = file.read()
    print(data)

    lexer = Lexer()
    lexer.test(data)

if __name__ == "__main__":
    main()