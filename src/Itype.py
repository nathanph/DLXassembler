__author__ = 'Nathan Hernandez'

from src.Instruction import Instruction


class Itype(Instruction):
    def __init__(self):
        registers = self.registers()
        if self.offset():
            self.__class__ = RegisterOffset
        elif self.mnemonic()[0].upper() == 'B':
            self.__class__ = Branch
        elif self.mnemonic().upper() == 'TRAP':
            self.__class__ = Trap
        elif len(self.registers()) == 2 and self.label():
            self.__class__ = TwoRegisterLabel
        elif len(self.registers()) == 1 and self.label():
            self.__class__ = RegisterLabel
        elif len(self.registers()) == 2 and self.numeric():
            self.__class__ = TwoRegisterNumeric
        elif len(self.registers()) == 1 and self.numeric():
            self.__class__ = RegisterNumeric


    def opcode(self):
        return int(self.iTypes[self.mnemonic()][0])

    def encode(self, labelAddress=None, currentAddress=None):
        for token in self.tokens:
            if token.type == 'REGISTER':
                print("R" + str(token.value), end=" ")


class TwoRegisterNumeric(Itype):
    def encode(self, labelAddress=None, currentAddress=None):
        immediateMask = 0xFFFF
        opcode = self.opcode() << (32 - 6)
        rs1 = self.register(1) << (32 - 6 - 5)
        rd = self.register(0) << (32 - 6 - 5 - 5)
        immediate = self.numeric() << (32 - 6 - 5 - 5 - 16)
        return '{:08x}'.format(opcode | rs1 | rd | immediate)


class TwoRegisterLabel(Itype):
    def encode(self, labelAddress=None, currentAddress=None):
        labelMask = 0xFFFF
        opcode = self.opcode() << (32 - 6)
        rs1 = self.register(1) << (32 - 6 - 5)
        rd = self.register(0) << (32 - 6 - 5 - 5)
        label = labelAddress << (32 - 6 - 5 - 5 - 16) & labelMask
        return '{:08x}'.format(opcode | rs1 | rd | label)


class RegisterNumeric(Itype):
    def encode(self, labelAddress=None, currentAddress=None):
        pass


class RegisterOffset(Itype):
    def encode(self, labelAddress=None, currentAddress=None):
        pass


class RegisterLabel(Itype):
    def encode(self, labelAddress=None, currentAddress=None):
        labelMask = 0xFFFF
        opcode = self.opcode() << (32 - 6)
        rs1 = self.register(0) << (32 - 6 - 5)
        unused = 0 << (32 - 6 - 5 - 5)
        label = labelAddress << (32 - 6 - 5 - 5 - 16) & labelMask
        return '{:08x}'.format(opcode | rs1 | unused | label)


class Trap(Itype):
    def encode(self, labelAddress=None, currentAddress=None):
        pass


class Branch(Itype):
    def encode(self, labelAddress=None, currentAddress=None):
        labelMask = 0xFFFF
        currentAddress += 4
        offset = labelAddress - currentAddress
        opcode = self.opcode() << (32 - 6)
        rs1 = self.register(0) << (32 - 6 - 5)
        unused = 0 << (32 - 6 - 5 - 5)
        offset = offset << (32 - 6 - 5 - 5 - 16) & labelMask
        return '{:08x}'.format(opcode | rs1 | unused | offset)