# 第7コマ 仮説を納得させるグラフを作るためのデータ集め
# 仮説 → 比べる相手 → 集め方、の順に設計します。
# ここでは既存データで「下見」をする例を示します。

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

try:
    import japanize_matplotlib  # noqa: F401
except ImportError:
    pass

BASE = Path(__file__).resolve().parent.parent if "__file__" in globals() else Path(".")

# --- 例: 仮説「音楽があると反応が遅くなるはず」 ---
# 比べる相手: 静かな条件の反応時間
# 必要な変数: 条件(名義尺度)、反応時間(比尺度)
# 下見: 手元の反応時間データで、比べる表と分布を作る
rt = pd.read_csv(BASE / "data" / "psych_rt.csv")
cmp_table = (rt.groupby("条件")["反応時間"].agg(["mean", "median", "count"])
             .rename(columns={"mean": "平均", "median": "中央値", "count": "人数"}))
print(cmp_table)

rt.boxplot(column="反応時間", by="条件")
plt.title("音楽があると反応は遅い(下見: 分布で比べる)")
plt.suptitle("")
plt.xlabel("")
plt.ylabel("反応時間(ミリ秒)")
plt.show()

# --- データ集め計画シート(記入例) ---
plan = {
    "仮説": "朝の課題は、夕方の課題より反応が速いはず",
    "比べる相手": "夕方に実施したときの反応時間",
    "必要な変数": ["時間帯(名義)", "反応時間(比尺度)", "年代(名義)"],
    "集め方": "実験: 同じ課題を、朝と夕方で実施する",
    "相手と数": "各時間帯30名ずつ。年代の内訳がそろうようにする",
    "期間": "来週の月曜〜金曜",
    "偏りへの対策": "同じ人が両方やると練習効果が出るので、人は分ける",
}
for k, v in plan.items():
    print(k, ":", v)

# --- 実習 ---
# 班ごとに仮説を1つ立て、計画シートを完成させましょう。
# 発表は「仮説」と「比べる相手」の2点を中心に。
# 記入例は answers/session7_answers.py
