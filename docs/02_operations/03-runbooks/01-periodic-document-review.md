---
title: "定期ドキュメントレビュー手順"
type: runbook
category: "documentation-quality"
tags: [quality, review, gap-markers, maintenance]
summary: |
  ドキュメント品質を維持するための定期レビュー作業の実行手順。
  ギャップマーカーの確認、リンク検証、内容更新の3段階で実施する。
keywords:
  - document review
  - gap markers
  - quality assurance
  - maintenance
frequency: "月次（推奨）"
estimated_time: "30-60分"
owner: "ドキュメント管理者"
executor: "技術ライター/開発者"
related:
  - ../../01_knowledge/concepts/01-framework-overview.md
  - ../04-cheatsheets/01-gap-markers-quick-reference.md
version: "1.0.0"
status: active
created: "2025-12-10"
updated: "2025-12-10"
---

# 定期ドキュメントレビュー手順

| 項目 | 内容 |
|------|------|
| **実行頻度** | 月次（推奨）または四半期 |
| **所要時間** | 30-60分 |
| **実行者** | 技術ライター/ドキュメント管理者 |
| **最終実行** | [TODOCS: 実行時に記録] |

## 目的

ドキュメントの品質と正確性を維持するため、ギャップマーカーの解消状況、リンク切れ、内容の陳腐化を定期的に確認し、改善アクションを特定する。

## 前提条件チェック

実行前に以下を確認：

- [ ] プロジェクトルートディレクトリにいる
- [ ] `docs/` ディレクトリへの読み書き権限がある
- [ ] `grep` コマンドが利用可能
- [ ] Markdownエディタが利用可能

```bash
# 環境確認
pwd  # プロジェクトルートにいることを確認
ls -la docs/  # docs ディレクトリが存在することを確認
which grep  # grep が利用可能か確認
```

## 実行手順

### Step 1: ギャップマーカーの抽出

全ドキュメントからギャップマーカーを検索し、現状を把握する。

```bash
# すべてのギャップマーカーを抽出（ファイル名、行番号、マーカー付き）
grep -rn "\[TODOCS:\|\[NEEDS_EXAMPLE:\|\[NEEDS_VERIFICATION:\|\[INCOMPLETE:\|\[SME_NEEDED:\|\[ASSUMPTION:\|\[OUTDATED:\|\[LINK_NEEDED:" docs/ > gap_markers_report.txt

# 件数をカウント
echo "=== ギャップマーカー統計 ==="
echo "TODOCS: $(grep -o "\[TODOCS:" gap_markers_report.txt | wc -l)"
echo "NEEDS_EXAMPLE: $(grep -o "\[NEEDS_EXAMPLE:" gap_markers_report.txt | wc -l)"
echo "NEEDS_VERIFICATION: $(grep -o "\[NEEDS_VERIFICATION:" gap_markers_report.txt | wc -l)"
echo "INCOMPLETE: $(grep -o "\[INCOMPLETE:" gap_markers_report.txt | wc -l)"
echo "SME_NEEDED: $(grep -o "\[SME_NEEDED:" gap_markers_report.txt | wc -l)"
echo "ASSUMPTION: $(grep -o "\[ASSUMPTION:" gap_markers_report.txt | wc -l)"
echo "OUTDATED: $(grep -o "\[OUTDATED:" gap_markers_report.txt | wc -l)"
echo "LINK_NEEDED: $(grep -o "\[LINK_NEEDED:" gap_markers_report.txt | wc -l)"
```

**期待される出力**：
```
=== ギャップマーカー統計 ===
TODOCS: 15
NEEDS_EXAMPLE: 23
NEEDS_VERIFICATION: 8
INCOMPLETE: 5
SME_NEEDED: 3
ASSUMPTION: 2
OUTDATED: 1
LINK_NEEDED: 18
```

**チェック**: [ ] レポートファイル `gap_markers_report.txt` が生成された

---

### Step 2: 優先度別の分類

HIGH優先度（TODOCS, NEEDS_EXAMPLE）のマーカーを特定し、対応優先度を判断する。

```bash
# HIGH優先度マーカーのみ抽出
grep -rn "\[TODOCS:\|\[NEEDS_EXAMPLE:" docs/ > high_priority_gaps.txt

echo "=== HIGH優先度マーカー（対応必須） ==="
cat high_priority_gaps.txt

# ファイル別の集計
echo -e "\n=== ファイル別HIGH優先度マーカー数 ==="
awk -F: '{print $1}' high_priority_gaps.txt | sort | uniq -c | sort -rn
```

**チェック**: [ ] HIGH優先度マーカーが特定され、対応が必要なファイルが明確になった

