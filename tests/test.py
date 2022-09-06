from src.main import *
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
		list = ["a","a","a","a","b","b","c"]
		for x in list:
			sym.add(x)
		mode = sym.mid()
		entropy = sym.div()
		entropy = Math.round(entropy,3)
		print("mid="+mode)
		print("div="+entropy)
		self.assertEqual()
