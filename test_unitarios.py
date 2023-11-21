import unittest
from unittest.mock import patch
from io import StringIO
from main import WordCounter, WordCounterObserver, PrintObserver

# Use o comando py -m unittest test_unitarios.py para executar os testes unitarios

class TestWordCounter(unittest.TestCase):
    def setUp(self):
        self.word_counter = WordCounter()

    def test_count_words_basic(self):
        result = self.word_counter.count_words("Hello there")
        self.assertEqual(result, {"Total Words": 2, "Even Length Words": 0, "Uppercase Words": 1})

    def test_count_words_empty_phrase(self):
        result = self.word_counter.count_words("")
        self.assertEqual(result, {"Total Words": 0, "Even Length Words": 0, "Uppercase Words": 0})

    def test_count_words_special_characters(self):
        result = self.word_counter.count_words("Praise the sun!")
        self.assertEqual(result, {"Total Words": 3, "Even Length Words": 2, "Uppercase Words": 1})

    def test_count_words_mixed_case(self):
        result = self.word_counter.count_words("Palavras com Maiúsculas Ooo")
        self.assertEqual(result, {'Total Words': 4, 'Even Length Words': 2, 'Uppercase Words': 3})


    def test_observer_not_called(self):
        observer = WordCounterObserver()

if __name__ == '__main__':
    unittest.main()

