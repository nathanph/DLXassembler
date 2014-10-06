__author__ = 'Nathan Hernandez'


class Encoder:
    def __init__(self, instructions):
        self.instructions = instructions
        self.lineNumber = 0x0
        self.labels = {}
        self.firstPass()
        self.encoding = ""


    def align(self, instruction):
        align = instruction.numeric()
        mask = 0xFFFFFFFF >> (32 - align)
        # print('{:08x}'.format(mask))
        if (self.lineNumber & mask == 0):
            return
        else:
            self.lineNumber &= ~mask
            self.lineNumber += (1 << align)
            # print('{:08x}'.format(self.lineNumber))

    def asciiz(self, instruction):
        encodings = instruction.encode()
        ret = ""
        for encoding in encodings:
            lineNumber = '{:08x}'.format(self.lineNumber)
            ret += lineNumber + ": " + encoding + "\t#" + instruction.__str__() + "\n"
            # print("Length: " + str(int(len(encoding)/2)))
            # print("lineNumber: " + hex(self.lineNumber))
            self.lineNumber += int(len(encoding) / 2)
        return ret

    def word(self, instruction):
        encodings = instruction.encode()
        ret = ""
        for encoding in encodings:
            lineNumber = '{:08x}'.format(self.lineNumber)
            ret += lineNumber + ": " + encoding + "\t#" + instruction.__str__() + "\n"
            self.lineNumber += 4
        return ret

    def space(self, instruction):
        space = instruction.numeric()
        self.lineNumber += space

    def double(self, instruction):
        encodings = instruction.encode()
        ret = ""
        for encoding in encodings:
            lineNumber = '{:08x}'.format(self.lineNumber)
            ret += lineNumber + ": " + encoding + "\t#" + instruction.__str__() + "\n"
            self.lineNumber += int(len(encoding) / 2)
        return ret

    def float(self, instruction):
        encodings = instruction.encode()
        ret = ""
        for encoding in encodings:
            lineNumber = '{:08x}'.format(self.lineNumber)
            ret += lineNumber + ": " + encoding + "\t#" + instruction.__str__() + "\n"
            self.lineNumber += int(len(encoding) / 2)
        return ret

    def text(self, instruction):
        numeric = instruction.numeric()
        if numeric is not None:
            self.lineNumber = instruction.numeric()
        else:
            self.lineNumber = 0

    def data(self, instruction):
        numeric = instruction.numeric()
        if numeric is not None:
            self.lineNumber = instruction.numeric()
        else:
            self.lineNumber = 0x200

    def firstPass(self):
        for instruction in self.instructions:
            directive = instruction.directive()
            if directive:
                if directive == '.align':
                    self.align(instruction)
                    # continue
                elif directive == '.space':
                    self.space(instruction)
                    # continue
                elif directive == '.text':
                    self.text(instruction)
                    # continue
                elif directive == '.data':
                    self.data(instruction)
                    # continue

            # Ignore comments
            if len(instruction.tokens) <= 1 and instruction.comment():
                continue

            labelDeclaration = instruction.labelDeclaration()
            if (labelDeclaration is not None):
                self.labels[labelDeclaration] = self.lineNumber
                if directive is None:
                    self.lineNumber += 4
                continue
            if (instruction.mnemonic() is not None):
                if directive is None:
                    self.lineNumber += 4
                continue

            if directive == '.asciiz':
                self.asciiz(instruction)
                # continue
            elif directive == '.word':
                self.word(instruction)
                # continue
            elif directive == '.double':
                self.double(instruction)
                # continue
            elif directive == '.float':
                self.float(instruction)
                # continue
        self.lineNumber = 0x0


    def encode(self):
        ret = ""
        for instruction in self.instructions:
            directive = instruction.directive()
            if directive:
                if directive == '.align':
                    self.align(instruction)
                    continue
                elif directive == '.asciiz':
                    ret += self.asciiz(instruction)
                    continue
                elif directive == '.word':
                    ret += self.word(instruction)
                    continue
                elif directive == '.space':
                    self.space(instruction)
                    continue
                elif directive == '.double':
                    ret += self.double(instruction)
                    continue
                elif directive == '.float':
                    ret += self.float(instruction)
                    continue
                elif directive == '.text':
                    self.text(instruction)
                    continue
                elif directive == '.data':
                    self.data(instruction)
                    continue

            lineNumber = '{:08x}'.format(self.lineNumber)
            labelAddress = None

            # Ignore comments
            if len(instruction.tokens) <= 1 and instruction.comment():
                continue

            # If the instruction contains a label then set the labelAddress
            if instruction.label():
                labelAddress = self.labels[instruction.label()]

            # Build the encoding
            ret += lineNumber + ": " + instruction.encode(labelAddress,
                                                          self.lineNumber) + "\t#" + instruction.__str__() + "\n"

            # Print for debugging
            # print(lineNumber + ": " + instruction.encode(labelAddress,
            #                                              self.lineNumber) + "\t#" + instruction.__str__() + "\n")

            labelDeclaration = instruction.labelDeclaration()
            if (labelDeclaration is not None):
                self.lineNumber += 4
                continue
            if (instruction.mnemonic() is not None):
                self.lineNumber += 4
                continue
        return ret
        # print('{:08x}: {1}\t#{2}'.format(self.lineNumber, instruction.encode(), instruction.__str__()))
        # print(instruction.encode() + "\t# " + instruction.__str__())
