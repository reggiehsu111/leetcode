'''
Class to report algorithm running time 
'''
from time import time

class Report:
    def __init__(self, args):
        self.records = {}
        self.args = args
        self.o_file = 'Experiments/'+self.args.expr_name+'_'+self.args.mode+'.txt'

    def start_report(self):
        self.start_time = time()

    def record_event(self, event):
        self.records[event] = time() - self.start_time 

    def output_events(self):
        for r in self.records:
            print("Log list length: " + r, ':', self.records[r])
        self.output_file()

    def output_file(self):
        with open(self.o_file, 'w') as f:
            for r in self.records:
                f.write(str(self.records[r]) + '\n')

