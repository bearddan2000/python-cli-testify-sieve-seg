from testify import *
from io import StringIO
from unittest.mock import patch
import unittest

import main

class TestMain(TestCase):
    """docstring for TestMain."""
    def test_simpleSieve(self):
        with patch('sys.stdout', new = StringIO()) as captured:
            main.simpleSieve(5)
            assert_equal(captured.getvalue(), "2 3 ")

    def test_segmentedSieve(self):
        with patch('sys.stdout', new = StringIO()) as captured:
            main.segmentedSieve(5)
            assert_equal(captured.getvalue(), "2 3 ")

if __name__ == '__main__':
    run()
