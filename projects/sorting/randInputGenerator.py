import random

class randListGenerator:
	def __init__(self, Max=10000, Min=0):
		self.randlist = []
		self.max = Max
		self.min = Min
		self.outputFilename = ""
		return

	def gen(self, num, Max=None, Min=None):
		if Max!=None:
			self.max = Max
		if Min!=None:
			self.min = Min
		self.randlist = random.sample(range(self.min, self.max), num)
		return self.randlist	

	def outputFile(self, filename=None):
		if filename!=None:
			self.outputFilename = filename
		outputStr = "["
		for x in self.randlist:
			outputStr += (str(x) + ",")
		outputStr = outputStr[:-2] + "]"
		with open(self.outputFilename, "w") as f:
			f.write(outputStr+'\n')

if __name__ == "__main__":
	rlg = randListGenerator()
	randlist = rlg.gen(10)
	rlg.outputFile("input.txt")
