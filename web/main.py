from bs4 import BeautifulSoup
import requests

def main():
    url = "https://www.p-world.co.jp/index.html"

    # TODO: requests.get()でurlのHTMLを取得してください

    # TODO: BeautifulSoup()でHTMLを解析してください

    # TODO: soup.select()でh1タグの要素を出力してください

    return soup.select("h1")
if __name__ == "__main__":
    main()