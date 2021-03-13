import pandas as pd
import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from bs4 import BeautifulSoup

df = pd.DataFrame(columns=["主題類別", "討論主題", "互動/人氣度"])

h = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
}
for page in range(1, 51):
    print("頁數", page)
    url = "https://forum.gamer.com.tw/B.php?page=" + str(page) + "&bsn=17532"
    response = requests.get(url, verify=False, headers=h)

    html = BeautifulSoup(response.text)

    rows = html.find_all("tr", class_="b-list__row b-list-item b-imglist-item")
    for r in rows:
        title = r.find("p", class_="b-list__summary__sort")
        name = r.find("p", class_="b-list__main__title")
        popular = r.find("p", class_="b-list__count__number")
        print(title.text)
        print(name.text)
        print(name["href"])
        print(popular.text)
        print("-" * 30)
        s = pd.Series([title.text, name.text, popular.text],
                      index=["主題類別", "討論主題", "互動/人氣度"])
        df = df.append(s, ignore_index=True)
    df.to_csv("巴哈.csv", encoding="utf-8", index=False)


