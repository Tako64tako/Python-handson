import unittest
from io import StringIO
from contextlib import redirect_stdout

import main


class TestCase(unittest.TestCase):
    def test_main(self):
        io = StringIO()
        with redirect_stdout(io):
            main.main()
        self.assertRegex(
            io.getvalue(), r'37\n*')

if __name__ == '__main__':
    unittest.main()