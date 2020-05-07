import unittest
from .get_products_of_all_ints_except_at_index import (
    get_products_of_all_ints_except_at_index,
)


class TestGetProductsOfAllIntsExceptAtIndex(unittest.TestCase):
    def test_positive_nums(self):
        products = get_products_of_all_ints_except_at_index([1, 7, 3, 4])
        expected = [84, 12, 28, 21]
        self.assertEqual(products, expected)

    def test_negative_nums(self):
        products = get_products_of_all_ints_except_at_index([0, 1, 2, 3])
        expected = [6, 0, 0, 0]
        self.assertEqual(products, expected)
