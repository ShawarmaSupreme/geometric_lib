def perimeter(a, b):
    '''
    Calculates the perimeter of a perimeter of a rectangle
    a, b (int): width and height
    returns perimeter of a rectangle (int)

    perimeter(10, 5)
    return: 30
    '''
    if a > 0 and b > 0:
        return 2 * (a + b)
    else:
        return 0

def area(a, b):
    '''
    Calculates the area of the area of a rectangle
    a, b (int): width and height
    returns area of a rectangle (int)

    area(10, 5)
    return: 50
    '''
    return a * b

import unittest
class rectangleqweqwe(unittest.TestCase):
    def test_area_rectangle(self):
        self.assertEqual(area(10, 5), 50)  # ожидаемый результат 50
    def test_area_zero(self):
        self.assertEqual(area(10, 0), 0)   # площадь при одной из сторон 0
    def test_perimeter_rectangle(self):
        self.assertEqual(perimeter(10, 5), 30)  # ожидаемый результат 30
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(10, 0), 0)   # периметр при одной из сторон 0