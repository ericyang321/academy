import unittest
from .array_partition_1 import array_partition_1


class TestArrayPartition1(unittest.TestCase):
    def test_it_works(self):
        given = array_partition_1([1, 2, 3, 4])
        expected = 4
        self.assertEqual(given, expected)

    def test_with_negatives(self):
        given = array_partition_1([-1, -4, 8, 3])
        expected = -1
        self.assertEqual(given, expected)
