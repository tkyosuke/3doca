---
title: "フロントマターリファレンス"
type: reference
category: "documentation"
tags: [frontmatter, yaml, metadata, specification]
audience: advanced
summary: |
  3docaフレームワークで使用するYAMLフロントマターの完全仕様です。
  全フィールドの定義、型、必須/任意の別、使用例、検証方法を提供します。
keywords:
  - frontmatter
  - YAML
  - metadata
  - フロントマター
  - メタデータ
  - 仕様
  - specification
related:
  - ./01-GAP-MARKER-SPEC.md
  - ./02-TIER-DESIGN-SPEC.md
  - ../03-how-to/01-template-usage-guide.md
applies_to: "3doca v1.0.0+"
version: "1.0.0"
status: published
created: "2025-12-10"
updated: "2025-12-10"
---

# フロントマターリファレンス

> **対象バージョン**: 3doca v1.0.0+
> **最終確認日**: 2025-12-10

## 概要

3docaフレームワークでは、Markdown文書の冒頭にYAML形式のフロントマター（メタデータ）を配置します。これにより、ドキュメントの検索性、分類、RAG最適化を実現します。

### フロントマターの役割

1. **検索最適化**: devrag/RAGツールによる検索精度向上
2. **分類管理**: タイプ、カテゴリ、タグによる体系的整理
3. **ドキュメント間連携**: related/prerequisitesによる関連付け
4. **メタ情報管理**: バージョン、ステータス、更新日の追跡
5. **認知負荷軽減**: summaryによる概要把握

## クイックリファレンス

### 最小構成（全ドキュメント共通）

```yaml
---
title: "ドキュメントタイトル"
type: concept | tutorial | how-to | reference | process | playbook | runbook | cheatsheet | architecture
category: "カテゴリ名"
tags: [tag1, tag2, tag3]
summary: |
  2-3文の簡潔な要約。
  このドキュメントで何ができるか/何が書かれているか。
version: "1.0.0"
status: draft | review | published
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
---
```

### タイプ別追加フィールド早見表

| type | 追加フィールド |
|------|--------------|
| `tutorial` | `estimated_time`, `difficulty`, `prerequisites` |
| `how-to` | `prerequisites`, `audience` |
| `playbook` | `severity`, `triggers`, `owner`, `last_tested` |
| `runbook` | `frequency`, `estimated_time`, `owner`, `executor` |
| `process` | `owner`, `stakeholders`, `triggers`, `frequency` |
| `reference` | `applies_to`, `audience` |
| `architecture` | `level`, `parent_container` |

## 共通フィールド詳細

### title

| 項目 | 値 |
|------|-----|
| **型** | String |
| **必須** | Yes |
| **説明** | ドキュメントのタイトル。検索結果・目次に表示される |
| **推奨形式** | 簡潔で具体的（50文字以内） |

**使用例**:
```yaml
# 良い例
title: "iRICでメッシュを生成する方法"
title: "ギャップマーカー仕様書"

# 悪い例（抽象的すぎる）
title: "メッシュについて"
title: "仕様"
```

### type

| 項目 | 値 |
|------|-----|
| **型** | Enum（列挙型） |
| **必須** | Yes |
| **説明** | ドキュメントタイプ（Diátaxis/運用/C4軸に対応） |
| **許可値** | 下記「typeフィールド一覧」参照 |

#### typeフィールド一覧

**Diátaxis軸（`docs/01_knowledge/`）**:

| 値 | 説明 | ティア | 配置先 |
|----|------|-------|--------|
| `concept` | 説明・概念 | Tier 4 | `01-concepts/` |
| `tutorial` | チュートリアル | Tier 1 | `02-tutorials/` |
| `how-to` | ハウツーガイド | Tier 2 | `03-how-to/` |
| `reference` | リファレンス | Tier 3 | `04-reference/` |

**運用軸（`docs/02_operations/`）**:

