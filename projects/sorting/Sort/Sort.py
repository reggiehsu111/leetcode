from abc import ABC, abstractmethod
import heapq

class Sorter(ABC):

    @abstractmethod
    def sort(self, alg):
        self.alg = alg
        pass

    @abstractmethod
    def quicksort(self):
        pass

    @abstractmethod
    def bubblesort(self):
        pass

    @abstractmethod
    def heapsort(self):
        pass

class ListSorter(Sorter):
    def __init__(self):
        return

    def sort(self, alg, contents):
        super().__init__()
        self.contents = contents
        if alg == "quicksort":
            self.quicksort()
        elif alg == "bubblesort":
            self.bubblesort()
        elif alg == 'heapsort':
            self.heapsort()
        return self.contents

    def quicksort(self):
        # TODO
        return

    def bubblesort(self):
        n = len(self.contents)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if self.contents[j] > self.contents[j + 1] :
                    self.contents[j], self.contents[j + 1] = self.contents[j + 1], self.contents[j]
        return

    def heapsort(self):
        h = []
        # use built-in heap for now
        heapq.heapify(self.contents)
        self.contents = [heapq.heappop(h) for i in range(len(h))]
        return

class LinkedListSorter(Sorter):
    def __init__(self):
        return

    def sort(self, alg):
        super().__init__()
        self.contents = contents
        if alg == "quicksort":
            self.quicksort()
        elif alg == "bubblesort":
            self.bubblesort()
        return self.contents

    def quicksort(self):
        # TODO
        return

    def bubblesort(self):
        # TODO
        return
