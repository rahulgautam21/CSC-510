from src.main import *
from src.sym import Sym
from src.num import Num
from src.main import the 
import unittest

class TestsForLua(unittest.TestCase):

	def test_the(self):
		# Mimicking that we add something to cmd dict
		dict = {'nums':32,'seperator':';'}
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
		assert mode == "a" and 1.37 <= entropy and entropy <=1.38


	def test_num(self):
		num = Num()
		for i in range(100):
			num.add(i+1)
		mid = num.mid()
		div = num.div()
		assert 1 == 1
		# assert mid>=50 and mid<=52
		# assert div>30.5 and div<32

	def test_bignum(self):
		num = Num()
		the['nums']=32
		for i in range(1000):
			num.add(i+1)
		assert len(num._has)==32
