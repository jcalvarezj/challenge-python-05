import math


def square_area(side):
    """Returns the area of a square"""
    return side ** 2


def rectangle_area(base, height):
    """Returns the area of a rectangle"""
    return base * height


def triangle_area(base, height):
    """Returns the area of a triangle"""
    return base * height / 2


def rhombus_area(diagonal_1, diagonal_2):
    """Returns the area of a rhombus"""
    return diagonal_1 * diagonal_2 / 2


def trapezoid_area(base_minor, base_major, height):
    """Returns the area of a trapezoid"""
    return height * (base_minor + base_major) / 2


def regular_polygon_area(perimeter, apothem):
    """Returns the area of a regular polygon"""
    return perimeter * apothem / 2


def circumference_area(radius):
    """Returns the area of a circumference"""
    return math.pi * radius ** 2


if __name__ == '__main__':
    import unittest

    class GeometrySuite(unittest.TestCase):

        def setUp(self):
            self.square_areas = {
                1: 1,
                2: 4,
                3: 9
            }

            self.rectangle_params = [(1, 1), (2, 1), (3, 2)]
            self.rectangle_areas = [1, 2, 6]

            self.triangle_params = [(2, 1), (3, 2), (4, 3)]
            self.triangle_areas = [1, 3, 6]

            self.rhombus_params = [(2, 1), (3, 2), (4, 3)]
            self.rhombus_areas = [1, 3, 6]

            self.trapezoid_params = [(1, 1, 1), (2, 4, 2), (3, 5, 4)]
            self.trapezoid_areas = [1, 6, 16]

            self.polygon_params = [(4, 1), (2, 2), (3, 6)]
            self.polygon_areas = [2, 2, 9]

            self.circumference_areas = {
                1: 3.141592653589793,
                2: 12.566370614359172,
                3: 28.274333882308138
            }

        def test_square_area(self):
            for key, value in self.square_areas.items():
                self.assertEqual(value, square_area(key))

        def test_rectangle_area(self):
            for i, params in enumerate(self.rectangle_params):
                self.assertEqual(self.rectangle_areas[i], rectangle_area(*params))

        def test_triangle_area(self):
            for i, params in enumerate(self.triangle_params):
                self.assertEqual(self.triangle_areas[i], triangle_area(*params))

        def test_rhombus_area(self):
            for i, params in enumerate(self.rhombus_params):
                self.assertEqual(self.rhombus_areas[i], rhombus_area(*params))

        def test_trapezoid_area(self):
            for i, params in enumerate(self.trapezoid_params):
                self.assertEqual(self.trapezoid_areas[i], trapezoid_area(*params))

        def test_regular_polygon_area(self):
            for i, params in enumerate(self.polygon_params):
                self.assertEqual(self.polygon_areas[i], regular_polygon_area(*params))

        def test_circumference_area(self):
            for key, value in self.circumference_areas.items():
                self.assertEqual(value, circumference_area(key))

        def tearDown(self):
            del self.square_areas
            del self.rectangle_params
            del self.rectangle_areas
            del self.triangle_params
            del self.triangle_areas
            del self.rhombus_params
            del self.rhombus_areas
            del self.trapezoid_params
            del self.trapezoid_areas
            del self.polygon_params
            del self.polygon_areas
            del self.circumference_areas


    unittest.main()
