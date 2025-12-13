---
# **[重要]** RAG対応必須フィールド
title: "ランブック: データクレンジング"
description: "データソースから取得した生データの品質問題（欠損値、外れ値、型不整合、重複）を修正し、分析に適した形式に整形するための標準クレンジング手順。Pandas活用によるステップバイステップ実行ガイド"

# 分類（RAGフィルタリング用）
tags:
  - runbook
  - data-cleansing
  - data-quality
  - pandas
  - operations
category: runbook
domain: data-analysis
difficulty: intermediate

# 関連性（グラフ構造用）
related_docs:
  - data-quality-analysis-process.md
  - anomaly-detection-playbook.md
  - anti-patterns-data-analysis.md
prerequisites:
  - Python 3.8+環境
  - Pandas基礎知識

# メタデータ
created_at: 2025-11-30
updated_at: 2025-11-30
version: "1.0"
author: data-engineering-team
---

# ランブック: データクレンジング

**サービス**: データ分析パイプライン（ETL）
**所要時間**: 30-90分（データ規模により変動）
**実行頻度**: daily（自動バッチ）または on-demand（手動実行）
**対象読者**: データエンジニア、データアナリスト

## 📋 概要

### タスクの目的

このランブックは、データソースから取得した生データの品質問題（**欠損値、外れ値、型不整合、重複、形式不統一**）を修正し、分析に適した形式に整形するためのデータクレンジング手順を提供します。Pandasライブラリを活用した段階的な処理により、データ品質を向上させ、下流の分析・機械学習タスクの精度を確保します。

### 実行タイミング

**✅ 実行すべき場合**:
- データ品質分析で品質スコア < 80%と判定された場合
- 新規データソース統合後の初回データ整形時
- 定期バッチ実行（日次/週次）でのデータ前処理
- ビジネスルール変更に伴うデータ整形ルール更新時

**❌ 実行すべきでない場合**:
- データソース側で品質保証されているマスタデータ
- 既にクレンジング済みのデータ（重複実行によるデータ破損リスク）
- リアルタイムストリーム処理（別途ストリーム用パイプライン使用）

## ⚙️ 前提条件

### 必要な権限

- [x] データソースへの読み取り権限（DB接続、ファイルアクセス等）
- [x] 出力先ディレクトリへの書き込み権限
- [x] バックアップディレクトリへのアクセス権限

### 必要なツール

| ツール | バージョン | 確認方法 |
|--------|-----------|---------|
| Python | 3.8+ | `python --version` |
| pandas | 1.5+ | `python -c "import pandas; print(pandas.__version__)"` |
| numpy | 1.23+ | `python -c "import numpy; print(numpy.__version__)"` |
| scikit-learn | 1.0+ (optional) | `python -c "import sklearn; print(sklearn.__version__)"` |

### 環境変数

```bash
# 必要な環境変数を設定
export DATA_SOURCE_PATH="/data/raw/sales_data.csv"
export OUTPUT_PATH="/data/cleaned/sales_data_cleaned.csv"
export BACKUP_DIR="/data/backup"
export LOG_DIR="/data/logs"
```

## 📝 事前確認チェックリスト

**⚠️ [重要]** 実行前に以下を必ず確認してください。

- [x] **バックアップ作成済み**: 生データのバックアップが`${BACKUP_DIR}`に保存されている
  ```bash
  ls -lh ${BACKUP_DIR}/sales_data_$(date +%Y%m%d).csv.bak
  ```
- [x] **リソース確認**: メモリ使用率 < 80%、ディスク空き容量 > 10GB
  ```bash
  free -h | awk '/Mem:/ {print $3/$2*100"%"}'
  df -h ${OUTPUT_PATH%/*} | awk 'NR==2 {print $4}'
  ```
- [x] **依存サービス稼働**: データソース（DB/ファイルストレージ）が正常稼働中
- [x] **実行時間帯確認**: ピーク時間外（深夜0-6時推奨）または手動実行の承認取得済み
- [x] **品質ルール確認**: クレンジングルール定義ファイル（`cleansing_rules.yaml`）が最新版

### システム状態確認

```bash
# ディスク容量確認（10GB以上必要）
df -h ${OUTPUT_PATH%/*}

# メモリ確認（8GB以上推奨）
free -h

# データソースファイル確認
ls -lh ${DATA_SOURCE_PATH}
wc -l ${DATA_SOURCE_PATH}

# Pythonライブラリ確認
python -c "import pandas, numpy; print('OK')"
```

