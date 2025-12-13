# 技術ドキュメント体系 - テンプレート＆実例集

## プロジェクト概要

このディレクトリは、**Diátaxisフレームワーク**と**運用系ドキュメント階層**に基づいた技術ドキュメント体系のテンプレート・実例を提供します。

データ解析ドメインを対象とし、RAG（Retrieval-Augmented Generation）対応のフロントマター標準化、Mermaidダイアグラム活用、重要箇所の明示を徹底しています。

### 🚀 使用ガイド

**📖 [USAGE-GUIDE.md](./1USAGE-GUIDE.md)** - テンプレート使用ガイド（優先度: ★★★★★）

**5-10分で読了**できる実用的なガイド：
- クイックスタート（3ステップで即開始）
- カスタマイズ手順（フォルダ番号、ファイル名、フロントマッター）
- フロントマター必須項目（RAG対応の最小要件）
- よくある落とし穴（10項目、問題・影響・対策）
- 品質チェックリスト（完成前の確認項目）

### 📦 移行ガイド

**🔄 [MIGRATION.md](./2MIGRATION.md)** - 別プロジェクトへの移行手順（優先度: ★★★★）

**3ステップで移行完了**できる実用的なガイド：
- クイックスタート（rsyncコピー、カスタマイズ、検証）
- 詳細手順（Git履歴保持、フォルダ番号変更、domain変更、examples差し替え）
- トラブルシューティング（リンク切れ、フロントマッター不適合、Git競合）

### ポリシー文書

**📚 [POLICY.md](./3POLICY.md)** - プロジェクト全体のドキュメンテーション方針

このプロジェクトの設計原則、命名規則、品質基準、可視化方針、更新・拡張方針を定義した重要なドキュメントです。

### セクション間依存関係マップ

**🗺️ [SECTION-DEPENDENCY-MAP.md](./5SECTION-DEPENDENCY-MAP.md)** - セクション間依存関係の可視化（優先度: ★★★★）

8ドキュメントタイプのセクション間依存関係をMermaid図で可視化：
- ドキュメントタイプ間の関係（Policy → SOP → Runbook 等）
- 各タイプ内のセクション依存関係
- ドキュメント作成推奨順序

### フロントマター拡張仕様

**📋 [FRONTMATTER-EXTENSION-SPEC.md](./4FRONTMATTER-EXTENSION-SPEC.md)** - RAG優先度制御のための拡張仕様（優先度: ★★★★）

RAG検索最適化とドキュメント品質向上のための拡張フィールド定義：
- `priority`: ドキュメントの重要度（framework/template/canonical/example/reference/general）
- `is_canonical`: 基準ドキュメントフラグ
- `document_type`: 詳細なドキュメント種別
- `section_schema`: スキーマ検証ファイルへの参照

### DevRAGインデックス最適化

**🔍 [DEVRAG-OPTIMIZATION-GUIDE.md](./6DEVRAG-OPTIMIZATION-GUIDE.md)** - DevRAG設定最適化ガイド（優先度: ★★★）

3docaドキュメントをDevRAGに最適にインデックスするためのガイド：
- DevRAG制約事項（優先度制御なし）と対応戦略
- インデックス設定手順（コピー→インデックス追加）
- ドキュメント構造最適化（タイトル、description、キーワード密度）
- 検索クエリ最適化（日英混合、同義語展開）

### CI/CDパイプライン

**🔄 [CI-CD-GUIDE.md](./7CI-CD-GUIDE.md)** - GitHub Actions品質検証パイプライン（優先度: ★★★）

ドキュメント品質を自動検証するCI/CD設定ガイド：
- 5つの検証ジョブ（markdownlint、Vale、lychee、frontmatter、sections）
- ローカル実行方法とトラブルシューティング
- カスタムValeルール（3doca専用）

### 陳腐化検出仕様

**📅 [STALENESS-DETECTION-SPEC.md](./8STALENESS-DETECTION-SPEC.md)** - ドキュメント陳腐化検出仕様（優先度: ★★★）

