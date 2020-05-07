import unittest
from .unique_email_addresses import unique_email_addresses


class TestUniqueEmailAddresses(unittest.TestCase):
    def test_it_works(self):
        emails = [
            "test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@lee.tcode.com",
        ]
        count = unique_email_addresses(emails)
        self.assertEqual(count, 2)
