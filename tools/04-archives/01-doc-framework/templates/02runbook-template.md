---
# === 必須：識別情報 ===
document_id: "RUN-DOMAIN-NNN"  # RUN-data-001, RUN-ops-001等
title: "<!-- TEMPLATE: ランブック: タスク名（例: ランブック: データクレンジング） -->"
type: runbook
version: "1.0"
status: active  # draft | review | approved | active | deprecated

# === 所有権 ===
owner: "@team-name"
author: "<!-- TEMPLATE: 作成者名 -->"
created: <!-- TEMPLATE: YYYY-MM-DD -->
updated: <!-- TEMPLATE: YYYY-MM-DD -->

# === RAG最適化 ===
tags:
  - runbook
  - <!-- TEMPLATE: タスクタグ（例: data-cleansing, maintenance） -->
  - <!-- TEMPLATE: ドメインタグ（例: data-analysis, operations） -->
key_concepts:
  - "<!-- TEMPLATE: セマンティック用語1（例: データクレンジング、品質検証） -->"
  - "<!-- TEMPLATE: セマンティック用語2（例: バックアップ、ロールバック） -->"
summary: "<!-- TEMPLATE: 検索結果用の一文説明（150文字以内） -->"

# === ドメインコンテキスト ===
category: runbook
domain: <!-- TEMPLATE: data-analysis | cfd | gis | visualization | infrastructure -->
difficulty: <!-- TEMPLATE: beginner | intermediate | advanced -->
audience: <!-- TEMPLATE: developers | operators | architects | scientists -->

# === 関連ドキュメント ===
related_docs:
  - path: "<!-- TEMPLATE: /path/to/related-process.md -->"
    relationship: "implements"  # implements | governed-by | references | depends-on | escalates-to
  - path: "<!-- TEMPLATE: /path/to/related-playbook.md -->"
    relationship: "references"

# === メンテナンス ===
next_review: <!-- TEMPLATE: YYYY-MM-DD -->
review_cycle_days: 90
---

# ランブック: <!-- TEMPLATE: タスク名 -->

---

## 必須セクション一覧

このテンプレートには以下の必須セクションが含まれています：

| セクション | 目的 | 省略時の影響 |
|-----------|------|-------------|
| 概要 | 手順の目的と範囲 | 何のための手順か不明 |
| 前提条件 | 実行前の確認事項 | 実行中に問題発生 |
| 手順 | 具体的なコマンド/ステップ | 再現性のない作業になる |
| ロールバック | 失敗時の復旧方法 | 障害からの復旧が困難 |
| 検証 | 完了確認方法 | 完了判定ができない |

---

**サービス**: <!-- TEMPLATE: 対象システム/サービス名 -->
**所要時間**: <!-- TEMPLATE: 目安時間（例: 30-60分） -->
**実行頻度**: <!-- TEMPLATE: daily | weekly | monthly | on-demand -->
**対象読者**: <!-- TEMPLATE: 役割（例: データエンジニア、運用担当者） -->

## 📋 概要

<!--
なぜ必要か: 手順の目的を明確化し、適切なタイミングで実行できるようにするため
省略するとどうなるか: 不要な実行や実行漏れが発生する
-->

### タスクの目的

<!-- TEMPLATE: 2-3文でタスクの目的を記述 -->
<!-- 例: このランブックは、データソースから取得したデータの品質問題（欠損値、外れ値、形式不統一）を修正し、分析に適した形式に整形するためのデータクレンジング手順を提供します。 -->

### 実行タイミング

**✅ 実行すべき場合**:
- <!-- TEMPLATE: 実行条件1 -->
- <!-- TEMPLATE: 実行条件2 -->
- <!-- TEMPLATE: 実行条件3 -->

**❌ 実行すべきでない場合**:
- <!-- TEMPLATE: 除外条件1 -->
- <!-- TEMPLATE: 除外条件2 -->

## ⚙️ 前提条件

<!--
なぜ必要か: 実行に必要な環境・権限を事前確認し、実行失敗を防ぐため
省略するとどうなるか: 実行途中でエラーが発生し、中途半端な状態で停止する
-->

### 必要な権限

- [ ] <!-- TEMPLATE: 必要な権限1（例: データベース読み取り権限） -->
- [ ] <!-- TEMPLATE: 必要な権限2（例: ファイルシステム書き込み権限） -->
- [ ] <!-- TEMPLATE: 必要な権限3 -->

### 必要なツール

| ツール | バージョン | 確認方法 |
|--------|-----------|---------|
| <!-- TEMPLATE: ツール名 --> | <!-- TEMPLATE: バージョン --> | `<!-- TEMPLATE: コマンド -->` |

### 環境変数

```bash
# TEMPLATE: 必要な環境変数を記載
# 例:
# export DATA_SOURCE="postgresql://localhost/mydb"
# export OUTPUT_DIR="/data/cleaned"
```

