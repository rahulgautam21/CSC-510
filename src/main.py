from sys import argv
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--eg', help="start-up example", default="nothing", type=str)
    parser.add_argument('-d', '--dump', help="on test failure, exit with stack dump", default=False, type=str)
    parser.add_argument('-f', '--file', help="file with csv data", default="../data/auto93.csv", type=str)
    parser.add_argument('-n', '--nums', help="numbers to keep", default=512, type=int)
    parser.add_argument('-s', '--seed', help="random number seed", default=10019, type=int)
    parser.add_argument('-S', '--seperator', help="feild seperator", default=",", type=str)
    args = parser.parse_args()
    input_arguments = vars(args)
    print(input_arguments)