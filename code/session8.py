# 第8コマ テスト(受験者用スターター)
# 課題: data/test_psych.csv を眺めて、気づきを1つ挙げ、
# それを「グラフだけで納得させる」形で示しなさい。
# 提出物: 1. 気づき(1文) 2. その気づきのグラフ 3. このプログラム

from pathlib import Path

import matplotlib.pyplot as plt  # noqa: F401 (表示と仕上げに使う)
import pandas as pd

BASE = Path(__file__).resolve().parent.parent if "__file__" in globals() else Path(".")
df = pd.read_csv(BASE / "data" / "test_psych.csv")

# --- まず眺める ---
print(df.head(10))
print(df.shape)
print(df.describe(include="all"))
print("欠けた値の数:")
print(df.isna().sum())

# --- ここから下に、自分の分析を書く ---
# 気づき(1つに絞る):
# (集計の表を作る)
# (グラフを描く: タイトル=主張。比べる場合は分布の格差が見える形に)

# 提出前チェック:
# - 気づきは1つに絞った / タイトルが主張になっている
# - 軸ラベルと単位がそろっている / 棒グラフの軸は0から
# - 比べる相手が同じ図の中にいる
