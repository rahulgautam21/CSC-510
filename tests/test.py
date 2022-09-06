from src.main import *
from src.sym import Sym
from src.num import Num
import unittest

class TestsForLua(unittest.TestCase):
        
    def test_the(self):
        global the
        # Mimicking that we add something to cmd dict
        dict = {'seperator':';'}
        the = cli(dict)
        self.assertEqual(the,dict)
		
	def test_sym()
		sym = Sym()
		l = ["a","a","a","a","b","b","c"]
		for x in l:
			sym.add(x)
		mode = sym.mid()
		entropy = sym.div()
		entropy = Math.round(entropy,3)
		print("mid="+mode)
		print("div="+entropy)
		assert mode=="a" and 1.37 <= entropy and entropy <=1.38

	def test_num()
		sym = Num()
		for i in range(100):
			num.add(i+1)
		mid = num.mid()
		div = num.div()
		print("mid:",mid)
		print("div:",div)
		assert mid>=50 and mid<=52
		assert div>30.5 and div<32
