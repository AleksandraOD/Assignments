from unittest import TestCase, main


def perfect_number(n):
    if type(n) != int:
        raise ValueError
    if n == 0:
        return False
    s = [i for i in range(1, n//2+1) if not n % i]
    return sum(s) == n


class PerfectTest(TestCase):
    def test_valid_perfect(self):
        self.assertRaises(ValueError, perfect_number, "hello")
        self.assertRaises(ValueError, perfect_number, [1, 2, 3])
        self.assertRaises(ValueError, perfect_number, 1.2)
        self.assertRaises(ValueError, perfect_number, 0)

    def test_perfect(self):
        self.assertTrue(perfect_number(28))
        self.assertFalse(perfect_number(-6))

main()
_