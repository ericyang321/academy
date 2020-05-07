import unittest
from .binary_search import binary_search


class TestBinarySearch(unittest.TestCase):
    def test_even_counts(self):
        nums = [0, 1, 2, 3, 4, 5, 6]
        for num in nums:
            self.assertEqual(binary_search(nums=nums, target=num), True)

    def test_odd_counts(self):
        nums = [0, 1, 2, 3, 4, 5]
        for num in nums:
            self.assertEqual(binary_search(nums=nums, target=num), True)