---

### Step 3: リンク検証

内部リンク（相対パス）の存在確認を実施する。

```bash
# 内部リンクを含むファイルを抽出
find docs -name "*.md" -exec grep -l "](\.\./" {} \; > files_with_internal_links.txt

echo "=== 内部リンクを含むファイル数 ==="
wc -l files_with_internal_links.txt

# 各ファイルのリンクを抽出（手動検証用）
echo -e "\n=== 内部リンク一覧（サンプル） ==="
head -5 files_with_internal_links.txt | while read file; do
  echo "File: $file"
  grep -o "](\.\.\/[^)]*)" "$file" | head -3
  echo ""
done
```

**チェック**: [ ] リンクを含むファイルが特定され、手動検証の準備ができた

**手動作業**: リンク先ファイルが実在するか確認（自動化は将来の改善項目）

---

### Step 4: 陳腐化リスクの特定

6ヶ月以上更新されていないドキュメントを抽出し、内容の見直しが必要か判断する。

```bash
# 6ヶ月以上更新されていないファイルを検索
find docs -name "*.md" -type f -mtime +180 > outdated_files_candidate.txt

echo "=== 6ヶ月以上未更新のファイル ==="
cat outdated_files_candidate.txt

# フロントマターのupdatedフィールドを確認（存在する場合）
echo -e "\n=== フロントマターのupdated日付（サンプル） ==="
head -5 outdated_files_candidate.txt | while read file; do
  echo "File: $file"
  grep "^updated:" "$file" 2>/dev/null || echo "  (updated field not found)"
  echo ""
done
```

**チェック**: [ ] 陳腐化リスクのあるファイルが特定された

---

### Step 5: アクションアイテムの作成

レビュー結果をまとめ、次のアクションを決定する。

```bash
# レポートサマリーの生成
cat > review_summary_$(date +%Y%m%d).md << 'EOF'
# ドキュメントレビューサマリー

**実行日**: $(date +%Y-%m-%d)
**実行者**: [記入してください]

## 統計

- 総ギャップマーカー数: [gap_markers_report.txt から記入]
- HIGH優先度: [high_priority_gaps.txt から記入]
- 内部リンク含有ファイル数: [files_with_internal_links.txt から記入]
- 6ヶ月以上未更新ファイル数: [outdated_files_candidate.txt から記入]

## アクションアイテム

### 優先度: HIGH
- [ ] [ファイル名]: [TODOCS] [具体的な内容]
- [ ] [ファイル名]: [NEEDS_EXAMPLE] [具体的な内容]

### 優先度: MEDIUM
- [ ] リンク切れの修正: [ファイル名]
- [ ] 内容更新: [ファイル名]

### 優先度: LOW
- [ ] [LINK_NEEDED] の解消: [ファイル名]

## 次回レビュー予定

- 日付: [1ヶ月後の日付を記入]
EOF

echo "レビューサマリーファイルを作成しました: review_summary_$(date +%Y%m%d).md"
```

**完了基準**：
- [ ] すべてのギャップマーカーが抽出された
- [ ] HIGH優先度マーカーが特定された
- [ ] リンク検証が完了した
- [ ] レビューサマリーファイルが作成された
- [ ] アクションアイテムが明確になった

## クイックコマンド集

全ステップを一括で実行する場合（出力を確認しながら実行すること）：

```bash
# === 定期ドキュメントレビュー 一括実行 ===
# 注意: 各ステップの出力を確認しながら実行すること

# Step 1: ギャップマーカー抽出
grep -rn "\[TODOCS:\|\[NEEDS_EXAMPLE:\|\[NEEDS_VERIFICATION:\|\[INCOMPLETE:\|\[SME_NEEDED:\|\[ASSUMPTION:\|\[OUTDATED:\|\[LINK_NEEDED:" docs/ > gap_markers_report.txt
echo "=== ギャップマーカー統計 ==="
echo "TODOCS: $(grep -o "\[TODOCS:" gap_markers_report.txt | wc -l)"
echo "NEEDS_EXAMPLE: $(grep -o "\[NEEDS_EXAMPLE:" gap_markers_report.txt | wc -l)"
echo "NEEDS_VERIFICATION: $(grep -o "\[NEEDS_VERIFICATION:" gap_markers_report.txt | wc -l)"
echo "INCOMPLETE: $(grep -o "\[INCOMPLETE:" gap_markers_report.txt | wc -l)"
echo "SME_NEEDED: $(grep -o "\[SME_NEEDED:" gap_markers_report.txt | wc -l)"
echo "ASSUMPTION: $(grep -o "\[ASSUMPTION:" gap_markers_report.txt | wc -l)"
echo "OUTDATED: $(grep -o "\[OUTDATED:" gap_markers_report.txt | wc -l)"
echo "LINK_NEEDED: $(grep -o "\[LINK_NEEDED:" gap_markers_report.txt | wc -l)"

# Step 2: HIGH優先度マーカー抽出
grep -rn "\[TODOCS:\|\[NEEDS_EXAMPLE:" docs/ > high_priority_gaps.txt
echo -e "\n=== HIGH優先度マーカー数 ==="
wc -l high_priority_gaps.txt

# Step 3: 内部リンク検証準備
find docs -name "*.md" -exec grep -l "](\.\./" {} \; > files_with_internal_links.txt
echo -e "\n=== 内部リンクファイル数 ==="
wc -l files_with_internal_links.txt

# Step 4: 陳腐化候補検索
find docs -name "*.md" -type f -mtime +180 > outdated_files_candidate.txt
echo -e "\n=== 6ヶ月以上未更新ファイル数 ==="
wc -l outdated_files_candidate.txt

echo -e "\n完了"
echo "次のステップ: review_summary_YYYYMMDD.md を作成し、アクションアイテムを記入してください"
```