| 値 | 説明 | ティア | 配置先 |
|----|------|-------|--------|
| `process` | プロセス定義 | Tier 2 | `processes/` |
| `playbook` | プレイブック | Tier 2 | `playbooks/` |
| `runbook` | ランブック | Tier 2 | `runbooks/` |
| `cheatsheet` | チートシート | Tier 0/3 | `cheatsheets/` |

**C4軸（`docs/03_architecture/`）**:

| 値 | 説明 | ティア | 配置先 |
|----|------|-------|--------|
| `architecture` | アーキテクチャ | Tier 0/4 | `context/`, `containers/`, `components/` |

**使用例**:
```yaml
type: how-to      # ハウツーガイド
type: reference   # リファレンス
type: playbook    # プレイブック
```

### category

| 項目 | 値 |
|------|-----|
| **型** | String |
| **必須** | Yes |
| **説明** | ドキュメントのカテゴリ分類 |
| **推奨値** | プロジェクト固有（例: simulation, gis, data-processing） |

**使用例**:
```yaml
# CFDプロジェクトの例
category: "simulation"
category: "mesh-generation"
category: "post-processing"

# GISプロジェクトの例
category: "spatial-analysis"
category: "data-import"

# 汎用
category: "documentation"
category: "development"
```

[NEEDS_VERIFICATION: プロジェクト標準カテゴリリストの確定が必要]

### tags

| 項目 | 値 |
|------|-----|
| **型** | Array of Strings |
| **必須** | Yes（空配列でも可） |
| **説明** | フィルタリング・分類用のタグ |
| **推奨数** | 3-7個 |

**使用例**:
```yaml
# 良い例（適度な粒度）
tags: [mesh, iric, nays2dflood, cfd]

# 悪い例（多すぎる）
tags: [mesh, grid, iric, nays2dflood, cfd, simulation, river, flood, 2d, numerical]

# 悪い例（少なすぎる）
tags: [simulation]
```

**tagsとkeywordsの使い分け**:

| フィールド | 用途 | 例 |
|-----------|------|-----|
| `tags` | カテゴリ分類、フィルタリング | `[mesh, iric, cfd]` |
| `keywords` | 全文検索、類似検索、同義語 | `[メッシュ, 格子, grid, mesh generation]` |

### summary

| 項目 | 値 |
|------|-----|
| **型** | String（複数行） |
| **必須** | Yes |
| **説明** | RAG検索用の要約（2-3文） |
| **推奨形式** | パイプ記法（`|`）で複数行 |

**書き方のポイント**:
- 2-3文で具体的に
- 何ができるようになるか / 何が書かれているかを明記
- 検索されそうなキーワードを含める

**使用例**:
```yaml
# 良い例（具体的）
summary: |
  iRIC Nays2DFloodでメッシュを生成する手順を説明します。
  河川形状データから計算用メッシュを作成し、品質検証まで行います。

# 悪い例（抽象的）
summary: "メッシュ生成について説明します。"

# 悪い例（長すぎる）
summary: |
  このドキュメントは、iRIC Nays2DFloodソフトウェアを使用して、
  河川形状データからメッシュを生成する詳細な手順を提供します。
  まず、データの準備から始め、次にメッシュ生成設定を行い、
  最後に品質検証を実施します。（5文以上は長すぎる）
```

### keywords

| 項目 | 値 |
|------|-----|
| **型** | Array of Strings |
| **必須** | No（推奨） |
| **説明** | 検索用キーワード（同義語・別名含む） |
| **推奨数** | 5-10個 |

**使用例**:
```yaml
keywords:
  - メッシュ生成
  - 格子生成
  - mesh generation
  - grid generation
  - iRIC
  - Nays2DFlood
  - 河川シミュレーション
  - CFD
```

**多言語対応の考慮**:
```yaml
keywords:
  - 境界条件        # 日本語
  - boundary condition  # 英語
  - 边界条件        # 中国語（必要に応じて）
```

### related

