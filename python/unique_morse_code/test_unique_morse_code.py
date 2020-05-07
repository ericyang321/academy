import unittest
from .unique_morse_code import unique_morse_code


class TestUniqueMorseCode(unittest.TestCase):
    def test_it_works(self):
        words = ["gin", "zen", "gig", "msg"]
        count = unique_morse_code(words)
        self.assertEqual(count, 2)

    def test_one_match(self):
        words = ["aaa", "aaa"]
        count = unique_morse_code(words)
        self.assertEqual(count, 1)

    def test_no_words(self):
        words = []
        count = unique_morse_code(words)
        self.assertEqual(count, 0)
