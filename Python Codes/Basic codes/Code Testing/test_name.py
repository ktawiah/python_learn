import unittest
from name import formatted_name


class NameTestCase(unittest.TestCase):
    def test_name_format(self):
        new_name = formatted_name('Kelvin', 'Tawiah')
        self.assertEqual(new_name, 'Kelvin Tawiah')