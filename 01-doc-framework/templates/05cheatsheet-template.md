---
# === 必須：識別情報 ===
document_id: "CS-DOMAIN-NNN"  # CS-python-001, CS-tools-001等
title: "<!-- TEMPLATE: ツール名チートシート（例: Pandas データ解析チートシート） -->"
type: cheatsheet
version: "1.0"
status: active  # draft | review | approved | active | deprecated

# === 所有権 ===
owner: "@team-name"
author: "<!-- TEMPLATE: 作成者名 -->"
created: <!-- TEMPLATE: YYYY-MM-DD -->
updated: <!-- TEMPLATE: YYYY-MM-DD -->

# === RAG最適化 ===
tags:
  - cheatsheet
  - <!-- TEMPLATE: ツール名タグ（例: pandas, numpy） -->
  - <!-- TEMPLATE: 用途タグ（例: data-analysis, visualization） -->
key_concepts:
  - "<!-- TEMPLATE: セマンティック用語1（例: データ解析、統計処理） -->"
  - "<!-- TEMPLATE: セマンティック用語2（例: クイックリファレンス、コマンド集） -->"
summary: "<!-- TEMPLATE: 検索結果用の一文説明（150文字以内） -->"

# === ドメインコンテキスト ===
category: cheatsheet
domain: <!-- TEMPLATE: data-analysis | cfd | gis | visualization | infrastructure -->
difficulty: <!-- TEMPLATE: beginner | intermediate | advanced -->
audience: <!-- TEMPLATE: developers | operators | architects | scientists -->
tool_version: <!-- TEMPLATE: 対象ツールバージョン -->

# === 関連ドキュメント ===
related_docs:
  - path: "<!-- TEMPLATE: /path/to/related-tutorial.md -->"
    relationship: "references"  # implements | governed-by | references | depends-on

# === メンテナンス ===
next_review: <!-- TEMPLATE: YYYY-MM-DD -->
review_cycle_days: 180
---

# <!-- TEMPLATE: ツール名 --> チートシート

---

## 必須セクション一覧

このテンプレートには以下の必須セクションが含まれています：

| セクション | 目的 | 省略時の影響 |
|-----------|------|-------------|
| クイックリファレンス | 即座参照用の要点 | 参照したい情報が見つからない |
| コマンド/コード例 | コピペ可能な例 | 使い方がわからない |

---

**対象バージョン**: <!-- TEMPLATE: バージョン番号 -->
**更新日**: <!-- TEMPLATE: YYYY-MM-DD -->
**対象読者**: <!-- TEMPLATE: 初心者 | 中級者 | 上級者 -->

## 📌 最頻出コマンド TOP 5

<!--
なぜ必要か: 最もよく使うコマンドを優先表示し、検索時間を削減するため
省略するとどうなるか: 必要な情報を探すのに時間がかかる
-->

**⚠️ [重要]** 最もよく使うコマンドを優先的に配置

| # | コマンド | 説明 | 使用頻度 |
|---|---------|------|---------|
| 1 | `<!-- TEMPLATE: コマンド1 -->` | <!-- TEMPLATE: 説明 --> | ⭐⭐⭐⭐⭐ |
| 2 | `<!-- TEMPLATE: コマンド2 -->` | <!-- TEMPLATE: 説明 --> | ⭐⭐⭐⭐ |
| 3 | `<!-- TEMPLATE: コマンド3 -->` | <!-- TEMPLATE: 説明 --> | ⭐⭐⭐⭐ |
| 4 | `<!-- TEMPLATE: コマンド4 -->` | <!-- TEMPLATE: 説明 --> | ⭐⭐⭐ |
| 5 | `<!-- TEMPLATE: コマンド5 -->` | <!-- TEMPLATE: 説明 --> | ⭐⭐⭐ |

## 🚀 クイックスタート

<!--
なぜ必要か: 初心者が迅速に使い始められるようにするため
省略するとどうなるか: 初期セットアップで躓き、使用開始が遅れる
-->

### インストール

```bash
# TEMPLATE: インストールコマンド
# 例:
# pip install pandas
# conda install pandas
```

### 基本構文

```python
# TEMPLATE: 基本的な使用パターン
# 例:
# import pandas as pd
# df = pd.read_csv('data.csv')
# df.head()
```

### 最小限の例

```python
# TEMPLATE: 最も簡単な動作例（Hello World相当）
```

## 📊 基本コマンド

<!--
なぜ必要か: カテゴリ別に整理されたコマンド集を提供し、目的のコマンドを見つけやすくするため
省略するとどうなるか: コマンドが無秩序に並び、必要な情報を探せない
-->

### カテゴリ1: <!-- TEMPLATE: カテゴリ名（例: データ読み込み） -->

| コマンド | 説明 | 例 |
|---------|------|-----|
| `<!-- TEMPLATE: コマンド -->` | <!-- TEMPLATE: 機能説明 --> | `<!-- TEMPLATE: 使用例 -->` |

### カテゴリ2: <!-- TEMPLATE: カテゴリ名（例: データ変換） -->

| コマンド | 説明 | 例 |
|---------|------|-----|
| `<!-- TEMPLATE: コマンド -->` | <!-- TEMPLATE: 機能説明 --> | `<!-- TEMPLATE: 使用例 -->` |

### カテゴリ3: <!-- TEMPLATE: カテゴリ名（例: 集計・統計） -->

**⚠️ 必要に応じてカテゴリを追加または削除してください**

| コマンド | 説明 | 例 |
|---------|------|-----|
| `<!-- TEMPLATE: コマンド -->` | <!-- TEMPLATE: 機能説明 --> | `<!-- TEMPLATE: 使用例 -->` |

## 🎯 頻出パターン

