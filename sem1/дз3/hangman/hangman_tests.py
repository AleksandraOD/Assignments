from unittest import TestCase, main
import hangman_logic as hg


class HangmanTest(TestCase):
    def test_errors(self):
        self.assertRaises(ValueError, hg.valid_letters, 'hello', "а")

    def test_guessing(self):
        alphabet = "абвгдеёжзийклмнопрстуфхцчщъыьэюя"
        self.assertTrue(hg.is_letter_guessed("биосфера", "о"))
        self.assertTrue(hg.is_word_guessed("биосфера", "биосфера"))
        self.assertTrue(hg.valid_letters("б", alphabet))


main()
