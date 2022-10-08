import sqlite3
from urllib import response
import requests
import json 

# Tuple  Convert to String　function
def CT(tup):
    str = "".join(tup)
    return str

# sqliteに接続する
con = sqlite3.connect('test.db')
c = con.cursor()

# 任意のテーブルを削除する
c.execute("DROP TABLE small_area;")


# middle_areaのテーブルを作成する
c.execute("CREATE TABLE small_area(code STRING, name STRING, m_code STRING, m_name STRING, l_code STRING, l_name STRING, ss_code STRING, ss_name STRING, lss_code STRING, lss_name STRING, api_version FLOAT)")

# large_areaテーブルから中エリアコードを取得する
ma = c.execute("SELECT code FROM middle_area;")
ma = c.fetchall()


# 小エリアテーブルにAPIからデータを取得し、格納する
for j in range(len(ma)):
    # 小リアマスタAPIからデータを取得する
    query = {
        'key':'2bc4f479e6c2392d',
        'middle_area':CT(ma[j]),  # 中エリアを入力する
        'format':'json'
        }
        # エリアマスタAPIのリクエストURL
    url = 'http://webservice.recruit.co.jp/hotpepper/small_area/v1/'
    # JSONを取得
    responce = requests.get(url, query)
    # JSONの読み込み
    result = json.loads(responce.text)['results']

    # APIからデータを取得し、テーブルに格納する
    for i in range(len(result["small_area"])):
        sql = "INSERT INTO small_area VALUES(?,?,?,?,?,?,?,?,?,?,?)"
        c.execute(sql,[result["small_area"][i]["code"],result["small_area"][i]["name"],result["small_area"][i]["middle_area"]["code"],result["small_area"][i]["middle_area"]["name"],result["small_area"][i]["large_area"]["code"],result["small_area"][i]["large_area"]["name"],result["small_area"][i]["service_area"]["code"],result["small_area"][i]["service_area"]["name"],result["small_area"][i]["large_service_area"]["code"],result["small_area"][i]["large_service_area"]["name"],result["api_version"]])
    con.commit()
con.close()



