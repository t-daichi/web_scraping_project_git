import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

# スクレイピング対象のURL
URL = "https://techcrunch.com/"

# User-Agentを設定
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# HTTPリクエストを送信
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 記事タイトルのリンクを取得
articles = soup.find_all("a", class_="loop-card__title-link")

data = []
for article in articles[:10]:  # 最新の10記事を取得
    title = article.get_text(strip=True)
    link = article["href"]
    data.append({"title": title, "link": link})

# データが空なら処理を終了
if not data:
    print("エラー: データを取得できませんでした。対象サイトの構造を確認してください。")
    exit()

# DataFrame化
df = pd.DataFrame(data)

# 現在の日付で保存
today = datetime.date.today().strftime("%Y-%m-%d")
csv_filename = f"news_{today}.csv"

# CSVに保存
df.to_csv(csv_filename, index=False, encoding="utf-8-sig")
print(f"データを {csv_filename} に保存しました")
