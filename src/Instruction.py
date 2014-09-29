__author__ = 'Nathan Hernandez'

from abc import ABCMeta, abstractmethod


class Instruction(object):
    __metaclass__ = ABCMeta

    def __init__(self, opcode, encoding, function_code=None):
        self.opcode = opcode
        self.encoding = encoding
        self.function_code = function_code
        pass

    @abstractmethod
    def encode(self):
        pass

    def __str__(self):
        str = "Opcode:\t\t\t" + self.opcode.upper() + "\n"
        str += "Encoding:\t\t" + hex(self.encoding) + "\n"
        str += "Function Code:\t" + hex(self.function_code) + "\n" if (self.function_code is not None) else ""
        return str
