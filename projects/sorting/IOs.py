from linkedList import *

def readInputs(filename, mode):
    # mode: List or LinkedList
    with open(filename, 'r') as f:
        Lines = f.readlines()
    assert len(Lines) == 1
    ap = ArrayParser(mode)
    return ap.parse(Lines[0])

class ArrayParser:
    def __init__(self, mode="List"):
        # There are 2 modes:
        # List and LinkedList
        self.mode = mode

    def parse(self, line):
        if self.mode == "List":
            self.parseStr2List(line)
        elif self.mode == "LinkedList":
            self.parseStr2LinkedList(line)
        assert self.contents
        return self.contents

    def parseStr2List(self, line):
        self.contents = [int(x.strip()) for x in line[1:-2].split(',')]
        return self.contents

    def parseList2LinkedList(self, input_list):
        self.contents = constructLinkedList(input_list)
        return self.contents

    def parseStr2LinkedList(self, line):
        self.parseStr2List(line)
        return self.parseList2LinkedList(self.contents)
