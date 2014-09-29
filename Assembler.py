__author__ = 'Nathan Hernandez'

import sys
from Rtype import Rtype
from Jtype import Jtype
from DLEX import Lexer
import ply.yacc as yacc
import ply.lex as lex

from calc import MyLexer


def main():
    # rTest = Rtype("nop", 0, 0)
    # jTest = Jtype("j", 2)
    # print(sys.argv)
    # print(rTest)
    # print(jTest)
    data = "TEST TEST TEST"
    # lexer = Lexer()
    l = MyLexer()
    l.build()
    l.test("3 + 4")


if __name__ == "__main__":
    main()