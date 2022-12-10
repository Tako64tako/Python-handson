from bs4 import BeautifulSoup
import requests

def main():
    url = "https://www.p-world.co.jp/index.html"

    # TODO: requests.get()でurlのHTMLを取得してください
    r = requests.get(url)

    # TODO: BeautifulSoup()でHTMLを解析してください
    soup = BeautifulSoup(r.content, "html.parser")

    # TODO: soup.select()でh1タグの要素を出力してください
    print(soup.select("h1"))

    return soup.select("h1")
if __name__ == "__main__":
    main()