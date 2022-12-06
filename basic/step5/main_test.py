import unittest
import subprocess

min = "20"
max = "25"


class TestCase(unittest.TestCase):
    def test_main(self):
        ret = subprocess.run(["python3", "main.py"],
                             capture_output=True, text=True)
        bmi = ret.stdout
        if bmi > min and bmi < max:
            self.assertTrue(True)
        elif bmi < min and bmi > max:
            self.assertFalse(True)
        else:
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
