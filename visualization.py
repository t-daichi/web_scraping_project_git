import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# スクレイピングデータの最新ファイルを取得
csv_files = glob.glob("news_*.csv")

# ファイルが1つもない場合のエラーハンドリング
if not csv_files:
    print("エラー: news_*.csv が見つかりません。スクレイピングを実行してください。")
    exit()

# 最新のCSVファイルを取得
latest_file = max(csv_files, key=os.path.getctime)

# ファイルが空でないかチェック
if os.path.getsize(latest_file) == 0:
    print(f"エラー: {latest_file} は空です。スクレイピングを確認してください。")
    exit()

# CSVファイルを読み込む
df = pd.read_csv(latest_file)

# タイトルの長さをヒストグラムで可視化
df["title_length"] = df["title"].apply(len)

plt.figure(figsize=(8, 5))
sns.histplot(df["title_length"], bins=10, kde=True)
plt.xlabel("タイトルの文字数")
plt.ylabel("記事数")
plt.title(f"記事タイトルの長さ分布 ({latest_file})")
plt.show()
