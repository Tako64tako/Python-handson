import unittest
import main


class TestCase(unittest.TestCase):
    def test_main(self):
        return_val = main.main()
        self.assertRegex(
            return_val, r'[hH][eE][lL][lL][oO][,\s]*[wW][oO][rR][lL][dD][!]*')


if __name__ == '__main__':
    unittest.main()
