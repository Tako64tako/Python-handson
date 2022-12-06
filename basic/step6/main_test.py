import unittest
import re
import subprocess

qq_odd = ['1', '3', '5', '7', '9', '3', '9', '15', '21', '27', '5',
          '15', '25', '35', '45', '7', '21', '35', '49', '9', '27', '45']


class TestCase(unittest.TestCase):
    def test_main(self):

        ret = subprocess.run(['python3', 'main.py'],
                             capture_output=True, text=True)

        for line in qq_odd, ret.stdout.splitlines():
            self.assertEqual(line, qq_odd)


if __name__ == '__main__':
    unittest.main()
