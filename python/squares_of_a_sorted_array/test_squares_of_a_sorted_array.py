import unittest
from .squares_of_a_sorted_array import (
    squares_of_a_sorted_array,
    sectionize_arrays,
    merge_two_sorted_arrays,
)


class TestSquaresOfASorterArray(unittest.TestCase):
    def squares_of_a_sorted_array(self):
        array = [-10, -8, -4, -1, 0, 4, 6, 9, 10]
        self.assertEqual(
            squares_of_a_sorted_array(array), [0, 1, 4, 6, 9, 10, 16, 64, 100]
        )

    def test_sectionize_arrays(self):
        negatives_and_positives_array = [-3, -2, -1, 7, 9, 11]
        negatives, positives = sectionize_arrays(negatives_and_positives_array)
        self.assertEqual(negatives, [-3, -2, -1])
        self.assertEqual(positives, [7, 9, 11])

    def test_sectionize_arrays_positives_only(self):
        positives_only_array = [1, 2, 3]
        negatives, positives = sectionize_arrays(positives_only_array)
        self.assertEqual(negatives, [])
        self.assertEqual(positives, [1, 2, 3])

    def test_sectionize_arrays_negatives_only(self):
        negatives_only_array = [-3, -2, -1]
        negatives, positives = sectionize_arrays(negatives_only_array)
        self.assertEqual(negatives, [-3, -2, -1])
        self.assertEqual(positives, [])

    def test_merge_two_sorted_arrays(self):
        array1 = [1, 3, 5, 7, 9, 11]
        array2 = [2, 4, 6, 8, 10, 12]
        self.assertEqual(
            merge_two_sorted_arrays(array1, array2),
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        )

    def test_merge_two_sorted_arrays_equal(self):
        array1 = [0, 0, 0, 0, 0]
        array2 = [0, 0, 0, 0, 0]
        self.assertEqual(
            merge_two_sorted_arrays(array1, array2), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        )
