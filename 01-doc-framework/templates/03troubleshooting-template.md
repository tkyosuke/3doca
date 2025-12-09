---
# === 必須：識別情報 ===
document_id: "TRS-DOMAIN-NNN"  # TRS-data-001, TRS-ops-001等
title: "<!-- TEMPLATE: トラブルシューティング: 問題名（例: トラブルシューティング: メッシュ非直交性エラー） -->"
type: troubleshooting
version: "1.0"
status: active  # draft | review | approved | active | deprecated

# === 所有権 ===
owner: "@team-name"
author: "<!-- TEMPLATE: 作成者名 -->"
created: <!-- TEMPLATE: YYYY-MM-DD -->
updated: <!-- TEMPLATE: YYYY-MM-DD -->

# === RAG最適化 ===
tags:
  - troubleshooting
  - <!-- TEMPLATE: 問題タグ（例: error, performance, configuration） -->
  - <!-- TEMPLATE: ドメインタグ（例: data-analysis, operations） -->
key_concepts:
  - "<!-- TEMPLATE: セマンティック用語1（例: エラー診断、根本原因分析） -->"
  - "<!-- TEMPLATE: セマンティック用語2（例: ワークアラウンド、恒久対応） -->"
summary: "<!-- TEMPLATE: 検索結果用の一文説明（150文字以内） -->"

# === ドメインコンテキスト ===
category: troubleshooting
domain: <!-- TEMPLATE: data-analysis | cfd | gis | visualization | infrastructure -->
difficulty: <!-- TEMPLATE: beginner | intermediate | advanced -->
severity: <!-- TEMPLATE: critical | high | medium | low -->
audience: <!-- TEMPLATE: developers | operators | architects | scientists -->

# === 関連ドキュメント ===
related_docs:
  - path: "<!-- TEMPLATE: /path/to/related-runbook.md -->"
    relationship: "references"  # implements | governed-by | references | depends-on | escalates-to
  - path: "<!-- TEMPLATE: /path/to/related-playbook.md -->"
    relationship: "escalates-to"

# === メンテナンス ===
next_review: <!-- TEMPLATE: YYYY-MM-DD -->
review_cycle_days: 90
reported_date: <!-- TEMPLATE: YYYY-MM-DD（問題が最初に報告された日） -->
resolved_date: <!-- TEMPLATE: YYYY-MM-DD（問題が解決された日） -->
---

# トラブルシューティング: <!-- TEMPLATE: 問題名 -->

---

## 必須セクション一覧

このテンプレートには以下の必須セクションが含まれています：

| セクション | 目的 | 省略時の影響 |
|-----------|------|-------------|
| 問題の特定 | 症状の明確化 | 問題の切り分けができない |
| 原因分析 | 根本原因の調査 | 表面的な対処で再発する |
| 解決手順 | 修正方法の提示 | 解決方法がわからない |
| 予防策 | 再発防止策 | 同じ問題が繰り返される |

---

**重要度**: <!-- TEMPLATE: 🔴 Critical | 🟡 High | 🟢 Medium | ⚪ Low -->
**ステータス**: <!-- TEMPLATE: Resolved | Ongoing | Known Issue -->
**影響範囲**: <!-- TEMPLATE: 影響を受けるシステム/ユーザー -->

## 📋 概要

<!--
なぜ必要か: 問題の全体像を迅速に把握し、対応の緊急度を判断するため
省略するとどうなるか: 問題の深刻さが伝わらず、適切な優先度で対応されない
-->

### 問題の要約

<!-- TEMPLATE: 2-3文で問題を要約 -->
<!-- 例: データ品質チェック実行時に、特定のカラムで欠損値検出が正常に動作せず、NaN値が見逃されるという問題が発生しています。この問題は、Pandas 1.5.0以降で発生し、データ型がobjectの場合に顕在化します。 -->

### 発生環境

- **OS**: <!-- TEMPLATE: OS情報 -->
- **ソフトウェアバージョン**: <!-- TEMPLATE: バージョン情報 -->
- **環境**: <!-- TEMPLATE: 開発/ステージング/本番 -->
- **発生頻度**: <!-- TEMPLATE: 常時 | 間欠的 | 特定条件下 -->

## 🔍 症状

<!--
なぜ必要か: 問題を正確に特定し、同じ問題かどうか判断できるようにするため
省略するとどうなるか: 異なる問題に対して誤った解決策を適用してしまう
-->

### 観測された現象

**⚠️ [重要]** 問題を特定するための具体的な症状を記載

1. **エラーメッセージ**:
```
TEMPLATE: 実際のエラーメッセージをここに記載
例:
Traceback (most recent call last):
  File "analyze.py", line 42, in <module>
    result = df.isnull().sum()
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
```

2. **異常な動作**:
<!-- TEMPLATE: エラーメッセージ以外の異常な動作を記述 -->
- <!-- TEMPLATE: 異常1 -->
- <!-- TEMPLATE: 異常2 -->
- <!-- TEMPLATE: 異常3 -->

