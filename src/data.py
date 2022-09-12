from src.col import Cols
from src.main import the
from src.misc import isfloat, coerce, csv, push
from src.row import Row

class Data(object):
    def __init__(self, src):
        self.cols = None
        self.rows = []
        if isinstance(src, str):
            csv(src, self.add)
        else:
            for _, row in enumerate(src or []):
                self.add(row)
                
                
    def add(self, row):
        if not self.cols:
            self.cols = Cols(row)
        else:
            row = push(self.rows, Row(row))
            for _, todo in enumerate([self.cols.x, self.cols.y]):
                for _, col in enumerate(todo):
                    col.add(row.cells[col.at])
                    
                    
    def stats(self, places, show_cols, fun):
        places, show_cols, fun = places or 2, show_cols or self.cols.x, fun or "mid"
        table = {}       
        for _, col in enumerate(show_cols):
            if fun == "mid":
                value = col.mid()
            else:
                value = col.div()
            value = round(value, places)
            table[col.name] = value
        return table