| 項目 | 値 |
|------|-----|
| **型** | Array of Strings（相対パス） |
| **必須** | No（推奨） |
| **説明** | 関連ドキュメントへのパス |

**使用例**:
```yaml
related:
  - ./mesh-parameters-reference.md         # 同じフォルダ
  - ../02-tutorials/iric-quickstart.md     # 親フォルダ経由
  - ../../02_operations/02-playbooks/mesh-troubleshooting.md  # 別軸
```

**パス記法のルール**:
- 相対パスを使用（`.`から始める）
- ファイル名まで明記（`.md`拡張子含む）
- 存在しないパスは`[LINK_NEEDED:]`マーカーで明示

```yaml
# 未作成ドキュメントへの参照
related:
  - [LINK_NEEDED: メッシュパラメータリファレンスへのリンク]
```

### version

| 項目 | 値 |
|------|-----|
| **型** | String（セマンティックバージョニング） |
| **必須** | Yes |
| **説明** | ドキュメントのバージョン |
| **形式** | `MAJOR.MINOR.PATCH` |

**バージョン付け規則**:
- `1.0.0`: 初版公開
- `1.1.0`: 新セクション追加（MINOR更新）
- `1.0.1`: 誤字修正、軽微な改善（PATCH更新）
- `2.0.0`: 構造変更、非互換変更（MAJOR更新）

**使用例**:
```yaml
version: "1.0.0"   # 初版
version: "1.2.3"   # セカンドマイナー、サードパッチ
```

### status

| 項目 | 値 |
|------|-----|
| **型** | Enum |
| **必須** | Yes |
| **説明** | ドキュメントのステータス |
| **許可値** | `draft`, `review`, `published` |

**ステータス定義**:

| 値 | 説明 | ギャップマーカー許容度 |
|----|------|---------------------|
| `draft` | 草稿（作成中） | HIGH/MEDIUM多数OK |
| `review` | レビュー中 | HIGHは解消、MEDIUM残OK |
| `published` | 公開済み | HIGHは0、MEDIUM最小限 |

**使用例**:
```yaml
status: draft      # 作成中
status: review     # レビュー依頼中
status: published  # 正式公開
```

### created / updated

| 項目 | 値 |
|------|-----|
| **型** | String（ISO 8601日付） |
| **必須** | Yes |
| **説明** | 作成日/最終更新日 |
| **形式** | `YYYY-MM-DD` |

**使用例**:
```yaml
created: "2025-12-10"
updated: "2025-12-10"

# 更新後
created: "2025-12-10"
updated: "2025-12-15"
```

**更新日の変更タイミング**:
- 誤字修正: 更新しない
- セクション追加: 更新する
- コード例修正: 更新する

[ASSUMPTION: 軽微な修正（誤字・リンク修正）は更新日を変えない方針]

## タイプ別追加フィールド

### tutorial

チュートリアル（`type: tutorial`）で使用する追加フィールド。

#### estimated_time

| 項目 | 値 |
|------|-----|
| **型** | String |
| **必須** | Yes（tutorialの場合） |
| **説明** | 所要時間の目安 |
| **推奨形式** | `XX分` または `X時間` |

**使用例**:
```yaml
estimated_time: "15分"
estimated_time: "1時間30分"
```

**Tier 1目標**: 15分以内で完了できる内容を推奨。

#### difficulty

| 項目 | 値 |
|------|-----|
| **型** | Enum |
| **必須** | Yes（tutorialの場合） |
| **説明** | 難易度レベル |
| **許可値** | `beginner`, `intermediate`, `advanced` |

**使用例**:
```yaml
difficulty: beginner      # 初心者向け
difficulty: intermediate  # 中級者向け
difficulty: advanced      # 上級者向け
```

#### prerequisites（tutorial）

| 項目 | 値 |
|------|-----|
| **型** | Array of Strings |
| **必須** | No（推奨） |
| **説明** | 前提となるチュートリアル/ドキュメント |

