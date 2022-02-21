from Report import Report

def sort(contents, mode="LinkedList"):
	# TODO: Sort the contents
	return

class Sorter:
	def __init__(self, contents, mode):
		'''
		contents: array or linked list
		mode: LinkedList or normal python list
		'''
		self.contents = contents
		self.mode = mode
		self.report = Report()

	def sort(self, alg):
		if alg == "quicksort":
			self.quicksort()
		elif alg == "bubblesort":
			self.bubblesort()
		self.report_time()
		return self.contents
	def quicksort(self):
		# TODO
		return

	def bubblesort(self):
		if self.mode == "List":
			n = len(self.contents)
			for i in range(n-1):
				for j in range(0, n-i-1):
					if self.contents[j] > self.contents[j + 1] :
						self.contents[j], self.contents[j + 1] = self.contents[j + 1], self.contents[j]
			return

	def report_time(self):
		# TODO
		return
