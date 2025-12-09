---
title: "3doca スキーマリファレンス"
description: "全9スキーマの統合リファレンス。フロントマター定義、必須セクション、依存関係、品質基準を一覧化"
document_id: REF-SCH-001
tags: [schema, reference, frontmatter, sections, validation]
category: reference
domain: documentation
difficulty: intermediate
created_at: 2025-12-06
updated_at: 2025-12-06
version: "1.0"
author: claude-code
key_concepts: [スキーマ定義, フロントマター, 必須セクション, 整合性]
related_docs:
  - path: ../templates/README.md
    relationship: references
  - path: ../../02-project-records/TASK-SPECIFICATION.md
    relationship: references
---

# 3doca スキーマリファレンス

## 概要

本ドキュメントは、3docaドキュメントフレームワークの全9スキーマを統合したリファレンスです。

### スキーマ一覧

| スキーマ | ドキュメントタイプ | テンプレート | バージョン |
|---------|------------------|-------------|-----------|
| common.yaml | 共通定義 | - | 2.0 |
| process.yaml | プロセス | 00process-document-template.md | 1.0 |
| playbook.yaml | プレイブック | 01playbook-template.md | 2.0 |
| runbook.yaml | ランブック | 02runbook-template.md | 2.0 |
| troubleshooting.yaml | トラブルシューティング | 03troubleshooting-template.md | 1.0 |
| adr.yaml | ADR | 04adr-template.md | 2.0 |
| cheatsheet.yaml | チートシート | 05cheatsheet-template.md | 2.0 |
| policy.yaml | ポリシー | 06policy-template.md | - |
| sop.yaml | SOP | 07sop-template.md | - |
| cfd-ocean.yaml | CFD/海洋モデリング | 08cfd-ocean-sop-template.md | 1.0 |

---

## 共通フロントマター定義 (common.yaml)

### 必須フィールド

| フィールド | 型 | パターン/値 | 説明 |
|-----------|---|------------|------|
| `document_id` | string | `^[A-Z]{2,4}-[A-Z]{2,4}-\d{3}$` | 一意識別子 |
| `title` | string | 最大150文字 | ドキュメントタイトル |
| `type` | enum | policy, sop, playbook, runbook, cheatsheet, adr, process, troubleshooting, guide, specification | ドキュメントタイプ |
| `version` | string | `^\d+\.\d+(\.\d+)?$` | セマンティックバージョン |
| `status` | enum | draft, review, approved, active, deprecated, superseded | ステータス |
| `owner` | string | `^@[\w-]+$` | 責任チーム |
| `author` | string | - | 作成者名 |
| `created` | date | YYYY-MM-DD | 作成日 |
| `updated` | date | YYYY-MM-DD | 最終更新日 |
| `tags` | array | 最小2項目 | 検索キーワード |
| `key_concepts` | array | 最小1項目 | セマンティックマッチング用語 |
| `summary` | string | 最大200文字 | 一文説明 |
| `domain` | enum | infrastructure, security, data, application, scientific, operations, documentation | ドメイン分類 |
| `audience` | enum | developers, operators, architects, scientists, all | 対象読者 |

### 任意フィールド

| フィールド | 型 | 説明 |
|-----------|---|------|
| `next_review` | date | 次回レビュー予定日 |
| `review_cycle_days` | integer | レビューサイクル日数（デフォルト180） |
| `related_docs` | array | 関連ドキュメント配列 |
| `supersedes` | string | 置き換えるドキュメントID |
| `superseded_by` | string | 置き換えられるドキュメントID |
| `priority` | enum | framework, template, canonical, example, reference, general |
| `is_canonical` | boolean | 基準ドキュメントフラグ |
| `difficulty` | enum | beginner, intermediate, advanced |

### relationship値の定義

| 値 | 説明 | 方向 |
|---|------|------|
| `implements` | 実装する | child → parent |
| `governed-by` | 管理下にある | child → parent |
| `references` | 参照関係 | bidirectional |
| `depends-on` | 前提条件として依存 | child → parent |
| `escalates-to` | エスカレーション先 | child → parent |
| `supersedes` | 置き換える | new → old |
| `superseded-by` | 置き換えられる | old → new |

---

## ドキュメントタイプ別スキーマ

### 1. Process (process.yaml)

**目的**: ワークフロー全体の流れを記述

**必須セクション**:

| セクション | 目的 | 制約 |
|-----------|------|------|
| 概要 | 目的、範囲、対象読者 | 最小50語 |
| プロセスフロー | Mermaid flowchartで可視化 | **Mermaid必須** |
| ステップ詳細 | 各ステップの実行方法 | 最小3サブセクション |
| 品質ゲート | 次ステップへの判断基準 | チェックリスト必須 |

