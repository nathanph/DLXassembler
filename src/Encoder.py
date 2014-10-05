__author__ = 'Nathan Hernandez'


class Encoder:

    def __init__(self, instructions):
        self.instructions = instructions
        self.lineNumber = 0x0
        self.labels = {}
        self.firstPass()

    def firstPass(self):
        for instruction in self.instructions:
            labelDeclaration = instruction.labelDeclaration()
            if(labelDeclaration is not None):
                self.labels[labelDeclaration] = self.lineNumber
                self.lineNumber+=4
                continue
            if(instruction.mnemonic() is not None):
                self.lineNumber+=4
                continue
        self.lineNumber = 0x0

    def encode(self):
        for instruction in self.instructions:
            lineNumber = '{:08x}'.format(self.lineNumber)
            labelAddress = 0

            if len(instruction.tokens) <= 1:
                continue

            if instruction.label():
                labelAddress = self.labels[instruction.label()]

            print(lineNumber + ": " + instruction.encode(labelAddress, self.lineNumber) + "\t#" + instruction.__str__())

            labelDeclaration = instruction.labelDeclaration()
            if(labelDeclaration is not None):
                self.labels[labelDeclaration] = self.lineNumber
                self.lineNumber+=4
                continue
            if(instruction.mnemonic() is not None):
                self.lineNumber+=4
                continue

            # print('{:08x}: {1}\t#{2}'.format(self.lineNumber, instruction.encode(), instruction.__str__()))
            # print(instruction.encode() + "\t# " + instruction.__str__())
