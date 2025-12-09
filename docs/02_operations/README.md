---
title: "02_operations - 運用軸（実行）"
description: "運用ドキュメント階層に基づく実行・運用のためのドキュメント体系"
tags:
  - operations
  - runbook
  - playbook
  - process
category: reference
domain: documentation
difficulty: beginner
created_at: 2025-12-09
updated_at: 2025-12-09
version: "1.0"
author: Claude Code
---

# 02_operations - 運用軸（実行）

運用ドキュメント階層に基づく実行・運用のためのドキュメント体系。

## 運用ドキュメント階層

```
プロセスドキュメント          ← ワークフロー全体の流れ
    ↓
プレイブック                  ← 複雑シナリオの意思決定枠組
    ↓
ランブック                    ← 具体的なタスク実行手順
    ↓
チートシート                  ← 即座参照用の要点集約
```

## サブディレクトリ

### [processes/](./processes/README.md) - プロセス定義（Tier 2）
- **目的**: ワークフロー全体を図示
- **特徴**: 入力・出力を明確に、責任範囲の明記
- **関連**: playbook/runbookへのリンク

### [playbooks/](./playbooks/README.md) - 状況対応（Tier 2）
- **目的**: 複雑シナリオの意思決定枠組
- **特徴**: トリガー条件、判断分岐、エスカレーション基準

### [runbooks/](./runbooks/README.md) - 定常作業（Tier 2）
- **目的**: 具体的なタスク実行手順
- **特徴**: コピー&ペースト可能、ロールバック手順

### [cheatsheets/](./cheatsheets/README.md) - クイックリファレンス（Tier 0/3）
- **目的**: 即座参照用の要点集約
- **特徴**: 1ページ以内、視覚的構成、印刷可能

## ティア対応

| フォルダ | ティア | ビジュアル/テキスト比率 |
|----------|--------|----------------------|
| processes/ | Tier 2 | 40/60 |
| playbooks/ | Tier 2 | 40/60 |
| runbooks/ | Tier 2 | 40/60 |
| cheatsheets/ | Tier 0/3 | 90/10 または 20/80 |

## 関連リンク

- [Diátaxis軸（01_knowledge）](../01_knowledge/README.md)
- [C4軸（03_architecture）](../03_architecture/README.md)
