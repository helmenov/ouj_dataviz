# 第5コマ グラフのいろいろ。伝わるデザイン。pandasによるグラフ作成
# グラフは pandas の plot で描きます(裏側では matplotlib が動いています)。
# 表示の show() と、仕上げの調整だけ matplotlib を使います。

import matplotlib.pyplot as plt
import pandas as pd

try:
    import japanize_matplotlib  # noqa: F401
except ImportError:
    pass

days = ["月", "火", "水", "木", "金", "土", "日"]
temp = pd.Series([21, 23, 22, 25, 27, 26, 24], index=days)
sales = pd.Series([120, 85, 64, 42],
                  index=["コーヒー", "紅茶", "ジュース", "水"])

# --- 例1: 折れ線(変化) ---
temp.plot.line(marker="o", title="週の後半に暑くなった", ylabel="最高気温(℃)")
plt.grid(alpha=0.3)
plt.show()

# --- 例2: 棒(比べる) ---
sales.plot.bar(color="#4C78A8", title="売上の中心はコーヒー", ylabel="杯数")
plt.show()

# --- 例3: 散布図(関係) ---
import numpy as np

rng = np.random.default_rng(42)
study = pd.DataFrame({
    "勉強時間": rng.uniform(0, 8, 40),
})
study["点数"] = np.clip(35 + 8 * study["勉強時間"] + rng.normal(0, 8, 40), 0, 100)
study.plot.scatter(x="勉強時間", y="点数", color="#F58518",
                   title="勉強時間とテストの点数")
plt.show()

# --- 例4: ヒストグラム(分布) ---
heights = pd.Series(rng.normal(162, 8, 200))
heights.plot.hist(bins=12, color="#54A24B", edgecolor="white",
                  title="受講生200人の身長の分布", xlabel="身長(cm)")
plt.show()

# --- 例5: 箱ひげ図(分布の比較) ---
scores = pd.DataFrame({
    "A組": rng.normal(65, 10, 40),
    "B組": rng.normal(72, 7, 40),
    "C組": rng.normal(58, 14, 40),
})
scores.boxplot()
plt.title("クラスごとのテストの点数")
plt.ylabel("点数")
plt.show()

# --- 例5b: 四分位数と外れ値 ---
one_class = pd.Series([42, 48, 52, 55, 57, 58, 60, 61, 62, 63, 64, 65, 66,
                       67, 68, 69, 70, 71, 73, 75, 77, 79, 82, 86, 118])
q1 = one_class.quantile(0.25)   # 第1四分位数
med = one_class.median()        # 中央値
q3 = one_class.quantile(0.75)   # 第3四分位数
iqr = q3 - q1                   # 四分位範囲
print(f"Q1={q1}, 中央値={med}, Q3={q3}, IQR={iqr}")
lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr
print("外れ値の候補:", one_class[(one_class < lo) | (one_class > hi)].tolist())
plt.figure()
one_class.plot.box()
plt.show()

# --- 例6: デザイン(軸は0から / 強調色 / 注釈) ---
vals = pd.Series([98, 100], index=["A店", "B店"])
fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.2))
vals.plot.bar(ax=axes[0], color="#E45756", ylim=(90, 102), title="悪い例:軸が90から")
vals.plot.bar(ax=axes[1], color="#4C78A8", ylim=(0, 110), title="良い例:軸は0から")
plt.tight_layout()
plt.show()

sales.plot.bar(color=["gray", "gray", "#E45756", "gray"],
               title="ジュースの売上が伸びている", ylabel="杯数")
plt.show()

ax = temp.plot.line(marker="o", title="週の後半に暑くなった", ylabel="最高気温(℃)")
ax.annotate("今週の最高", xy=("金", 27), xytext=("水", 28),
            arrowprops=dict(arrowstyle="->"))
plt.show()

# --- 例7: 複数のグラフを並べる ---
fig, axes = plt.subplots(2, 2, figsize=(8, 6))
temp.plot.line(ax=axes[0, 0], marker="o", title="最高気温(折れ線)")
sales.plot.bar(ax=axes[0, 1], color="#4C78A8", title="飲み物の売上(棒)")
study.plot.scatter(ax=axes[1, 0], x="勉強時間", y="点数", s=14,
                   color="#F58518", title="勉強時間と点数(散布)")
heights.plot.hist(ax=axes[1, 1], bins=12, color="#54A24B",
                  title="身長の分布(ヒスト)")
plt.tight_layout()
plt.show()

# --- 演習 ---
# 1. お題(出席率の変化/満足度の偏り/身長と体重の関係)に合う形を描きましょう
# 2. 軸が90からの棒グラフを、0からに直しましょう
# 3. タイトルを「結論を書く形」に書き換えましょう
# 解答例は answers/session5_answers.py
