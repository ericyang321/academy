import unittest
from .sorts import swap, bubble_sort, selection_sort


class TestSortMethods(unittest.TestCase):
    def test_swap(self):
        given = [1, 2]
        expected = [2, 1]
        swap(given, 0, 1)
        self.assertEqual(given, expected)

    def test_bubble_sort(self):
        given = [3, 5, 1, 4, 7, 3, 7, 8]
        expected = [1, 3, 3, 4, 5, 7, 7, 8]
        bubble_sort(given)
        self.assertEqual(given, expected)

    def test_selection_sort(self):
        given = [3, 5, 1, 4, 7, 3, 7, 8]
        expected = [1, 3, 3, 4, 5, 7, 7, 8]
        selection_sort(given)
        self.assertEqual(given, expected)

    def test_insertion_sort(self):
        pass


if __name__ == "__main__":
    unittest.main()
