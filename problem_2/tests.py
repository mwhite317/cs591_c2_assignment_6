import unittest

from solution import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_can_create_square_with_side_length(self):
        self.assertIsNotNone(Square(1))

    def test_correct_square_perimeter(self):
        shape = Square(5)
        self.assertEqual(shape.perimeter(), 20)

    def test_correct_area(self):
        shape = Square(5)
        self.assertEqual(shape.area(), 25)

    def test_square_toString(self):
        shape = Square(4)
        self.assertEqual(shape.__str__(), "Area: 16 square units and Perimeter: 16 units")

    def test_can_create_rectangle_with_sides(self):
        self.assertIsNotNone(Rectangle(4, 4))

    def test_correct_rectangle_perimeter(self):
        shape = Rectangle(5, 3)
        self.assertEqual(shape.perimeter(), 16)

    def test_correct_square_area(self):
        shape = Rectangle(5, 3)
        self.assertEqual(shape.area(), 15)

    def test_rectangular_toString(self):
        shape = Rectangle(5, 3)
        self.assertEqual(shape.__str__(), "Area: 15 square units and Perimeter: 16 units")

    def test_can_create_circle_with_radius(self):
        self.assertIsNotNone(Circle(3))

    def test_correct_circum(self):
        shape = Circle(4)
        self.assertEqual(shape.circumference(), 25.13)

    def test_correct_circle_area(self):
        shape = Circle(4)
        self.assertEqual(shape.area(), 50.27)

    def test_circular_toString(self):
        shape = Circle(4)
        self.assertEqual(shape.__str__(), "Area: 50.27 square units and Circumference: 25.13 units")

    def test_get_input_functions(self):
        self.assertEqual(shapes.get("C"), circle_input)
        self.assertEqual(shapes.get("R"), rectangle_input)
        self.assertEqual(shapes.get("S"), square_input)
        self.assertEqual(shapes.get("Q"), quit_input)
        self.assertEqual(shapes.get("", unknown_input), unknown_input)


if __name__ == '__main__':
    unittest.main()
