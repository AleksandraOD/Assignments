from unittest import TestCase, main

import poly_logic as pl


class PolyTest(TestCase):
    def test_poly(self):
        self.assertEqual(pl.derivative('3x^4+x^3+13x^2+8'), '12x^3+3x^2+26x')
        self.assertEqual(pl.derivative(''), '')
        self.assertEqual(pl.derivative('x-1'), '1')
        self.assertEqual(pl.derivative('0'), '0')
        self.assertEqual(pl.derivative('1'), '0')


main()
