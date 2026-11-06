# 第6コマ 演習の解答例(講師用デモ: 年代と反応時間 / 外れ値)
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

try:
    import japanize_matplotlib  # noqa: F401
except ImportError:
    pass

BASE = Path(__file__).resolve().parent.parent.parent if "__file__" in globals() else Path(".")
rt = pd.read_csv(BASE / "data" / "psych_rt.csv")

# 気づき1: 年代が上がると反応時間が長い → 箱ひげ図で分布ごと比べる
rt.boxplot(column="反応時間", by="年代")
plt.title("年代が上がると、反応時間は長くなる")
plt.suptitle("")
plt.xlabel("")
plt.ylabel("反応時間(ミリ秒)")
plt.show()

# 気づき2: 音楽条件には飛び抜けて遅い人がいる → ヒストグラムで姿を見る
music = rt[rt["条件"] == "音楽あり"]
music["反応時間"].plot.hist(bins=15, color="#F58518", edgecolor="white",
                          title="音楽条件には、飛び抜けて遅い人が混ざっている",
                          xlabel="反応時間(ミリ秒)")
plt.show()
print("700ミリ秒以上:", len(music[music["反応時間"] >= 700]), "名")
