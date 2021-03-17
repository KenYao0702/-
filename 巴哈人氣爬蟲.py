import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import requests
import json
import pandas as pd
h = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}
table = {
    "名稱":[],
    "排行":[],
    "人氣":[],
    "版主":[]
}

for page in range(1, 5):
    print("第"+ str(page) +"頁")
    url = "https://forum.gamer.com.tw/ajax/rank.php?c=21&page=" + str(page) + ""
    response = requests.get(url, verify=False, headers=h)
    print(response.status_code)
    gamers = json.loads(response.text)
    print(gamers)
    for r in gamers:
        title = r["title"]
        administrator = r["userid"]
        popular = r["hot"]
        rank = r["ranking"]
        print("標題", title)
        print("排行", rank)
        print("人氣", popular)
        print("版主", administrator)
        print("*" * 50)
        table["名稱"].append(title)
        table["排行"].append(rank)
        table["人氣"].append(popular)
        table["版主"].append(administrator)
        df = pd.DataFrame(table)
        df.to_csv("巴哈人氣爬蟲.csv", encoding="utf-8", index=False)

