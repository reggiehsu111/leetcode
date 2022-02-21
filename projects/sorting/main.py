from os import path

from IOs import readInputs
from Sort.Sort import Sorter
from utils.parser import ConfigParser
from Report import Report
from Experiments.expr import Expr

parser = ConfigParser(description="Sort Lab")
parser.add_argument('--input-file', default='input.txt', type=str, help='input file that stores the unsorted array')
parser.add_argument('--alg', default='bubblesort', type=str, help='sorting algorithm')
parser.add_argument('--mode', default='List', type=str, help='Mode of the underlying data structure. Right now it can be Lists or LinkedLists')
parser.add_argument('-c','--config', default=None, help='Specify which config to read')
parser.add_argument('-wc','--write-config', action='store_true', help='specify if you want to write the current arguments to config')
parser.add_argument('--expr', default='New Experiment', help='experiment name')

def main():
    args = parser.parse_args()
    if args.config and path.exists(args.config):
        parser.read_config(args.config)
    if args.write_config and args.config:
        parser.write_config(args.config)

    report = Report()
    expr = Expr(args)

    contents = readInputs(args.input_file, args.mode)
    print(contents)
    sorter = Sorter(contents, args.mode)
    contents = sorter.sort(args.alg)
    print(contents) 

if __name__ == "__main__":
    main()
