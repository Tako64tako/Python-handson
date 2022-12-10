import unittest
import pandas as pd


class TestCase(unittest.TestCase):
    def test_main(self):
        get_csv = pd.read_csv("./iris-dataset.csv")


if __name__ == '__main__':
    unittest.main()