## 📝 事前確認チェックリスト

**⚠️ [重要]** 実行前に以下を必ず確認してください。

- [ ] **バックアップ作成済み**: <!-- TEMPLATE: バックアップ確認方法 -->
- [ ] **リソース確認**: <!-- TEMPLATE: CPU/メモリ/ディスク容量確認 -->
- [ ] **依存サービス稼働**: <!-- TEMPLATE: 確認対象サービス -->
- [ ] **実行時間帯確認**: <!-- TEMPLATE: 実行可能な時間帯 -->
- [ ] <!-- TEMPLATE: その他の確認項目 -->

### システム状態確認

```bash
# TEMPLATE: システム状態確認コマンド
# 例:
# df -h  # ディスク容量確認
# free -h  # メモリ確認
# systemctl status myservice  # サービス状態確認
```

**期待される出力**:
<!-- TEMPLATE: 正常な状態の出力例 -->

## 🔧 実行手順

<!--
なぜ必要か: 具体的なコマンド・ステップを提供し、再現性の高い作業を実現するため
省略するとどうなるか: 作業者によって実行内容が異なり、結果が不安定になる
-->

### ステップ1: <!-- TEMPLATE: ステップ名（動詞で始める、例: データソース接続確認） -->

<!--
なぜ必要か: このステップで何を達成するかを明確化
省略するとどうなるか: ステップの重要性が理解されず、スキップされる可能性
-->

**目的**: <!-- TEMPLATE: このステップの目的 -->

**実行内容**:
```bash
# TEMPLATE: 実際のコマンドをここに記載
# 例:
# psql -h localhost -U user -d mydb -c "SELECT COUNT(*) FROM source_table;"
```

**期待される結果**:
```
TEMPLATE: 正常時の出力例
例:
 count
-------
 10000
(1 row)
```

**⚠️ エラー時の対処**:
- エラー: <!-- TEMPLATE: エラーメッセージ例 -->
  - 原因: <!-- TEMPLATE: 原因 -->
  - 対処: <!-- TEMPLATE: 対処方法 -->

---

### ステップ2: <!-- TEMPLATE: ステップ名 -->

<!--
なぜ必要か: このステップで何を達成するかを明確化
省略するとどうなるか: ステップの重要性が理解されず、スキップされる可能性
-->

**目的**: <!-- TEMPLATE: このステップの目的 -->

**実行内容**:
```python
# TEMPLATE: Pythonコード例の場合
# 例:
# import pandas as pd
# df = pd.read_csv('input.csv')
# print(f"Loaded {len(df)} rows")
```

**期待される結果**:
```
TEMPLATE: 正常時の出力例
例:
Loaded 10000 rows
```

**⚠️ エラー時の対処**:
<!-- TEMPLATE: エラーと対処方法 -->

---

### ステップ3: <!-- TEMPLATE: ステップ名 -->

**目的**: <!-- TEMPLATE: このステップの目的 -->

**実行内容**:
```bash
# TEMPLATE: コマンド
```

**期待される結果**:
<!-- TEMPLATE: 正常時の出力例 -->

**⚠️ 必要に応じてステップを追加または削除してください**

## ✅ 検証チェックリスト

<!--
なぜ必要か: 作業完了を客観的に確認し、不完全な状態での完了報告を防ぐため
省略するとどうなるか: 作業が正しく完了したか判断できず、後続処理で問題が発生する
-->

**[重要]** 全ステップ完了後、以下を確認してください。

- [ ] **出力ファイル生成**: <!-- TEMPLATE: 確認方法 -->
- [ ] **データ件数一致**: <!-- TEMPLATE: 確認方法 -->
- [ ] **品質基準達成**: <!-- TEMPLATE: 確認方法 -->
- [ ] **ログ記録**: <!-- TEMPLATE: 確認方法 -->
- [ ] <!-- TEMPLATE: その他の検証項目 -->

### 検証コマンド

```bash
# TEMPLATE: 検証用コマンド
# 例:
# wc -l output.csv  # 行数確認
# head -n 5 output.csv  # サンプル確認
```

**期待される結果**:
<!-- TEMPLATE: 検証成功時の出力 -->

## 🚨 トラブルシューティング

よくある問題と対処法：

| 症状 | 原因 | 対処法 | 参考 |
|------|------|--------|------|
| <!-- TEMPLATE: エラーメッセージ/症状 --> | <!-- TEMPLATE: 考えられる原因 --> | <!-- TEMPLATE: 対処手順 --> | <!-- TEMPLATE: 関連ドキュメント --> |

### 詳細なトラブルシューティング

#### 問題1: <!-- TEMPLATE: 問題の症状 -->

**症状の詳細**:
<!-- TEMPLATE: 詳細な症状説明 -->

**診断方法**:
```bash
# TEMPLATE: 診断コマンド
```

