import unittest
from .merge_meeting_times import merge_meeting_times


class TestMergeMeetingTimes(unittest.TestCase):
    def test_does_not_merge_non_overlapping_times(self):
        result = [(1, 2), (8, 9), (3, 4)]
        expected = [(1, 2), (3, 4), (8, 9)]
        self.assertEqual(merge_meeting_times(result), expected)

    def test_does_merge_overlapping_times(self):
        result = [(1, 2), (8, 9), (1, 4)]
        expected = [(1, 4), (8, 9)]
        self.assertEqual(merge_meeting_times(result), expected)

    def test_does_merge_consumed_meeting_times(self):
        result = [(1, 8), (1, 2), (2, 3), (18, 20), (1, 4)]
        expected = [(1, 8), (18, 20)]
        self.assertEqual(merge_meeting_times(result), expected)

    def test_does_all_subsuming(self):
        result = [(1, 10), (2, 6), (3, 5), (7, 9)]
        expected = [(1, 10)]
        self.assertEqual(merge_meeting_times(result), expected)

