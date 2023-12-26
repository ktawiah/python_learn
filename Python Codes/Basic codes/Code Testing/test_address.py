import unittest
from address import get_address

class AddressTestCase(unittest.TestCase):
    def test_format(self):
        self.assertEqual(get_address('Ghana', 'Kumasi', '500000'), 'Kumasi, Ghana - population 500000')