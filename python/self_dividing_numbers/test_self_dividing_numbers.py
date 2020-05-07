import unittest
from .self_dividing_numbers import self_dividing_numbers


class TestSelfDividingNumbers(unittest.TestCase):
    def test_it_works(self):
        result = self_dividing_numbers(1, 22)
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
        self.assertEqual(result, expected)

