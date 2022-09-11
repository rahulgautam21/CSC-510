from src.num import Num
from src.sym import Sym

# Singleton object


class Cols(object):
    def __init__(self, names=[]):
        self.names = names
        self.all = []
        self.klass = None
        self.x = []
        self.y = []
        for index, colName in enumerate(self.names):
            # If upper that means that number else it is a symbol
            col = Num(index, colName) if colName[0].isupper() else Sym(index, colName)
            self.all.append(col)
            # If last letter in column name is : then it is to be ignored
            if colName[-1] != ':':
                self.y.append(col) if colName[-1] == '-' or colName[-1] == '+' else self.x.append(col)
                if colName[-1] == '!':
                    self.klass = col
