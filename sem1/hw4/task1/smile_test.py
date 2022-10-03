from unittest import TestCase, main

from smile_logic import is_right


class SmileTest(TestCase):
    def test_different_False(self):
        self.assertFalse(is_right("(sjjs[lkkd<wp]]hjd>)"))
        self.assertFalse(is_right("(123"))

    def test_different_True(self):
        self.assertTrue(is_right(""))
        self.assertTrue(is_right("лолкекчебурек"))
        self.assertTrue(is_right("{{no}}"))
        self.assertTrue(is_right("123"))


main()
