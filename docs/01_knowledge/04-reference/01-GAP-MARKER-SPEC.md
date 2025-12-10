---
title: "ギャップマーカー仕様書"
description: "ドキュメント作成時に不完全・未検証・要確認の情報を明示するためのマーカー仕様"
tags:
  - gap-marker
  - quality
  - anti-hallucination
  - specification
category: reference
domain: documentation
difficulty: beginner
created_at: 2025-12-09
updated_at: 2025-12-09
version: "1.0"
author: Claude Code
---

# ギャップマーカー仕様書

## 概要

ギャップマーカーは、ドキュメント作成時に**不完全・未検証・要確認の情報を明示する**ためのマーカーシステムです。

### 目的

1. **反ハルシネーション**: AI/LLMによるドキュメント生成時の推測・捏造を防止
2. **品質保証**: 不完全な箇所を明示し、レビュー・改善を促進
3. **追跡可能性**: 検索コマンドで未解決項目を一覧化
4. **優先度管理**: HIGH/MEDIUM/LOW/INFOで解消順序を明確化

### 基本原則

> **不完全でも正確なドキュメントは、完全だが不正確なドキュメントより価値がある。**

推測や仮定で補完してはならない。マーカーを残すことが品質を保証する。

---

## マーカー一覧

| マーカー | 優先度 | 用途 | 説明 |
|----------|--------|------|------|
| `[TODOCS: 説明]` | HIGH | 未完成セクション | 後で記述が必要な部分 |
| `[NEEDS_EXAMPLE: 説明]` | HIGH | コード例必要 | 実行可能なコード例・実行結果が必要 |
| `[NEEDS_VERIFICATION: 説明]` | MEDIUM | 未検証 | 技術的主張が未検証、要確認 |
| `[INCOMPLETE: 説明]` | MEDIUM | 情報不足 | 追加調査が必要 |
| `[OUTDATED: 説明]` | MEDIUM | 古い可能性 | バージョン依存情報で更新が必要かも |
| `[SME_NEEDED: 説明]` | LOW | 専門家レビュー必要 | ドメイン専門家の確認が必要 |
| `[LINK_NEEDED: 説明]` | LOW | リンク必要 | 関連ドキュメントへのリンクが必要 |
| `[ASSUMPTION: 説明]` | INFO | 仮定に基づく記述 | 明示的に仮定であることを示す |

---

## 使用ルール

### 1. 推測禁止

**不明な点はマーカーで明示し、推測で埋めない。**

```markdown
<!-- 悪い例 -->
デフォルト値は10に設定されています。

<!-- 良い例 -->
デフォルト値は [NEEDS_VERIFICATION: デフォルト値を公式ドキュメントで確認必要] に設定されています。
```

### 2. 具体的に記述

**何が必要か具体的に記述する。**

```markdown
<!-- 悪い例 -->
[TODOCS: 後で書く]

<!-- 良い例 -->
[TODOCS: メッシュ生成パラメータの説明と推奨値を追加]
```

### 3. 優先度考慮

**HIGH → MEDIUM → LOW → INFO の順で解消を推奨。**

- **HIGH**: ドキュメントとして公開する前に必ず解消
- **MEDIUM**: 次回更新時に解消
- **LOW**: 時間があるときに解消
- **INFO**: 解消不要（明示的な注記として残す）

### 4. 検索可能性

**すべてのマーカーは正規表現 `\[.*?:` で検索可能。**

---

## 使用例

### 例1: 技術仕様の不確実性

```markdown
## メッシュ生成パラメータ

最小メッシュサイズは通常 [NEEDS_VERIFICATION: デフォルト値要確認] に設定される。

[NEEDS_EXAMPLE: iRIC Nays2DFloodでのメッシュ設定コード例]

境界条件の設定については [LINK_NEEDED: 境界条件リファレンスへのリンク] を参照。
```

### 例2: ドメイン知識の不足

```markdown
## シミュレーション設定

[SME_NEEDED: CFDエンジニアによる推奨パラメータ範囲の確認が必要]

収束判定の閾値は [ASSUMPTION: 一般的な値として1e-6を仮定] としている。
```

### 例3: 未完成セクション

```markdown
## 高度な設定

[TODOCS: 以下のセクションを追加予定]
- マルチスレッド設定
- メモリ最適化オプション
- カスタムソルバー設定

[INCOMPLETE: 各オプションの影響範囲と推奨値の調査が必要]
```

### 例4: バージョン依存情報

```markdown
## APIエンドポイント

[OUTDATED: v2.0リリース後に確認が必要]

現在のエンドポイント: `/api/v1/data`
```

---

## 検索コマンド

### すべてのギャップマーカーを抽出

```bash
grep -rn "\[TODOCS:\|​\[NEEDS_EXAMPLE:\|​\[NEEDS_VERIFICATION:\|​\[INCOMPLETE:\|​\[SME_NEEDED:\|​\[ASSUMPTION:\|​\[OUTDATED:\|​\[LINK_NEEDED:" docs/
```

