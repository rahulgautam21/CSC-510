import math
from collections import OrderedDict

the = {}


def per(t, p=0):
    p = math.floor(((p if p != 0 else 0.5)*len(t)) + 0.5 )
    return t[math.max(1, math.min(len(t), p))]


class Num:

    def __init__(self, s="", c=0):
        self.n = 0
        self.at = c
        self.name = s
        self._has = {}
        self.lo = math.inf
        self.hi = -math.inf
        self.isSorted = True
        self.w = 1
        if self.name != "" and self.name[-1] == '-':
            self.w = -1

    def nums(self):
        if not self.isSorted:
            self._has = OrderedDict(sorted(self._has.items()))
            self.isSorted = True
            return self._has

    def add(self, v, pos = 0):
        if v != "?":
            self.n += 1
            self.lo = math.min(v, self.lo)
            self.hi = math.max(v, self.hi)

            if len(self._has) < the["nums"]:
                pos = 1 + len(self._has)

            elif math.random() < the["nums"] / self.n:
                pos = math.random(len(self._has))

            if pos:
                self.isSorted = False
                self._has[pos] = int(v)

    def div(self, a = None):
        a = self.nums()
        return (per(a, 0.9) - per(a, 0.1))/2.58

    def mid(self):
        return per(self.nums(), 0.5)
