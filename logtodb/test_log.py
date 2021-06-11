import unittest
from stats import read


class TestLog(unittest.TestCase):
    def test_read(self):
        self.assertEqual(read('test.db'), [(200, 59), (404, 39)])
