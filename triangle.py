def area(a, h):
    '''
    Calculate the area of a triangle
    :param a (int): First side of the triangle
    :param h (int): Second side of the triangle
    :return: Area of the triangle (int)

    area(10, 5)
    return: 25
    '''
    return a * h / 2

def perimeter(a, b, c):
    '''
    Calculate the perimeter of a triangle
    :param a (int): First side of the triangle
    :param b (int): Second side of the triangle
    :param c (int): Third side of the triangle
    :return: Perimeter of the triangle (int)

    perimeter(10, 5, 3)
    return: 18
    '''
    if a > 0 and b > 0 and c > 0:
        return a + b + c
    else:
        return 0


import unittest

class circleqweqwe(unittest.TestCase):
    def test_area_triangle(self):
        self.assertEqual(area(10, 5), 25)  # ожидаемый результат 50
    def test_area_zero(self):
        self.assertEqual(area(10, 0), 0)   # площадь при одной из сторон 0
    def test_perimeter_triangle(self):
        self.assertEqual(perimeter(10, 5, 3), 18)  # ожидаемый результат 30
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(10, 0, 3), 0)   # периметр при одной из сторон 0