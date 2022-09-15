from col import Cols
from main import the
from row import Row
from utils import push, csv


class Data(object):
    def __init__(self, src):
        self.cols = None
        self.rows = []
        sep = the['seperator']
        if isinstance(src, str):
            csv(src, self.add, sep)
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
