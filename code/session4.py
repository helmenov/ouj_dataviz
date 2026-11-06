# 第4コマ 表のいろいろ。pandasによる表作成
# CSV はプログラムと同じ場所の data フォルダに置いてください。

from pathlib import Path

import pandas as pd

BASE = Path(__file__).resolve().parent.parent if "__file__" in globals() else Path(".")

# --- 例1: 読み込んで眺める ---
df = pd.read_csv(BASE / "data" / "weather_week.csv")
print(df.head())
print(df.shape)
print(df.columns.tolist())
print("最高気温の最大:", df["最高気温"].max(), "/ 平均:", df["最高気温"].mean())

# --- 例2: 条件で絞る ---
hot = df[df["最高気温"] >= 25]
print(hot)

# --- 例3: 列を足して、一元表を作る ---
sales = pd.read_csv(BASE / "data" / "shop_sales.csv")
sales["金額"] = sales["単価"] * sales["個数"]
by_item = (sales.groupby("商品")[["金額", "個数"]].sum()
           .rename(columns={"金額": "金額合計", "個数": "個数合計"})
           .sort_values("金額合計", ascending=False))
print(by_item)  # 一元表

# --- 例4: クロス集計表(アンケート: 年代×満足度) ---
survey = pd.read_csv(BASE / "data" / "survey.csv")
cross = pd.crosstab(survey["年代"], survey["満足度"])
print(cross)

# --- 例5: 段階2 要約の表 ---
rt = pd.read_csv(BASE / "data" / "psych_rt.csv")
print(rt[["反応時間", "正答数"]].describe())  # 個数・平均・四分位数・最小最大

# --- 例6: 段階4 推測と混同行列(信号検出理論のデータ) ---
sdt = pd.read_csv(BASE / "data" / "sdt_trials.csv")
cm = pd.crosstab(sdt["刺激"], sdt["反応"])
print(cm)  # 混同行列: ヒット38 / 見落とし12 / 誤警報9 / 正棄却41
hit_rate = cm.loc["あり", "あった"] / cm.loc["あり"].sum()
fa_rate = cm.loc["なし", "あった"] / cm.loc["なし"].sum()
print(f"ヒット率: {hit_rate:.0%} / 誤警報率: {fa_rate:.0%}")

# --- 演習 ---
# 1. weather_week.csv の最低気温の平均と、降水量が0より大きい日を作りましょう
# 2. shop_sales.csv で商品ごとの個数合計の一元表を作りましょう
# 3. survey.csv で年代×満足度のクロス集計を作り、気づいたことを1つ書きましょう
# 解答例は answers/session4_answers.py
