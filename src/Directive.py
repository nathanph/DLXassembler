__author__ = 'Nathan Hernandez'

from src.Instruction import Instruction
import binascii
import struct


class Directive(Instruction):
    def __init__(self):
        if self.directive() == ".asciiz":
            self.__class__ = Asciiz
        elif self.directive() == ".word":
            self.__class__ = Word
        elif self.directive() == '.double':
            self.__class__ = Double
        elif self.directive() == '.float':
            self.__class__ = Float


class Asciiz(Directive):
    def encode(self, labelAddress=None, currentAddress=None):
        encodings = []
        for string in self.strings():
            encodings.append("".join("{:02x}".format(ord(c)) for c in string))
        return encodings


class Word(Instruction):
    def encode(self, labelAddress=None, currentAddress=None):
        encodings = []
        numericMask = 0xFFFFFFFF
        for numeric in self.numerics():
            numeric &= numericMask
            encodings.append('{:08x}'.format(numeric))
        return encodings

class Double(Instruction):
    def encode(self, labelAddress=None, currentAddress=None):
        encodings = []
        for float in self.floats():
            encodings.append(hex(struct.unpack('<Q', struct.pack('<d', float))[0])[2:])
        return encodings

class Float(Instruction):
    def encode(self, labelAddress=None, currentAddress=None):
        encodings = []
        for float in self.floats():
            encodings.append(hex(struct.unpack('<I', struct.pack('<f', float))[0])[2:])
        return encodings