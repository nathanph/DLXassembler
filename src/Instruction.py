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
        from src.Itype import Itype
        from src.Jtype import Jtype
        from src.Rtype import Rtype
        from src.Directive import Directive

        self.tokens = tokens
        if self.isItype():
            self.__class__ = Itype
            self.__init__()
        elif self.isJtype():
            self.__class__ = Jtype
            self.__init__()
        elif self.isRtype():
            self.__class__ = Rtype
            self.__init__()
        elif self.directive() is not None:
            self.__class__ = Directive
            self.__init__()


    @abstractmethod
    def encode(self, labelAddress=None, currentAddress=None):
        pass

    @abstractmethod
    def opcode(self):
        pass

    # def __str__(self):
    # str = "Opcode:\t\t\t" + self.opcode.upper() + "\n"
    # str += "Encoding:\t\t" + hex(self.encoding) + "\n"
    # str += "Function Code:\t" + hex(self.function_code) + "\n" if (self.function_code is not None) else ""
    # return str

    # Return the OPCODE token.
    def mnemonic(self):
        for token in self.tokens:
            if token.type == 'OPCODE':
                return token.value
        return None

    def isItype(self):
        mnemonic = self.mnemonic()
        for iType in self.iTypes:
            if mnemonic == iType:
                return True
        return False

    def isJtype(self):
        mnemonic = self.mnemonic()
        for jType in self.jTypes:
            if mnemonic == jType:
                return True
        return False

    def isRtype(self):
        mnemonic = self.mnemonic()
        for rType in self.rTypes:
            if mnemonic == rType:
                return True
        # Check for NOP
        if self.labelDeclaration() and self.mnemonic() is None and self.directive() is None:
            return True
        return False

    def directive(self):
        for token in self.tokens:
            if token.type == 'DIRECTIVE':
                return token.value
        return None

    def label(self):
        for token in self.tokens:
            if token.type == 'LABEL':
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

    def registers(self):
        registers = []
        for token in self.tokens:
            if token.type == 'REGISTER' or token.type == 'FP_REGISTER':
                registers.append(token)
        return registers

    def register(self, num):
        registers = self.registers()
        return int(registers[num].value)

    def offset(self):
        for token in self.tokens:
            if token.type == 'RPAREN':
                return True
        return None

    def strings(self):
        strings = []
        for token in self.tokens:
            if token.type == 'STRING':
                strings.append(token.value+"\0")
        return strings

    def patternMatch(self, tokenTypes):
        matchIndex = 0
        for token in self.tokens:
            if(matchIndex>=len(tokenTypes)):
                break
            if tokenTypes[matchIndex] == 'NUMERIC':
                if token.type == 'DECIMAL' or token.type == 'HEXADECIMAL' or token.type == 'OCTAL':
                    matchIndex += 1
            elif tokenTypes[matchIndex] == 'REGISTER':
                if token.type == 'REGISTER' or token.type == 'FP_REGISTER':
                    matchIndex += 1
            elif token.type == tokenTypes[matchIndex]:
                matchIndex+=1
        if matchIndex == len(tokenTypes):
            return True
        return False

    def numeric(self):
        for token in self.tokens:
            if token.type == 'DECIMAL':
                return int(token.value)
            elif token.type == 'HEXADECIMAL':
                return int(token.value,16)
            elif token.type == 'OCTAL':
                return int(token.value,8)
        return None

    def numerics(self):
        numerics = []
        for token in self.tokens:
            if token.type == 'DECIMAL':
                numerics.append(int(token.value))
            elif token.type == 'HEXADECIMAL':
                numerics.append(int(token.value,16))
            elif token.type == 'OCTAL':
                numerics.append(int(token.value,8))
        return numerics

    def floats(self):
        floats = []
        for token in self.tokens:
            if token.type == 'FLOAT':
                floats.append(float(token.value))
        return floats

    def __str__(self):
        ret = ''
        for token in self.tokens:
            if token.type == 'OPCODE':
                ret += token.value + " "
            elif token.type == 'LABEL_DECLARATION':
                ret += token.value + ": "
            elif token.type == 'REGISTER':
                ret += 'R' + str(token.value) + " "
            elif token.type == 'FP_REGISTER':
                ret += 'F' + str(token.value) + " "
            elif token.type == 'LPAREN':
                ret += '('
            elif token.type == 'RPAREN':
                ret += ')'
            elif token.type == 'FLOAT':
                ret += str(token.value) + " "
            elif token.type == 'HEXADECIMAL':
                ret += str(token.value) + " "
            elif token.type == 'DECIMAL':
                ret += str(token.value) + " "
            elif token.type == 'OCTAL':
                ret += str(token.value) + " "
            else:
                ret += token.value + " "
        return ret