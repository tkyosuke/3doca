---
title: "_templates - テンプレート格納"
description: "各軸用ドキュメントテンプレートの格納場所"
tags:
  - templates
  - boilerplate
  - standards
category: reference
domain: documentation
difficulty: beginner
created_at: 2025-12-09
updated_at: 2025-12-09
version: "1.0"
author: Claude Code
---

# _templates - テンプレート格納

各軸（Diátaxis/運用/C4）用のドキュメントテンプレートを格納。

## テンプレート分類

### Diátaxis軸（01_knowledge）

| テンプレート | ティア | 用途 |
|-------------|--------|------|
| concept-template.md | Tier 4 | 概念説明 |
| tutorial-template.md | Tier 1 | チュートリアル |
| how-to-template.md | Tier 2 | ハウツーガイド |
| reference-template.md | Tier 3 | リファレンス |

### 運用軸（02_operations）

| テンプレート | ティア | 用途 |
|-------------|--------|------|
| process-template.md | Tier 2 | プロセス定義 |
| playbook-template.md | Tier 2 | プレイブック |
| runbook-template.md | Tier 2 | ランブック |
| cheatsheet-template.md | Tier 0/3 | チートシート |
| sop-template.md | Tier 2 | 標準作業手順書 |
| troubleshooting-template.md | Tier 2 | トラブルシューティング |

### C4軸（03_architecture）

| テンプレート | ティア | 用途 |
|-------------|--------|------|
| c4-context-template.md | Tier 0 | コンテキスト図 |
| c4-containers-template.md | Tier 4 | コンテナ図 |
| c4-components-template.md | Tier 4 | コンポーネント図 |

### その他

| テンプレート | 用途 |
|-------------|------|
| adr-template.md | アーキテクチャ決定記録 |
| policy-template.md | ポリシー |

## 現在のコンテンツ

[TODOCS: 以下のテンプレートを01-doc-framework/templates/から移行予定]

### 移行予定

- [ ] 00process-document-template.md → process-template.md
- [ ] 01playbook-template.md → playbook-template.md
- [ ] 02runbook-template.md → runbook-template.md
- [ ] 03troubleshooting-template.md → troubleshooting-template.md
- [ ] 04adr-template.md → adr-template.md
- [ ] 05cheatsheet-template.md → cheatsheet-template.md
- [ ] 06policy-template.md → policy-template.md
- [ ] 07sop-template.md → sop-template.md
- [ ] 08cfd-ocean-sop-template.md → cfd-ocean-sop-template.md

### 新規作成予定

- [ ] concept-template.md
- [ ] tutorial-template.md
- [ ] how-to-template.md
- [ ] reference-template.md
- [ ] c4-context-template.md
- [ ] c4-containers-template.md
- [ ] c4-components-template.md

## テンプレート使用方法

1. 適切なテンプレートを選択
2. `docs/`配下の対応フォルダにコピー
3. フロントマターを編集
4. ギャップマーカーを使用して不明点を明示
5. コンテンツを作成

## 関連リンク

- [ギャップマーカー仕様](../01_knowledge/reference/GAP-MARKER-SPEC.md)
- [ティア設計仕様](../01_knowledge/reference/TIER-DESIGN-SPEC.md)
