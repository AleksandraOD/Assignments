from caesar_logic import encrypt, decrypt
from unittest import TestCase, main


class CaesarTest(TestCase):
    def test_encrypt(self):
        self.assertEqual(encrypt(3, 'Hello World'), "Khoor Zruog")
        self.assertEqual(encrypt(-1, 'Hello World'), "Gdkkn Vnqkc")

    def test_decrypt(self):
        self.assertEqual(decrypt(3, 'Zlqh lv jrrg'), "Wine is good")
        self.assertEqual(decrypt(-1, 'good vibes only'), "hppe wjcft pomz")
        self.assertEqual(encrypt(7, 'Zero'), 'Glyv')


main()
