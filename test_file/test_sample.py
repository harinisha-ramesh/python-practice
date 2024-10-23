import unittest
from sample import *

class TestMathFunction(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(5))
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(37))

if __name__ == '__main__': 
    unittest.main()       