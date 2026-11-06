# Pythonによるデータ可視化 講義資料（90分×8コマ）

公開先：https://github.com/helmenov/lecture-dataviz
受講者向けデータ（data フォルダを固めた data.zip）：https://github.com/helmenov/lecture-dataviz/blob/main/data.zip
※ data の内容を更新したら、リポジトリ直下の `data.zip` も作り直すこと（`zip -r data.zip data`）

対象：Pythonを初めて触る一般の受講者
環境：Thonny（Python本体と編集画面が一緒になった初心者向け無料ソフト）
- インストール（Windows）：ターミナルで `winget install AivarAnnamaa.Thonny`
使用ライブラリ：pandas（表とグラフ）、japanize-matplotlib（日本語表示）

## カリキュラム（確定版）
| コマ | テーマ |
|---|---|
| 1 | データ可視化（導入編） |
| 2 | Python入門 |
| 3 | データ集め、データ（変数）の尺度 |
| 4 | 表のいろいろ。pandasによる表作成 |
| 5 | グラフのいろいろ。伝わるデザイン。pandasによるグラフ作成 |
| 6 | データを眺めて、気づいたことをグラフだけで納得させる（データ分析） |
| 7 | 仮説を納得させるグラフを作るためのデータ集め |
| 8 | テスト。データを眺めて、気づいたことをグラフで納得させよ |

## ファイル構成
- `slides.pdf` … 講義スライド（全71枚、全8コマ＋付録）。投影・配布兼用
- `slides.tex` … スライドのソース（TeX Live / LuaLaTeX Beamer）
- `code/session1.py`〜`session8.py` … 各コマの例題コード＋演習問題
- `code/answers/` … 演習の解答例（講師用）。session8 はテストの模範解答
- `test_guide.md` … 第8コマ テスト実施ガイド（講師用。埋め込みパターンと評価基準）
- `data/` … 練習用データ（すべてサンプルデータ）。**受講者にはこのフォルダを配布ページからダウンロードしてもらう**（第2コマのスライドで指示）
  - `weather_week.csv` 1週間の天気（第4コマ）
  - `shop_sales.csv` 小さな店の30日分の売上（第4コマ）
  - `survey.csv` アンケート60人分（第4・5コマ）
  - `sdt_trials.csv` 信号検出理論の実験100試行（第4コマ）
  - `psych_rt.csv` 反応時間の実験80名分（第6・7コマ）
  - `test_psych.csv` 注意課題の実験120名分（第8コマ テスト用）
- `assets/` … スライドで使う例図と、Thonnyの画面写真（番号注釈つき）

## 進め方の想定
- 1日目：第1〜4コマ、2日目：第5〜8コマ
- 各コマは「講義 → 一緒に実習 → 演習 → まとめ」を基本形とし、
  スライド冒頭のコマ表紙に90分の内訳を記載

## 注意
- コード例はすべて動作確認済み（pandas 2.1 / matplotlib 3.6 で検証）
- 方針：有意差検定は対象者のレベルに合わせ扱わない。「平均などの要約だけでは分からない、データの姿をグラフで確かめる」ことを動機の中心に置く
- 日本語表示は japanize-matplotlib を使う（Thonnyの「ツール→パッケージを管理」から初回のみインストール）
- Thonny では CSV をプログラムと同じフォルダ（配布構成では data フォルダ）に置いて使う