**解決手順**:
1. <!-- TEMPLATE: 解決ステップ1 -->
2. <!-- TEMPLATE: 解決ステップ2 -->
3. <!-- TEMPLATE: 解決ステップ3 -->

詳細は [トラブルシューティングガイド](<!-- TEMPLATE: パス -->) を参照。

## ⏮️ ロールバック手順

<!--
なぜ必要か: 失敗時の復旧手順を明確化し、迅速な復旧を可能にするため
省略するとどうなるか: 障害から復旧できず、システムが長時間停止する
-->

**⚠️ [重要]** 問題が発生した場合の復旧手順

### ロールバックが必要な状況

- <!-- TEMPLATE: ロールバック条件1 -->
- <!-- TEMPLATE: ロールバック条件2 -->
- <!-- TEMPLATE: ロールバック条件3 -->

### ロールバック手順

#### ステップ1: 実行中断

<!--
なぜ必要か: 被害拡大を防ぐため
省略するとどうなるか: 問題が悪化し、復旧が困難になる
-->

```bash
# TEMPLATE: プロセス停止コマンド
# 例:
# kill -SIGTERM $(cat /var/run/myprocess.pid)
```

#### ステップ2: バックアップ復元

<!--
なぜ必要か: 実行前の状態に戻すため
省略するとどうなるか: データ不整合が残る
-->

```bash
# TEMPLATE: バックアップ復元コマンド
# 例:
# cp /backup/data.csv.bak /data/data.csv
```

#### ステップ3: 状態確認

```bash
# TEMPLATE: 状態確認コマンド
```

**復旧確認**:
- [ ] <!-- TEMPLATE: 確認項目1 -->
- [ ] <!-- TEMPLATE: 確認項目2 -->

## 📊 成果物とログ

### 成果物

| ファイル | 場所 | 形式 | 保持期間 |
|---------|------|------|---------|
| <!-- TEMPLATE: 成果物名 --> | <!-- TEMPLATE: パス --> | <!-- TEMPLATE: 形式 --> | <!-- TEMPLATE: 期間 --> |

### ログファイル

- **実行ログ**: <!-- TEMPLATE: ログパス -->
- **エラーログ**: <!-- TEMPLATE: ログパス -->
- **監査ログ**: <!-- TEMPLATE: ログパス -->

### 実行記録

実行後、以下を記録：

- 実行日時: <!-- TEMPLATE: YYYY-MM-DD HH:MM:SS -->
- 実行者: <!-- TEMPLATE: 名前 -->
- 実行結果: <!-- TEMPLATE: 成功/失敗 -->
- 処理件数: <!-- TEMPLATE: 件数 -->
- 所要時間: <!-- TEMPLATE: 時間 -->
- 備考: <!-- TEMPLATE: 特記事項 -->

## 🔗 関連ドキュメント

### プロセスドキュメント
- [<!-- TEMPLATE: プロセス名 -->](<!-- TEMPLATE: パス -->) - <!-- TEMPLATE: 説明 -->

### プレイブック
- [<!-- TEMPLATE: プレイブック名 -->](<!-- TEMPLATE: パス -->) - <!-- TEMPLATE: 説明 -->

### トラブルシューティング
- [<!-- TEMPLATE: トラブルシューティング名 -->](<!-- TEMPLATE: パス -->) - <!-- TEMPLATE: 説明 -->

### 参考資料
- <!-- TEMPLATE: 参考資料1 -->
- <!-- TEMPLATE: 参考資料2 -->

## 📈 メトリクスとモニタリング

### 監視項目

| メトリクス | 閾値 | アラート条件 |
|-----------|------|-------------|
| <!-- TEMPLATE: メトリクス名（例: 処理時間） --> | <!-- TEMPLATE: 閾値 --> | <!-- TEMPLATE: 条件 --> |
| <!-- TEMPLATE: メトリクス名（例: エラー率） --> | <!-- TEMPLATE: 閾値 --> | <!-- TEMPLATE: 条件 --> |

### 成功基準

- <!-- TEMPLATE: 成功基準1（例: 処理完了時間 < 60分） -->
- <!-- TEMPLATE: 成功基準2（例: エラー率 < 1%） -->
- <!-- TEMPLATE: 成功基準3 -->

## 🔄 改善履歴

### バージョン履歴

| バージョン | 日付 | 変更内容 | 変更者 |
|-----------|------|---------|-------|
| 1.0 | <!-- TEMPLATE: YYYY-MM-DD --> | 初版作成 | <!-- TEMPLATE: 名前 --> |

### 既知の問題

- <!-- TEMPLATE: 既知の問題1とワークアラウンド -->
- <!-- TEMPLATE: 既知の問題2とワークアラウンド -->

---

**最終更新**: <!-- TEMPLATE: YYYY-MM-DD -->
**次回レビュー予定**: <!-- TEMPLATE: YYYY-MM-DD -->
**メンテナー**: <!-- TEMPLATE: 担当者名 -->
