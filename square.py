
def area(a):
    '''
    Calculate the area of a square
    :param a (int): the area of the square
    :return: the area of the square (int)
    '''
    return a * a


def perimeter(a):
    '''
    Calculate the perimeter of a square
    :param a (int): the perimeter of the square
    :return: the perimeter of a square (int)
    '''
    return 4 * a

import unittest

class circleqweqwe(unittest.TestCase):
    def test_area_square(self):
        self.assertEqual(area(10), 100)  # ожидаемый результат 50
    def test_area_zero(self):
        self.assertEqual(area(0), 0)   # площадь при одной из сторон 0
    def test_perimeter_square(self):
        self.assertEqual(perimeter(10), 40)  # ожидаемый результат 30
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)   # периметр при одной из сторон 0