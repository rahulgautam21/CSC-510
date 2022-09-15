import math
from collections import OrderedDict
from main import the
import random


def per(t, p=0.5):
    p = math.floor((p*len(t)) + 0.5)
    return t[max(0, min(len(t)-1, p))]


class Num:

    def __init__(self, c=0, s="",):
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

    def add(self, v, pos=0):
        if v != "?":
            self.n += 1
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)

            if len(self._has) < the["nums"]:
                pos = len(self._has)

            elif random.random() < the["nums"] / self.n:
                pos = random.randint(0, len(self._has) - 1)

            self.isSorted = False
            self._has[pos] = int(v)

    def div(self, a=None):
        a = self.nums()
        return (per(a, 0.9) - per(a, 0.1))/2.58

    def mid(self):
        return per(self.nums(), 0.5)
