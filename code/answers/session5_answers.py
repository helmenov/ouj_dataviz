# 第5コマ 演習の解答例(pandasでグラフ作成)
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

BASE = Path(__file__).resolve().parent.parent.parent if "__file__" in globals() else Path(".")

# 1a. 出席率の変化 → 折れ線
rate = pd.Series(np.clip(90 + np.cumsum(np.random.default_rng(1).normal(0, 1.5, 30)), 70, 100))
rate.plot.line(marker="o", markersize=3, title="出席率は月を通してほぼ横ばい",
               xlabel="日", ylabel="出席率(%)")
plt.show()

# 1b. 満足度の偏り → 度数の棒グラフ
survey = pd.read_csv(BASE / "data" / "survey.csv")
counts = survey["満足度"].value_counts().sort_index()
counts.plot.bar(color="#4C78A8", title="満足度は4に山がある",
                xlabel="満足度", ylabel="人数")
plt.show()

# 1c. 身長と体重の関係 → 散布図
rng = np.random.default_rng(2)
body = pd.DataFrame({"身長": rng.normal(165, 8, 50)})
body["体重"] = (body["身長"] - 100) + rng.normal(0, 5, 50)
body.plot.scatter(x="身長", y="体重", title="身長が高い人ほど体重も重い傾向")
plt.show()

# 2-3. 軸は0から、タイトルは結論形に(本文の例6がその形になっています)