3. **影響**:
- **パフォーマンス**: <!-- TEMPLATE: 処理時間、リソース使用率の変化 -->
- **データ整合性**: <!-- TEMPLATE: データへの影響 -->
- **ユーザー影響**: <!-- TEMPLATE: ユーザーへの影響 -->

### 再現手順

```bash
# TEMPLATE: 問題を再現するための具体的な手順
# 例:
# 1. サンプルデータ作成
# python create_test_data.py

# 2. 問題のあるスクリプト実行
# python analyze.py --input test_data.csv

# 3. エラー発生を確認
```

**再現率**: <!-- TEMPLATE: 100% | 50% | まれ -->

## 🔬 根本原因

<!--
なぜ必要か: 問題の本質を理解し、適切な解決策を選択するため
省略するとどうなるか: 表面的な対処療法のみで、問題が再発する
-->

### 原因分析

**[重要]** 問題の技術的な根本原因を説明

<!-- TEMPLATE: 原因の詳細説明 -->
<!-- 例: Pandas 1.5.0でNaN検出ロジックが変更され、object型カラムに対するisnull()の動作が変更されました。従来はNoneとNaNの両方を検出しましたが、新バージョンではNoneのみを検出するようになりました。 -->

### 原因特定プロセス

1. **仮説**: <!-- TEMPLATE: 最初の仮説 -->
2. **検証**: <!-- TEMPLATE: 検証方法 -->
3. **結論**: <!-- TEMPLATE: 検証結果と最終結論 -->

### 関連する技術的背景

<!-- TEMPLATE: 原因を理解するための技術的背景 -->
- <!-- TEMPLATE: 背景1 -->
- <!-- TEMPLATE: 背景2 -->

## 🛠️ 解決手順

<!--
なぜ必要か: 具体的な解決方法を提供し、迅速な復旧を可能にするため
省略するとどうなるか: 解決方法が不明で、長時間システムが停止する
-->

### 即時対応（ワークアラウンド）

<!--
なぜ必要か: 一時的な回避策で迅速に影響を最小化するため
省略するとどうなるか: 根本解決まで影響が継続する
-->

**⚠️ 一時的な回避策（根本解決ではない）**

```python
# TEMPLATE: ワークアラウンドコード
# 例:
# 明示的な型変換でNaN検出を正常化
df = df.astype(str).replace('nan', np.nan)
missing_count = df.isnull().sum()
```

**適用条件**:
- <!-- TEMPLATE: この回避策が適用できる条件 -->

**制限事項**:
- <!-- TEMPLATE: この回避策の制限事項 -->

---

### 恒久対応（根本解決）

<!--
なぜ必要か: 問題を根本から解決し、再発を防止するため
省略するとどうなるか: ワークアラウンドに依存し続け、メンテナンスコストが増大する
-->

**⚠️ [重要]** 問題を根本から解決する手順

#### ステップ1: <!-- TEMPLATE: 解決ステップ名 -->

<!--
なぜ必要か: このステップで何を達成するかを明確化
省略するとどうなるか: 解決手順が不完全になる
-->

```bash
# TEMPLATE: 実行コマンド
# 例:
# pip install pandas==1.4.4  # 安定バージョンにダウングレード
```

**期待される結果**:
```
TEMPLATE: 正常な出力例
```

#### ステップ2: <!-- TEMPLATE: 解決ステップ名 -->

<!--
なぜ必要か: このステップで何を達成するかを明確化
省略するとどうなるか: 解決手順が不完全になる
-->

```python
# TEMPLATE: コード修正例
# 例:
# コードを修正してobject型を明示的に処理
def detect_missing(df, column):
    if df[column].dtype == 'object':
        return df[column].replace('', np.nan).isnull().sum()
    return df[column].isnull().sum()
```

#### ステップ3: <!-- TEMPLATE: 解決ステップ名 -->

```bash
# TEMPLATE: 検証コマンド
```

**検証結果**:
<!-- TEMPLATE: 期待される検証結果 -->

## ✅ 検証方法

<!--
なぜ必要か: 解決が正しく適用されたことを客観的に確認するため
省略するとどうなるか: 問題が実際には解決していない可能性がある
-->

### 解決確認チェックリスト

- [ ] **エラー再発なし**: <!-- TEMPLATE: 確認方法 -->
- [ ] **パフォーマンス正常**: <!-- TEMPLATE: 確認方法 -->
- [ ] **データ整合性**: <!-- TEMPLATE: 確認方法 -->
- [ ] **回帰テスト通過**: <!-- TEMPLATE: テスト内容 -->

### テストケース

```python
# TEMPLATE: 検証用テストコード
# 例:
def test_null_detection():
    df = pd.DataFrame({'col': [1, None, np.nan, 'value']})
    assert detect_missing(df, 'col') == 2  # NoneとNaNの2つ
```

## 🚫 予防策

<!--
なぜ必要か: 同様の問題の再発を防ぎ、システムの安定性を高めるため
省略するとどうなるか: 同じ問題が繰り返し発生し、信頼性が低下する
-->

