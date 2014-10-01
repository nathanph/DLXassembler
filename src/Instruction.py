__author__ = 'Nathan Hernandez'

from abc import ABCMeta, abstractmethod


class Instruction(object):
    __metaclass__ = ABCMeta

    # def __init__(self, opcode, encoding, function_code=None):
    # self.opcode = opcode
    # self.encoding = encoding
    # self.function_code = function_code

    iTypes = {}
    jTypes = {}
    rTypes = {}

    iFile = open('./data/Itypes', 'r')
    rFile = open('./data/Rtypes', 'r')
    jFile = open('./data/Jtypes', 'r')

    for line in iFile:
        words = line.split()
        iTypes[words[0]] = (words[1],)

    for line in jFile:
        words = line.split()
        jTypes[words[0]] = (words[1],)

    for line in rFile:
        words = line.split()
        rTypes[words[0]] = (words[1], words[2])

    def __init__(self, tokens):
        from Itype import Itype
        from Jtype import Jtype
        from Rtype import Rtype
        from Directive import Directive

        self.tokens = tokens
        if self.isItype():
            self.__class__ = Itype
        elif self.isJtype():
            self.__class__ = Jtype
        elif self.isRtype():
            self.__class__ = Rtype
        elif self.directive() is not None:
            self.__class__ = Directive


    @abstractmethod
    def encode(self):
        pass

    # def __str__(self):
    # str = "Opcode:\t\t\t" + self.opcode.upper() + "\n"
    #     str += "Encoding:\t\t" + hex(self.encoding) + "\n"
    #     str += "Function Code:\t" + hex(self.function_code) + "\n" if (self.function_code is not None) else ""
    #     return str

    # Return the OPCODE token.
    def opcode(self):
        for token in self.tokens:
            if token.type == 'OPCODE':
                return token.value
        return None

    def isItype(self):
        opcode = self.opcode()
        for iType in self.iTypes:
            if opcode == iType:
                return True
        return False

    def isJtype(self):
        opcode = self.opcode()
        for jType in self.jTypes:
            if opcode == jType:
                return True
        return False

    def isRtype(self):
        opcode = self.opcode()
        for rType in self.rTypes:
            if opcode == rType:
                return True
        return False

    def directive(self):
        for token in self.tokens:
            if token.type == 'DIRECTIVE':
                return token.value
        return None

    def labelDeclaration(self):
        for token in self.tokens:
            if token.type == 'LABEL_DECLARATION':
                return token.value
        return None

    def comment(self):
        for token in self.tokens:
            if token.type == 'COMMENT':
                return token.value
        return None

    def __str__(self):
        ret = ''
        for token in self.tokens:
            if token.type == 'REGISTER':
                ret += 'R' + str(token.value) + " "
            else:
                ret += token.value + " "
        return ret