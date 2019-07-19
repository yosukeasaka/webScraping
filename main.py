# Requests: WebページのHTMLを取得
import requests
# Beautiful Soupのインポート
from bs4 import BeautifulSoup
# Pandas をインポート
import pandas as pd

reuters = requests.get("https://jp.reuters.com/news/topNews").text
# BeautifulSoupの初期化
soup = BeautifulSoup(reuters, 'html.parser')

# このページのaタグをすべて抜き出す
tags = soup.find_all("h2")

key_word = input("What do you want to know : ")
result = False
columns = ["Name", "Post Date", "URL"]
df = pd.DataFrame(columns=columns)  # 列名を指定する
i = 0
for tag in tags:
    ahref = tag.find("a")
    time = tag.find("span", {"class": "timestamp"})
    name = ahref.string  # 記事名を取得
    url = "https://jp.reuters.com" + ahref.get("href")  # URLを取得

    if str(key_word) in str(ahref.string):
        if not time is None:
            '''print("---------------------------------------")
            print(name)
            print("投稿日時",time.string)
            print(url)
            print("---------------------------------------")'''
            se = pd.Series([name, time.string, url], columns)  # 行を作成
            df = df.append(se, columns)  # データフレームに行を追加
            i += 1
        elif not ahref.string is None:
            '''print("---------------------------------------")
            print(name)
            print(url)
            print("---------------------------------------")'''
            se = pd.Series([name, None, url], columns)  # 行を作成
            df = df.append(se, columns)  # データフレームに行を追加
            i += 1
        result = True
if result is False:
    print("There are no news of " + key_word)

filename = "result.csv"
df.to_csv(filename, encoding='utf-8-sig')
df.head(i)
