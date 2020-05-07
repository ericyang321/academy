import unittest
from .merge_sorted_lists import merge_sorted_lists

class TestMergeSortedLists(unittest.TestCase):
    def test_case(self):
        list1 = [3, 4, 6, 10, 11, 15]
        list2 = [1, 5, 8, 12, 14, 19]

        self.assertEqual(merge_sorted_lists(list1, list2), [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19])
