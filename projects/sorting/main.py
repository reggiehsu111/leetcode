from IOs import readInputs
from Sort import Sorter 

def main():
	filename = "input.txt"
	mode = "List"
	alg = "bubblesort"
	contents = readInputs(filename, mode)
	print(contents)
	sorter = Sorter(contents, mode)
	contents = sorter.sort(alg)
	print(contents)
	

if __name__ == "__main__":
	main()
