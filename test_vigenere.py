from string import digits
from vigenere import Vigenere
from unittest import TestCase

class TestVigenere(TestCase):
    def test_ascii_alphabet(self):
        vigenere = Vigenere()

        self.assertEqual(vigenere.encrypt('banana', 'a'), 'banana')
        self.assertEqual(vigenere.encrypt('banana', 'b'), 'cbobob')
        self.assertEqual(vigenere.encrypt('banana', 'aba'), 'bbnaoa')
        self.assertEqual(vigenere.encrypt('banana', 'lemon'), 'mezoal')
        self.assertEqual(vigenere.encrypt('banana', 'banana'), 'caaaaa')

        self.assertEqual(vigenere.decrypt('banana', 'a'), 'banana')
        self.assertEqual(vigenere.decrypt('cbobob', 'b'), 'banana')
        self.assertEqual(vigenere.decrypt('bbnaoa', 'aba'), 'banana')
        self.assertEqual(vigenere.decrypt('mezoal', 'lemon'), 'banana')
        self.assertEqual(vigenere.decrypt('caaaaa', 'banana'), 'banana')

    def test_digits(self):
        vigenere = Vigenere(list(digits))

        self.assertEqual(vigenere.encrypt('1234', '0'), '1234')
        self.assertEqual(vigenere.encrypt('1234', '420'), '5438')

        self.assertEqual(vigenere.decrypt('1234', '0'), '1234')
        self.assertEqual(vigenere.decrypt('5438', '420'), '1234')

    def test_mixed_case(self):
        vigenere = Vigenere(['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D'])

        self.assertEqual(vigenere.encrypt('aAbB', 'a'), 'aAbB')
        self.assertEqual(vigenere.encrypt('aAbB', 'cDaB'), 'cdbc')

        self.assertEqual(vigenere.decrypt('aAbB', 'a'), 'aAbB')
        self.assertEqual(vigenere.decrypt('cdbc', 'cDaB'), 'aAbB')

    def test_unicode(self):
        vigenere = Vigenere([
            'á', 'à', 'â', 'ã', 'ä', 'é', 'è', 'ê', 'ë', 'í',
            'ì', 'ï', 'ó', 'ò', 'õ', 'ö', 'ú', 'ù', 'ü'
        ])

        self.assertEqual(vigenere.encrypt('áéíóú', 'á'), 'áéíóú')
        self.assertEqual(vigenere.encrypt('áéíóú', 'äïü'), 'äúëúë')

        self.assertEqual(vigenere.decrypt('áéíóú', 'á'), 'áéíóú')
        self.assertEqual(vigenere.decrypt('äúëúë', 'äïü'), 'áéíóú')

    def test_lists(self):
        vigenere = Vigenere(['bar', 'foo', 'hello', 'man', 'woman', 'world'])

        self.assertEqual(
            vigenere.encrypt(['hello', 'world'], ['bar']),
            ['hello', 'world']
        )
        self.assertEqual(
            vigenere.encrypt(['hello', 'world'], ['foo', 'bar']),
            ['man', 'world']
        )

        self.assertEqual(
            vigenere.decrypt(['hello', 'world'], ['bar']),
            ['hello', 'world']
        )
        self.assertEqual(
            vigenere.decrypt(['man', 'world'], ['foo', 'bar']),
            ['hello', 'world']
        )

    def test_invalid_alphabet(self):
        with self.assertRaises(ValueError) as e:
            Vigenere('abcd')
            self.assertEqual(str(e.exception), 'Alphabet must be a list of characters or strings')

        with self.assertRaises(ValueError) as e:
            Vigenere('abcda')
            self.assertEqual(str(e.exception), 'Alphabet must not have duplicated symbols')

    def test_invalid_text(self):
        with self.assertRaises(ValueError) as e:
            vigenere = Vigenere()
            vigenere.encrypt(123, 'aaa')
            self.assertEqual(str(e.exception), 'Text must be a string or a list of strings')

    def test_invalid_key(self):
        vigenere = Vigenere()

        with self.assertRaises(ValueError) as e:
            vigenere.encrypt('', '')
            self.assertEqual(str(e.exception), 'Key must not be empty')

        with self.assertRaises(ValueError) as e:
            vigenere.encrypt('', 123)
            self.assertEqual(str(e.exception), 'Key must be a string or a list of strings')

    def test_text_not_in_alphabet(self):
        with self.assertRaises(ValueError) as e:
            vigenere = Vigenere()
            vigenere.encrypt('abcD', 'banana')

            self.assertEqual(str(e.exception), 'Symbols in text must be in the alphabet')

    def test_key_not_in_alphabet(self):
        with self.assertRaises(ValueError) as e:
            vigenere = Vigenere()
            vigenere.decrypt('abcdefgh', 'bananA')

            self.assertEqual(str(e.exception), 'Symbols in key must be in the alphabet')

