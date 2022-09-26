import re
from sys import argv, exit

# # Common or utility functions go here
# def push(t, k):
# 	keyss = sorted(t.keys())
# 	t[len(keyss)] = k
# 	return k


def coerce(s):
    def isNumber(string):
        try:
            float(string)
            return True
        except ValueError:
            return False

    def fun1(s1):
        if s1 == "true":
            return True
        elif s1 == "false":
            return False
        return s1

    if isNumber(s):
        return float(s)
    else:
        return fun1(s) or None


def csv(fileName, fun, sep=','):
    """Call fun on each row. Row cells are divided in the.seperator"""
    with open(fileName, "r") as f:
        for line in f.readlines():
            table = []
            for value in line.split(sep):
                table.append(coerce(value.strip()))
            fun(table)


def push(t, x):
    t.append(x)
    return x


# Strings
def o(t):
    if type(t) != dict:
        return str(t)

    def show(k, v):
        match_str = re.compile("^_")
        if not re.findall(match_str, str(k)):
            v = o(v)
            return len(t) == 0 and "{}".format(k, v) or str(v)

    u = dict()
    for k, v in t.items():
        u[len(u)] = show(k, v)
    if len(t) == 0:
        sorted(u)
    return u


def oo(t):
    print(o(t))
    return t


def msg(status):
    return "PASS" if status else "FAIL"


the = {"nums": 512, "seperator": ','}

# Update dict with args dict.
# Technically we do not need this function as we are handling this with defaults
# However since we require this as parts of the requirements thus adding it


def cli(args_dict):
    global the
    the['eg'] = 'nothing'
    the['dump'] = False
    the['csvFilePath'] = '../data/data1.csv'
    the['nums'] = 512
    the['seed'] = 10019
    the['seperator'] = ','
    args_dict = {}
    for index, opt in enumerate(argv):
        if opt in ("-h", "--help"):
            print('''
                OPTIONS:
                -e  --eg        start-up example                      = nothing
                -d  --dump      on test failure, exit with stack dump = false
                -f  --file      file with csv data                    = ../data/auto93.csv
                -h  --help      show help                             = false
                -n  --nums      number of nums to keep                = 512
                -s  --seed      random number seed                    = 10019
                -S  --seperator feild seperator                       = ,
            ''')
            exit()
        if opt in ("-e", "--eg"):
            args_dict["eg"] = argv[index+1].strip()
        if opt in ("-d", "--dump"):
            args_dict["dump"] = True
        if opt in ("-f", "--file"):
            args_dict["csvFilePath"] = argv[index+1].strip()
        if opt in ("-n", "--nums"):
            args_dict["nums"] = int(argv[index+1].strip())
        if opt in ("-s", "--seed"):
            args_dict["seed"] = int(argv[index+1].strip())
        if opt in ("-S", "--seperator"):
            args_dict["seperator"] = argv[index+1].strip()
    updated_dict = dict(list(the.items()) + list(args_dict.items()))
    return updated_dict
