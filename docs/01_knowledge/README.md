---
title: "01_knowledge - Diátaxis軸（理解・習得）"
description: "Diátaxisフレームワークに基づく知識習得のためのドキュメント体系"
tags:
  - diataxis
  - learning
  - knowledge
  - documentation
category: reference
domain: documentation
difficulty: beginner
created_at: 2025-12-09
updated_at: 2025-12-09
version: "1.0"
author: Claude Code
---

# 01_knowledge - Diátaxis軸（理解・習得）

Diátaxisフレームワークの4タイプに基づく知識習得のためのドキュメント体系。

## Diátaxisフレームワーク

| タイプ | 目的 | 読者の状態 | 対応フォルダ | ティア |
|--------|------|-----------|-------------|-------|
| **説明** | 概念理解の促進 | 「理解しようとしている」 | concepts/ | Tier 4 |
| **チュートリアル** | 学習体験の提供 | 「学んでいる」 | tutorials/ | Tier 1 |
| **ハウツー** | 特定タスクの解決 | 「やろうとしている」 | how-to/ | Tier 2 |
| **リファレンス** | 技術仕様の提供 | 「調べている」 | reference/ | Tier 3 |

## サブディレクトリ

### [concepts/](./concepts/README.md) - 説明（Tier 4）
- **目的**: 「なぜ」「何」に焦点を当てた概念説明
- **ビジュアル/テキスト比率**: 25/75
- **特徴**: 背景・理論・設計意図を説明

### [tutorials/](./tutorials/README.md) - チュートリアル（Tier 1）
- **目的**: 15分以内に初回成功を体験させる
- **ビジュアル/テキスト比率**: 60/40
- **特徴**: 完走可能な手順、各ステップに検証ポイント

### [how-to/](./how-to/README.md) - ハウツー（Tier 2）
- **目的**: 特定タスクの完了方法を提供
- **ビジュアル/テキスト比率**: 40/60
- **特徴**: 前提条件明確、1ドキュメント1タスク

### [reference/](./reference/README.md) - リファレンス（Tier 3）
- **目的**: 包括的なルックアップドキュメント
- **ビジュアル/テキスト比率**: 20/80
- **特徴**: 網羅性重視、検索・スキャン最適化

## 関連リンク

- [運用軸（02_operations）](../02_operations/README.md)
- [C4軸（03_architecture）](../03_architecture/README.md)
- [ティア設計仕様](./reference/TIER-DESIGN-SPEC.md)
