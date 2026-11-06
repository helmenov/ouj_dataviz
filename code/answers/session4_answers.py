# 第4コマ 演習の解答例(pandas)
from pathlib import Path

import pandas as pd

BASE = Path(__file__).resolve().parent.parent.parent if "__file__" in globals() else Path(".")

df = pd.read_csv(BASE / "data" / "weather_week.csv")
# 1. 最低気温の平均 / 降水量が0より大きい日
print("最低気温の平均:", df["最低気温"].mean())
print(df[df["降水量"] > 0])

# 2. 商品ごとの個数合計の一元表
sales = pd.read_csv(BASE / "data" / "shop_sales.csv")
by_qty = (sales.groupby("商品")["個数"].sum()
          .sort_values(ascending=False))
print(by_qty)

# 3. survey.csv で年代×満足度のクロス集計(人数)と気づき(例):
# 「満足度5は若い年代に多い」のように、行と列の交わりを見て1つ書けばよい。
survey = pd.read_csv(BASE / "data" / "survey.csv")
print(pd.crosstab(survey["年代"], survey["満足度"]))
