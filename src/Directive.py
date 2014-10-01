__author__ = 'Nathan Hernandez'

from Instruction import Instruction


class Directive(Instruction):
    def encode(self):
        for token in self.tokens:
            if token.type == 'STRING':
                print(token.value + " ")
        pass