**使用例**:
```yaml
prerequisites:
  - ../02-tutorials/getting-started.md
  - ./iric-installation.md
```

### how-to

ハウツーガイド（`type: how-to`）で使用する追加フィールド。

#### audience

| 項目 | 値 |
|------|-----|
| **型** | Enum |
| **必須** | No（推奨） |
| **説明** | 対象読者レベル |
| **許可値** | `beginner`, `intermediate`, `advanced` |

**使用例**:
```yaml
audience: intermediate
```

#### prerequisites（how-to）

tutorialと同様。特定タスク実行前の前提条件を明記。

### playbook

プレイブック（`type: playbook`）で使用する追加フィールド。

#### severity

| 項目 | 値 |
|------|-----|
| **型** | Enum |
| **必須** | Yes（playbookの場合） |
| **説明** | 重要度/緊急度 |
| **許可値** | `high`, `medium`, `low` |

**使用例**:
```yaml
severity: high    # 緊急対応必要
severity: medium  # 通常対応
severity: low     # 参考情報
```

#### triggers

| 項目 | 値 |
|------|-----|
| **型** | Array of Strings |
| **必須** | Yes（playbookの場合） |
| **説明** | プレイブック起動条件 |

**使用例**:
```yaml
triggers:
  - "シミュレーションが収束しない"
  - "計算結果が物理的に不合理"
  - "実行時間が異常に長い"
```

#### owner

| 項目 | 値 |
|------|-----|
| **型** | String |
| **必須** | Yes（playbook/runbook/processの場合） |
| **説明** | 責任者/担当チーム |

**使用例**:
```yaml
owner: "CFDチーム"
owner: "田中太郎"
owner: "データ分析グループ"
```

#### last_tested

| 項目 | 値 |
|------|-----|
| **型** | String（ISO 8601日付） |
| **必須** | No（推奨） |
| **説明** | プレイブックを最後にテストした日 |

**使用例**:
```yaml
last_tested: "2025-12-10"
```

**更新タイミング**: 実際にプレイブックを実行して検証した日に更新。

### runbook

ランブック（`type: runbook`）で使用する追加フィールド。

#### frequency

| 項目 | 値 |
|------|-----|
| **型** | String |
| **必須** | Yes（runbookの場合） |
| **説明** | 実行頻度 |

**使用例**:
```yaml
frequency: "日次"
frequency: "週次"
frequency: "月次"
frequency: "随時"
frequency: "年2回（4月・10月）"
```

#### estimated_time（runbook）

| 項目 | 値 |
|------|-----|
| **型** | String |
| **必須** | No（推奨） |
| **説明** | 作業所要時間 |

**使用例**:
```yaml
estimated_time: "30分"
estimated_time: "2時間"
```

#### executor

| 項目 | 値 |
|------|-----|
| **型** | String |
| **必須** | No（推奨） |
| **説明** | 実行者のロール |

**使用例**:
```yaml
executor: "運用担当者"
executor: "システム管理者"
executor: "データサイエンティスト"
```

### process

プロセス定義（`type: process`）で使用する追加フィールド。

#### stakeholders

| 項目 | 値 |
|------|-----|
| **型** | Array of Strings |
| **必須** | No（推奨） |
| **説明** | 関係者リスト |

**使用例**:
```yaml
stakeholders:
  - "プロジェクトマネージャー"
  - "CFDエンジニア"
  - "品質保証チーム"
```

#### triggers（process）

| 項目 | 値 |
|------|-----|
| **型** | Array of Strings |
| **必須** | No（推奨） |
| **説明** | プロセス開始トリガー |

**使用例**:
```yaml
triggers:
  - "新規プロジェクト開始時"
  - "四半期レビュー"
```

#### frequency（process）

runbookと同様。プロセス実行の頻度。

### reference

リファレンス（`type: reference`）で使用する追加フィールド。

#### applies_to

| 項目 | 値 |
|------|-----|
| **型** | String |
| **必須** | No（推奨） |
| **説明** | 適用対象バージョン/環境 |

