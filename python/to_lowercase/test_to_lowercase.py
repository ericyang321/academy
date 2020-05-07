import unittest
from .to_lowercase import to_lowercase


class TestToLowercase(unittest.TestCase):
    def test_lowers_case(self):
        upper_cases = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower_cases = "abcdefghijklmnopqrstuvwxyz"

        self.assertEqual(to_lowercase(upper_cases), lower_cases)

    def test_nonalphabet_chars(self):
        nonalphabet_chars = ",. 1234567890`~!@#$%^&*()_+\\][/?.>,<"

        self.assertEqual(to_lowercase(nonalphabet_chars), nonalphabet_chars)
