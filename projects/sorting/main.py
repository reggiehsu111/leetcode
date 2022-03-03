from os import path

from IOs import readInputs
from utils.parser import ConfigParser
from Experiments.expr import Expr

parser = ConfigParser(description="Sort Lab")
parser.add_argument('--input-file', default='input.txt', type=str, help='input file that stores the unsorted array')
parser.add_argument('--alg', default='bubblesort', type=str, help='sorting algorithm')
parser.add_argument('--mode', default='List', type=str, help='Mode of the underlying data structure. Right now it can be Lists or LinkedLists')
parser.add_argument('-c','--config', default=None, help='Specify which config to read')
parser.add_argument('-wc','--write-config', action='store_true', help='specify if you want to write the current arguments to config')
parser.add_argument('--expr-name', default='new_expr', help='experiment name')
parser.add_argument('--max-exponent', default=2, type=int, help='maximum exponential ofthe lenght of random generated list for Expr to run')

def main():
    args = parser.parse_args()
    if args.config and path.exists(args.config):
        parser.read_config(args.config)
    if args.write_config and args.config:
        parser.write_config(args.config)

    expr = Expr(args)
    expr.run()

if __name__ == "__main__":
    main()
