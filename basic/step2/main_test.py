import unittest
import subprocess

class TestCase(unittest.TestCase):
    def test_main(self):
        ret = subprocess.run(["python3", "main.py"],capture_output=True,text=True)
        self.assertRegex(
            ret.stdout, '37')

if __name__ == '__main__':
    unittest.main()