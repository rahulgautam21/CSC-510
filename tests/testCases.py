from src.data import Data
from src.num import Num
from src.sym import Sym
from src.utils import oo, csv, msg, the, cli
from tests import testCases
import sys


def test_bignum():
    num = Num()
    the['nums'] = 32
    for i in range(1000):
        num.add(i+1)
    return True if len(num._has) == 32 else False


def test_data():
    d = Data("./data/auto93.csv")
    l = list(d.cols.y)
    return True if len(d.cols.y) == 3 else False


def test_num():
    num = Num()
    the['nums'] = 512
    for i in range(100):
        num.add(i+1)
    mid = num.mid()
    div = num.div()
    print(mid, div)
    if (mid >= 50 and mid <= 52 and div > 30.5 and div < 32):
        return True
    else:
        return False


def test_stats():
    data = Data("./data/auto93.csv")
    print('xmid=', data.stats(2, data.cols.x, "mid"))
    print('xdiv=', data.stats(3, data.cols.x, "div"))
    print('ymid=', data.stats(2, data.cols.y, "mid"))
    print('ymid=', data.stats(3, data.cols.y, "div"))
    return True


def test_sym():
    sym = Sym()
    l = ["a", "a", "a", "a", "b", "b", "c"]
    for x in l:
        sym.add(x)
    mode = sym.mid()
    entropy = sym.div()
    entropy = round(entropy, 3)
    if (mode == "a" and 1.37 <= entropy and entropy <= 1.38):
        return True
    else:
        return False


def test_the():
    the = cli(dict)
    return True


def test_csv():
    global n
    n = 0

    def func_row(row):
        global n
        n = n + 1
        if n > 10:
            return n
        else:
            return oo(row)
    csv('./data/auto93.csv', func_row)
    return True


def ALL():
    tests = dir(testCases)
    tests = list(filter(lambda x: x[0:5] == "test_", tests))

    status = True
    for t in tests:
        print("\n−−−−−−−−−−−−−−−−−----------------−−−−−−−−−−−−−−−−−−")
        kstatus = run_tests(t)
        if kstatus == False:
            status = False
    return status


def run_tests(k):
    tests = dir(testCases)
    tests = list(filter(lambda x: x[0:5] == "test_", tests))

    if k not in tests and k != "ALL":
        return

    old = {}
    for u, v in the.items():
        old[u] = v

    if the['dump'] == True:
        fun = getattr(testCases, k)
        status = fun()
        print("!!!!!!", msg(status), k, status)
    else:
        try:
            fun = getattr(testCases, k)
            status = fun()
            print("!!!!!!", msg(status), k, status)
        except:
            status = False
            print("!!!!!!", msg(status), k, status)

    for u, v in old.items():
        the[u] = v
    if (status == False):
        sys.exit(1)
