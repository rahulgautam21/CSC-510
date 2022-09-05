from src.main import *
import unittest

class TestsForLua(unittest.TestCase):
        
    def test_the(self):
        global the
        # Mimicking that we add something to cmd dict
        dict = {'seperator':';'}
        the = cli(dict)
        self.assertEqual(the,dict)