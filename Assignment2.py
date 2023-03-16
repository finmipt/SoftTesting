import unittest


def triangle_program(a, b, c):
    # Check if input values satisfy the range condition c1
    if a <= 0 or b <= 0 or c <= 0:
        return "Value of a, b, or c is not in the range of permitted values."

    # Check if input values satisfy the range condition c2
    if a > 200 or b > 200 or c > 200:
        return "Value of a, b, or c is not in the range of permitted values."

    # Check if input values satisfy the range condition c3
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "NotATriangle"

    # Check if input values satisfy the condition c4
    if a == b and b == c:
        return "Equilateral"

    # Check if input values satisfy the condition c5
    if a == b or b == c or c == a:
        return "Isosceles"

    # Check if input values satisfy the condition c6
    if a != b and b != c and c != a:
        return "Scalene"


class TestTriangleProgram(unittest.TestCase):
    def test_equilateral_triangles(self):
        self.assertEqual(triangle_program(1, 1, 1), "Equilateral")
        self.assertEqual(triangle_program(100, 100, 100), "Equilateral")

    def test_isosceles_triangles(self):
        self.assertEqual(triangle_program(10, 10, 19), "Isosceles")
        self.assertEqual(triangle_program(5, 13, 13), "Isosceles")
        self.assertEqual(triangle_program(7, 11, 7), "Isosceles")

    def test_scalene_triangles(self):
        self.assertEqual(triangle_program(3, 5, 7), "Scalene")
        self.assertEqual(triangle_program(8, 5, 10), "Scalene")
        self.assertEqual(triangle_program(12, 15, 8), "Scalene")

    def test_not_a_triangle(self):
        self.assertEqual(triangle_program(5, 7, 12), "NotATriangle")
        self.assertEqual(triangle_program(4, 10, 6), "NotATriangle")
        self.assertEqual(triangle_program(13, 8, 5), "NotATriangle")


if __name__ == '__main__':
    unittest.main()
