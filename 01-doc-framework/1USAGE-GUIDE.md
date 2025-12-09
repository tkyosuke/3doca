---
title: "使用ガイド"
description: "ドキュメントフレームワークテンプレートの使用方法、カスタマイズ手順、よくある落とし穴、品質チェックリスト"
tags: [usage-guide, template, best-practices]
category: guide
domain: documentation
difficulty: beginner
created_at: 2025-12-03
version: "1.0"
---

# ドキュメントフレームワーク使用ガイド

このガイドは、テンプレートを使って高品質なドキュメントを**5-10分で作成開始**できるよう設計されています。

## 📚 クイックスタート

### Step 1: テンプレートをコピー

```bash
# プロセスドキュメントを作成する例
cp templates/00-process-document-template.md your-project/docs/your-process.md
```

### Step 2: フロントマッターを編集

```yaml
---
title: "あなたのプロセス名"
description: "150文字以内の検索用説明"
tags: [tag1, tag2, tag3]
category: process  # process, playbook, runbook, reference, guide
domain: your-domain  # data-analysis, cfd, gis等
difficulty: beginner  # beginner, intermediate, advanced
---
```

### Step 3: 内容をカスタマイズ

- `<!-- TEMPLATE: ... -->` コメントを具体的な内容に置き換え
- Mermaidダイアグラムを実際のワークフローに調整
- 重要箇所マーク（**[重要]**, ⚠️）はそのまま活用

---

## 🔧 カスタマイズ手順

### フォルダ番号の変更

**Git履歴を保持する方法**:

```bash
# 既存フォルダの番号変更
git mv 01-doc-framework 02-technical-docs

# ファイル番号の変更
git mv examples/00-example.md examples/01-example.md
```

### ファイル名の命名規則

**形式**: `NN-descriptive-name.md`

- **kebab-case**: 単語を `-` で区切る（例: `data-quality-analysis`）
- **番号プレフィックス**: 2桁の番号で優先順位を示す（例: `00`, `10`, `20`）
- **説明的な名前**: 内容が推測できる名前にする

**例**:
- ✅ `10-data-quality-issues-playbook.md`
- ❌ `playbook1.md`, `DataQuality.md`

### フロントマッターのカスタマイズポイント

| フィールド | 必須 | カスタマイズ方法 |
|-----------|-----|----------------|
| `title` | ✅ | ドキュメントタイトル（検索表示用） |
| `description` | ✅ | 150文字以内、検索結果スニペット |
| `tags` | ✅ | 3-5個、検索用キーワード |
| `category` | ✅ | 下記の固定値から選択 |
| `domain` | ✅ | プロジェクトドメイン |
| `difficulty` | ✅ | beginner / intermediate / advanced |
| `related_docs` | 推奨 | 関連ドキュメントへの相対パス |

**category固定値**: `process`, `playbook`, `runbook`, `reference`, `guide`, `concepts`

---

## 📋 フロントマター必須項目

### RAG対応の最小要件

| フィールド | 役割 | 記入例 | RAG重要度 |
|-----------|------|--------|----------|
| `title` | ドキュメントタイトル | "データ解析プロセス" | 高 |
| `description` | セマンティック検索用説明 | "Pandasを使用したデータ解析の標準ワークフロー" | **最高** |
| `tags` | キーワードフィルタリング | `[process, pandas, python]` | 高 |
| `category` | ドキュメントタイプ分類 | `process` | 中 |
| `domain` | プロジェクトドメイン | `data-analysis` | 中 |

### descriptionの書き方

**良い例** ✅:
```yaml
description: "Pandas/NumPyを使用したデータ解析の標準ワークフロー。データ取得から可視化・レポート作成まで"
```

**悪い例** ❌:
```yaml
description: "プロセスドキュメント"  # 具体性なし
description: "これはデータ解析のためのドキュメントです。これを使って..."  # 代名詞使用
```

---

## ⚠️ よくある落とし穴

