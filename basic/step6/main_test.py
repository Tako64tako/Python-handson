import unittest
from io import StringIO
from contextlib import redirect_stdout

import main

qq_odd = [1, 3, 5, 7, 9, 3, 9, 15, 21, 27, 5,
          15, 25, 35, 45, 7, 21, 35, 49, 9, 27, 45]


class TestCase(unittest.TestCase):
    def test_main(self):
        for line in qq_odd, main.main():
            self.assertEqual(line, qq_odd)


if __name__ == '__main__':
    unittest.main()
