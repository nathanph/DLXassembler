__author__ = 'Nathan Hernandez'

from src.Instruction import Instruction

class Jtype(Instruction):
    def __init__(self):
        pass

    def opcode(self):
        return int(self.jTypes[self.mnemonic()][0])

    def encode(self, labelAddress=None, currentAddress=None):
        offsetMask = 0x03FFFFFF
        currentAddress += 4
        offset = labelAddress - currentAddress
        opcode = self.opcode() << (32 - 6)
        offset = offset << (32 - 6 - 26) & offsetMask
        return  '{:08x}'.format(opcode | offset)
