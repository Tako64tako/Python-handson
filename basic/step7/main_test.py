import unittest
import subprocess

jouken1 = 400
jouken2 = 100
jouken3 = 4

# うるう年の条件
# 1. 西暦が4で割り切れる年はうるう年
# 2. また，西暦が400で割り切れる年はうるう年
# 3. ただし，西暦が100で割り切れる年はうるう年ではない


class TestCase(unittest.TestCase):
    def test_main(self):

        ret = subprocess.run(["python3", "main.py"],
                             capture_output=True, text=True)
        res = ret.stdout.splitlines()

        year = res[0]
        flag = res[1]
        print(flag)

        if (int(year) % jouken1) == 0 and flag == "うるう年です":
            # print("条件1に合致")
            self.assertTrue(True)
        elif (int(year) % jouken1) != 0 and int(year) % jouken2 == 0 and flag == "うるう年ではありません":
            # print("条件2に合致")
            self.assertFalse(True)
        elif (int(year) % jouken1) != 0 and (int(year) % jouken2) != 0 and (int(year) % jouken3) == 0 and flag == "うるう年です":
            # print("条件3に合致")
            self.assertTrue(True)
        elif (int(year) % jouken1) != 0 and (int(year) % jouken2) != 0 and (int(year) % jouken3) != 0 and flag == "うるう年ではありません":
            # print("全条件不一致")
            self.assertTrue(True)
        else:
            # print("条件外")
            self.assertFalse(True)


if __name__ == '__main__':
    unittest.main()
