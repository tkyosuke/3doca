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
├── 01_knowledge/       # Diátaxis軸（理解・習得）
│   ├── concepts/       # 説明（なぜ・何）- Tier 4
│   ├── tutorials/      # チュートリアル（学習）- Tier 1
│   ├── how-to/         # ハウツー（タスク）- Tier 2
│   └── reference/      # リファレンス（仕様）- Tier 3
├── 02_operations/      # 運用軸（実行）
│   ├── processes/      # プロセス定義 - Tier 2
│   ├── playbooks/      # 状況対応 - Tier 2
│   ├── runbooks/       # 定常作業 - Tier 2
│   └── cheatsheets/    # クイックリファレンス - Tier 0/3
├── 03_architecture/    # C4軸（構造）
│   ├── context/        # Level 1 システムコンテキスト - Tier 0
│   ├── containers/     # Level 2 コンテナ図 - Tier 4
│   └── components/     # Level 3 コンポーネント図 - Tier 4
└── _templates/         # テンプレート格納
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
- [テンプレート](./_templates/README.md)

## 仕様書

- [ギャップマーカー仕様](./01_knowledge/reference/GAP-MARKER-SPEC.md)
- [ティア設計仕様](./01_knowledge/reference/TIER-DESIGN-SPEC.md)
- [移行マップ](./01_knowledge/reference/MIGRATION-MAP.md)

---

**作成日**: 2025-12-09
**バージョン**: 2.0
