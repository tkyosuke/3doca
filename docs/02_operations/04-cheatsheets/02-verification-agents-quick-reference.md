---
title: "検証エージェント早見表"
type: cheatsheet
category: "quality-assurance"
tags: [agents, verification, quick-reference, quality]
summary: "4つの検証エージェントの使い方を1ページにまとめたクイックリファレンス。コマンド、権限、ワークフローを含む。"
keywords:
  - gap-detector
  - fact-checker
  - completeness-checker
  - document-refiner
  - verification agents
related:
  - ./01-gap-markers-quick-reference.md
  - ../../01_knowledge/01-concepts/02-quality-assurance-framework.md
  - ../../_templates/04_agents/README.md
version: "1.0.0"
status: active
created: "2025-12-10"
updated: "2025-12-10"
---

# 検証エージェント早見表

> **Tier 0資料** | 詳細: [品質保証フレームワーク](../../01_knowledge/01-concepts/02-quality-assurance-framework.md) | 関連: [ギャップマーカー早見表](./01-gap-markers-quick-reference.md)

## エージェント一覧

| エージェント | 目的 | 権限 | コマンド |
|-------------|------|------|----------|
| **gap-detector** | ギャップ検出 | read: docs | `/gap-detect` |
| **fact-checker** | ファクト検証 | read: docs+src | `/fact-check` |
| **completeness-checker** | 完全性確認 | read: docs+reports | `/completeness-check` |
| **document-refiner** | ドキュメント改善 | **write: docs** | `/refine` |

> **Note**: `document-refiner` のみがドキュメントを修正可能

## コマンド一覧（コピペ可能）

```bash
# ギャップ検出（単一ファイル）
/gap-detect docs/path/to/file.md

# ギャップ検出（ディレクトリ全体）
/gap-detect docs/01_knowledge/

# ファクトチェック
/fact-check docs/path/to/file.md

# 完全性チェック（ディレクトリ）
/completeness-check docs/

# ドキュメント改善
/refine docs/path/to/file.md

# 言語指定（日本語）
/gap-detect --lang ja docs/file.md

# 言語指定（英語）
/gap-detect --lang en docs/file.md
```

## ワークフロー

```mermaid
%%{init: {'theme': 'dark'}}%%
flowchart LR
    A["作成/更新"] --> B["gap-detector"]
    B --> C["fact-checker"]
    C --> D["refiner"]
    D --> E{"OK?"}
    E -->|No| D
    E -->|Yes| F["完了"]
```

### 用途別の実行順序

| 用途 | 実行順序 |
|------|----------|
| **新規作成** | gap-detector → fact-checker → refiner |
| **既存監査** | gap-detector → fact-checker → completeness-checker |
| **体系監査** | completeness-checker → 計画策定 |
| **クイック確認** | gap-detector のみ |

## 権限モデル

```
┌────────────────────────────────────────────────┐
│  gap-detector        : READ docs              │
│  fact-checker        : READ docs + src        │
│  completeness-checker: READ docs + reports    │
│  document-refiner    : READ all, WRITE docs   │
└────────────────────────────────────────────────┘
```

## レポート出力先

| エージェント | 出力先 |
|-------------|--------|
| gap-detector | `reports/gap-reports/` |
| fact-checker | `reports/fact-check-reports/` |
| completeness-checker | `reports/completeness-reports/` |
| document-refiner | `reports/refine-reports/` |

## 自動実行トリガー

| トリガー | エージェント | 動作 |
|----------|-------------|------|
| docs/ にファイル作成 | gap-detector | 自動実行 |
| docs/ のファイル更新 | gap-detector | 提案のみ |
| reference/**/*.md 更新 | fact-checker | 自動実行 |
| gap-detector 完了後 | document-refiner | 提案のみ |
| 週次（月曜9時） | completeness-checker | 自動実行 |

## トラブル対応

| 症状 | 対処 |
|------|------|
| エージェントが起動しない | `ls -la .claude/agents/` で構造確認 |
| 期待した出力でない | パスが正しいか確認、エージェント名を明示 |
| レポートが生成されない | `reports/` ディレクトリの存在確認 |
| 日本語で出力したい | `--lang ja` オプションを追加 |

## クイックスタート

```bash
# 1. 新規ドキュメントをテンプレートから作成
cp docs/_templates/01_knowledge/01-concept.md docs/01_knowledge/01-concepts/new-doc.md

# 2. 内容を記述（不明点はギャップマーカーを使用）

# 3. ギャップ検出
/gap-detect docs/01_knowledge/01-concepts/new-doc.md

# 4. ファクトチェック
/fact-check docs/01_knowledge/01-concepts/new-doc.md

# 5. 必要に応じて改善
/refine docs/01_knowledge/01-concepts/new-doc.md
```

---

**詳細**: [品質保証フレームワーク](../../01_knowledge/01-concepts/02-quality-assurance-framework.md) | **マーカー**: [ギャップマーカー早見表](./01-gap-markers-quick-reference.md) | **テンプレート**: [エージェント設定](../../_templates/04_agents/README.md)
