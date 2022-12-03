import unittest
from io import StringIO
from contextlib import redirect_stdout

import main

jouken1 = 400
jouken2 = 100
jouken3 = 4


class TestCase(unittest.TestCase):
    def test_main(self):
        io = StringIO()
        with redirect_stdout(io):
            main.main()
        year = io.getvalue()
        flag = main.main()

        if int(year) % jouken1 == 0 and flag == True:
            self.assertTrue(True)
        elif int(year) % jouken1 != 0 and int(year) % jouken2 == 0 and flag == False:
            self.assertFalse(True)
        elif int(year) % jouken1 != 0 and int(year) % jouken2 != 0 and int(year) % jouken3 == 0 and flag == True:
            self.assertTrue(False)
        else:
            self.assertFalse(False)


if __name__ == '__main__':
    unittest.main()
