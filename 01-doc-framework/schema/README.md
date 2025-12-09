# ドキュメントスキーマ定義 v2.0

このディレクトリには、各ドキュメントタイプの構造定義（スキーマ）が格納されています。

**基準文書**: [9251205claude.md](../9251205claude.md) - AIエージェントによる技術ドキュメント作成フレームワーク

## 目的

- **統一フロントマター**: document_id, key_concepts, related_docs(relationship付き)による一貫した識別
- **必須/任意セクションの明確化**: エージェントがドキュメント生成時に参照
- **セクション間依存関係の定義**: 整合性のあるドキュメント構造を保証
- **GraphRAG対応**: related_docs配列による明示的なグラフエッジ作成
- **検証機構の基盤**: check_frontmatter.pyによる自動検証

## スキーマファイル一覧

| ファイル | ドキュメントタイプ | 対応テンプレート | 基準セクション |
|----------|-------------------|-----------------|---------------|
| `common.yaml` | 共通定義 | （全テンプレート共通） | セクション1 |
| `policy.yaml` | ポリシー | 06policy-template.md | セクション2.1 |
| `sop.yaml` | 標準作業手順書 | 07sop-template.md | セクション2.2 |
| `playbook.yaml` | プレイブック | 01playbook-template.md | セクション2.3 |
| `runbook.yaml` | ランブック | 02runbook-template.md | セクション2.4 |
| `cheatsheet.yaml` | チートシート | 05cheatsheet-template.md | セクション2.5 |
| `adr.yaml` | ADR | 04adr-template.md | セクション2.6 |
| `process.yaml` | プロセス | 00process-document-template.md | - |
| `troubleshooting.yaml` | トラブルシューティング | 03troubleshooting-template.md | - |

## 統一フロントマタースキーマ

すべてのドキュメントは共通のフロントマター構造を共有します（`common.yaml`で定義）：

### 必須フィールド

```yaml
---
# === 識別情報 ===
document_id: "TYPE-DOMAIN-NNN"   # 一意識別子（例: RUN-DB-001）
title: "人間が読めるタイトル"
type: policy | sop | playbook | runbook | cheatsheet | adr
version: "1.0.0"                  # セマンティックバージョニング
status: draft | review | approved | active | deprecated | superseded

# === 所有権 ===
owner: "@team-name"               # 責任チーム
author: "作成者名"
created: 2024-01-15
updated: 2024-12-01

# === RAG最適化 ===
tags: [database, postgresql, backup]
key_concepts:                     # セマンティックマッチング用語
  - "災害復旧"
  - "データ保護"
summary: "検索結果用の一文説明"

# === ドメインコンテキスト ===
domain: infrastructure | security | data | application | scientific
audience: developers | operators | architects | scientists
---
```

### 任意フィールド（GraphRAG対応）

```yaml
# === 関連ドキュメント（グラフエッジ） ===
related_docs:
  - path: "/adr/0042-postgresql.md"
    relationship: "implements"    # 7種類から選択
  - path: "/runbooks/db-backup.md"
    relationship: "references"

# === メンテナンス ===
next_review: 2025-06-01
review_cycle_days: 180
```

## relationship値の標準定義

| 値 | 意味 | 使用例 |
|----|------|--------|
| `implements` | このドキュメントがそのドキュメントを実装 | ランブック → ADR |
| `governed-by` | このドキュメントがそのドキュメントの管理下 | SOP → ポリシー |
| `references` | 単純な参照関係 | プレイブック → ランブック |
| `depends-on` | 前提条件として依存 | ランブックA → ランブックB |
| `escalates-to` | 失敗時のエスカレーション先 | ランブック → プレイブック |
| `supersedes` | このドキュメントが置き換える | 新ADR → 旧ADR |
| `superseded-by` | このドキュメントを置き換えるもの | 旧ADR → 新ADR |

## スキーマ構造

各スキーマファイルは以下の構造を持ちます：

```yaml
# 基準参照
extends: common.yaml
document_type: playbook
version: "2.0"
description: "スキーマの説明"

# ドキュメントタイプ固有フロントマター
frontmatter:
  required:
    - name: trigger
      type: object
      properties: ...
  optional:
    - name: severity_classification
      type: object

# セクション定義
sections:
  required:
    - name: "トリガー条件"
      description: "いつこのプレイブックを使用するか"
      order: 1
      validation:
        must_contain_table: true
  optional:
    - name: "コミュニケーションテンプレート"

# セクション間依存関係
dependencies:
  - if: "シナリオ別対応戦略"
    then: "意思決定フレームワーク"
    reason: "シナリオは意思決定フローの分岐先として定義される"

# 制約条件
constraints:
  - type: "mermaid_required"
    sections: ["意思決定フレームワーク"]

# 品質基準
quality_criteria:
  - "各シナリオが相互排他的かつ網羅的（MECE）"
```

## 使用方法

### 1. エージェントによるドキュメント生成時

```python
# スキーマを読み込んで必須セクションを確認
schema = load_schema("playbook.yaml")
required_sections = schema["sections"]["required"]
frontmatter_fields = schema["frontmatter"]["required"]
```

### 2. 検証スクリプトでの使用

```bash
# フロントマターとセクション構造を検証
python check_frontmatter.py --schema schema/playbook.yaml examples/10-*.md

# JSON形式で出力（CI/CD用）
python check_frontmatter.py --format json examples/
```

### 3. 後方互換性

既存のドキュメントは`backward_compatibility`マッピングにより自動変換されます：

- `category` → `type`
- `created_at` → `created`
- `updated_at` → `updated`
- `description` → `summary`

## 関連ドキュメント

- [9251205claude.md](../9251205claude.md) - AIエージェントによる技術ドキュメント作成フレームワーク（基準文書）
- [4FRONTMATTER-EXTENSION-SPEC.md](../4FRONTMATTER-EXTENSION-SPEC.md) - フロントマター拡張仕様
- [3POLICY.md](../3POLICY.md) - プロジェクトポリシー
- [1USAGE-GUIDE.md](../1USAGE-GUIDE.md) - テンプレート使用ガイド

---

**バージョン**: 2.0
**更新日**: 2025-12-05
**基準**: 9251205claude.md