## パラメータ一覧

| パラメータ | 説明 | デフォルト | 例 |
|------------|------|------------|-----|
| 検索対象ディレクトリ | レビュー対象のドキュメントディレクトリ | `docs/` | `docs/`, `documentation/` |
| 陳腐化判定日数 | この日数以上更新されていないファイルを陳腐化候補とする | 180日（6ヶ月） | 90日（3ヶ月）、365日（1年） |
| 出力ファイル名 | レポートファイルの名前 | `gap_markers_report.txt` | `review_YYYYMMDD.txt` |

## トラブルシューティング

### エラー: `grep: docs/: No such file or directory`

**原因**: プロジェクトルートディレクトリにいない、または `docs/` ディレクトリが存在しない

**対処**:
```bash
# プロジェクトルートに移動
cd /mnt/j/pcloud_sync/5agent/1conf/3doca

# docs ディレクトリの存在確認
ls -la docs/
```

---

### エラー: `grep: unmatched \[`

**原因**: grepの正規表現エスケープが不適切

**対処**:
```bash
# エスケープを修正（バックスラッシュを追加）
grep -rn "\\\[TODOCS:" docs/
```

---

### 問題: ギャップマーカーが多すぎて対応できない

**原因**: ドキュメントが未成熟、またはレビュー頻度が低い

**対処**:
1. HIGH優先度（TODOCS, NEEDS_EXAMPLE）のみに絞る
2. 重要なドキュメント（チュートリアル、リファレンス）から優先対応
3. 定期レビューの頻度を上げる（月次→隔週）

---

### 問題: リンク切れの自動検証ができない

**原因**: 手動検証が必要（現状の制約）

**対処**: 将来の改善として以下を検討
- markdownlintのリンクチェック機能を導入
- CI/CDパイプラインでの自動検証
- 詳細は [LINK_NEEDED: CI/CD設定ガイド]

## ロールバック

このランブックはドキュメントの読み取り専門のため、ロールバックは不要です。
誤って生成したレポートファイルを削除する場合：

```bash
# レポートファイルの削除
rm -f gap_markers_report.txt high_priority_gaps.txt files_with_internal_links.txt outdated_files_candidate.txt review_summary_*.md
```

## 実行記録

| 日付 | 実行者 | 結果 | 備考 |
|------|--------|------|------|
| 2025-12-10 | 初回作成 | - | ランブック作成 |
| | | □ 成功 / □ 失敗 | |
| | | □ 成功 / □ 失敗 | |

## 関連ドキュメント

- **フレームワーク概要**: [../../01_knowledge/concepts/01-framework-overview.md](../../01_knowledge/concepts/01-framework-overview.md)
- **ギャップマーカー早見表**: [../04-cheatsheets/01-gap-markers-quick-reference.md](../04-cheatsheets/01-gap-markers-quick-reference.md)
- **プロジェクトルール**: [../../../CLAUDE.md](../../../CLAUDE.md)
- **テンプレート**: [../../_templates/](../../_templates/)

---

<!-- 検証チェックリスト（作成完了時に確認）
✓ コマンドはコピー&ペーストで実行可能か
✓ 各ステップに確認ポイントがあるか
✓ パラメータの説明があるか
✓ トラブルシューティングがあるか
✓ ロールバック手順があるか
✓ 前提条件チェックリストがあるか
✓ 実行記録欄があるか
-->
