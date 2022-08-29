import pytest
from Calculator import *

    # test methods for add, subtract, multiply and divide
    def test_add():
      assert add(3,4) == 7
        
    def test_subtract(self):
      assert subtract(5,2) == 3
        
    def test_multiply(self):
       assert multiply(5,2) == 8
        
    def test_divide(self):
      assert divide(6,2) == 4
