from sys import argv,exit
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
    the['eg'] = 'nothing'
    the['dump'] = False
    the['csvFilePath'] = '../data/data1.csv'
    the['nums'] = 512
    the['seed'] = 10019
    the['seperator'] = ',]]'
    args_dict = {}
    for index, opt in enumerate(argv):
        if opt in ("-h","--help"):
            print( '''
                OPTIONS:
                -e  --eg        start-up example                      = nothing
                -d  --dump      on test failure, exit with stack dump = false
                -f  --file      file with csv data                    = ../data/auto93.csv
                -h  --help      show help                             = false
                -n  --nums      number of nums to keep                = 512
                -s  --seed      random number seed                    = 10019
                -S  --seperator feild seperator                       = , ]]
            ''')
            exit()
        if opt in ("-e", "--eg"):
            args_dict["eg"] = argv[index+1].strip()
        if opt in ("-d", "--dump"):
            args_dict["dump"] = True if argv[index+1].strip().lower() == 'true' else False
        if opt in ("-f", "--file"):
            args_dict["file"] = argv[index+1].strip()
        if opt in ("-n", "--nums"):
            args_dict["nums"] = int(argv[index+1].strip())
        if opt in ("-s", "--seed"):
            args_dict["seed"] = int(argv[index+1].strip())
        if opt in ("-S", "--seperator"):
            args_dict["seperator"] = argv[index+1].strip()
    the = cli(args_dict)