**期待される出力**:
```
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       100G   80G   15G  85% /data

              total        used        free
Mem:           16Gi       8.0Gi       6.0Gi

-rw-r--r-- 1 user group 500M Nov 30 10:00 /data/raw/sales_data.csv
100000 /data/raw/sales_data.csv

OK
```

## 🔧 実行手順

### ステップ1: データ読み込みと初期プロファイリング

**目的**: 生データを読み込み、基本統計量と品質問題を把握する

**実行内容**:
```python
import pandas as pd
import numpy as np
from datetime import datetime

# ログ設定
import logging
logging.basicConfig(
    filename=f"{os.getenv('LOG_DIR')}/cleansing_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log",
    level=logging.INFO
)

# データ読み込み
logging.info("データ読み込み開始")
df = pd.read_csv(os.getenv('DATA_SOURCE_PATH'))
logging.info(f"読み込み完了: {len(df)}行, {len(df.columns)}列")

# 初期プロファイリング
print("=== 初期プロファイル ===")
print(f"行数: {len(df)}")
print(f"カラム数: {len(df.columns)}")
print(f"メモリ使用量: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
print(f"\n欠損値サマリー:\n{df.isnull().sum()}")
print(f"\n重複行数: {df.duplicated().sum()}")
print(f"\nデータ型:\n{df.dtypes}")
```

**期待される結果**:
```
=== 初期プロファイル ===
行数: 100000
カラム数: 10
メモリ使用量: 7.63 MB

欠損値サマリー:
order_id           0
customer_id        0
product_id       150
order_date         0
amount          1200
status             5
email            800
postal_code     2000
dtype: int64

重複行数: 35

データ型:
order_id        int64
customer_id     int64
product_id     object  # ← 本来はint64であるべき
order_date     object  # ← 本来はdatetimeであるべき
amount         float64
status         object
email          object
postal_code    object
dtype: object
```

**⚠️ エラー時の対処**:
- エラー: `FileNotFoundError: [Errno 2] No such file or directory`
  - 原因: データソースパスが間違っている
  - 対処: 環境変数`DATA_SOURCE_PATH`を確認、パスを修正
- エラー: `MemoryError`
  - 原因: データサイズが大きすぎてメモリ不足
  - 対処: `chunksize`パラメータで分割読み込み、またはサンプリング

---

### ステップ2: 欠損値処理

**目的**: 欠損値を適切な方法（削除、補完、フラグ化）で処理する

**実行内容**:
```python
logging.info("欠損値処理開始")

# 2-1. 必須カラムの欠損行削除
required_cols = ['order_id', 'customer_id', 'order_date', 'amount']
df_before = len(df)
df = df.dropna(subset=required_cols)
logging.info(f"必須カラム欠損削除: {df_before - len(df)}行削除")

# 2-2. product_id欠損を補完（後方埋め、または"UNKNOWN"）
df['product_id'] = df['product_id'].fillna('UNKNOWN')
logging.info("product_id欠損を'UNKNOWN'で補完")

# 2-3. email欠損をフラグ化して保持
df['email_missing'] = df['email'].isnull().astype(int)
df['email'] = df['email'].fillna('no-email@example.com')
logging.info("email欠損をフラグ化し、ダミー値で補完")

# 2-4. postal_code欠損を中央値で補完（数値の場合）
# または最頻値で補完（カテゴリの場合）
if df['postal_code'].dtype == 'object':
    mode_value = df['postal_code'].mode()[0] if not df['postal_code'].mode().empty else 'UNKNOWN'
    df['postal_code'] = df['postal_code'].fillna(mode_value)
    logging.info(f"postal_code欠損を最頻値'{mode_value}'で補完")

# 2-5. status欠損を"pending"で補完（ビジネスルール）
df['status'] = df['status'].fillna('pending')
logging.info("status欠損を'pending'で補完")

print(f"\n欠損値処理後:\n{df.isnull().sum()}")
```

**期待される結果**:
```
欠損値処理後:
order_id           0
customer_id        0
product_id         0
order_date         0
amount             0
status             0
email              0
postal_code        0
email_missing      0
dtype: int64
```

**⚠️ エラー時の対処**:
- 警告: `SettingWithCopyWarning`
  - 原因: DataFrameのビュー操作による警告
  - 対処: `df = df.copy()`で明示的にコピー作成

---

### ステップ3: データ型変換と形式統一