**任意セクション**: 検証とレビュー、成果物、ツールと環境、メトリクス、トラブルシューティング、参考資料、関連ドキュメント

**依存関係**:
```
ステップ詳細 → プロセスフロー
品質ゲート → ステップ詳細
メトリクス → 品質ゲート
```

---

### 2. Playbook (playbook.yaml)

**目的**: 判断を伴う複雑なシナリオへの対応指針

**固有フロントマター**:
- `trigger`: トリガー条件（必須）
- `severity_classification`: 重大度分類
- `escalation`: エスカレーションパス
- `related_runbooks`: 関連ランブック

**必須セクション**:

| セクション | 目的 | 制約 |
|-----------|------|------|
| 概要 | 目的、適用範囲、想定シナリオ | 最小50語 |
| 意思決定フレームワーク | フローチャートまたは決定木 | **Mermaid必須** |
| シナリオ別対応戦略 | 各シナリオの対応手順 | 最小3シナリオ |
| エスカレーション基準 | 報告・エスカレーション条件 | 連絡先・報告フォーマット必須 |

**任意セクション**: 判断支援ツール、事例集、レビューと改善、ツールとリソース、メトリクス、関連ドキュメント

---

### 3. Runbook (runbook.yaml)

**目的**: コピペで実行可能な具体的タスク手順書

**固有フロントマター**:
- `estimated_duration`: 推定所要時間（必須）
- `downtime_required`: ダウンタイム要否（必須）
- `automation`: 自動化メタデータ
- `prerequisites`: 前提条件

**必須セクション**:

| セクション | 目的 | 制約 |
|-----------|------|------|
| 概要 | 目的と実行タイミング | 最小30語 |
| 前提条件 | 権限、ツール、環境要件 | - |
| 事前確認チェックリスト | 実行前確認項目 | **チェックリスト必須** |
| 実行手順 | コピペ可能なコマンド | 最小3サブセクション、**コードブロック必須** |
| 検証チェックリスト | 完了確認項目 | **チェックリスト必須** |
| トラブルシューティング | 問題と解決策 | 最小2ケース |
| ロールバック手順 | 復旧手順 | **コードブロック必須** |

---

### 4. Troubleshooting (troubleshooting.yaml)

**目的**: 問題解決記録と再発防止

**必須セクション**:

| セクション | 目的 | 制約 |
|-----------|------|------|
| 概要 | 問題の概要と影響範囲 | 最小30語 |
| 症状 | 具体的な症状と検出方法 | エラーメッセージ必須 |
| 根本原因 | 原因分析 | - |
| 解決手順 | 具体的な解決手順 | **コードブロック必須** |
| 検証方法 | 解決確認方法 | **チェックリスト必須** |
| 予防策 | 再発防止策 | 短期・長期対策 |

**任意セクション**: 影響分析、タイムライン、教訓と改善点、添付資料、関連情報

---

### 5. ADR (adr.yaml)

**目的**: 技術的選択の理由（Why）を記録（MADR 4.0準拠）

**固有フロントマター**:
- `adr_id`: ADR識別子（必須、`^ADR-\d{4}$`）
- `slug`: URLスラッグ（必須）
- `decision_type`: 決定タイプ（必須）
- `decision_makers`: 決定者リスト
- `related_adrs`: 関連ADRリスト

**必須セクション**:

| セクション | 目的 | 制約 |
|-----------|------|------|
| 背景と課題 | 決定が必要となった背景 | 最小50語 |
| 評価基準 | 選択肢評価基準 | 重み付け必須 |
| 検討した選択肢 | 各選択肢の詳細 | 最小2選択肢 |
| 選択肢比較表 | 評価基準での比較 | **テーブル必須** |
| 決定 | 採用選択肢と理由 | 決定日・決定者必須 |
| 影響 | 決定による影響とトレードオフ | - |

---

### 6. Cheatsheet (cheatsheet.yaml)

**目的**: 情報密度を最大化したクイックリファレンス

**固有フロントマター**:
- `cheatsheet_id`: 識別子（必須、`^CS-[A-Z]{2,4}-\d{3}$`）
- `technology`: 対象技術（必須）
- `format`: フォーマット（single_page, multi_page, interactive）
- `print_optimized`: 印刷最適化フラグ

**必須セクション**:

| セクション | 目的 | 制約 |
|-----------|------|------|
| 最頻出コマンド TOP 5 | 最もよく使う操作 | **テーブル必須**、最大5項目 |
| クイックスタート | すぐに使うための最小手順 | 最大200語 |
| 基本コマンド | 基本操作一覧 | **テーブル必須** |

