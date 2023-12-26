import unittest
from circles import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        #Test areas when radius >= 0
        self.assertEqual(circle_area(1), pi)
        self.assertEqual(circle_area(0), 0)
        self.assertEqual(circle_area(2.1), pi*(2.1**2))

    def test_values(self):
        #Test area when raduis<0
        self.assertRaises(ValueError, circle_area, -2)

    def test_type(self):
        #Make sure a corect type of input is used
        self.assertRaises(TypeError, circle_area, 3+5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "radius")