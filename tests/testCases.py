import sys
sys.path.insert(0, '../src')
from data import Data
from num import Num
from main import the, cli
from sym import Sym

def test_bignum():
    num = Num()
    the['nums'] = 32
    for i in range(1000):
        num.add(i+1)
    return 0 if len(num._has) == 32 else 1


def test_data():
    d = Data("../data/auto93.csv")
    l = list(d.cols.y)
    for x in l:
        print(x)
    return 0 if len(d.cols.y) == 3 else 1


def test_num():
    num = Num()
    the['nums'] = 512
    for i in range(100):
        num.add(i+1)
    mid = num.mid()
    div = num.div()
    print(mid, div)
    if (mid >= 50 and mid <= 52 and div > 30.5 and div < 32):
        return 0
    else:
        return 1


def test_stats():
    data = Data("../data/auto93.csv")
    print('xmid=', data.stats(2, data.cols.x, "mid"))
    print('xdiv=', data.stats(3, data.cols.x, "div"))
    print('ymid=', data.stats(2, data.cols.y, "mid"))
    print('ymid=', data.stats(3, data.cols.y, "div"))
    return 0


def test_sym():
    sym = Sym()
    l = ["a", "a", "a", "a", "b", "b", "c"]
    for x in l:
        sym.add(x)
    mode = sym.mid()
    entropy = sym.div()
    entropy = round(entropy, 3)
    if (mode == "a" and 1.37 <= entropy and entropy <= 1.38):
        return 0
    else:
        return 1


def test_the():
    # Mimicking that we add something to cmd dict
    dict = {'nums': 32, 'seperator': ';'}
    the = cli(dict)
    if(the == dict):
        return 0
    else:
        return 1
