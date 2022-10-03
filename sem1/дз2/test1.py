from unittest import TestCase, main


def factorial_rec(n):
    if type(n) != int:
        raise ValueError('ненатуральное число')

    if n == 0:
        return 1
    else:
        return n*factorial_rec(n-1)


def factorial_not_rec(x):
    if type(x) != int:
        raise ValueError('ненатуральное число')
    res = 1
    while x > 0:
        res *= x
        x -= 1
    return res


class FactorialTest(TestCase):

    def test_Factorial_rec(self):
        self.assertRaises(ValueError, factorial_rec, "hello")
        self.assertRaises(ValueError, factorial_rec, [1, 2, 3])
        self.assertRaises(ValueError, factorial_rec, 1.2)
        self.assertEqual(factorial_rec(0), 1)
        self.assertEqual(factorial_rec(4), 24)

    def test_Factorial_not_rec(self):
        self.assertRaises(ValueError, factorial_not_rec, "hello")
        self.assertRaises(ValueError, factorial_not_rec, [1, 2, 3])
        self.assertRaises(ValueError, factorial_not_rec, 1.2)
        self.assertEqual(factorial_not_rec(0), 1)
        self.assertEqual(factorial_not_rec(5), 120)


main()