### 1. description欠落
**問題**: フロントマッターに `description` フィールドがない
**影響**: RAG検索が機能しない（セマンティック検索失敗）
**対策**: 必ず150文字以内の説明を追加

### 2. チャンクサイズ過大（500行超）
**問題**: 1つのセクションが500行を超える
**影響**: RAG検索精度が20-30%低下
**対策**: セクションを250-512トークン（約1000-2000文字）に分割

### 3. related_docs未設定
**問題**: 関連ドキュメントへのリンクがない
**影響**: ナレッジグラフ構築不可、ドキュメント間の関係が不明
**対策**: `related_docs` フィールドに相対パスを追加

### 4. 代名詞使用（「これは」「それは」）
**問題**: 文中に「これ」「それ」「その」を使用
**影響**: RAG検索時にコンテキストが喪失
**対策**: 具体的な用語を繰り返す（例: 「データ品質」を毎回明記）

### 5. category不統一
**問題**: `category: process-document` のように独自の値を使用
**影響**: フィルタリング失敗、検索結果に表示されない
**対策**: 固定値（process, playbook, runbook等）を使用

### 6. キーワード後置
**問題**: 重要なキーワードが段落や文の後半に配置
**影響**: スキャン性が低下、RAG検索ランクが低下
**対策**: キーワードを段落・文の冒頭に配置

### 7. フロントマッターコメント残存
**問題**: `<!-- TEMPLATE: ... -->` コメントが残っている
**影響**: メタデータが汚染され、検索結果が不正確
**対策**: 全てのコメントを具体的な値に置き換える

### 8. 番号重複
**問題**: 同じディレクトリ内で同じ番号を使用（例: `10-doc1.md`, `10-doc2.md`）
**影響**: 視認性低下、ソート順が不安定
**対策**: 番号を重複しないように割り当て（10, 11, 12...）

### 9. README未更新
**問題**: 新しいドキュメントを追加してもREADMEにリンクを追加しない
**影響**: ドキュメントの発見不可、利用されない
**対策**: README.mdに必ずリンクと説明を追加

### 10. Git履歴非保持
**問題**: `mv` コマンドでファイル移動・リネーム
**影響**: Git履歴が失われ、変更追跡が不可能
**対策**: `git mv` コマンドを使用して履歴を保持

---

## ✅ 品質チェックリスト

ドキュメント完成前に以下を確認してください：

### フロントマター完全性
- [ ] `title`, `description`, `tags`, `category`, `domain`, `difficulty` が全て記入済み
- [ ] `description` が150文字以内で具体的な内容
- [ ] `category` が固定値（process/playbook/runbook等）
- [ ] テンプレートコメント（`<!-- TEMPLATE: ... -->`）が全て削除済み

### コンテンツ品質
- [ ] 代名詞（これ・それ）を使用せず、具体的な用語を繰り返している
- [ ] 重要なキーワードが段落・文の冒頭に配置されている
- [ ] 各セクションが250-512トークン（約1000-2000文字）に収まっている
- [ ] Mermaidダイアグラムが実際のワークフローに合わせて調整済み

### リンク整合性
- [ ] `related_docs` に関連ドキュメントへの相対パスを記入
- [ ] README.mdに新規ドキュメントへのリンクを追加
- [ ] 内部リンクがすべて有効（リンク切れなし）

### 番号体系
- [ ] ファイル名が `NN-descriptive-name.md` 形式
- [ ] 同じディレクトリ内で番号重複なし
- [ ] Git履歴保持（`git mv` 使用）

### 最終確認
- [ ] 読了時間が5-10分以内（約1500-2000文字）
- [ ] プロジェクト固有の情報に置き換え済み
- [ ] 重要箇所マーク（**[重要]**, ⚠️）を適切に配置

---

## 📚 参考資料

- **[POLICY.md](./3POLICY.md)** - プロジェクト全体のドキュメンテーション方針
- **[templates/README.md](./templates/README.md)** - 全テンプレートの使い分けガイド
- **[examples/README.md](./examples/README.md)** - 実例の活用方法

**作成日**: 2025-12-03
**バージョン**: 1.0
