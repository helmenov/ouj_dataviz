# 第2コマ Python入門

# --- 例1: 変数 ---
price = 450
name = "コーヒー"
total = price * 3
print(name, total)  # コーヒー 1350

# --- 例2: リスト ---
sales = [120, 85, 64, 42]
print(sales[0])     # 120 (数え方は0から)
print(len(sales))   # 4
sales.append(30)
print(sum(sales))   # 合計

# --- 例3: 辞書(表の1行分のイメージ) ---
row = {"商品": "コーヒー", "単価": 450, "個数": 12}
print(row["商品"], row["単価"] * row["個数"])  # コーヒー 5400

# --- 例4: 繰り返し ---
for day in ["月", "火", "水"]:
    print(day, "曜日です")

for price in [450, 400, 350]:
    print(price * 1.1)  # 消費税込み

# --- 例5: 条件分岐 ---
temp = 27
if temp >= 30:
    print("真夏日です")
elif temp >= 25:
    print("夏日です")
else:
    print("過ごしやすい日です")

# --- 例6: 関数 ---
def tax_included(price):
    return price * 1.1

print(tax_included(450))  # 495.0

# --- 演習 ---
# 1. リスト [80, 90, 70, 100] の平均を sum と len で求めましょう
# 2. 辞書で好きな商品の1行を作り、単価×個数を表示しましょう
# 3. 繰り返しで、1から5までの2倍の数を順に表示しましょう
# 解答例は answers/session2_answers.py
