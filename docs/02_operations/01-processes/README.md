---
title: "processes - プロセス定義"
description: "ワークフロー全体を図示するプロセスドキュメント"
tags:
  - process
  - workflow
  - tier-2
category: reference
domain: documentation
difficulty: beginner
created_at: 2025-12-09
updated_at: 2025-12-10
version: "1.0"
author: Claude Code
---

# processes - プロセス定義（Tier 2）

## 目的

ワークフロー全体を図示し、入力・出力を明確にする。

## ティア仕様

| 項目 | 値 |
|------|-----|
| **ティア** | Tier 2 |
| **ビジュアル/テキスト比率** | 40/60 |
| **必須要素** | Mermaid flowchart |

## プロセスドキュメントの要件

1. **ワークフロー全体を図示**（Mermaid flowchart推奨）
2. **入力・出力を明確に**
3. **関連するplaybook/runbookへのリンク**
4. **責任範囲の明記**

## 現在のコンテンツ

### [01-document-creation-process.md](./01-document-creation-process.md)
技術ドキュメント作成の全体プロセス定義。

**優先度**: ★★★★★ (必須)

[TODOCS: 以下のプロセスを移行予定]

- [ ] データ解析プロセス（00data-analysis-process.md）
- [ ] データ品質分析プロセス（01data-quality-analysis-process.md）

## 移行予定ファイル

- `01-doc-framework/examples/00data-analysis-process.md`
- `01-doc-framework/examples/01data-quality-analysis-process.md`

## テンプレート

[LINK_NEEDED: _templates/process-template.md]

## 関連リンク

- [プレイブック](../02-playbooks/README.md)
- [ランブック](../03-runbooks/README.md)
