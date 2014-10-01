__author__ = 'Nathan Hernandez'

from Instruction import Instruction


class Itype(Instruction):
    def encode(self):
        for token in self.tokens:
            if token.type == 'REGISTER':
                print("R"+str(token.value),end=" ")