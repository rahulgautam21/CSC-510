from src.main import the

def isfloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def coerce(string):
    if isfloat(string):
        return float(string)
    elif string == "true":
            return True
    elif string == "false":
        return False
    else:
        return string

def csv(src, fn):
    sep = the['seperator']
    with open(src, "r") as f:
        for line in f.readlines():
            table = []
            for value in line.split(sep):
                table.append(coerce(value.strip()))
            fn(table)

def push(table, row):
    table.append(row)
    return row
