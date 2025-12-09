---
title: "[TODOCS: ランブック名]"
type: runbook
category: "[TODOCS: カテゴリ]"
tags: []
summary: |
  [TODOCS: この定常作業の目的と概要]
keywords:
  - [TODOCS: キーワード]
frequency: "[TODOCS: 日次/週次/月次/随時]"
estimated_time: "[TODOCS: 所要時間]"
owner: "[TODOCS: 責任者]"
executor: "[TODOCS: 実行者のロール]"
related:
  - [LINK_NEEDED: 関連ドキュメント]
version: "1.0.0"
status: draft
created: "[TODOCS: YYYY-MM-DD]"
updated: "[TODOCS: YYYY-MM-DD]"
---

# [TODOCS: ランブック名]

| 項目 | 内容 |
|------|------|
| **実行頻度** | [TODOCS: 頻度] |
| **所要時間** | [TODOCS: 目安時間] |
| **実行者** | [TODOCS: ロール/担当] |
| **最終実行** | [TODOCS: YYYY-MM-DD] |

## 目的

[TODOCS: この作業を行う目的（1-2文）]

## 前提条件チェック

実行前に以下を確認：

- [ ] [TODOCS: 前提条件1]
- [ ] [TODOCS: 前提条件2]
- [ ] [TODOCS: 必要な権限/アクセス]

```bash
# 環境確認
[NEEDS_EXAMPLE: 環境確認コマンド]
```

## 実行手順

### Step 1: [TODOCS: ステップ名]

[TODOCS: 簡潔な説明]

```bash
[NEEDS_EXAMPLE: 実行コマンド]
```

**期待される出力**：
```
[NEEDS_EXAMPLE: 期待される出力]
```

**チェック**: [ ] 出力が期待通りである

---

### Step 2: [TODOCS: ステップ名]

[TODOCS: 説明]

```bash
[NEEDS_EXAMPLE: コマンド]
```

**チェック**: [ ] [TODOCS: 確認項目]

---

### Step 3: [TODOCS: ステップ名]

[TODOCS: 説明]

```python
[NEEDS_EXAMPLE: スクリプト/コード]
```

**チェック**: [ ] [TODOCS: 確認項目]

---

### Step 4: 完了確認

```bash
[NEEDS_EXAMPLE: 最終確認コマンド]
```

**完了基準**：
- [ ] [TODOCS: 完了条件1]
- [ ] [TODOCS: 完了条件2]

## クイックコマンド集

よく使うコマンドをまとめて実行する場合：

```bash
# === [TODOCS: 作業名] 一括実行 ===
# 注意: 各ステップの出力を確認しながら実行すること

[NEEDS_EXAMPLE: Step 1]

[NEEDS_EXAMPLE: Step 2]

[NEEDS_EXAMPLE: Step 3]

echo "完了"
```

## パラメータ一覧

| パラメータ | 説明 | デフォルト | 例 |
|------------|------|------------|-----|
| [TODOCS] | [TODOCS] | [TODOCS] | [TODOCS] |

## トラブルシューティング

### エラー: [TODOCS: エラー内容]

**原因**: [TODOCS: 原因]

**対処**:
```bash
[NEEDS_EXAMPLE: 対処コマンド]
```

---

### エラー: [TODOCS: エラー内容]

**原因**: [TODOCS: 原因]

**対処**: [LINK_NEEDED: プレイブックへのリンク]

## ロールバック

問題が発生した場合の復旧手順：

```bash
[NEEDS_EXAMPLE: ロールバックコマンド]
```

## 実行記録

| 日付 | 実行者 | 結果 | 備考 |
|------|--------|------|------|
| | | □ 成功 / □ 失敗 | |

## 関連ドキュメント

- **プロセス全体**: [LINK_NEEDED: プロセスドキュメント]
- **障害対応**: [LINK_NEEDED: プレイブック]
- **詳細設定**: [LINK_NEEDED: リファレンス]
- **背景知識**: [LINK_NEEDED: 概念説明]

---

<!-- 検証チェックリスト（作成完了時に確認）
□ コマンドはコピー&ペーストで実行可能か
□ 各ステップに確認ポイントがあるか
□ パラメータの説明があるか
□ トラブルシューティングがあるか
□ ロールバック手順があるか
□ 前提条件チェックリストがあるか
□ 実行記録欄があるか
-->