### 優先度別に抽出

```bash
# HIGH優先度
grep -rn "\[TODOCS:\|​\[NEEDS_EXAMPLE:" docs/

# MEDIUM優先度
grep -rn "\[NEEDS_VERIFICATION:\|​\[INCOMPLETE:\|​\[OUTDATED:" docs/

# LOW優先度
grep -rn "\[SME_NEEDED:\|​\[LINK_NEEDED:" docs/
```

### マーカー数のカウント

```bash
# 全マーカー数
grep -rc "\[.*?:" docs/ | awk -F: '{sum+=$2} END {print sum}'

# マーカー種別ごとのカウント
for marker in TODOCS NEEDS_EXAMPLE NEEDS_VERIFICATION INCOMPLETE OUTDATED SME_NEEDED LINK_NEEDED ASSUMPTION; do
  count=$(grep -rc "\[$marker:" docs/ 2>/dev/null | awk -F: '{sum+=$2} END {print sum}')
  echo "$marker: ${count:-0}"
done
```

---

## CI/CD統合

### GitHub Actionsでのマーカーチェック

```yaml
name: Gap Marker Check

on:
  pull_request:
    paths:
      - 'docs/**/*.md'

jobs:
  check-markers:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Count gap markers
        id: count
        run: |
          HIGH=$(grep -rc "\[TODOCS:\|\[NEEDS_EXAMPLE:" docs/ 2>/dev/null | awk -F: '{sum+=$2} END {print sum+0}')
          MEDIUM=$(grep -rc "\[NEEDS_VERIFICATION:\|\[INCOMPLETE:\|\[OUTDATED:" docs/ 2>/dev/null | awk -F: '{sum+=$2} END {print sum+0}')
          LOW=$(grep -rc "\[SME_NEEDED:\|\[LINK_NEEDED:" docs/ 2>/dev/null | awk -F: '{sum+=$2} END {print sum+0}')
          echo "high=$HIGH" >> $GITHUB_OUTPUT
          echo "medium=$MEDIUM" >> $GITHUB_OUTPUT
          echo "low=$LOW" >> $GITHUB_OUTPUT

      - name: Post summary
        run: |
          echo "## Gap Marker Summary" >> $GITHUB_STEP_SUMMARY
          echo "| Priority | Count |" >> $GITHUB_STEP_SUMMARY
          echo "|----------|-------|" >> $GITHUB_STEP_SUMMARY
          echo "| HIGH | ${{ steps.count.outputs.high }} |" >> $GITHUB_STEP_SUMMARY
          echo "| MEDIUM | ${{ steps.count.outputs.medium }} |" >> $GITHUB_STEP_SUMMARY
          echo "| LOW | ${{ steps.count.outputs.low }} |" >> $GITHUB_STEP_SUMMARY

      - name: Warn on HIGH markers
        if: steps.count.outputs.high > 0
        run: |
          echo "::warning::${{ steps.count.outputs.high }} HIGH priority gap markers found"
```

### PRコメントへの自動投稿

```yaml
      - name: Comment on PR
        uses: actions/github-script@v7
        with:
          script: |
            const high = ${{ steps.count.outputs.high }};
            const medium = ${{ steps.count.outputs.medium }};
            const low = ${{ steps.count.outputs.low }};

            const body = `## 📋 Gap Marker Report

            | Priority | Count | Status |
            |----------|-------|--------|
            | 🔴 HIGH | ${high} | ${high > 0 ? '⚠️ Needs attention' : '✅ OK'} |
            | 🟡 MEDIUM | ${medium} | ${medium > 5 ? '⚠️ Consider resolving' : '✅ OK'} |
            | 🟢 LOW | ${low} | ℹ️ Info |

            ${high > 0 ? '**Note:** HIGH priority markers should be resolved before merging.' : ''}
            `;

            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: body
            });
```

---

## 検証チェックリスト

### ドキュメント作成時

- [ ] 不明な技術的主張に `[NEEDS_VERIFICATION:]` を使用したか
- [ ] コード例が必要な箇所に `[NEEDS_EXAMPLE:]` を使用したか
- [ ] 未完成セクションに `[TODOCS:]` を使用したか
- [ ] 内部リンクが必要な箇所に `[LINK_NEEDED:]` を使用したか
- [ ] 仮定に基づく記述に `[ASSUMPTION:]` を使用したか

### レビュー時

- [ ] HIGH優先度マーカーが公開前に解消されているか
- [ ] マーカーの説明が具体的で次のアクションが明確か
- [ ] 推測で埋められた箇所がないか

---

## 関連リンク

- [ティア設計仕様](./02-TIER-DESIGN-SPEC.md)
- [移行マップ](./03-MIGRATION-MAP.md)
- [フロントマター拡張仕様](./04-frontmatter-reference.md)

---

**作成日**: 2025-12-09
**バージョン**: 1.0
**元ファイル**: `01-doc-framework/9251207claude-2.md`
