import sys, unittest
from task_4 import fib, fib_iter, fib_memo

recursion_limit = sys.getrecursionlimit()

class Task4Test_fib(unittest.TestCase):
    def test_zero(self):
        result = fib(0)
        self.assertEqual(result, 0)
    
    def test_one(self):
        result = fib(1)
        self.assertEqual(result, 1)
    
    def test_small(self):
        result = fib(7)
        self.assertEqual(result, 13)
    
    def test_large(self):
        with self.assertRaises(RecursionError):
            fib(recursion_limit + 50)

class Task4Test_fib_iter(unittest.TestCase):
    def test_zero(self):
        result = fib_iter(0)
        self.assertEqual(result, 0)
    
    def test_one(self):
        result = fib_iter(1)
        self.assertEqual(result, 1)
    
    def test_small(self):
        result = fib_iter(7)
        self.assertEqual(result, 13)
    
    def test_large(self):
        result = fib_iter(recursion_limit + 50)
        self.assertGreater(result, 0)

class Task4Test_fib_memo(unittest.TestCase):
    def test_zero(self):
        result = fib_memo(0)
        self.assertEqual(result, 0)
    
    def test_one(self):
        result = fib_memo(1)
        self.assertEqual(result, 1)
    
    def test_small(self):
        result = fib_memo(7)
        self.assertEqual(result, 13)
    
    def test_large(self):
        with self.assertRaises(RecursionError):
            fib(recursion_limit + 50)