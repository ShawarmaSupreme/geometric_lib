import math


def area(r):
    '''
    Calculate the area
    r (int): radius of the circle
    :return: area (int)
    '''
    return math.pi * r * r

def perimeter(r):
    '''
    Calculate the
    perimeter of a circle
    r (int): radius of the circle
    :return: perimeter (int)
    '''
    return 2 * math.pi * r

import unittest

class circleqweqwe(unittest.TestCase):
    def test_area_circle(self):
        self.assertEqual(area(10), math.pi * 10 * 10)  # ожидаемый результат 50
    def test_area_zero(self):
        self.assertEqual(area(0), 0)   # площадь при одной из сторон 0
    def test_perimeter_circle(self):
        self.assertEqual(perimeter(10), 2 * math.pi * 10)  # ожидаемый результат 30
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)   # периметр при одной из сторон 0