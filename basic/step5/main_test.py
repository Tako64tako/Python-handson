import unittest
import subprocess

min = "20"
max = "25"


class TestCase(unittest.TestCase):
    def test_main(self):
        ret = subprocess.run(["python3", "main.py"],
                             capture_output=True, text=True)
        ret_list = ret.stdout.splitlines()

        bmi = ret_list[0]
        flag = ret_list[1]

        if bmi > min and bmi < max and flag == "OK":
            self.assertTrue(True)
        elif bmi < min and bmi > max and flag == "NG":
            self.assertFalse(True)
        else:
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
