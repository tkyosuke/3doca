---
title: "ギャップマーカー早見表"
type: cheatsheet
category: "documentation-quality"
tags: [gap-markers, quick-reference, quality]
summary: "ドキュメント作成時に使用するギャップマーカーの1ページリファレンス。用途、優先度、使用例を含む。"
keywords:
  - gap markers
  - quality markers
  - documentation standards
  - quick reference
related:
  - ../03-runbooks/01-periodic-document-review.md
  - ../../01_knowledge/01-concepts/01-framework-overview.md
  - ../../../CLAUDE.md
version: "1.0.0"
status: active
created: "2025-12-10"
updated: "2025-12-10"
---

# ギャップマーカー早見表

> 📋 **クイックリファレンス** | 詳細: [CLAUDE.md ギャップマーカー仕様](../../../CLAUDE.md#ギャップマーカー仕様critical)

## 基本原則

| 原則 | 内容 |
|------|------|
| **推測禁止** | 不明な点はマーカーで明示、推測で埋めない |
| **具体的に** | マーカーには何が必要か具体的に記述 |
| **優先度順** | HIGH → MEDIUM → LOW の順で解消 |
| **検索可能** | すべてのマーカーは `\[.*?:` で検索可能 |

## マーカー一覧

| マーカー | 用途 | 優先度 | 使用タイミング |
|----------|------|--------|----------------|
| `[TODOCS: 説明]` | 未完成セクション、後で記述が必要 | **HIGH** | セクション作成時に内容が不明 |
| `[NEEDS_EXAMPLE: 説明]` | コード例・実行例が必要 | **HIGH** | 説明だけで実例がない |
| `[NEEDS_VERIFICATION: 説明]` | 未検証の主張、要確認 | MEDIUM | 確証がない技術情報 |
| `[INCOMPLETE: 説明]` | 情報不足、追加調査が必要 | MEDIUM | 部分的な情報しかない |
| `[SME_NEEDED: 説明]` | 専門家レビューが必要 | LOW | 専門知識の確認が必要 |
| `[ASSUMPTION: 説明]` | 仮定に基づく記述（明示的に） | INFO | 仮定を明示する |
| `[OUTDATED: 説明]` | 古い可能性がある情報 | MEDIUM | バージョン依存情報 |
| `[LINK_NEEDED: 説明]` | 関連ドキュメントへのリンクが必要 | LOW | 参照先が未作成 |

## 使用例

### TODOCS: 未完成セクション

```markdown
## インストール手順

[TODOCS: Windows環境でのインストール手順を追加]

Linux環境では以下のコマンドを実行：
```

### NEEDS_EXAMPLE: 実例が必要

```markdown
## 設定ファイルの作成

以下のパラメータを設定します：

[NEEDS_EXAMPLE: config.yamlの完全な設定例]
```

### NEEDS_VERIFICATION: 未検証の情報

```markdown
## パフォーマンス

最大メッシュ数は [NEEDS_VERIFICATION: 100万セル程度まで処理可能か要確認] です。
```

### INCOMPLETE: 情報不足

```markdown
## 境界条件

サポートされる境界条件タイプ：
- ディリクレ境界
- ノイマン境界
- [INCOMPLETE: その他の境界条件タイプを調査]
```

### SME_NEEDED: 専門家レビュー

```markdown
## 数値スキーム

[SME_NEEDED: この数値スキームの安定性条件について専門家確認]
```

### ASSUMPTION: 仮定の明示

```markdown
## メモリ要件

[ASSUMPTION: 1セルあたり100バイトのメモリを想定] した場合、
100万セルで約100MBのメモリが必要です。
```

### OUTDATED: 古い可能性

```markdown
## API仕様

[OUTDATED: この情報はv1.2.0時点のもの。最新版で変更された可能性あり]
```

### LINK_NEEDED: リンクが必要

```markdown
## 次のステップ

詳細な設定方法は [LINK_NEEDED: 設定リファレンスへのリンク] を参照してください。
```

## よく使うパターン

### パターン1: セクション骨組み作成時

```markdown
## 新機能の説明

[TODOCS: この機能の概要を記述]

### 使用方法

[NEEDS_EXAMPLE: 基本的な使用例]

### 設定

[INCOMPLETE: 設定可能なパラメータの一覧]

### 注意事項

[SME_NEEDED: パフォーマンスへの影響について専門家確認]
```

### パターン2: 技術情報の記述時

```markdown
## アルゴリズム

このソルバーは [ASSUMPTION: CFL条件を満たす] ことを前提としています。

計算時間は [NEEDS_VERIFICATION: メッシュ数に対して線形か確認] です。

詳細は [LINK_NEEDED: アルゴリズム詳細ドキュメント] を参照。
```

### パターン3: バージョン依存情報

```markdown
## 互換性

v2.0以降でサポート [OUTDATED: v3.0での動作を未確認]

[NEEDS_VERIFICATION: v2.5で追加されたオプションの動作確認]
```

## 検索コマンド

### 全マーカー検索

```bash
# すべてのギャップマーカーを検索
grep -rn "\[TODOCS:\|\[NEEDS_EXAMPLE:\|\[NEEDS_VERIFICATION:\|\[INCOMPLETE:\|\[SME_NEEDED:\|\[ASSUMPTION:\|\[OUTDATED:\|\[LINK_NEEDED:" docs/
```

### 優先度別検索

```bash
# HIGH優先度のみ
grep -rn "\[TODOCS:\|\[NEEDS_EXAMPLE:" docs/

# MEDIUM優先度のみ
grep -rn "\[NEEDS_VERIFICATION:\|\[INCOMPLETE:\|\[OUTDATED:" docs/

# LOW優先度のみ
grep -rn "\[SME_NEEDED:\|\[LINK_NEEDED:" docs/
```

### ファイル別集計

```bash
# ファイルごとのマーカー数をカウント
grep -r "\[TODOCS:\|\[NEEDS_EXAMPLE:" docs/ | cut -d: -f1 | sort | uniq -c | sort -rn
```

### マーカータイプ別集計

```bash
# 各マーカータイプの総数
echo "TODOCS: $(grep -ro "\[TODOCS:" docs/ | wc -l)"
echo "NEEDS_EXAMPLE: $(grep -ro "\[NEEDS_EXAMPLE:" docs/ | wc -l)"
echo "NEEDS_VERIFICATION: $(grep -ro "\[NEEDS_VERIFICATION:" docs/ | wc -l)"
echo "INCOMPLETE: $(grep -ro "\[INCOMPLETE:" docs/ | wc -l)"
echo "SME_NEEDED: $(grep -ro "\[SME_NEEDED:" docs/ | wc -l)"
echo "ASSUMPTION: $(grep -ro "\[ASSUMPTION:" docs/ | wc -l)"
echo "OUTDATED: $(grep -ro "\[OUTDATED:" docs/ | wc -l)"
echo "LINK_NEEDED: $(grep -ro "\[LINK_NEEDED:" docs/ | wc -l)"
```

## 優先度判断フロー

```
質問: この情報は確実か？
  ├─ NO → 確認可能？
  │        ├─ YES → [NEEDS_VERIFICATION]
  │        └─ NO  → [ASSUMPTION] で明示
  │
  └─ YES → セクションは完成？
           ├─ NO → 何が不足？
           │       ├─ コード例 → [NEEDS_EXAMPLE] (HIGH)
           │       ├─ 本文内容 → [TODOCS] (HIGH)
           │       ├─ 追加情報 → [INCOMPLETE] (MEDIUM)
           │       └─ リンク → [LINK_NEEDED] (LOW)
           │
           └─ YES → 専門家確認が必要？
                    ├─ YES → [SME_NEEDED] (LOW)
                    └─ NO  → マーカー不要
```

## トラブル対応

| 症状 | 対処 |
|------|------|
| マーカーが多すぎる | HIGH優先度から順に解消、または [定期レビュー手順](../03-runbooks/01-periodic-document-review.md) を実施 |
| どのマーカーを使うか迷う | 優先度判断フローを参照 |
| マーカーが検索で見つからない | エスケープ確認: `\[` でエスケープされているか |
| 推測で書いてしまった | `[ASSUMPTION:]` に変更して仮定を明示 |

## 解消の目安

| 優先度 | 対応目標 | 備考 |
|--------|----------|------|
| HIGH | ドキュメント公開前に解消 | TODOCS, NEEDS_EXAMPLE |
| MEDIUM | 次回レビュー時に対応 | 1-3ヶ月以内 |
| LOW | 機会があれば対応 | 必須ではない |
| INFO | 明示目的のため残す | ASSUMPTION |

## ベストプラクティス

1. **早めにマーク**: 不明点はすぐマーカーを付ける
2. **具体的に**: 何が必要か明確に記述する
3. **推測禁止**: 不明なら正直にマーカーを残す
4. **定期レビュー**: 月次でマーカーを確認・解消
5. **優先度重視**: HIGH → MEDIUM → LOW の順で対応

---

**詳細**: [CLAUDE.md ギャップマーカー仕様](../../../CLAUDE.md#ギャップマーカー仕様critical) | **定期レビュー**: [ドキュメントレビュー手順](../03-runbooks/01-periodic-document-review.md)
