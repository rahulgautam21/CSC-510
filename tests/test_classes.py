from src.main import *
from src.sym import Sym
from src.num import Num


def test_the(self):
	global the
	# Mimicking that we add something to cmd dict
	dict = {'seperator':';'}
	the = cli(dict)
	self.assertEqual(the,dict)


def test_sym(self):
	sym = Sym()
	l = ["a","a","a","a","b","b","c"]
	for x in l:
		sym.add(x)
	mode = sym.mid()
	entropy = sym.div()
	entropy = round(entropy,3)
	print("mid="+mode)
	print("div="+entropy)
	assert mode == "a" and 1.37 <= entropy and entropy <=1.38


def test_num(self):
	num = Num()
	for i in range(100):
		num.add(i+1)
	mid = num.mid()
	div = num.div()
	print("mid:",mid)
	print("div:",div)
	assert mid>=50 and mid<=52
	assert div>30.5 and div<32

def test_bignum(self):
    the['nums']=32
    num = Num()
    for i in range(1,1001):
        num.add(i)
    print(num.nums())
    assert len(num._has)==32
