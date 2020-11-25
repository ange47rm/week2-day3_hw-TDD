import unittest

from src.compare import compare

class TestCompare(unittest.TestCase):

    def test_compare_3_1_returns_3_is_greater_than_1(self):
        self.assertEqual("3 is greater than 1", compare(3, 1))
        self.assertEqual("5 is less than 10", compare (5, 10))
        self.assertEqual("Both numbers are the same", compare (8, 8))