# CLAUDE.md - 3doca ドキュメントフレームワーク

このファイルは、3docaプロジェクト固有のルールとパターンを定義します。

## プロジェクト概要

3docaは、Diátaxisフレームワークと運用系ドキュメント階層に基づいた技術ドキュメント体系のテンプレート・実例集です。

## ディレクトリ構造

```
3doca/
├── 01-doc-framework/     # メインフレームワーク
│   ├── templates/        # 6ドキュメントテンプレート
│   ├── examples/         # 実例集
│   └── schema/           # スキーマ定義
├── 02-project-records/   # プロジェクト記録
└── shrimp-rules.md       # AIエージェント用ガイドライン
```

## ドキュメントスキーマ設計パターン

**適用シーン**: ドキュメントテンプレート体系にスキーマ定義を追加する際

**スキーマファイルの標準構造**:

```yaml
# ドキュメントタイプスキーマ
document_type: <type>
version: "1.0"
description: "スキーマの説明"
template_file: "対応するテンプレートファイル"

# セクション定義
sections:
  required:
    - name: "セクション名"
      purpose: "セクションの目的"
      min_words: 50  # 最小語数（任意）
      contains:      # 含むべき要素
        - "要素1"
        - "要素2"
      requires_mermaid: true  # Mermaid必須（任意）
  optional:
    - name: "任意セクション名"
      purpose: "目的"

# セクション順序
section_order:
  - "セクション1"
  - "セクション2"

# セクション間依存関係
dependencies:
  - if: "依存元セクション"
    then: "依存先セクション"
    reason: "依存理由"

# 制約条件
constraints:
  - type: "constraint_type"
    sections: ["対象セクション"]
    reason: "制約理由"

# 品質基準
quality_criteria:
  - "品質基準1"
  - "品質基準2"
```

**必須要素**:
1. **sections.required/optional**: 必須/任意セクションを明確に分離
2. **dependencies**: `if-then-reason`形式でセクション間依存関係を定義
3. **constraints**: Mermaid必須、チェックリスト必須等の制約
4. **quality_criteria**: ドキュメント品質の評価基準

**共通定義の分離**:
- `common.yaml`にフロントマター定義とMermaid設定を集約
- 各ドキュメントタイプスキーマから共通定義を参照

## フロントマター必須フィールド

すべてのドキュメントに以下のフロントマターを含める：

```yaml
---
title: "ドキュメントタイトル"
description: "150文字以内の検索用説明"
tags: [tag1, tag2]
category: process | playbook | runbook | reference | concepts | decision | troubleshooting
domain: data-analysis | cfd | gis | visualization | documentation | operations | architecture
difficulty: beginner | intermediate | advanced
created_at: YYYY-MM-DD
updated_at: YYYY-MM-DD
version: "1.0"
author: author-name
---
```

## Mermaidダイアグラム設定

ダークモード対応の必須設定：

```
%%{init: {'theme': 'dark'}}%%
```

推奨カラー：
- 完了/Done: `#4ade80` (bright green)
- 進行中/In Progress: `#fbbf24` (bright orange)
- 未着手/Not Started: `#a78bfa` (bright purple)
- エラー/Error: `#f87171` (bright red)

## セッション中断からの復旧パターン

**適用シーン**: ファイル書き込み途中でセッションが中断した場合

**復旧手順**:
1. Serenaプロジェクトをアクティベート
2. `current_work_session`メモリを読み込んで前回の状態を確認
3. Shrimpタスク状況を`list_tasks(status="all")`で確認
4. `get_task_detail`で進行中タスクの詳細と検証基準を確認
5. 途中のファイルを`Read`で確認し、完成度を判断
6. 必要に応じて残りの作業を完了
7. `verify_task`でタスクを完了

**重要**:
- ファイルが存在しても内容が途中で切れている可能性があるため、必ず`Read`で内容を確認する
- テンプレートファイルはYAMLパースエラーになりやすい（`<!-- TEMPLATE: -->`プレースホルダーが原因）

## YAMLフロントマター検証のフォールバック解析

**適用シーン**: `<!-- TEMPLATE: ... -->`を含むYAMLフロントマターの解析

**問題**:
- YAML標準の`yaml.safe_load()`は`<!-- TEMPLATE: YYYY-MM-DD -->`のような未クォートの値でパースエラーになる

**解決策**:
- `try/except`でYAMLパースを試み、失敗時は行ベースのフォールバック解析を使用
- フォールバック解析では`:` で分割してキー・値を抽出
- `TEMPLATE`文字列を含む値は検証をスキップ

## 3docaフレームワーク開発パターン

### Shrimpタスクマネージャーとの連携

- 依存関係が解消されたタスクを順次`execute_task` → `verify_task`で完了
- 各タスク完了後は成果物サマリーを提示（ファイル名、行数、主要内容）
- TodoWriteで進捗を可視化しつつ、Shrimpで正式な完了登録

### ドキュメントフレームワーク拡張パターン

