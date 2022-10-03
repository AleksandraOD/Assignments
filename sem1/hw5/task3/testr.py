from unittest import TestCase, main

from roman2 import Roman


class RomanTest(TestCase):
    def test_values(self):
        values_error = [-1, 0, 2000, 12.23, '', [123, 'asf']]
        for value in values_error:
            self.assertRaises(ValueError, Roman, value)

    def test_print(self):
        text = []
        for el in range(1, 2000):
            text.append(Roman(el))
        for i in range(1, 2000):
            self.assertEqual(Roman(i), text[i - 1])

    def test_sum_error(self):
        for i in range(20):
            with self.assertRaises(ValueError):
                Roman(1999 - i) + Roman(i + 1)

    def test_equal(self):
        for i in range(1, 4, 27):
            self.assertTrue(Roman(i) == Roman(i))
        for i in range(1, 4, 56):
            self.assertFalse(Roman(i) == Roman(1999 - i))

    def test_int(self):
        for i in range(1, 2000):
            self.assertTrue(int(Roman(i)) == i)

    def test_str(self):
        self.assertEqual(str(Roman(1)), 'I')
        self.assertEqual(str(Roman(32)), 'XXXII')
        self.assertEqual(str(Roman(55)), 'LV')


main()