**目的**: 各カラムを適切なデータ型に変換し、形式を統一する

**実行内容**:
```python
logging.info("データ型変換開始")

# 3-1. order_date を datetime型に変換
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
invalid_dates = df['order_date'].isnull().sum()
if invalid_dates > 0:
    logging.warning(f"日付変換失敗: {invalid_dates}行")
    df = df.dropna(subset=['order_date'])  # 無効な日付行を削除

# 3-2. product_id を整数に変換（"UNKNOWN"は-1に）
df['product_id'] = df['product_id'].replace('UNKNOWN', '-1')
df['product_id'] = pd.to_numeric(df['product_id'], errors='coerce').fillna(-1).astype(int)

# 3-3. amount を float64に統一（カンマ除去等）
if df['amount'].dtype == 'object':
    df['amount'] = df['amount'].str.replace(',', '').astype(float)

# 3-4. email を小文字に統一
df['email'] = df['email'].str.lower().str.strip()

# 3-5. postal_code を統一形式（日本: 123-4567）
import re
def format_postal_code(code):
    if pd.isnull(code):
        return code
    # 数字のみ抽出
    digits = re.sub(r'\D', '', str(code))
    if len(digits) == 7:
        return f"{digits[:3]}-{digits[3:]}"
    return code

df['postal_code'] = df['postal_code'].apply(format_postal_code)

# 3-6. status をカテゴリ型に変換（メモリ削減）
df['status'] = df['status'].astype('category')

print(f"\n型変換後のデータ型:\n{df.dtypes}")
```

**期待される結果**:
```
型変換後のデータ型:
order_id               int64
customer_id            int64
product_id             int64
order_date    datetime64[ns]
amount               float64
status              category
email                 object
postal_code           object
email_missing          int64
dtype: object
```

**⚠️ エラー時の対処**:
- エラー: `ValueError: unconverted data remains`
  - 原因: 日付フォーマットが複数混在
  - 対処: `pd.to_datetime(..., format='%Y-%m-%d', errors='coerce')`で柔軟変換

---

### ステップ4: 外れ値検出と処理

**目的**: 統計的手法で外れ値を検出し、キャッピングまたは削除する

**実行内容**:
```python
logging.info("外れ値処理開始")

# 4-1. amount の外れ値検出（IQR法）
Q1 = df['amount'].quantile(0.25)
Q3 = df['amount'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['amount'] < lower_bound) | (df['amount'] > upper_bound)]
logging.info(f"外れ値検出: {len(outliers)}行 (下限{lower_bound:.2f}, 上限{upper_bound:.2f})")

# 4-2. 外れ値をキャッピング（削除ではなく上下限に丸める）
df['amount'] = df['amount'].clip(lower=lower_bound, upper=upper_bound)

# 4-3. 負の金額を0に修正（ビジネスルール）
negative_amount = (df['amount'] < 0).sum()
if negative_amount > 0:
    logging.warning(f"負の金額を検出: {negative_amount}行 → 0に修正")
    df['amount'] = df['amount'].clip(lower=0)

# 4-4. 未来日付の削除
future_dates = df[df['order_date'] > pd.Timestamp.now()]
if len(future_dates) > 0:
    logging.warning(f"未来日付を検出: {len(future_dates)}行 → 削除")
    df = df[df['order_date'] <= pd.Timestamp.now()]

print(f"外れ値処理後の行数: {len(df)}")
```

**期待される結果**:
```
外れ値処理後の行数: 99800
```

**⚠️ エラー時の対処**:
- 警告: 外れ値が50%以上
  - 原因: 閾値設定が厳しすぎる、またはデータ分布が歪んでいる
  - 対処: IQR係数を1.5→3.0に緩和、または対数変換後に検出

---

### ステップ5: 重複削除とビジネスルール検証

**目的**: 重複行を削除し、ビジネスルールに違反するデータを修正する

