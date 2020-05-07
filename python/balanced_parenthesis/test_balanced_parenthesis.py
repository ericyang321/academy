import unittest
from .balanced_parenthesis import is_balanced_parenthesis


class TestBalancedParenthesis(unittest.TestCase):
    def test_matching_parens(self):
        matching_parens = "()()()()()()()"
        self.assertEqual(is_balanced_parenthesis(matching_parens), True)

    def test_unmatched_parens(self):
        unmatched_parens = "(()(()())()()()())))("
        self.assertEqual(is_balanced_parenthesis(unmatched_parens), False)