**使用例**:
```yaml
applies_to: "iRIC v4.0.0 - v4.5.0"
applies_to: "ROMS v3.7+"
applies_to: "Python 3.8+"
applies_to: "3doca v1.0.0+"
```

### architecture

アーキテクチャ図（`type: architecture`）で使用する追加フィールド。

#### level

| 項目 | 値 |
|------|-----|
| **型** | Enum |
| **必須** | Yes（architectureの場合） |
| **説明** | C4モデルのレベル |
| **許可値** | `context`, `container`, `component` |

**使用例**:
```yaml
type: architecture
level: context    # Level 1: システム全体図

type: architecture
level: container  # Level 2: コンテナ図

type: architecture
level: component  # Level 3: コンポーネント図
```

#### parent_container

| 項目 | 値 |
|------|-----|
| **型** | String |
| **必須** | No（Level 3の場合は推奨） |
| **説明** | 親コンテナ名（Level 3のみ） |

**使用例**:
```yaml
# Level 3（Component）の場合
type: architecture
level: component
parent_container: "データ処理モジュール"
```

## 検証・自動化

### YAMLシンタックスチェック

```bash
# 単一ファイルのチェック
python3 -c "
import yaml
import sys
try:
    with open('docs/01_knowledge/03-how-to/my-doc.md') as f:
        content = f.read()
        frontmatter = content.split('---')[1]
        yaml.safe_load(frontmatter)
    print('OK: YAML syntax is valid')
except Exception as e:
    print(f'ERROR: {e}')
    sys.exit(1)
"
```

### 必須フィールドチェックスクリプト

[NEEDS_EXAMPLE: フロントマター検証スクリプト]

```python
# docs/_scripts/validate_frontmatter.py （作成予定）
import yaml
import sys
from pathlib import Path

REQUIRED_FIELDS = ['title', 'type', 'category', 'tags', 'summary', 'version', 'status', 'created', 'updated']

def validate_frontmatter(md_file):
    with open(md_file) as f:
        content = f.read()
        if not content.startswith('---'):
            return False, "No frontmatter found"

        try:
            frontmatter = content.split('---')[1]
            data = yaml.safe_load(frontmatter)
        except Exception as e:
            return False, f"YAML parse error: {e}"

        # 必須フィールドチェック
        missing = [field for field in REQUIRED_FIELDS if field not in data]
        if missing:
            return False, f"Missing fields: {missing}"

        # typeフィールド検証
        valid_types = ['concept', 'tutorial', 'how-to', 'reference', 'process', 'playbook', 'runbook', 'cheatsheet', 'architecture']
        if data['type'] not in valid_types:
            return False, f"Invalid type: {data['type']}"

        return True, "Valid"

# 使用例
# python3 docs/_scripts/validate_frontmatter.py docs/01_knowledge/03-how-to/*.md
```

[INCOMPLETE: 検証スクリプトの実装が必要]

### CI/CD統合

```yaml
# .github/workflows/validate-docs.yml
name: Validate Documentation

on:
  pull_request:
    paths:
      - 'docs/**/*.md'

jobs:
  validate-frontmatter:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install pyyaml

      - name: Validate frontmatter
        run: |
          python3 docs/_scripts/validate_frontmatter.py docs/**/*.md
```

[LINK_NEEDED: CI/CD設定ガイドへのリンク]

## エラーパターンと対処法

### よくあるエラー

| エラーメッセージ | 原因 | 対処法 |
|----------------|------|--------|
| `mapping values are not allowed here` | コロン後のスペース不足 | `key: value`の形式に修正（`:` の後に半角スペース） |
| `could not find expected ':'` | インデント不正 | スペース2個でインデント、タブ文字は使用禁止 |
| `found undefined tag` | YAMLタグの誤用 | 不要なタグ（`!`記法）を削除 |
| `duplicate key` | 同じキーの重複 | 重複するキーを削除または統合 |
| `unexpected end of file` | 閉じ`---`の欠落 | 末尾に`---`を追加 |