1. スキーマ定義（`schema/*.yaml`）を先に作成
2. テンプレート（`templates/*.md`）を作成
3. 具体例（`examples/*.md`）を1つ以上作成
4. README.mdにリンクを追加
5. 既存ドキュメント（0README.md等）にセクション追加

### CI/CD設計の標準構成

- 検証ジョブは並列実行（markdownlint、Vale、lychee、frontmatter、sections）
- `concurrency`設定でPRごとに1つのワークフローのみ
- 初期段階は`fail: false`で警告のみ（段階的に厳格化）
- サマリージョブで結果を一覧表示

### 陳腐化検出の設計原則

- フロントマターに`next_review`、`review_cycle_days`、`owner`フィールド
- 4段階レベル（CRITICAL: 365日、HIGH: 180日、MEDIUM: 90日、LOW: 30日）
- GitHub Issue自動作成による通知

### カバレッジ評価スクリプト設計パターン

**適用シーン**: フレームワーク準拠度やドキュメント品質を定量評価するスクリプト作成時

**必須実施事項**:

1. **セクション別加重スコア方式**
   - 各評価セクションに重要度に応じた配点（weight）を設定
   - 配点合計は必ず1.0（100%）になるように設計
   - 例: ドキュメント階層15%、フロントマター仕様15%、スキーマ定義15%など

2. **チェック項目の定義形式**
   ```python
   "checks": [
       ("チェック項目名", "検証対象パス"),
       ("ファイル内容チェック", "file:keyword"),  # ファイル存在+キーワード
   ]
   ```

3. **レポート出力の標準構成**
   - フロントマター（RAG対応：title, description, tags, category, domain）
   - 総合スコアテーブル（スコア、目標、達成状況）
   - セクション別サマリー表（配点、パス数/総数、スコア、加重スコア）
   - セクション別詳細（各チェック項目の✅/❌）
   - 改善提案（80%未満セクションのリスト）
   - 結論（PASS/FAIL判定）

4. **終了コードの設計**
   - 0: 目標スコア達成
   - 1: 目標スコア未達成またはエラー

**成果物例**:
```
coverage_report.py → 02-project-records/quality-reviews/framework-coverage-report.md
```

### Shrimpタスク実行時のツール呼び出し順序

**重要ルール**:
- `verify_task`は`pending`状態のタスクには使用不可
- 必ず`execute_task` → 作業実行 → `verify_task`の順序で呼び出す
- エラー「任務當前狀態為 pending，不處於進行中狀態」が出たら`execute_task`を先に呼ぶ

### coverage_report.pyスクリプトのパス解決パターン

**問題**: 評価スクリプトでファイル存在チェックを行う際、パスパターンが実際のファイル名と一致しないと誤検出が発生する

**対策**:
- ファイル名のパターン（ハイフン、ゼロパディング）を実際のファイル名と完全一致させる
- 例: `templates/00process` ではなく `templates/00process-document-template.md`
- 内容チェック用の「ファイル:キーワード」形式は廃止し、ファイル存在確認に統一

**検証方法**:
```bash
ls -la 01-doc-framework/templates/  # 実際のファイル名を確認
python3 coverage_report.py          # スクリプト実行で検証
```

### テンプレートファイルのYAMLパースエラー対策

**問題**: `<!-- TEMPLATE: YYYY-MM-DD -->`のようなプレースホルダーを含むYAMLはパースエラーになる

**解決策**:
```python
try:
    frontmatter = yaml.safe_load(yaml_content)
except yaml.YAMLError:
    # フォールバック: 行ベース解析
    frontmatter = {}
    for line in yaml_content.split('\n'):
        if ':' in line and 'TEMPLATE' not in line:
            key, value = line.split(':', 1)
            frontmatter[key.strip()] = value.strip()
```

## 関連ドキュメント

- [POLICY.md](./01-doc-framework/3POLICY.md) - プロジェクトポリシー
- [USAGE-GUIDE.md](./01-doc-framework/1USAGE-GUIDE.md) - テンプレート使用ガイド
- [FRONTMATTER-EXTENSION-SPEC.md](./01-doc-framework/4FRONTMATTER-EXTENSION-SPEC.md) - フロントマター拡張仕様
- [SECTION-DEPENDENCY-MAP.md](./01-doc-framework/5SECTION-DEPENDENCY-MAP.md) - セクション間依存関係マップ
- [DEVRAG-OPTIMIZATION-GUIDE.md](./01-doc-framework/6DEVRAG-OPTIMIZATION-GUIDE.md) - DevRAG最適化ガイド
- [CI-CD-GUIDE.md](./01-doc-framework/7CI-CD-GUIDE.md) - CI/CDパイプラインガイド
- [STALENESS-DETECTION-SPEC.md](./01-doc-framework/8STALENESS-DETECTION-SPEC.md) - 陳腐化検出仕様
- [shrimp-rules.md](./shrimp-rules.md) - AIエージェント用ガイドライン
