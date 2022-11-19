import unittest
from io import StringIO
from contextlib import redirect_stdout

import main


class TestCase(unittest.TestCase):
    def test_main(self):
        io = StringIO()
        with redirect_stdout(io):
            main.main()
        bmi = io.getvalue()
        flag = main.main()

        if bmi > "20" and bmi < "25" and flag == True:
            self.assertTrue(True)
        elif bmi < "20" and bmi > "25" and flag == False:
            self.assertFalse(True)
        else:
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
