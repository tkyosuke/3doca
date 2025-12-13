---
title: "フロントマター拡張仕様書"
description: "RAG優先度制御とドキュメント品質向上のためのフロントマター拡張フィールド定義"
tags:
  - specification
  - frontmatter
  - rag
  - schema
category: reference
domain: documentation
difficulty: intermediate
priority: framework
is_canonical: true
document_type: specification
created_at: 2025-12-05
updated_at: 2025-12-05
version: "1.0"
author: Claude Code
---

# フロントマター拡張仕様書

## 概要

本仕様書は、RAG検索最適化とドキュメント品質向上を目的としたフロントマター拡張フィールドを定義します。

### 背景

- **DevRAGの制約**: 現時点でDevRAGには優先度制御機能（boost/weight）がない
- **目的**: 将来のRAG拡張に備えつつ、現時点でもドキュメント分類と品質管理に活用
- **互換性**: 既存の必須6フィールドを維持し、新規フィールドを追加

---

## 既存フィールド（必須6項目）

| フィールド | 型 | 必須 | 説明 |
|-----------|-----|------|------|
| `title` | string | **必須** | ドキュメントタイトル（150文字以内） |
| `description` | string | **必須** | 検索用説明（150文字以内、RAGキーワード含む） |
| `tags` | array[string] | **必須** | 分類タグ（1つ目はcategory固定値推奨） |
| `category` | enum | **必須** | `process \| playbook \| runbook \| reference \| concepts` |
| `domain` | enum | **必須** | `data-analysis \| cfd \| gis \| visualization \| documentation` |
| `difficulty` | enum | **必須** | `beginner \| intermediate \| advanced` |

---

## 拡張フィールド（新規追加）

### 1. priority

**目的**: ドキュメントの重要度と参照優先順位を示す

| 属性 | 値 |
|------|-----|
| **型** | enum |
| **必須** | 任意（テンプレート/フレームワークでは必須） |
| **デフォルト** | `general` |

**許容値**:

