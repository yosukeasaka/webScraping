# 必要なライブラリーのインポート

# サーバーから情報を取る際に必要
import requests
import json  # JSONデータを扱う際に必要
from pandas import DataFrame # 集めた情報をデータフレームにして見やすく

# 保有しているコインのレート
coins = {'ETC': 'etc_jpy',
         'XEM': 'xem_jpy', 
         'BCH': 'bch_jpy'}

# 購入してコインの量
bought_coin = {'ETC': 10,
               'XEM': 1500, 
               'BCH': 0.35}

# コインの購入価格
bought_coin_price = {'ETC': 6523.3,
                     'XEM': 10319, 
                     'BCH': 12925}
# 利益を計算してくれる関数
def check_profit(key, price):
        price *= bought_coin[key]
        profit = price - bought_coin_price[key]
        return round(profit, 4)

# 売り時のメッセージを返す関数
def better_time_tosell(key, profit):
    if profit >= bought_coin_price[key] * 1.1:
        return '売り時！'
    else:
        return 'Do not sell'

# データの取得からデータフレームの作成までを行う関数
def make_dataframe():
    #APIの取得先
    URL = 'https://coincheck.com/api/rate/'
    
    # データを収納するリスト作成
    current_rate_list = []
    bought_price_list = []
    profit_list = [] 
    message_list = []

    for key, item in coins.items():
        #APIの取得
        coincheck = requests.get(URL+item).json()
        coincheck_rate = float(coincheck['rate'])

        # 現在のレートをリストに収納
        current_rate_list.append(round(coincheck_rate * bought_coin[key],4))

        # 購入時の価格をリストに収納
        bought_price_list.append(bought_coin_price[key])

        # 利益をリストに収納
        profit = check_profit(key, float(coincheck['rate']))
        profit_list.append(profit)
        
        # 売り時のメッセージを収納
        message = better_time_tosell(key, profit)
        message_list.append(message)
        
        #print(key +'の利益　¥'+ str(profit)+ " (" + message +")")
        
    # 取得し、リストに入力したデータを辞書として保管
    v_coin = {
        '保有仮想通貨':['ETC','XEM','BCH'],
        '現在のレート':current_rate_list, 
        '購入時のレート':bought_price_list, 
        '利益':profit_list,
        '売り時':['Do not sell', 'Do not sell', 'Do not sell']
    }
    
    return v_coin


DataFrame(make_dataframe())
