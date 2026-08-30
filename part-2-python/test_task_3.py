import unittest
from task_3 import Logger

class Task3Test(unittest.TestCase):
    def test_empty(self):
        logger = Logger()
        result = logger.get_logs()
        self.assertEqual(result, [])
    
    def test_get_log(self):
        logger = Logger()
        messages = [f'message {i}' for i in range(5)]
        for msg in messages:
            logger.log(msg)
        logs = logger.get_logs()
        self.assertEqual(logs, messages)
    
    def test_immutable_store(self):
        logger = Logger()
        messages = [f'message {i}' for i in range(5)]
        for msg in messages:
            logger.log(msg)
        logs1 = logger.get_logs()
        logs1.pop()
        logs2 = logger.get_logs()
        self.assertEqual(logs2, messages)
    
    def test_search_match(self):
        logger = Logger()
        messages = [f'message {i} of 5' for i in range(5)]
        for msg in messages:
            logger.log(msg)
        results = logger.search('3 of 5')
        expected = ['message 3 of 5']
        self.assertEqual(results, expected)
    
    def test_search_no_match(self):
        logger = Logger()
        messages = [f'message {i} of 5' for i in range(5)]
        for msg in messages:
            logger.log(msg)
        results = logger.search('xyz')
        expected = []
        self.assertEqual(results, expected)

    def test_search_empty_log(self):
        logger = Logger()
        results = logger.search('xyz')
        expected = []
        self.assertEqual(results, expected)
    
    def test_search_log_order(self):
        logger = Logger()
        messages = [
            'success, 1',
            'error, 2',
            'success, 3',
        ]
        for log in messages:
            logger.log(log)
        results = logger.search('success')
        expected = ['success, 1', 'success, 3']
        self.assertEqual(results, expected)
    
    def test_case_sensitivity(self):
        logger = Logger()
        messages = [
            'success, 1',
            'error, 2',
            'Success, 3',
        ]
        for log in messages:
            logger.log(log)
        results = logger.search('success')
        expected = ['success, 1']
        self.assertEqual(results, expected)