**任意セクション**: 頻出パターン、設定スニペット、データ解析向け、クイックトラブルシュート、ベストプラクティス、関連リンク、バージョン別の違い、応用例、印刷版

---

### 7. Policy (policy.yaml)

**目的**: 組織の方針とコンプライアンス要件を定義

**固有フロントマター**:
- `classification`: 情報分類（必須）
- `effective_date`: 発効日（必須）
- `review_frequency`: レビュー頻度（必須）
- `approval_signatures`: 承認署名リスト
- `frameworks`: コンプライアンスマッピング

**必須セクション**:

| セクション | 目的 | 制約 |
|-----------|------|------|
| 目的（Purpose） | ポリシーが存在する理由 | 最小50語 |
| 適用範囲（Scope） | 対象の人員・システム・プロセス | リスト必須 |
| 役割と責任 | 責任マトリクス | **テーブル必須** |
| ポリシー声明 | 明確な指令 | 番号付きリスト必須 |
| コンプライアンス要件 | 規制マッピング | - |
| 執行 | 違反時の結果と対応 | - |
| レビュースケジュール | 次回見直し日と頻度 | - |

**スタイル**: フォーマル、能動態、三人称

---

### 8. SOP (sop.yaml)

**目的**: ポリシー要件を再現可能なプロセスに変換

**固有フロントマター**:
- `estimated_duration`: 推定所要時間（必須）
- `roles`: 実行に必要な役割（必須）
- `prerequisites`: 前提条件

**必須セクション**:

| セクション | 目的 | 制約 |
|-----------|------|------|
| 目的 | 何を達成するか | 最大5文 |
| 適用範囲 | 対象システム・プロセス | - |
| 前提条件 | アクセス、ツール、知識要件 | **テーブル必須** |
| 手順 | 番号付きステップ | 各ステップに目的・コマンド・期待出力 |
| 品質メトリクス | 定量的閾値と検証コマンド | **テーブル必須** |
| トラブルシューティング | 問題・原因・解決策 | **テーブル必須** |
| ロールバック手順 | 失敗時の復旧方法 | **コードブロック必須** |

**スタイル**: 指示的、能動態、二人称

---

### 9. CFD/Ocean (cfd-ocean.yaml)

**目的**: CFD/海洋モデリング向けドメイン固有拡張

**固有フロントマター**:
- `validation_cases`: 検証ケース配列
- `verification`: 検証方法（グリッド収束、ソリューション検証）
- `standards`: 準拠する品質標準
- `hpc_requirements`: HPC要件
- `solver_config`: ソルバー設定
- `domain_config`: 計算領域設定

**必須セクション**:

| セクション | 目的 | 制約 |
|-----------|------|------|
| 計算領域と境界条件 | ドメイン、グリッド、境界条件 | - |
| 検証と妥当性確認（V&V） | コード/ソリューション検証 | グリッド収束必須 |
| 不確かさ定量化 | 不確かさ評価 | 入力・数値誤差必須 |
| HPC要件とリソース | 計算リソース要件 | **テーブル必須** |
| コミュニティ標準参照 | 準拠する品質標準 | リスト必須 |

---

## Mermaid設定

### 必須初期化

```
%%{init: {'theme': 'dark'}}%%
```

### 推奨カラー

| 用途 | カラーコード |
|------|------------|
| 完了 (done) | `#4ade80` |
| 進行中 (in_progress) | `#fbbf24` |
| 未着手 (not_started) | `#a78bfa` |
| エラー (error) | `#f87171` |

### ダークモード最適化

```yaml
pieOuterStrokeColor: "#1E1E2E"
pieOuterStrokeWidth: "0.5px"
primaryBorderColor: "#1E1E2E"
lineColor: "#89B4FA"
```

---

## RAGチャンキングガイドライン

| コンテンツタイプ | チャンクサイズ | オーバーラップ | 理由 |
|----------------|--------------|--------------|------|
| 概念説明 | 256-512トークン | 15% | 広いコンテキスト |
| ステップバイステップ | 128-256トークン | 10% | 精密な検索 |
| コード例 | 保持 | N/A | コードブロック分割禁止 |
| APIリファレンス | 256トークン | 10% | 精度とコンテキストのバランス |

---

## 後方互換性マッピング

| レガシーフィールド | 新フィールド |
|------------------|-------------|
| `category` | `type` |
| `created_at` | `created` |
| `updated_at` | `updated` |
| `description` | `summary` |

---

## 参照ドキュメント

- [テンプレートREADME](../templates/README.md)
- [TASK-SPECIFICATION.md](../../02-project-records/TASK-SPECIFICATION.md)
- [9251205claude.md](../9251205claude.md)
