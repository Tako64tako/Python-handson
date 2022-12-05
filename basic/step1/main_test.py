import unittest
import subprocess

class TestCase(unittest.TestCase):
    def test_main(self):
        ret = subprocess.run(["python3","main.py"],capture_output=True,text=True)
        #main.pyを実行して，標準出力を文字列で受け取り
　　#ret.stdoutが標準出力の結果
        self.assertRegex(
            ret.stdout, r'[hH][eE][lL][lL][oO][,\s]*[wW][oO][rR][lL][dD][!]*\n*')

if __name__ == '__main__':
    unittest.main()
