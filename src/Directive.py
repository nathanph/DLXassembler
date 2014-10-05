__author__ = 'Nathan Hernandez'

from src.Instruction import Instruction


class Directive(Instruction):
    def encode(self):
        for token in self.tokens:
            if token.type == 'STRING':
                print(token.value + " ")
            else:
                print(token.value)
        pass

