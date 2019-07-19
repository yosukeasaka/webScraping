# Requests: WebページのHTMLを取得
import requests
# Beautiful Soupのインポート
from bs4 import BeautifulSoup
# CSVにデータを保存しよう
import pandas as pd

mazukoko = requests.get("https://mazuwakokokara.com/").text
# print (mazukoko.text)

soup = BeautifulSoup(mazukoko, 'html.parser')  # BeautifulSoupの初期化
# print(soup.prettify())

# このページのaタグをすべて抜き出す
tags = soup.find_all("a")

'''
# このページのaタグのURLのみ
for tag in tags:
    print(tag.get("href"))


# このページのaタグのテキストのみ
for tag in tags:
    print(tag.string)
'''

# 記事のHTMLタグを確認して、クラスで記事タイトルを取得
h2s = soup.find_all("h2", {"class": "entry-title"})
# print(h2s)
columns = ["Name", "Url"]
df = pd.DataFrame(columns=columns)  # 列名を指定する

for h2 in h2s:
    name = h2.a.string  # 記事名を取得
    url = h2.a.get("href")  # 記事のURLを取得
    se = pd.Series([name, url], columns)  # 行を作成
    df = df.append(se, columns)  # データフレームに行を追加
print(df)

filename = "result.csv"
df.to_csv(filename, encoding='utf-8-sig')
