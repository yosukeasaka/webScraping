# Requests: WebページのHTMLを取得
import requests
# Beautiful Soupのインポート
from bs4 import BeautifulSoup
# Pandas をインポート
import pandas as pd

# requestsを使ってURLからデータを取得
reuters = requests.get("https://jp.reuters.com/news/topNews").text

# BeautifulSoupの初期化
soup = BeautifulSoup(reuters, 'html.parser')

# このページのaタグをすべて抜き出す
tags = soup.find_all("h2")

# コラムの作成
columns = ["Name", "Post Date", "URL"]　
# 列名を指定する
df = pd.DataFrame(columns=columns)

# インプットを作成
key_word = input("What do you want to know : ")

# 結果が何も表示されない時のため
result = False  

# カウントするための変数の作成
i = 0

# ここからtags = soup.find_all("h2")をループさせて出力
for tag in tags:
    ahref = tag.find("a")
    time = tag.find("span", {"class": "timestamp"})
    name = ahref.string  # 記事名を取得
    url = "https://jp.reuters.com" + ahref.get("href")  # URLを取得
    
    # キーワードを含むものを探す
    if str(key_word) in str(ahref.string):
        # 時間の情報あるものとないもので分ける。これしないとエラーが出たので作りました。
        if not time is None:
            print("---------------------------------------")
            print(name)
            print("投稿日時",time.string)
            print(url)
            print("---------------------------------------")
            se = pd.Series([name, time.string, url], columns)  # 行を作成
            df = df.append(se, columns)  # データフレームに行を追加
            i += 1  # 入手できた投稿数をカウント
        elif not ahref.string is None:
            print("---------------------------------------")
            print(name)
            print(url)
            print("---------------------------------------")
            se = pd.Series([name, None, url], columns)  # 行を作成
            df = df.append(se, columns)  # データフレームに行を追加
            i += 1　# 入手できた投稿数をカウント
        result = True

# 結果が何も表示されない時はこれを表示
if result is False:
    print("There are no news of " + key_word)

#ここからは出た結果をCSVファイルとして保存するコード
filename = "result.csv"
df.to_csv(filename, encoding='utf-8-sig')
df.head(i)　# テストでカウント数分だけ出力