| 値 | 説明 | 使用シーン |
|----|------|-----------|
| `framework` | フレームワーク基準文書 | POLICY.md、本仕様書 |
| `template` | テンプレートファイル | templates/*.md |
| `canonical` | 基準となる実例 | examples/の模範例 |
| `example` | 一般的な実例 | examples/の通常例 |
| `reference` | 参照用ドキュメント | API仕様、設定リファレンス |
| `general` | 一般ドキュメント | その他すべて |

**RAG活用**:
- 将来のRAG拡張時に`priority: framework`を高いboostで検索
- 現時点では分類・フィルタリング用メタデータとして使用

---

### 2. is_canonical

**目的**: 同種のドキュメントの中で基準となるドキュメントを示す

| 属性 | 値 |
|------|-----|
| **型** | boolean |
| **必須** | 任意 |
| **デフォルト** | `false` |

**使用例**:
- `is_canonical: true` → このドキュメントを参考にして類似ドキュメントを作成すべき
- テンプレートファイルには自動的に`true`を設定

**検証ルール**:
- 同一`document_type`内で`is_canonical: true`は1つのみ推奨
- 複数存在する場合は警告を出力

---

### 3. document_type

**目的**: ドキュメントの種別をより詳細に分類

| 属性 | 値 |
|------|-----|
| **型** | enum |
| **必須** | 任意（スキーマ検証を有効にする場合は必須） |
| **デフォルト** | `guide` |

**許容値**:

| 値 | 説明 | 対応テンプレート |
|----|------|-----------------|
| `process` | プロセスドキュメント | 00process-document-template.md |
| `playbook` | プレイブック | 01playbook-template.md |
| `runbook` | ランブック | 02runbook-template.md |
| `troubleshooting` | トラブルシューティング | 03troubleshooting-template.md |
| `adr` | アーキテクチャ決定記録 | 04adr-template.md |
| `cheatsheet` | チートシート | 05cheatsheet-template.md |
| `specification` | 仕様書 | （本ドキュメント） |
| `guide` | ガイド・説明 | 汎用 |
| `policy` | ポリシー文書 | POLICY.md |

**スキーマ連携**:
- `document_type`に対応するスキーマファイルで必須セクションを検証
- 例: `document_type: playbook` → `schema/playbook.yaml`で検証

---

### 4. section_schema

**目的**: ドキュメント構造を検証するスキーマファイルへの参照

| 属性 | 値 |
|------|-----|
| **型** | string (相対パス) |
| **必須** | 任意 |
| **デフォルト** | `document_type`から自動推定 |

**使用例**:
```yaml
section_schema: schema/playbook.yaml
```

**検証時の動作**:
1. `section_schema`が指定されていればそれを使用
2. 未指定の場合、`document_type`から`schema/{document_type}.yaml`を推定
3. スキーマファイルが存在しない場合はスキップ

---

### 5. related_docs

**目的**: 関連ドキュメントへの参照（グラフ構造構築用）

| 属性 | 値 |
|------|-----|
| **型** | array[string] |
| **必須** | 任意 |
| **デフォルト** | `[]` |

**形式**:
```yaml
related_docs:
  - ../templates/01playbook-template.md
  - ./02-example-runbook.md
```

**検証ルール**:
- 相対パスで指定
- リンク先ファイルの存在確認（警告のみ）

---

### 6. prerequisites

**目的**: 事前に読むべきドキュメントへの参照

| 属性 | 値 |
|------|-----|
| **型** | array[string] |
| **必須** | 任意 |
| **デフォルト** | `[]` |

**使用例**:
```yaml
prerequisites:
  - ../3POLICY.md
  - ./01-basic-process.md
```

**RAG活用**:
- 順序付きの学習パスを構築
- 将来的にはGraphRAGでの関係性検索に活用

---

## 拡張フィールドサマリー

| フィールド | 型 | 必須 | デフォルト | RAG活用 |
|-----------|-----|------|-----------|---------|
| `priority` | enum | 任意 | `general` | 将来のboost用 |
| `is_canonical` | boolean | 任意 | `false` | 基準文書の特定 |
| `document_type` | enum | 任意 | `guide` | スキーマ検証、分類 |
| `section_schema` | string | 任意 | 自動推定 | 構造検証 |
| `related_docs` | array | 任意 | `[]` | グラフ構造 |
| `prerequisites` | array | 任意 | `[]` | 学習パス |

---

## 使用例

### 例1: フレームワークドキュメント（本仕様書）

```yaml
---
title: "フロントマター拡張仕様書"
description: "RAG優先度制御とドキュメント品質向上のためのフロントマター拡張フィールド定義"
tags:
  - specification
  - frontmatter
  - rag
category: reference
domain: documentation
difficulty: intermediate
priority: framework
is_canonical: true
document_type: specification
created_at: 2025-12-05
updated_at: 2025-12-05
version: "1.0"
author: Claude Code
---
```

### 例2: テンプレートファイル

```yaml
---
title: "プレイブックテンプレート"
description: "シナリオ別対応戦略のためのプレイブックテンプレート"
tags:
  - playbook
  - template
  - scenario
category: playbook
domain: operations
difficulty: intermediate
priority: template
is_canonical: true
document_type: playbook
section_schema: schema/playbook.yaml
created_at: 2025-12-05
updated_at: 2025-12-05
version: "1.0"
author: Claude Code
---
```

### 例3: 実例ドキュメント

```yaml
---
title: "異常検知結果判断プレイブック"
description: "データ品質異常検知結果の真偽判断と対応手順"
tags:
  - playbook
  - anomaly-detection
  - data-quality
category: playbook
domain: data-analysis
difficulty: intermediate
priority: example
is_canonical: false
document_type: playbook
related_docs:
  - ../templates/01playbook-template.md
  - ./10-data-quality-process.md
prerequisites:
  - ../3POLICY.md
created_at: 2025-12-05
updated_at: 2025-12-05
version: "1.0"
author: Claude Code
---
```

### 例4: 一般ドキュメント（最小構成）

```yaml
---
title: "クイックスタートガイド"
description: "3docaドキュメントフレームワークの基本的な使い方"
tags:
  - guide
  - quickstart
category: concepts
domain: documentation
difficulty: beginner
created_at: 2025-12-05
updated_at: 2025-12-05
version: "1.0"
author: Claude Code
---
```

*拡張フィールドを省略した場合、デフォルト値が適用されます。*

---

## 検証ルール

### check_frontmatter.py への追加

```python
# 拡張フィールドの検証
PRIORITY_VALUES = ['framework', 'template', 'canonical', 'example', 'reference', 'general']
DOCUMENT_TYPE_VALUES = ['process', 'playbook', 'runbook', 'troubleshooting', 'adr', 'cheatsheet', 'specification', 'guide', 'policy']

def validate_extended_fields(frontmatter):
    errors = []
    warnings = []

    # priority検証
    if 'priority' in frontmatter:
        if frontmatter['priority'] not in PRIORITY_VALUES:
            errors.append(f"Invalid priority: {frontmatter['priority']}")

    # is_canonical検証
    if 'is_canonical' in frontmatter:
        if not isinstance(frontmatter['is_canonical'], bool):
            errors.append("is_canonical must be boolean")

    # document_type検証
    if 'document_type' in frontmatter:
        if frontmatter['document_type'] not in DOCUMENT_TYPE_VALUES:
            errors.append(f"Invalid document_type: {frontmatter['document_type']}")

    # related_docs検証
    if 'related_docs' in frontmatter:
        for doc in frontmatter['related_docs']:
            if not os.path.exists(resolve_path(doc)):
                warnings.append(f"Related doc not found: {doc}")

    return errors, warnings
```

---

## RAG優先度制御への効果

### 現時点（DevRAG）

DevRAGにはboost機能がないため、以下の方法で間接的に優先度を制御:

1. **descriptionの最適化**
   - `priority: framework`のドキュメントはdescriptionに「基準」「標準」「テンプレート」等のキーワードを含める
   - 検索時にこれらのキーワードを含むクエリで優先的にヒット

2. **インデックス順序**
   - フレームワークドキュメントを先にインデックス（未検証だが効果の可能性）

3. **フィルタリング**
   - 検索結果から`priority`フィールドでフィルタリング可能（アプリケーション層で実装）

### 将来のRAG拡張時

RAGシステムがメタデータboostをサポートした場合:

```python
# 想定される検索クエリ
search(
    query="プレイブックの書き方",
    boost={
        "priority": {
            "framework": 2.0,
            "template": 1.5,
            "canonical": 1.2,
            "example": 1.0
        }
    }
)
```

---

## 移行ガイド

### 既存ドキュメントへの適用

1. **必須ではない**: 既存ドキュメントはそのままでも動作
2. **段階的追加**: 重要度の高いドキュメントから順次追加
3. **優先順位**:
   - POLICY.md → `priority: framework`
   - templates/*.md → `priority: template`, `is_canonical: true`
   - examples/の模範例 → `priority: canonical`
   - その他 → 追加不要（デフォルト適用）

### テンプレート更新

各テンプレートのフロントマターセクションに拡張フィールドの説明を追加（次のタスクで実施）。

---

## 関連ドキュメント

- [3POLICY.md](./3POLICY.md) - プロジェクトポリシー（既存フロントマター定義）
- [1USAGE-GUIDE.md](./1USAGE-GUIDE.md) - テンプレート使用ガイド
- [../shrimp-rules.md](../shrimp-rules.md) - AIエージェント用ガイドライン

---

**作成日**: 2025-12-05
**バージョン**: 1.0
**メンテナー**: Claude Code
