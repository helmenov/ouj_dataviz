# 第1コマ データ可視化(導入編)
# このコマは「見る」ことが中心です。コードを書くのは第2コマから。
# このファイルは、スライドの図(平均が同じでも姿が違う)を
# 再現するための講師演示用です。

import matplotlib.pyplot as plt
import numpy as np

try:
    import japanize_matplotlib  # noqa: F401
except ImportError:
    pass

# --- 平均が同じでも姿が違う(ヒストグラム) ---
rng = np.random.default_rng(3)
d1 = rng.normal(65, 5, 60)
d2 = np.concatenate([rng.normal(50, 4, 30), rng.normal(80, 4, 30)])
d3 = np.concatenate([rng.normal(62, 4, 55), [100] * 5])
fig, axes = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
for ax, d, t in zip(axes, (d1, d2, d3), ["データ1", "データ2", "データ3"]):
    ax.hist(d, bins=12, color="#4C78A8", edgecolor="white")
    ax.set_title(f"{t}(平均 {d.mean():.0f}点)")
plt.tight_layout()
plt.show()

# --- 演習(口頭・ワーク) ---
# データ1〜3の姿を、それぞれ一文で説明しましょう。
# 「平均65点」という要約だけで伝わるもの／伝わらないものはどれですか。
# 解答例は answers/session1_answers.py
