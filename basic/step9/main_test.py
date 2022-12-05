# coding:utf-8

import unittest
from io import StringIO
from contextlib import redirect_stdout

import main

class UnitTest(unittest.TestCase):
    def test_main(self):
        io = StringIO()
        with redirect_stdout(io):
            main.main()
        self.assertRegex(
            io.getvalue(), r'勇者は荒野を歩いていた\n勇者はスライムを攻撃した\n*')

if __name__ == "__main__":
    unittest.main()