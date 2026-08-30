import unittest
from task_2 import merge_intervals

class Task2Test(unittest.TestCase):
    def test_empty(self):
        input = []
        result = merge_intervals(input)
        self.assertEqual(result, [])

    def test_single_interval(self):
        input = [[1, 2]]
        result = merge_intervals(input)
        expected = [[1, 2]]
        self.assertEqual(result, expected)
    
    def test_point_interval(self):
        input = [[1, 1]]
        result = merge_intervals(input)
        expected = [[1, 1]]
        self.assertEqual(result, expected)

    def test_non_overlap(self):
        input = [[1, 2], [3, 4]]
        result = merge_intervals(input)
        expected = [[1, 2], [3, 4]]
        self.assertEqual(result, expected)

    def test_simple_overlap(self):
        input = [[1, 3], [2, 4]]
        result = merge_intervals(input)
        expected = [[1, 4]]
        self.assertEqual(result, expected)

    def test_same_start(self):
        input = [[1, 3], [1, 4]]
        result = merge_intervals(input)
        expected = [[1, 4]]
        self.assertEqual(result, expected)

    def test_same_end(self):
        input = [[1, 3], [2, 3]]
        result = merge_intervals(input)
        expected = [[1, 3]]
        self.assertEqual(result, expected)

    def test_contained(self):
        input = [[1, 5], [2, 4]]
        result = merge_intervals(input)
        expected = [[1, 5]]
        self.assertEqual(result, expected)

    def test_touching(self):
        input = [[1, 2], [2, 3]]
        result = merge_intervals(input)
        expected = [[1, 3]]
        self.assertEqual(result, expected)

    def test_unsorted(self):
        input = [[2, 4], [1, 3]]
        result = merge_intervals(input)
        expected = [[1, 4]]
        self.assertEqual(result, expected)

    def test_three_overlapping(self):
        input = [[1, 4], [3, 6], [5, 8]]
        result = merge_intervals(input)
        expected = [[1, 8]]
        self.assertEqual(result, expected)