### 再発防止策

**[重要]** 同様の問題を防ぐための対策

1. **コードレビュー基準追加**:
   - <!-- TEMPLATE: 追加すべきレビュー基準 -->

2. **テストケース追加**:
   - <!-- TEMPLATE: 追加すべきテストケース -->

3. **監視アラート設定**:
   - <!-- TEMPLATE: 設定すべきアラート -->

4. **ドキュメント更新**:
   - <!-- TEMPLATE: 更新すべきドキュメント -->

### ベストプラクティス

<!-- TEMPLATE: この問題から学んだベストプラクティス -->
- <!-- TEMPLATE: ベストプラクティス1 -->
- <!-- TEMPLATE: ベストプラクティス2 -->
- <!-- TEMPLATE: ベストプラクティス3 -->

### 禁則事項

**❌ やってはいけないこと**:
- <!-- TEMPLATE: 禁止事項1（例: object型カラムでのisnull()直接使用） -->
- <!-- TEMPLATE: 禁止事項2 -->

## 📚 関連情報

### 関連ドキュメント

- [<!-- TEMPLATE: 関連ランブック名 -->](<!-- TEMPLATE: パス -->) - <!-- TEMPLATE: 説明 -->
- [<!-- TEMPLATE: 関連プレイブック名 -->](<!-- TEMPLATE: パス -->) - <!-- TEMPLATE: 説明 -->

### 類似の問題

- [<!-- TEMPLATE: 類似問題1 -->](<!-- TEMPLATE: パス -->) - <!-- TEMPLATE: 説明 -->
- [<!-- TEMPLATE: 類似問題2 -->](<!-- TEMPLATE: パス -->) - <!-- TEMPLATE: 説明 -->

### 外部リソース

- <!-- TEMPLATE: 公式ドキュメントURL -->
- <!-- TEMPLATE: Stack Overflow URL -->
- <!-- TEMPLATE: GitHub Issue URL -->

## 📊 影響分析

### 影響を受けたシステム/ユーザー

| システム/ユーザー | 影響内容 | 影響期間 | 対応状況 |
|------------------|---------|---------|---------|
| <!-- TEMPLATE: システム名 --> | <!-- TEMPLATE: 影響内容 --> | <!-- TEMPLATE: 期間 --> | <!-- TEMPLATE: 対応済/対応中 --> |

### ダウンタイム/パフォーマンス影響

- **ダウンタイム**: <!-- TEMPLATE: 時間 -->
- **影響ユーザー数**: <!-- TEMPLATE: 人数 -->
- **データ損失**: <!-- TEMPLATE: 有/無、詳細 -->

## 🔄 タイムライン

### 問題対応の経緯

| 日時 | イベント | 担当者 | 備考 |
|------|---------|-------|------|
| <!-- TEMPLATE: YYYY-MM-DD HH:MM --> | 問題検出 | <!-- TEMPLATE: 名前 --> | <!-- TEMPLATE: 備考 --> |
| <!-- TEMPLATE: YYYY-MM-DD HH:MM --> | 原因特定 | <!-- TEMPLATE: 名前 --> | <!-- TEMPLATE: 備考 --> |
| <!-- TEMPLATE: YYYY-MM-DD HH:MM --> | 暫定対応実施 | <!-- TEMPLATE: 名前 --> | <!-- TEMPLATE: 備考 --> |
| <!-- TEMPLATE: YYYY-MM-DD HH:MM --> | 恒久対応完了 | <!-- TEMPLATE: 名前 --> | <!-- TEMPLATE: 備考 --> |

## 📝 教訓と改善点

### 学んだこと

<!-- TEMPLATE: この問題対応から学んだ重要な教訓 -->
1. <!-- TEMPLATE: 教訓1 -->
2. <!-- TEMPLATE: 教訓2 -->
3. <!-- TEMPLATE: 教訓3 -->

### 改善アクション

| アクション | 担当者 | 期限 | ステータス |
|-----------|-------|------|----------|
| <!-- TEMPLATE: 改善アクション1 --> | <!-- TEMPLATE: 担当者 --> | <!-- TEMPLATE: 期限 --> | <!-- TEMPLATE: 未着手/進行中/完了 --> |

## 🔗 添付資料

### ログファイル

- **エラーログ**: <!-- TEMPLATE: パス/URL -->
- **システムログ**: <!-- TEMPLATE: パス/URL -->
- **トレースログ**: <!-- TEMPLATE: パス/URL -->

### スクリーンショット

<!-- TEMPLATE: スクリーンショットへのリンクまたは説明 -->

### 追加資料

- <!-- TEMPLATE: 追加資料1 -->
- <!-- TEMPLATE: 追加資料2 -->

---

**最終更新**: <!-- TEMPLATE: YYYY-MM-DD -->
**レビュー担当**: <!-- TEMPLATE: 名前 -->
**承認**: <!-- TEMPLATE: 承認者名、承認日 -->