ドキュメントの陳腐化を検出・通知する仕組み：
- フロントマターフィールド（next_review、review_cycle_days、owner）
- 検出ロジック（4段階レベル：CRITICAL/HIGH/MEDIUM/LOW）
- GitHub Actions週次ジョブ（Issue自動作成）

### Diátaxisフレームワーク

| タイプ | 目的 | 想定読者の状態 |
|--------|------|---------------|
| **チュートリアル** | 学習体験の提供 | 「学んでいる」 |
| **ハウツーガイド** | 特定タスクの解決 | 「やろうとしている」 |
| **リファレンス** | 技術仕様の提供 | 「調べている」 |
| **説明** | 概念理解の促進 | 「理解しようとしている」 |

### 運用系ドキュメント階層

```
┌─────────────────────────────────────────┐
│ ポリシー（原則・方針）                    │
├─────────────────────────────────────────┤
│ プレイブック（状況対応指針）              │
├─────────────────────────────────────────┤
│ プロセスドキュメント（ワークフロー）       │
├─────────────────────────────────────────┤
│ ランブック（運用手順書）                  │
├─────────────────────────────────────────┤
│ チートシート（早見表）                    │
└─────────────────────────────────────────┘
```

## ディレクトリ構成

```
tmp2/
├── README.md                              # このファイル
├── 251129claude.md                        # 元ファイル（技術ドキュメント体系構築ガイド）
├── templates/                             # ドキュメントテンプレート
│   ├── README.md
│   ├── 00-process-document-template.md    # プロセスドキュメント
│   ├── 01-playbook-template.md            # プレイブック
│   ├── 02-runbook-template.md             # ランブック
│   ├── 03-troubleshooting-template.md     # トラブルシューティング
│   ├── 04-adr-template.md                 # ADR
│   └── 05-cheatsheet-template.md          # チートシート
└── examples/                              # 実例（データ解析ドメイン）
    ├── README.md
    ├── 00-data-analysis-process.md        # プロセス: 一般データ解析
    ├── 01-data-quality-analysis-process.md # プロセス: 品質分析
    ├── 10-data-quality-issues-playbook.md  # プレイブック: 品質問題対応
    ├── 11-anomaly-detection-playbook.md    # プレイブック: 異常検知判断
    ├── 20-data-cleansing-runbook.md        # ランブック: クレンジング
    └── 30-anti-patterns-data-analysis.md   # リファレンス: 禁則事項
```

## ファイル命名規則

### 番号体系の説明

このディレクトリでは、体系的な番号付けにより、ファイルの発見可能性とメンテナンス性を向上させています。

#### templates/ディレクトリの番号体系

**形式**: `NN-template-name.md`（00-05、機能順）

| 番号 | テンプレートタイプ | 説明 |
|-----|------------------|------|
| 00 | プロセスドキュメント | ワークフロー全体の流れ |
| 01 | プレイブック | 判断を伴う複雑なシナリオへの対応指針 |
| 02 | ランブック | 具体的なタスク実行手順書 |
| 03 | トラブルシューティング | 問題解決記録と再発防止 |
| 04 | ADR | 技術決定の記録と理由の文書化 |
| 05 | チートシート | 即座参照用の要点集約 |

#### examples/ディレクトリの番号体系

**形式**: `NN-example-name.md`（テンプレートタイプ別）

| 番号範囲 | ドキュメントタイプ | 説明 |
|---------|------------------|------|
| 0x | プロセスドキュメント | ワークフロー実例（例：00, 01） |
| 1x | プレイブック | 判断支援実例（例：10, 11） |
| 2x | ランブック | 手順書実例（例：20） |
| 3x | リファレンス | 禁則事項・仕様実例（例：30） |

**欠番の扱い**: 将来の拡張余地として、欠番（例：02-09、12-19）は許容されます。新規ファイル追加時は適切な番号範囲を選択してください。

**命名規則の継承**: この番号体系は、プロジェクト全体のドキュメント管理原則（`docs/00-project-meta/`等）と一貫性を保っています。

### `templates/` ディレクトリの役割

**📚 詳細**: [templates/README.md](./templates/README.md) - 全テンプレートへのリンクと使い分けガイド

