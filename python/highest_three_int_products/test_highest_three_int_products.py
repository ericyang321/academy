import unittest
from .highest_three_int_products import *


class TestHighestThreeIntProducts(unittest.TestCase):
    def test_multiply(self):
        result = multiply([1, 2, 3])
        expect = 6
        self.assertEqual(result, expect)

    def test_find_lowest_idx_excluding(self):
        result = find_lowest_idx_excluding([-1, -2, -3, -4, 5, 6], [4, 5])
        expect = 3
        self.assertEqual(result, expect)

    def test_find_highest_idx_excluding(self):
        result = find_highest_idx_excluding([-1, -2, 1, 2, 3, 4], [4, 5])
        expect = 3
        self.assertEqual(result, expect)

    def test_highest_products_with_space(self):
        no_diffs = highest_products_with_space([1, 1, 1, 1, 1], 3)
        negatives_highest = highest_products_with_space([-1, -2, -3, -4, 1, 2, 3], 3)
        positive_highest = highest_products_with_space([1, 1, 1, 1, 1, 4, 5], 3)
        only_three_numbers = highest_products_with_space([1, 2, 3], 3)

        self.assertEqual(no_diffs, 1)
        self.assertEqual(negatives_highest, 36)
        self.assertEqual(positive_highest, 20)
        self.assertEqual(only_three_numbers, 6)
