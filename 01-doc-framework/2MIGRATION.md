---
title: "移行ガイド"
description: "ドキュメントフレームワークを別プロジェクトへ移行する手順：rsync、Git履歴保持、カスタマイズ、トラブルシューティング"
tags: [migration, template, guide]
category: guide
domain: documentation
difficulty: intermediate
created_at: 2025-12-03
version: "1.0"
---

# ドキュメントフレームワーク移行ガイド

このガイドは、ドキュメントフレームワークを**3ステップで別プロジェクトへ移行**できるよう設計されています。

## 🚀 クイックスタート

### Step 1: ファイルをコピー

```bash
# rsyncで01-doc-frameworkをコピー（.gitは除外）
rsync -av --exclude='.git' \
  /path/to/source/01-doc-framework/ \
  /path/to/new-project/docs/
```

### Step 2: カスタマイズ

```bash
cd /path/to/new-project/docs/

# フォルダ番号変更（Git履歴保持）
git mv 01-doc-framework 02-technical-docs

# domainフィールド変更（全ファイル一括）
find . -name "*.md" -type f -exec sed -i 's/domain: data-analysis/domain: your-domain/g' {} +

# examples/の差し替え（プロジェクト固有の実例に置き換え）
rm -rf examples/*.md
cp your-examples/*.md examples/
```

### Step 3: 検証

```bash
# フロントマッター検証
python3 ../../02-project-records/quality-reviews/check_frontmatter.py

# 適合率100%を確認
```

---

## 📋 詳細手順

### Git履歴を保持する方法

```bash
# 移行先プロジェクトでリモート追加
cd /path/to/new-project
git remote add doc-framework /path/to/source

# フレームワークのブランチをフェッチ
git fetch doc-framework

# マージ（関連性のない履歴を許可）
git merge --allow-unrelated-histories doc-framework/main

# 競合解決後、コミット
git commit -m "Merge doc-framework into project"
```

### カスタマイズポイント

**1. フォルダ番号の変更**

```bash
# Git履歴を保持してリネーム
git mv 01-doc-framework 03-documentation-system
```

**2. フロントマッターのdomain変更**

全ファイルのdomainフィールドを一括変更：

```bash
find . -name "*.md" -type f -exec sed -i \
  's/domain: data-analysis/domain: your-domain/g' {} +
```

**3. examples/の差し替え**

プロジェクト固有の実例に置き換え：

```bash
# データ解析実例を削除
rm examples/00-data-analysis-process.md
rm examples/01-data-quality-analysis-process.md
# ... 他のexamplesも削除

# あなたのプロジェクトの実例をコピー
cp your-project/examples/*.md examples/
```

**4. README.mdの更新**

- プロジェクト概要を更新
- domainの説明を変更
- 参考資料セクションを更新

---

## ⚠️ トラブルシューティング

### 問題1: 内部リンク切れ

**症状**: README.mdやexamples/内のリンクが404エラー

**原因**: フォルダ名変更後、相対パスが無効化

**対策**:
```bash
# リンク切れを検索
grep -r "\](\.\./" .

# 相対パスを修正
# 例: [POLICY.md](../01-doc-framework/POLICY.md)
#  → [POLICY.md](../02-technical-docs/POLICY.md)
```

### 問題2: フロントマッター不適合

**症状**: check_frontmatter.py実行で適合率 < 100%

**原因**: 必須フィールド欠落、category不統一

**対策**:
```bash
# エラーメッセージを確認し、USAGE-GUIDE.mdを参照
python3 check_frontmatter.py

# エラーメッセージ例:
# ❌ Missing required field: 'description'
#    → See ../USAGE-GUIDE.md#フロントマター必須項目
```

### 問題3: Git履歴マージ競合

**症状**: `git merge` 実行時に競合エラー

**原因**: 移行先プロジェクトに同名ファイルが存在

**対策**:
```bash
# 競合ファイルを確認
git status

# 競合を手動解決（エディタで開いて編集）
vim path/to/conflicted-file.md

# 解決後、マージを完了
git add path/to/conflicted-file.md
git commit -m "Resolve merge conflicts"
```

---

## 📚 参考資料

- **[USAGE-GUIDE.md](./1USAGE-GUIDE.md)** - テンプレート使用方法
- **[POLICY.md](./3POLICY.md)** - ドキュメンテーション方針

**作成日**: 2025-12-03
**バージョン**: 1.0
