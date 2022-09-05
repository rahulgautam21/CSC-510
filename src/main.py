from sys import argv
import argparse

the={}

# Update dict with args dict.
# Technically we do not need this function as we are handling this with defaults
# However since we require this as parts of the requirements thus adding it
def cli(args_dict):
    global the
    updated_dict = dict(list(the.items()) + list(args_dict.items()))
    return updated_dict


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--eg', help="start-up example", default="nothing", type=str)
    parser.add_argument('-d', '--dump', help="on test failure, exit with stack dump", default=False, type=str)
    parser.add_argument('-f', '--file', help="file with csv data", default="../data/auto93.csv", type=str)
    parser.add_argument('-n', '--nums', help="numbers to keep", default=512, type=int)
    parser.add_argument('-s', '--seed', help="random number seed", default=10019, type=int)
    parser.add_argument('-S', '--seperator', help="feild seperator", default=",", type=str)
    args = parser.parse_args()
    args_dict = vars(args)
    the = cli(args_dict)
    print(the)