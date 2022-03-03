from Sort.Sort import Sorter, ListSorter, LinkedListSorter
from IOs import ArrayParser
from Report import Report
from randInputGenerator import randListGenerator

class Expr:
    def __init__(self, args):
        self.args = args
        self.expr_name = args.expr_name
        self.report = Report(self.args)
        if args.mode == 'List':
            self.sorter = ListSorter()
        elif args.mode == 'LinkedList':
            self.sorter = LinkedListSorter()

        self.RIG = randListGenerator(10**self.args.max_exponent)
        self.AP = ArrayParser(self.args.mode)
        return

    def run(self):
        for x in range(self.args.max_exponent):
            contents = self.RIG.gen(10**x)
            if self.args.mode == 'LinkedList':
                contents = self.AP.parseList2LinkedList(contents)
            print(contents)
            self.report.start_report()
            contents = self.sorter.sort(self.args.alg, contents)
            self.report.record_event(str(x))
        self.report.output_events()

