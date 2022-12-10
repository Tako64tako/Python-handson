import unittest
import main

from bs4 import BeautifulSoup
import requests

url = "https://www.p-world.co.jp/index.html"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

# print(soup.select("h1"))

class TestCase(unittest.TestCase):
    def test_main(self):
        return_val = main.main()
        self.assertEqual(return_val, soup.select("h1"))


if __name__ == '__main__':
    unittest.main()