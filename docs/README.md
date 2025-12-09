---
title: "3doca ドキュメントフレームワーク"
description: "Diátaxis + 運用 + C4 の3軸構造に基づく技術ドキュメント体系"
tags:
  - documentation
  - framework
  - diataxis
  - c4-model
category: reference
domain: documentation
difficulty: beginner
created_at: 2025-12-09
updated_at: 2025-12-09
version: "2.0"
author: Claude Code
---

# 3doca ドキュメントフレームワーク

技術ドキュメント（CFD、GIS、数値シミュレーション等）の体系的な作成・管理のための3軸構造フレームワーク。

## ディレクトリ構造

```
docs/
├── 01_knowledge/           # Diátaxis軸（理解・習得）
│   ├── 01-concepts/        # 説明（なぜ・何）- Tier 4
│   ├── 02-tutorials/       # チュートリアル（学習）- Tier 1
│   ├── 03-how-to/          # ハウツー（タスク）- Tier 2
│   └── 04-reference/       # リファレンス（仕様）- Tier 3
├── 02_operations/          # 運用軸（実行）
│   ├── 01-processes/       # プロセス定義 - Tier 2
│   ├── 02-playbooks/       # 状況対応 - Tier 2
│   ├── 03-runbooks/        # 定常作業 - Tier 2
│   └── 04-cheatsheets/     # クイックリファレンス - Tier 0/3
├── 03_architecture/        # C4軸（構造）
│   ├── 01-context/         # Level 1 システムコンテキスト - Tier 0
│   ├── 02-containers/      # Level 2 コンテナ図 - Tier 4
│   └── 03-components/      # Level 3 コンポーネント図 - Tier 4
└── _templates/             # テンプレート格納
```

## 3軸の役割

| 軸 | 目的 | 対象読者 |
|----|------|---------|
| **01_knowledge** | 理解・習得 | 学習者、新規参加者 |
| **02_operations** | 実行・運用 | オペレーター、実務者 |
| **03_architecture** | 構造・設計 | アーキテクト、設計者 |

## 5ティア設計

| Tier | 名称 | 時間目標 | V/T比率 |
|------|------|---------|---------|
| 0 | ビジュアルコンテキスト | 60秒 | 90/10 |
| 1 | クイックスタート | 15分 | 60/40 |
| 2 | ハウツーガイド | - | 40/60 |
| 3 | リファレンス | - | 20/80 |
| 4 | 説明・アーキテクチャ | - | 25/75 |

## クイックリンク

- [Diátaxis軸（知識）](./01_knowledge/README.md)
- [運用軸](./02_operations/README.md)
- [C4軸（アーキテクチャ）](./03_architecture/README.md)
- [テンプレート一覧](./_templates/00-INDEX.md)

## 仕様書

- [ギャップマーカー仕様](./01_knowledge/04-reference/01-GAP-MARKER-SPEC.md)
- [ティア設計仕様](./01_knowledge/04-reference/02-TIER-DESIGN-SPEC.md)
- [移行マップ](./01_knowledge/04-reference/03-MIGRATION-MAP.md)
- [フロントマターリファレンス](./01_knowledge/04-reference/04-FRONTMATTER-REFERENCE.md)

## 主要ドキュメント

### Knowledge軸
- [3軸フレームワーク概念](./01_knowledge/01-concepts/01-three-axis-framework.md)
- [初めてのドキュメント作成](./01_knowledge/02-tutorials/01-first-document.md)
- [テンプレート使用ガイド](./01_knowledge/03-how-to/01-template-usage-guide.md)

### Operations軸
- [ドキュメント作成プロセス](./02_operations/01-processes/01-document-creation-process.md)
- [品質問題対応プレイブック](./02_operations/02-playbooks/01-quality-issues-playbook.md)
- [定期レビュー手順](./02_operations/03-runbooks/01-periodic-document-review.md)
- [ギャップマーカー早見表](./02_operations/04-cheatsheets/01-gap-markers-quick-reference.md)

### Architecture軸
- [システムコンテキスト](./03_architecture/01-context/3doca-framework-context.md)
- [コンテナ構成](./03_architecture/02-containers/3doca-framework-containers.md)
- [テンプレートエンジン詳細](./03_architecture/03-components/template-engine-components.md)

---

**作成日**: 2025-12-09
**バージョン**: 2.0