### トラブルシューティング例

**ケース1: summary内の改行エラー**

```yaml
# エラー例
summary: "これは
複数行の要約です"

# 正しい書き方
summary: |
  これは
  複数行の要約です
```

**ケース2: tags配列の書き方**

```yaml
# エラー例（文字列として扱われる）
tags: tag1, tag2, tag3

# 正しい書き方（配列）
tags: [tag1, tag2, tag3]

# または
tags:
  - tag1
  - tag2
  - tag3
```

**ケース3: related内のリンクエラー**

```yaml
# エラー例（パスが存在しない）
related:
  - ../nonexistent/file.md

# 推奨: 未作成の場合はギャップマーカーを使用
related:
  - [LINK_NEEDED: 関連ドキュメントへのリンク]
```

## ベストプラクティス

### 1. summaryの書き方

**DO（推奨）**:
- 2-3文で簡潔に
- アクション志向（「〜する方法」「〜を説明」）
- 具体的なキーワードを含める

**DON'T（非推奨）**:
- 1文だけ
- 抽象的すぎる表現
- タイトルの繰り返し

### 2. keywordsの選定

**DO（推奨）**:
- 同義語・別名を含める
- 英語/日本語両方
- ドメイン固有用語

**DON'T（非推奨）**:
- tagsと完全に重複
- 一般的すぎる単語のみ
- 無関係なキーワード

### 3. versionの管理

**DO（推奨）**:
- セマンティックバージョニング厳守
- 大きな変更はMAJOR更新
- CHANGELOG.mdと連携（将来）

**DON'T（非推奨）**:
- 日付をバージョンに使用（`2025-12-10`）
- 連番のみ（`v1`, `v2`）

### 4. statusの使い分け

**推奨フロー**:
```
draft（作成中、HIGH/MEDIUM多数）
  ↓
review（レビュー依頼、HIGH解消済み）
  ↓
published（公開、HIGH=0、MEDIUM最小限）
```

## 制約・制限事項

| 項目 | 制限値 | 理由 |
|------|--------|------|
| title長さ | 50文字推奨、100文字以内 | 検索結果表示領域 |
| summary長さ | 2-3文、200文字推奨 | RAGチャンクサイズ |
| tags数 | 3-7個推奨 | 分類の効果と管理コスト |
| keywords数 | 5-10個推奨 | 検索精度 |
| related数 | 5個程度推奨 | 認知負荷 |

[ASSUMPTION: 上記制限値は経験則に基づく。プロジェクト運用中に調整する可能性あり]

## バージョン履歴

| バージョン | 日付 | 変更内容 |
|-----------|------|---------|
| 1.0.0 | 2025-12-10 | 初版作成。全フィールド定義、使用例、検証方法を記載 |

[OUTDATED: 将来的にフィールド追加・変更があれば更新]

## 関連ドキュメント

- **概念理解**: [ティア設計仕様](./02-TIER-DESIGN-SPEC.md) - フロントマターとティアの関係
- **使い方**: [テンプレート使用ガイド](../03-how-to/01-template-usage-guide.md) - 実際の編集方法
- **仕様**: [ギャップマーカー仕様](./01-GAP-MARKER-SPEC.md) - 不完全箇所の明示方法
- **スキーマ**: [フロントマタースキーマ定義](../../_templates/01-FRONTMATTER_SCHEMA.md) - 簡易版スキーマ

---

<!-- 検証チェックリスト（作成完了時に確認）
✅ 網羅性：全フィールドがカバーされているか
✅ 正確性：型定義は正確か
✅ 構造化：テーブルで整理されているか
✅ 検索性：キーワードが適切に配置されているか
✅ バージョン：対象バージョンが明記されているか（3doca v1.0.0+）
✅ 最新性：情報は最新か（2025-12-10確認）
-->
