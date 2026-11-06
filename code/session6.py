# 第6コマ データを眺めて、気づいたことをグラフだけで納得させる(データ分析)
# 手順: 眺める → 気づく → 確かめる → グラフで納得させる
# このファイルは「講師デモ」。演習では自分の気づきで作り直してください。

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

try:
    import japanize_matplotlib  # noqa: F401
except ImportError:
    pass

BASE = Path(__file__).resolve().parent.parent if "__file__" in globals() else Path(".")
rt = pd.read_csv(BASE / "data" / "psych_rt.csv")

# --- 手順1: 眺める ---
print(rt.head(10))
print(rt.describe(include="all"))

# --- 手順2-3: 気づきを、集計で確かめる ---
by_cond = rt.groupby("条件")["反応時間"].agg(["mean", "median", "std", "count"])
print(by_cond)  # 平均と中央値がずれる条件がある → 外れ値の気配

# --- 手順4: グラフだけで納得させる(タイトル=主張、分布で比べる) ---
rt.boxplot(column="反応時間", by="条件")
plt.title("音楽があると反応は遅く、ばらつきも大きい")
plt.suptitle("")
plt.xlabel("")
plt.ylabel("反応時間(ミリ秒)")
plt.show()

# --- 演習 ---
# 1. 自分の「気づき」を1つ選ぶ(年代との関係、正答数との関係、など)
# 2. それを、タイトル=主張のグラフ1枚で表す(説明文は書かない)。
#    比べる場合は、平均だけでなく分布を並べた図にすること
# 3. 隣の人と見せ合い、主張が一目で伝わるか確かめ合う
# 解答例(講師用)は answers/session6_answers.py
