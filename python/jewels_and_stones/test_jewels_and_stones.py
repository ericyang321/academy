import unittest
from .jewels_and_stones import jewels_and_stones


class TestJewelsAndStones(unittest.TestCase):
    def test_stone_recognition(self):
        J = "aA"
        S = "aAAbbbb"
        count = jewels_and_stones(J, S)
        self.assertEqual(count, 3)

    def test_no_stone_match(self):
        J = "aAbBcCdD"
        S = "ZZZZZZ"
        count = jewels_and_stones(J, S)
        self.assertEqual(count, 0)

    def test_no_jewel(self):
        J = ""
        S = "aAAbbb"
        count = jewels_and_stones(J, S)
        self.assertEqual(count, 0)

    def test_no_stones(self):
        J = "aAbBcCdD"
        S = ""
        count = jewels_and_stones(J, S)
        self.assertEqual(count, 0)