**実行内容**:
```python
logging.info("重複削除・ビジネスルール検証開始")

# 5-1. 完全重複行の削除
dup_before = df.duplicated().sum()
df = df.drop_duplicates()
logging.info(f"完全重複削除: {dup_before}行削除")

# 5-2. 主キー重複の削除（order_idでソートし、最新を保持）
df = df.sort_values('order_date', ascending=False)
dup_key = df.duplicated(subset=['order_id']).sum()
df = df.drop_duplicates(subset=['order_id'], keep='first')
logging.info(f"主キー重複削除: {dup_key}行削除")

# 5-3. ビジネスルール検証: order_dateが過去3年以内
three_years_ago = pd.Timestamp.now() - pd.DateOffset(years=3)
old_data = df[df['order_date'] < three_years_ago]
if len(old_data) > 0:
    logging.warning(f"古いデータを検出: {len(old_data)}行（3年以上前） → 削除")
    df = df[df['order_date'] >= three_years_ago]

# 5-4. ビジネスルール検証: statusの値が許可リスト内
allowed_status = ['pending', 'completed', 'cancelled', 'refunded']
invalid_status = df[~df['status'].isin(allowed_status)]
if len(invalid_status) > 0:
    logging.warning(f"無効なstatus: {len(invalid_status)}行 → 'pending'に修正")
    df.loc[~df['status'].isin(allowed_status), 'status'] = 'pending'

print(f"重複削除・ルール検証後の最終行数: {len(df)}")
```

**期待される結果**:
```
重複削除・ルール検証後の最終行数: 99750
```

**⚠️ エラー時の対処**:
- 警告: 主キー重複が多数（>10%）
  - 原因: データソースの品質問題
  - 対処: データオーナーに報告、上流での重複防止策を検討

---

### ステップ6: 最終検証と出力

**目的**: クレンジング結果を検証し、出力ファイルとして保存する

**実行内容**:
```python
logging.info("最終検証・出力開始")

# 6-1. 最終品質チェック
quality_report = {
    'total_rows': len(df),
    'missing_values': df.isnull().sum().sum(),
    'duplicate_rows': df.duplicated().sum(),
    'negative_amount': (df['amount'] < 0).sum(),
    'future_dates': (df['order_date'] > pd.Timestamp.now()).sum(),
    'invalid_status': (~df['status'].isin(allowed_status)).sum()
}

logging.info(f"品質レポート: {quality_report}")
print("\n=== 最終品質レポート ===")
for key, value in quality_report.items():
    print(f"{key}: {value}")

# 6-2. 品質基準チェック
assert quality_report['missing_values'] == 0, "欠損値が残っている"
assert quality_report['duplicate_rows'] == 0, "重複行が残っている"
assert quality_report['negative_amount'] == 0, "負の金額が残っている"

# 6-3. 出力ファイル保存
output_path = os.getenv('OUTPUT_PATH')
df.to_csv(output_path, index=False)
logging.info(f"出力完了: {output_path}")

# 6-4. サマリーレポート保存
summary = {
    'execution_time': datetime.now().isoformat(),
    'input_rows': 100000,  # 初期行数
    'output_rows': len(df),
    'rows_removed': 100000 - len(df),
    'quality_score': 100 - (quality_report['missing_values'] + quality_report['duplicate_rows']) / len(df) * 100
}

import json
with open(f"{os.getenv('LOG_DIR')}/summary_{datetime.now().strftime('%Y%m%d')}.json", 'w') as f:
    json.dump(summary, f, indent=2)

print(f"\n✅ クレンジング完了: {output_path}")
print(f"処理済み行数: {len(df)} (削除: {100000 - len(df)}行)")
```

**期待される結果**:
```
=== 最終品質レポート ===
total_rows: 99750
missing_values: 0
duplicate_rows: 0
negative_amount: 0
future_dates: 0
invalid_status: 0

✅ クレンジング完了: /data/cleaned/sales_data_cleaned.csv
処理済み行数: 99750 (削除: 250行)
```

## ✅ 検証チェックリスト

**[重要]** 全ステップ完了後、以下を確認してください。

- [x] **出力ファイル生成**: 出力パスにファイルが存在し、サイズが妥当
  ```bash
  ls -lh ${OUTPUT_PATH}
  ```
- [x] **データ件数一致**: 入力行数 - 削除行数 = 出力行数
  ```bash
  wc -l ${OUTPUT_PATH}
  ```
- [x] **品質基準達成**: 欠損値0件、重複0件、型変換エラー0件
  ```python
  df_check = pd.read_csv(os.getenv('OUTPUT_PATH'))
  assert df_check.isnull().sum().sum() == 0
  assert df_check.duplicated(subset=['order_id']).sum() == 0
  ```
- [x] **ログ記録**: 実行ログが保存され、エラーがないことを確認
  ```bash
  tail -n 20 ${LOG_DIR}/cleansing_*.log
  ```
- [x] **サマリーレポート確認**: 品質スコア ≥ 95%
  ```bash
  cat ${LOG_DIR}/summary_$(date +%Y%m%d).json
  ```