<!--
なぜ必要か: よくある使い方のパターンを提供し、コピペで使えるようにするため
省略するとどうなるか: 毎回ゼロからコードを書く必要があり、効率が悪い
-->

### パターン1: <!-- TEMPLATE: パターン名（例: CSVファイル読み込みと基本統計） -->

```python
# TEMPLATE: 実際のコード例
# 例:
# import pandas as pd
#
# # CSVファイル読み込み
# df = pd.read_csv('data.csv')
#
# # 基本統計量表示
# print(df.describe())
```

**用途**: <!-- TEMPLATE: このパターンの用途 -->
**注意点**: <!-- TEMPLATE: 注意すべきポイント -->

---

### パターン2: <!-- TEMPLATE: パターン名 -->

```python
# TEMPLATE: 実際のコード例
```

**用途**: <!-- TEMPLATE: このパターンの用途 -->
**注意点**: <!-- TEMPLATE: 注意すべきポイント -->

---

### パターン3: <!-- TEMPLATE: パターン名 -->

```bash
# TEMPLATE: コマンドライン例の場合
```

**用途**: <!-- TEMPLATE: このパターンの用途 -->
**注意点**: <!-- TEMPLATE: 注意すべきポイント -->

## ⚙️ 設定スニペット

### 基本設定

```yaml
# TEMPLATE: YAML設定例
# 例:
# pandas:
#   display:
#     max_rows: 100
#     max_columns: 20
```

### よく使う設定

```python
# TEMPLATE: Python設定例
# 例:
# pd.set_option('display.max_rows', 100)
# pd.set_option('display.precision', 3)
```

## 🔍 データ解析向けクイックリファレンス

**[重要]** データ解析でよく使う操作をまとめています

### データ品質チェック

```python
# TEMPLATE: データ品質チェックのワンライナー
# 例:
# # 欠損値確認
# df.isnull().sum()
#
# # データ型確認
# df.dtypes
#
# # 重複行確認
# df.duplicated().sum()
```

### 統計量算出

```python
# TEMPLATE: 統計量算出のワンライナー
# 例:
# # 基本統計量
# df.describe()
#
# # 相関係数
# df.corr()
#
# # 中央値
# df.median()
```

### 可視化クイックスタート

```python
# TEMPLATE: 可視化のクイックスタート例
# 例:
# import matplotlib.pyplot as plt
#
# # ヒストグラム
# df['column'].hist(bins=30)
# plt.show()
#
# # 散布図
# df.plot.scatter(x='col1', y='col2')
# plt.show()
```

## 🐛 クイックトラブルシュート

よくあるエラーと即座の解決策：

| 問題・エラー | 原因 | 解決コマンド/方法 |
|------------|------|------------------|
| <!-- TEMPLATE: エラーメッセージ --> | <!-- TEMPLATE: 原因 --> | `<!-- TEMPLATE: 解決コマンド -->` |

### 詳細なトラブルシューティング

#### 問題1: <!-- TEMPLATE: 問題名 -->

**症状**:
<!-- TEMPLATE: 症状説明 -->

**解決**:
```python
# TEMPLATE: 解決コード
```

## 💡 ベストプラクティス

**✅ 推奨事項**:
- <!-- TEMPLATE: ベストプラクティス1 -->
- <!-- TEMPLATE: ベストプラクティス2 -->
- <!-- TEMPLATE: ベストプラクティス3 -->

**❌ 避けるべきこと**:
- <!-- TEMPLATE: アンチパターン1 -->
- <!-- TEMPLATE: アンチパターン2 -->
- <!-- TEMPLATE: アンチパターン3 -->

## 🔗 関連リンク

### 公式ドキュメント
- [公式サイト](<!-- TEMPLATE: URL -->)
- [API リファレンス](<!-- TEMPLATE: URL -->)
- [チュートリアル](<!-- TEMPLATE: URL -->)

### コミュニティリソース
- [Stack Overflow](<!-- TEMPLATE: URL -->) - <!-- TEMPLATE: タグ名 -->
- [GitHub](<!-- TEMPLATE: URL -->)
- [公式フォーラム](<!-- TEMPLATE: URL -->)

### 学習リソース
- <!-- TEMPLATE: チュートリアルサイト -->
- <!-- TEMPLATE: 書籍 -->
- <!-- TEMPLATE: 動画コース -->

## 📝 バージョン別の違い

### バージョン <!-- TEMPLATE: 新バージョン -->

**新機能**:
- <!-- TEMPLATE: 新機能1 -->
- <!-- TEMPLATE: 新機能2 -->

**非推奨/削除**:
- <!-- TEMPLATE: 非推奨機能1 -->

### バージョン <!-- TEMPLATE: 旧バージョン -->

**主な違い**:
<!-- TEMPLATE: 主な違いの説明 -->

## 🎓 応用例

### ユースケース1: <!-- TEMPLATE: ユースケース名 -->

```python
# TEMPLATE: 実用的な応用例コード
```

### ユースケース2: <!-- TEMPLATE: ユースケース名 -->

```python
# TEMPLATE: 実用的な応用例コード
```

## 📋 チートシート印刷版

**1ページ要約版**（印刷用）:

```
TEMPLATE: 最重要コマンドのみをコンパクトにまとめた印刷可能な形式
例:
=== [ツール名] クイックリファレンス ===

基本操作:
  cmd1                  説明1
  cmd2 -o               説明2

頻出パターン:
  pattern1 | cmd       説明
```

---

**最終更新**: <!-- TEMPLATE: YYYY-MM-DD -->
**メンテナー**: <!-- TEMPLATE: 担当者名 -->
**フィードバック**: <!-- TEMPLATE: フィードバック先 -->
