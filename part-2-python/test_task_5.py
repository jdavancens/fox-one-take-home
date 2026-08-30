import unittest
from task_5 import create_anagram_key, group_anagrams

class Task5Test_create_anagram_key(unittest.TestCase):
    def test_empty(self):
        result = create_anagram_key('')
        self.assertEqual(result, '')

    def test_order(self):
        result = create_anagram_key('cba')
        self.assertEqual(result, 'abc')

    def test_casing(self):
        result = create_anagram_key('Abc')
        self.assertEqual(result, 'abc')

    def test_whitespace(self):
        result = create_anagram_key('a b')
        self.assertEqual(result, 'ab')

    def test_punctuation(self):
        result = create_anagram_key('a.b!')
        self.assertEqual(result, 'ab')

class Task5Test_group_anagrams(unittest.TestCase):
    def test_empty(self):
        result = group_anagrams([])
        self.assertEqual(result, [])

    def test_no_anagrams(self):
        words = ['dog', 'cat']
        result = group_anagrams(words)
        expected = [['dog'], ['cat']]
        self.assertEqual(result, expected)
    
    def test_simple_anagrams(self):
        words = ['dog', 'god']
        result = group_anagrams(words)
        expected = [['dog', 'god']]
        self.assertEqual(result, expected)

    def test_complex_anagrams(self):
        words = ['O, Cat!', 'taco', 'Clint Eastwood', 'old-west action']
        result = group_anagrams(words)
        expected = [['O, Cat!', 'taco'], ['Clint Eastwood', 'old-west action']]
        self.assertEqual(result, expected)