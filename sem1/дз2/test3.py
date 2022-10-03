from unittest import TestCase, main


def pascal_triangle(n):

    if n <= 0:
        raise ValueError

    if n == 1:
        return [[1]]

    triangle = [[1], [1, 1]]
    row = [1, 1]
    for i in range(2, n):
        row = [1] + [sum(column) for column in zip(row[1:], row)] + [1]
        triangle.append(row)

    return triangle


class PascalTest(TestCase):

    def test_triangle(self):
        self.assertRaises(TypeError, pascal_triangle, 'hello')
        self.assertRaises(TypeError, pascal_triangle, [1, 2, 3])
        self.assertRaises(ValueError, pascal_triangle, -1)
        self.assertRaises(ValueError, pascal_triangle, 0)
        self.assertTrue(pascal_triangle(3))


main()