再利用可能なドキュメントテンプレートを格納します。各テンプレートには：

- **RAG対応フロントマター** - title, description, tags, category等の必須フィールド
- **セクション構造** - 各ドキュメントタイプに適した標準構造
- **重要箇所マーク** - `**[重要]**`, ⚠️, `<!-- TEMPLATE: ... -->`コメント
- **Mermaidダイアグラム例** - フローチャート、意思決定ツリー等

### `examples/` ディレクトリの役割

**📚 詳細**: [examples/README.md](./examples/README.md) - 全実例へのリンクと活用方法

データ解析ドメインの実例を格納します。テンプレートをコピーして具体化した内容で、実際のプロジェクトで参考にできます。

### 元ファイルと採用レポート

**📊 [adoption-report.md](./4adoption-report.md)** - 元ファイル採用箇所レポート（優先度: ★★★）

元ファイル（251129claude.md）からの採用状況を可視化した詳細レポート：
- 🟢 完全反映 / 🟡 部分反映 / ⚪ 未反映の色分け
- セクション別反映率の統計表
- テンプレート・実例への具体的な落とし込み箇所

## 使用方法

### 1. テンプレートの選択

`templates/README.md` を参照し、作成したいドキュメントタイプに合ったテンプレートを選択します。

### 2. テンプレートのコピー

```bash
cp templates/process-document-template.md your-project/docs/your-process.md
```

### 3. カスタマイズ

- `<!-- TEMPLATE: ... -->` コメント部分を具体的な内容に置き換え
- フロントマターの各フィールドを埋める
- Mermaidダイアグラムを実際のワークフローに合わせて調整
- 重要箇所マーク（**[重要]**, ⚠️）はそのまま活用

### 4. 実例の参照

`examples/` ディレクトリの実例を参照し、具体的な記述方法を学習できます。

## RAG対応フロントマター標準

全てのテンプレート・実例は以下のYAMLフロントマターを標準化しています：

```yaml
---
# 必須フィールド
title: "ドキュメントタイトル"
description: "150文字以内の検索用説明"

# 分類（RAGフィルタリング用）
tags:
  - tag1
  - tag2
category: process | playbook | runbook | reference | concepts
domain: data-analysis | cfd | gis | visualization
difficulty: beginner | intermediate | advanced

# 関連性（グラフ構造用）
related_docs:
  - path/to/related-doc
prerequisites:
  - path/to/prerequisite-doc

# メタデータ
created_at: YYYY-MM-DD
updated_at: YYYY-MM-DD
version: "1.0"
author: your-name
---
```

このフロントマターは将来的なPostgreSQL/pgvector統合を見据えた設計です。

## 重要な原則

1. **1文書1概念** - 各ドキュメントは単一の主題を扱う
2. **自己完結型セクション** - 各見出し配下が独立して意味を持つ
3. **代名詞の回避** - 「それ」「この」を避け、具体的な用語を繰り返す
4. **キーワードの前置** - 重要な概念は段落・文の冒頭に配置
5. **チャンクサイズ最適化** - セクションは250〜512トークン（約1000〜2000文字）を目安に

## 参考資料

### 元ファイル

`251129claude.md` - 技術ドキュメント体系構築ガイド（完全版）

このファイルには以下の詳細情報が含まれています：

- Diátaxisフレームワークの詳細
- ファイル構造とRAG対応設計
- Mermaidダイアグラムの効果的活用
- ADRとトラブルシューティング記録
- AIエージェント活用のベストプラクティス
- 段階的導入ロードマップ
- PostgreSQL/pgvector統合設計

### 追加リソース

- [Diátaxis公式サイト](https://diataxis.fr/)
- [MADR（Markdown Architectural Decision Records）](https://adr.github.io/madr/)
- [Mermaid公式ドキュメント](https://mermaid.js.org/)

## ライセンスとクレジット

このテンプレート集は、Diátaxisフレームワーク（Daniele Procida）と業界標準のベストプラクティスに基づいて作成されています。

---

**作成日**: 2025-11-29
**バージョン**: 1.0
**メンテナー**: Claude Code (Shrimp Task Manager)