### 検証コマンド

```bash
# 行数確認
echo "入力行数: $(wc -l < ${DATA_SOURCE_PATH})"
echo "出力行数: $(wc -l < ${OUTPUT_PATH})"

# サンプル確認（先頭5行）
head -n 5 ${OUTPUT_PATH}

# 欠損値確認（Pythonワンライナー）
python -c "
import pandas as pd
df = pd.read_csv('${OUTPUT_PATH}')
print('欠損値:', df.isnull().sum().sum())
print('重複:', df.duplicated().sum())
"
```

**期待される結果**:
```
入力行数: 100000
出力行数: 99750
order_id,customer_id,product_id,order_date,amount,status,email,postal_code,email_missing
1,1001,5001,2024-11-30,12500.00,completed,user@example.com,123-4567,0
...

欠損値: 0
重複: 0
```

## 🚨 トラブルシューティング

よくある問題と対処法：

| 症状 | 原因 | 対処法 | 参考 |
|------|------|--------|------|
| `MemoryError`発生 | データサイズ > 利用可能メモリ | `chunksize=10000`で分割読み込み、またはDask使用 | [Pandas公式: chunksize](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) |
| `ValueError: could not convert string to float` | 数値カラムに非数値文字（$, カンマ等）混入 | `errors='coerce'`で強制変換、または正規表現で前処理 | [Pandas公式: to_numeric](https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html) |
| 処理時間が2時間超 | データ量過多、または非効率な処理 | ベクトル化操作に変更、`apply`の使用を削減 | [Pandas最適化ガイド](https://pandas.pydata.org/docs/user_guide/enhancingperf.html) |
| 品質スコア < 80% | クレンジングルールが不十分 | ドメイン知識でルール見直し、閾値調整 | [データ品質分析プロセス](data-quality-analysis-process.md) |

### 詳細なトラブルシューティング

#### 問題1: 日付変換エラー（多様な形式混在）

**症状の詳細**:
`ValueError: time data '30/11/2024' doesn't match format '%Y-%m-%d'`

**診断方法**:
```python
# 日付形式のパターン確認
print(df['order_date'].value_counts().head(10))
```

**解決手順**:
1. 複数形式を許容する変換
   ```python
   from dateutil import parser
   df['order_date'] = df['order_date'].apply(lambda x: parser.parse(x) if pd.notnull(x) else x)
   ```
2. または、`pd.to_datetime(..., infer_datetime_format=True, errors='coerce')`
3. 変換失敗行を確認し、手動修正または削除

#### 問題2: メモリ不足による処理中断

**症状の詳細**:
処理途中で`Killed`メッセージが表示、プロセスが終了

**診断方法**:
```bash
# メモリ使用量の監視
watch -n 1 free -h
```

**解決手順**:
1. チャンクサイズ読み込みに変更
   ```python
   chunks = []
   for chunk in pd.read_csv('data.csv', chunksize=10000):
       # 各チャンクをクレンジング
       chunk_cleaned = clean_chunk(chunk)
       chunks.append(chunk_cleaned)
   df = pd.concat(chunks, ignore_index=True)
   ```
2. データ型の最適化（`category`, `int8`等）
3. 不要なカラムを早期に削除

#### 問題3: 外れ値削除で90%以上のデータ喪失

**症状の詳細**:
IQR法で外れ値削除後、データが1万行 → 100行に激減

**診断方法**:
```python
# 分布の可視化
import matplotlib.pyplot as plt
df['amount'].hist(bins=50)
plt.savefig('distribution.png')

# 分位数確認
print(df['amount'].describe())
```

**解決手順**:
1. 対数変換で分布を正規化
   ```python
   df['amount_log'] = np.log1p(df['amount'])
   # 対数スケールで外れ値検出
   ```
2. IQR係数を緩和（1.5 → 3.0）
3. ドメイン知識で妥当な上下限を手動設定

詳細は [トラブルシューティングガイド](../templates/troubleshooting-template.md) を参照。

## ⏮️ ロールバック手順

**⚠️ [重要]** 問題が発生した場合の復旧手順

### ロールバックが必要な状況

- クレンジング後の品質スコア < 50%（大量のデータ喪失）
- ビジネスルール違反により下流処理がエラー
- 出力ファイルが破損または空ファイル

### ロールバック手順

#### ステップ1: 実行中断

```bash
# Pythonプロセスの停止（Ctrl+C または kill）
ps aux | grep python | grep cleansing
kill -SIGTERM <PID>
```

#### ステップ2: バックアップ復元

```bash
# 最新バックアップを確認
ls -lht ${BACKUP_DIR}/*.csv.bak | head -n 1

# バックアップ復元
cp ${BACKUP_DIR}/sales_data_$(date +%Y%m%d).csv.bak ${DATA_SOURCE_PATH}

# 出力ファイルの削除（不完全なファイル）
rm -f ${OUTPUT_PATH}
```

#### ステップ3: 状態確認

```bash
# データソースファイルの整合性確認
wc -l ${DATA_SOURCE_PATH}
head -n 5 ${DATA_SOURCE_PATH}

# ログの確認
tail -n 50 ${LOG_DIR}/cleansing_*.log
```

**復旧確認**:
- [x] データソースファイルがバックアップから復元された
- [x] 行数が元の値（例: 100000行）と一致する
- [x] 不完全な出力ファイルが削除された

## 📊 成果物とログ

### 成果物

| ファイル | 場所 | 形式 | 保持期間 |
|---------|------|------|---------|
| クレンジング済みデータ | `${OUTPUT_PATH}` | CSV | 30日（その後アーカイブ） |
| 品質レポート | `${LOG_DIR}/summary_*.json` | JSON | 90日 |
| バックアップ | `${BACKUP_DIR}/*_YYYYMMDD.csv.bak` | CSV | 7日 |

### ログファイル

- **実行ログ**: `${LOG_DIR}/cleansing_YYYYMMDD_HHMMSS.log`
- **エラーログ**: 実行ログ内にWARNING/ERRORレベルで記録
- **監査ログ**: `${LOG_DIR}/audit_YYYYMMDD.log`（実行者、時刻、結果を記録）

### 実行記録

実行後、以下をJIRA/Linearチケットに記録：

- **実行日時**: 2025-11-30 10:00:00
- **実行者**: data-engineer-name
- **実行結果**: 成功 / 失敗
- **処理件数**: 入力100000行 → 出力99750行（削除250行）
- **所要時間**: 45分
- **品質スコア**: 98.5%
- **備考**: product_id欠損150件、email欠損800件を補完

## 🔗 関連ドキュメント

### プロセスドキュメント
- [データ品質分析プロセス](data-quality-analysis-process.md) - クレンジング前の品質評価

### プレイブック
- [異常検知判断プレイブック](anomaly-detection-playbook.md) - クレンジング後の異常検知

### トラブルシューティング
- [データ品質トラブルシューティング](../templates/troubleshooting-template.md) - 品質問題の診断と対処

### 参考資料
- [Pandas公式ドキュメント](https://pandas.pydata.org/docs/)
- [データクレンジング禁則事項](anti-patterns-data-analysis.md) - カテゴリ2参照
- "Data Wrangling with Python" (O'Reilly, 2016)

## 📈 メトリクスとモニタリング

### 監視項目

| メトリクス | 閾値 | アラート条件 |
|-----------|------|-------------|
| 処理時間 | < 90分 | > 2時間で警告 |
| エラー率 | < 1% | > 5%で警告 |
| データ削除率 | < 5% | > 10%で警告 |
| 品質スコア | ≥ 95% | < 80%で警告 |
| メモリ使用量 | < 80% | > 90%で警告 |

### 成功基準

- 処理完了時間 < 90分（100万行の場合）
- エラー率 < 1%（変換エラー、検証失敗等）
- データ削除率 < 5%（過度な削除は上流問題を示唆）
- 品質スコア ≥ 95%（欠損・重複・型エラーの総合スコア）

## 🔄 改善履歴

### バージョン履歴

| バージョン | 日付 | 変更内容 | 変更者 |
|-----------|------|---------|-------|
| 1.0 | 2025-11-30 | 初版作成。6ステップのクレンジング手順、トラブルシューティング3事例追加 | data-engineering-team |

### 既知の問題

- **問題1**: 大規模データ（1000万行超）でメモリ不足が発生
  - ワークアラウンド: Daskライブラリへの移行を検討中（次バージョンで対応予定）
- **問題2**: 複数の日付形式が混在する場合、変換精度が低下
  - ワークアラウンド: データソース側で形式統一を依頼中

---

**最終更新**: 2025-11-30
**次回レビュー予定**: 2026-02-28（四半期レビュー）
**メンテナー**: data-engineering-team
