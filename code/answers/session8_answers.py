# 第8コマ テストの模範解答(講師用)
# 受験者は気づきを1つに絞る。ここには候補となる作例を載せる。
# 埋め込まれたパターン:
#  1. 年代が上がると反応時間が長い
#  2. ペア条件は速いが、ばらつきが大きい
#  3. 午後は午前より反応時間が長い
#  おまけ: 外れ値2名(980, 1050) / 反応時間の欠けた値2件
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

try:
    import japanize_matplotlib  # noqa: F401
except ImportError:
    pass

BASE = Path(__file__).resolve().parent.parent.parent if "__file__" in globals() else Path(".")
df = pd.read_csv(BASE / "data" / "test_psych.csv")

# 作例1: 年代と反応時間(分布で比べる)
df.boxplot(column="反応時間", by="年代")
plt.title("年代が上がると、反応時間は長くなる")
plt.suptitle("")
plt.xlabel("")
plt.ylabel("反応時間(ミリ秒)")
plt.show()

# 作例2: 条件の比較(速さとばらつきの両方)
df.boxplot(column="反応時間", by="条件")
plt.title("ペアは速い人が多いが、遅い人もいてばらつきが大きい")
plt.suptitle("")
plt.xlabel("")
plt.ylabel("反応時間(ミリ秒)")
plt.show()

# 作例3: 時間帯の比較
df.boxplot(column="反応時間", by="時間帯")
plt.title("午後は午前より反応が遅い")
plt.suptitle("")
plt.xlabel("")
plt.ylabel("反応時間(ミリ秒)")
plt.show()
