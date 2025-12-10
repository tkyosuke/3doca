---
title: "検証エージェントテンプレート"
type: template-index
category: "agents"
tags: [agents, verification, quality-assurance, templates]
summary: |
  ドキュメント検証・改善のための専門サブエージェント群のテンプレート。
  .claude/agents/からコピーされた設定ファイルで、他プロジェクトへの展開に使用。
version: "1.0.0"
status: active
created: "2025-12-10"
updated: "2025-12-10"
---

# 検証エージェントテンプレート

> このディレクトリは `.claude/agents/` のコピーです。
> 隠しフォルダの設定内容を可視化し、テンプレートとして参照可能にしています。

## 概要

本テンプレートは、ドキュメント品質保証のための4つの検証エージェントを定義しています。
これらのエージェントは、ギャップマーカーシステムと連携して、ドキュメントの正確性・完全性を担保します。

## ディレクトリ構成

```
04_agents/
├── README.md                 # このファイル
├── INDEX.md                  # エージェント一覧と使用方法
├── gap-detector/             # ギャップ検出エージェント
│   ├── agent.ja.md          # 日本語版
│   └── agent.en.md          # English version
├── fact-checker/             # ファクト検証エージェント
│   ├── agent.ja.md
│   └── agent.en.md
├── completeness-checker/     # 完全性確認エージェント
│   ├── agent.ja.md
│   └── agent.en.md
└── document-refiner/         # ドキュメント改善エージェント
    ├── agent.ja.md
    └── agent.en.md
```

## エージェント一覧

| エージェント | 目的 | 権限 |
|-------------|------|------|
| **gap-detector** | ギャップ検出 | read: docs, write: reports |
| **fact-checker** | ファクト検証 | read: docs+src, write: reports |
| **completeness-checker** | 完全性確認 | read: docs+reports, write: reports |
| **document-refiner** | ドキュメント改善 | read: all, **write: docs**, write: reports |

> **Note**: `document-refiner` のみがソースドキュメントを修正可能です。

## 使用方法

### 新規プロジェクトへの展開

1. このディレクトリの内容を新規プロジェクトの `.claude/agents/` にコピー
2. 必要に応じてエージェント定義をカスタマイズ
3. `reports/` ディレクトリを作成（エージェント出力先）

```bash
# コピー例
cp -r docs/_templates/04_agents/* /path/to/new-project/.claude/agents/
mkdir -p /path/to/new-project/reports/{gap-reports,fact-check-reports,completeness-reports,refine-reports}
```

### カスタマイズのポイント

- **言語選択**: `.ja.md`（日本語）または `.en.md`（英語）を選択
- **権限調整**: 各エージェントの権限（read/write対象）をプロジェクトに合わせて調整
- **トリガー条件**: Auto-execution Hooksのトリガー条件をカスタマイズ

## 関連ドキュメント

- [INDEX.md](./INDEX.md) - エージェント詳細と推奨ワークフロー
- [品質保証フレームワーク](../../01_knowledge/01-concepts/02-quality-assurance-framework.md) - 概念説明
- [ギャップマーカー仕様](../../01_knowledge/04-reference/01-GAP-MARKER-SPEC.md) - マーカー仕様

## 元ファイルとの関係

| 項目 | 説明 |
|------|------|
| **元ファイル** | `.claude/agents/` |
| **同期方針** | 手動同期（変更時にコピー） |
| **優先** | 元ファイル（`.claude/agents/`）が正 |

元ファイルを更新した場合は、このテンプレートも更新してください。

---

**作成日**: 2025-12-10 | **元ファイル**: `.claude/agents/`
