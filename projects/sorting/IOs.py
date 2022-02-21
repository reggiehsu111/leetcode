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
			self.parseList(line)
		elif self.mode == "LinkedList":
			self.parseLinkedList(line) 
		assert self.contents
		return self.contents

	def parseList(self, line):
		self.contents = [int(x.strip()) for x in line[1:-2].split(',')]
		return self.contents

	def parseLinkedList(self, line):
		self.parseList(line)
		self.contents = constructLinkedList(self.contents)
		return self.contents
		
