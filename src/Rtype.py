__author__ = 'Nathan Hernandez'

from src.Instruction import Instruction


class Rtype(Instruction):
    def __init__(self):
        registers = self.registers()
        if len(registers) == 3:
            self.__class__ = ThreeRegister
        elif len(registers) == 2:
            self.__class__ = TwoRegister
        elif len(registers) == 0:
            self.__class__ = NoRegister


    def encode(self, labelAddress=None, currentAddress=None ):
        for token in self.tokens:
            if token.type == 'REGISTER':
                print("R" + str(token.value), end=" ")

    def opcode(self):
        return int(self.rTypes[self.mnemonic()][0])

    def functionCode(self):
        return int(self.rTypes[self.mnemonic()][1])


class ThreeRegister(Rtype):
    def encode(self, labelAddress=None, currentAddress=None):
        # mnemonic = self.mnemonic()
        # registers = self.registers()
        # print(mnemonic + ": " + str(self.opcode()) + " " + str(registers[0].value) + " " + str(registers[1].value)
        # + " " + str(registers[2].value) + " " + str(self.functionCode()))
        opcode = self.opcode() << (32 - 6)
        rs1 = self.register(1) << (32 - 6 - 5)
        rs2 = self.register(2) << (32 - 6 - 5 - 5)
        rd = self.register(0) << (32 - 6 - 5 - 5 - 5)
        unused = 0 << (32 - 6 - 5 - 5 - 5 - 6)
        func = self.functionCode() << (32 - 6 - 5 - 5 - 5 - 6 - 5)
        return '{:08x}'.format(opcode | rs1 | rs2 | rd | unused | func)


class TwoRegister(Rtype):
    def encode(self, labelAddress=None, currentAddress=None):
        # mnemonic = self.mnemonic()
        # registers = self.registers()
        # print(mnemonic + ": " + str(self.opcode()) + " " + str(registers[0].value) + " " + str(registers[1].value)
        # + " " + str(self.functionCode()))
        opcode = self.opcode() << (32 - 6)
        rs1 = self.register(1) << (32 - 6 - 5)
        unused = 0 << (32 - 6 - 5 - 5)
        rd = self.register(0) << (32 - 6 - 5 - 5 - 5)
        unused |= 0 << (32 - 6 - 5 - 5 - 5 - 6)
        func = self.functionCode() << (32 - 6 - 5 - 5 - 5 - 6 - 5)
        return '{:08x}'.format(opcode | rs1 | unused | rd | unused | func)


class NoRegister(Rtype):
    def encode(self, labelAddress=None, currentAddress=None):
        # mnemonic = self.mnemonic()
        # print(mnemonic + ": " + str(self.opcode()) + " " + str(self.functionCode()))
        # opcode = self.opcode() << (32 - 6)
        # unused = 0
        # func = self.functionCode() << (32 - 6 - 5 - 5 - 5 - 5 - 5)
        return '{:08x}'.format(0)