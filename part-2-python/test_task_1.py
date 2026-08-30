import unittest
from task_1 import most_common_word

class Task1Test(unittest.TestCase):
    def test_empty_string(self):
        self.assertIsNone(most_common_word(''))

    def test_whitespace_only(self):
        self.assertIsNone(most_common_word(' '))

    def test_happy(self):
        result = most_common_word('cat cat dog')
        self.assertEqual(result, 'cat')

    def test_case_insensitivity(self):
        result = most_common_word('cat Cat dog')
        self.assertEqual(result, 'cat')

    def test_end_punctuation(self):
        result = most_common_word('cat, cat! dog')
        self.assertEqual(result, 'cat')

    def test_stopwords(self):
        input = 'the cat ran away from the dog but the dog was faster' # 'the' x 3,  'dog' x 2
        stopwords = {'the'}
        result = most_common_word(input, stopwords)
        self.assertEqual(result, 'dog')

    def test_normalized_stopwords(self):
        input = 'The cat ran away from the dog but the dog was faster.'
        stopwords = {'the'}
        result = most_common_word(input, stopwords)
        self.assertEqual(result, 'dog')

    def test_internal_apostrophes(self):
        input = "won't won't wont"
        result = most_common_word(input)
        self.assertEqual(result, "won't")

    def test_other_whitespace(self):
        input = "cat\tcat\ndog"
        result = most_common_word(input)
        self.assertEqual(result, 'cat')
