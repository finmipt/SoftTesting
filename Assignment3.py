import unittest
from Assignment2 import triangle_program as triangle_type


class TestTriangle(unittest.TestCase):

    def test_equilateral(self):
        # Equilateral triangle with smallest possible values
        self.assertEqual(triangle_type(1, 1, 1), "Equilateral")

        # Equilateral triangle with largest possible values
        self.assertEqual(triangle_type(100, 100, 100), "Equilateral")

        # Equilateral triangle with random values
        self.assertEqual(triangle_type(8, 8, 8), "Equilateral")

    def test_isosceles(self):
        # Isosceles triangle with smallest possible values
        self.assertEqual(triangle_type(2, 2, 3), "Isosceles")

        # Isosceles triangle with largest possible values
        self.assertEqual(triangle_type(100, 100, 99), "Isosceles")

        # Isosceles triangle with random values
        self.assertEqual(triangle_type(5, 5, 7), "Isosceles")

    def test_scalene(self):
        # Scalene triangle with smallest possible values
        self.assertEqual(triangle_type(2, 3, 4), "Scalene")

        # Scalene triangle with largest possible values
        self.assertEqual(triangle_type(99, 98, 97), "Scalene")

        # Scalene triangle with random values
        self.assertEqual(triangle_type(5, 7, 9), "Scalene")

    def test_not_a_triangle(self):
        # Not a triangle with smallest possible values
        self.assertEqual(triangle_type(1, 2, 3), "NotATriangle")

        # Not a triangle with largest possible values
        self.assertEqual(triangle_type(100, 1, 1), "NotATriangle")

        # Not a triangle with random values
        self.assertEqual(triangle_type(3, 4, 7), "NotATriangle")

    def test_invalid_input(self):
        # Invalid input with a side having a value less than 1
        self.assertEqual(triangle_type(-1, 2, 3), "Value of a is not in the range of permitted values.")

        # Invalid input with a side having a value greater than 100
        self.assertEqual(triangle_type(200, 2, 3), "Value of a is not in the range of permitted values.")

        # Invalid input with all sides having the same invalid value
        self.assertEqual(triangle_type(-5, -5, -5), "Value of a is not in the range of permitted values.")


if __name__ == '__main__':
    unittest.main()
