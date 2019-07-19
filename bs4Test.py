# Beautiful Soupのインポート
from bs4 import BeautifulSoup


# test HTML

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# BeautifulSoupの初期化
soup = BeautifulSoup(html_doc, 'html.parser')  # BeautifulSoupの初期化
# print(soup)
# print(soup.prettify())

# BeautifulSoupでtitleを取得
# print(soup.title) #<title>The Dormouse's story</title>と取得

# タイトルをタグなしで取得
# print(soup.title.string)

# BeautifulSoupで複数のaタグを取得
# print(soup.a) #　これだと一つしか取れない
# print(soup.find_all("a")) # find_allを使うと全て取得できる(as list)

# for loopを使って一つずつ取り出す
tags = soup.find_all("a")

for tag in tags:
    print(tag.string)
'''
Elsie
Lacie
Tillie
と表示される
'''

# BeautifulSoupでURLの取得
# print(soup.a.get("href"))  # http://example.com/elsieと出力
for tag in tags:
    print(tag.get("href"))
'''
http://example.com/elsie
http://example.com/lacie
http://example.com/tillie
と表示される
'''

