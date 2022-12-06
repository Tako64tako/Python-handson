# coding:utf-8

import unittest
import subprocess


class UnitTest(unittest.TestCase):
    def test_main(self):
        ret = subprocess.run(["python3", "main.py"],
                             capture_output=True, text=True)
        self.assertRegex(
            ret.stdout, r'勇者は荒野を歩いていた\n勇者はスライムを攻撃した\n*')


if __name__ == "__main__":
    unittest.main()
