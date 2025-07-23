import unittest
from esercizi_python import StringProcessor

class TestStringProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = StringProcessor()

    def test_reverse_string(self):
        self.assertEqual(self.processor.reverse_string("hello"), "olleh")
        self.assertEqual(self.processor.reverse_string(""), "")
        self.assertEqual(self.processor.reverse_string("a"), "a")
        self.assertEqual(self.processor.reverse_string("123"), "321")

    def test_capitalize_words(self):
        self.assertEqual(self.processor.capitalize_words("hello world"), "HELLO WORLD")
        self.assertEqual(self.processor.capitalize_words(""), "")
        self.assertEqual(self.processor.capitalize_words("Python3"), "PYTHON3")

    def test_count_vowels(self):
        self.assertEqual(self.processor.count_vowels("hello"), 2)
        self.assertEqual(self.processor.count_vowels("HELLO"), 2)
        self.assertEqual(self.processor.count_vowels("bcdfg"), 0)
        self.assertEqual(self.processor.count_vowels("AEIOUaeiou"), 10)
        self.assertEqual(self.processor.count_vowels(""), 0)

if __name__ == '__main__':
    unittest.main()
