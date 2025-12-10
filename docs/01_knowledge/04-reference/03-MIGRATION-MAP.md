---
title: "既存ドキュメント分類マップ"
description: "01-doc-framework/から新3軸構造への移行計画"
tags:
  - migration
  - classification
  - reorganization
category: reference
domain: documentation
difficulty: intermediate
created_at: 2025-12-09
updated_at: 2025-12-09
version: "1.0"
author: Claude Code
---

# 既存ドキュメント分類マップ

## 概要

`01-doc-framework/`内の既存ドキュメントを新3軸構造（`docs/`）に分類・移行するための計画書。

### 分類カテゴリ

| 分類 | 説明 | アクション |
|------|------|----------|
| **MIGRATE** | 新構造に移行 | ファイルを移動/コピー |
| **ARCHIVE** | アーカイブとして保存 | `docs/archives/`に移動 |
| **NEW** | 新規作成が必要 | テンプレートから作成 |
| **DEPRECATE** | 廃止（新仕様に統合済み） | 削除または参照のみ |

---

## 現状ファイル一覧

### ルートレベル（16ファイル）

| # | ファイル名 | 行数 | 内容概要 |
|---|-----------|------|---------|
| 1 | 0README.md | - | インデックス |
| 2 | 1USAGE-GUIDE.md | - | 使用ガイド |
| 3 | 2MIGRATION.md | - | 移行ガイド |
| 4 | 3POLICY.md | - | ポリシー |
| 5 | 4FRONTMATTER-EXTENSION-SPEC.md | - | フロントマター仕様 |
| 6 | 4adoption-report.md | - | 採用レポート |
| 7 | 5CLAUDE-CONFIG.md | - | Claude設定 |
| 8 | 5SECTION-DEPENDENCY-MAP.md | - | セクション依存関係 |
| 9 | 6DEVRAG-OPTIMIZATION-GUIDE.md | - | DevRAG最適化 |
| 10 | 7CI-CD-GUIDE.md | - | CI/CDガイド |
| 11 | 8STALENESS-DETECTION-SPEC.md | - | 陳腐化検出仕様 |
| 12 | 9251129claude.md | - | 元ファイル（方針） |
| 13 | 9251205claude.md | - | 元ファイル（方針） |
| 14 | 9251206claude.md | - | 元ファイル（5ティア設計） |
| 15 | 9251207claude-2.md | - | 元ファイル（3軸構造） |
| 16 | 9251207cloude-1.md | - | 元ファイル（方針） |

### templates/（9ファイル）

| # | ファイル名 | 内容概要 |
|---|-----------|---------|
| 1 | 00process-document-template.md | プロセステンプレート |
| 2 | 01playbook-template.md | プレイブックテンプレート |
| 3 | 02runbook-template.md | ランブックテンプレート |
| 4 | 03troubleshooting-template.md | トラブルシューティングテンプレート |
| 5 | 04adr-template.md | ADRテンプレート |
| 6 | 05cheatsheet-template.md | チートシートテンプレート |
| 7 | 06policy-template.md | ポリシーテンプレート |
| 8 | 07sop-template.md | SOPテンプレート |
| 9 | 08cfd-ocean-sop-template.md | CFD海洋SOPテンプレート |

### examples/（8ファイル）

| # | ファイル名 | 内容概要 |
|---|-----------|---------|
| 1 | 00data-analysis-process.md | データ解析プロセス |
| 2 | 01data-quality-analysis-process.md | データ品質分析プロセス |
| 3 | 10data-quality-issues-playbook.md | データ品質問題プレイブック |
| 4 | 11anomaly-detection-playbook.md | 異常検出プレイブック |
| 5 | 20data-cleansing-runbook.md | データクレンジングランブック |
| 6 | 30anti-patterns-data-analysis.md | データ解析アンチパターン |
| 7 | 40-roms-kuroshio-simulation-sop.md | ROMS黒潮シミュレーションSOP |
| 8 | README.md | 実例インデックス |

### schema/（2ファイル）

| # | ファイル名 | 内容概要 |
|---|-----------|---------|
| 1 | README.md | スキーマインデックス |
| 2 | REFERENCE.md | スキーマリファレンス |

---

## 分類テーブル

### ルートレベルファイル

| 現在のパス | 移行先 | 分類 | ティア | 備考 |
|-----------|--------|------|-------|------|
| `0README.md` | `docs/README.md` | DEPRECATE | - | 新README.mdに統合済み |
| `1USAGE-GUIDE.md` | `docs/01_knowledge/03-how-to/usage-guide.md` | MIGRATE | Tier 2 | |
| `2MIGRATION.md` | `docs/01_knowledge/03-how-to/migration-guide.md` | MIGRATE | Tier 2 | |
| `3POLICY.md` | `docs/01_knowledge/01-concepts/policy.md` | MIGRATE | Tier 4 | |
| `4FRONTMATTER-EXTENSION-SPEC.md` | `docs/01_knowledge/reference/frontmatter-spec.md` | MIGRATE | Tier 3 | |
| `4adoption-report.md` | `docs/archives/reports/adoption-report.md` | ARCHIVE | - | プロジェクト記録 |
| `5CLAUDE-CONFIG.md` | `docs/01_knowledge/reference/claude-config.md` | MIGRATE | Tier 3 | |
| `5SECTION-DEPENDENCY-MAP.md` | `docs/01_knowledge/reference/section-dependency.md` | MIGRATE | Tier 3 | |
| `6DEVRAG-OPTIMIZATION-GUIDE.md` | `docs/01_knowledge/03-how-to/devrag-optimization.md` | MIGRATE | Tier 2 | |
| `7CI-CD-GUIDE.md` | `docs/01_knowledge/03-how-to/ci-cd-guide.md` | MIGRATE | Tier 2 | |
| `8STALENESS-DETECTION-SPEC.md` | `docs/01_knowledge/reference/staleness-detection.md` | MIGRATE | Tier 3 | |
| `9251129claude.md` | `docs/archives/source-materials/` | ARCHIVE | - | 方針決定の根拠 |
| `9251205claude.md` | `docs/archives/source-materials/` | ARCHIVE | - | 方針決定の根拠 |
| `9251206claude.md` | `docs/archives/source-materials/` | ARCHIVE | - | 5ティア設計の根拠 |
| `9251207claude-2.md` | `docs/archives/source-materials/` | ARCHIVE | - | 3軸構造の根拠 |
| `9251207cloude-1.md` | `docs/archives/source-materials/` | ARCHIVE | - | 方針決定の根拠 |

### templates/

| 現在のパス | 移行先 | 分類 | 備考 |
|-----------|--------|------|------|
| `templates/00process-document-template.md` | `docs/_templates/process-template.md` | MIGRATE | リネーム |
| `templates/01playbook-template.md` | `docs/_templates/playbook-template.md` | MIGRATE | リネーム |
| `templates/02runbook-template.md` | `docs/_templates/runbook-template.md` | MIGRATE | リネーム |
| `templates/03troubleshooting-template.md` | `docs/_templates/troubleshooting-template.md` | MIGRATE | リネーム |
| `templates/04adr-template.md` | `docs/_templates/adr-template.md` | MIGRATE | リネーム |
| `templates/05cheatsheet-template.md` | `docs/_templates/cheatsheet-template.md` | MIGRATE | リネーム |
| `templates/06policy-template.md` | `docs/_templates/policy-template.md` | MIGRATE | リネーム |
| `templates/07sop-template.md` | `docs/_templates/sop-template.md` | MIGRATE | リネーム |
| `templates/08cfd-ocean-sop-template.md` | `docs/_templates/cfd-ocean-sop-template.md` | MIGRATE | |
| `templates/README.md` | `docs/_templates/README.md` | DEPRECATE | 新README.mdに統合済み |

### examples/

| 現在のパス | 移行先 | 分類 | ティア | 備考 |
|-----------|--------|------|-------|------|
| `examples/00data-analysis-process.md` | `docs/02_operations/01-processes/data-analysis.md` | MIGRATE | Tier 2 | |
| `examples/01data-quality-analysis-process.md` | `docs/02_operations/01-processes/data-quality-analysis.md` | MIGRATE | Tier 2 | |
| `examples/10data-quality-issues-playbook.md` | `docs/02_operations/02-playbooks/data-quality-issues.md` | MIGRATE | Tier 2 | |
| `examples/11anomaly-detection-playbook.md` | `docs/02_operations/02-playbooks/anomaly-detection.md` | MIGRATE | Tier 2 | |
| `examples/20data-cleansing-runbook.md` | `docs/02_operations/03-runbooks/data-cleansing.md` | MIGRATE | Tier 2 | |
| `examples/30anti-patterns-data-analysis.md` | `docs/01_knowledge/reference/anti-patterns.md` | MIGRATE | Tier 3 | リファレンス |
| `examples/40-roms-kuroshio-simulation-sop.md` | `docs/02_operations/03-runbooks/roms-kuroshio-sop.md` | MIGRATE | Tier 2 | |
| `examples/README.md` | - | DEPRECATE | - | 各フォルダREADMEに統合 |

### schema/

| 現在のパス | 移行先 | 分類 | 備考 |
|-----------|--------|------|------|
| `schema/README.md` | `docs/01_knowledge/reference/schema/README.md` | MIGRATE | |
| `schema/REFERENCE.md` | `docs/01_knowledge/reference/schema/reference.md` | MIGRATE | |

---

## 新規作成必要リスト

### Diátaxis軸（01_knowledge）

#### tutorials/（Tier 1）

**Phase 12で作成予定**:

- [ ] `getting-started.md` - 3docaフレームワーク入門（15分）
  - テンプレート選択、フロントマター設定、基本構造の理解
- [ ] `first-document.md` - 最初のドキュメント作成（15分）
  - ハウツードキュメント作成の実践、ギャップマーカー使用法
- [ ] `template-usage.md` - テンプレートの使い方（10分）
  - 各テンプレートの選定基準、カスタマイズ方法

**Phase 13で検討（ドメイン固有）**:

[SME_NEEDED: ドメイン固有チュートリアルの題材選定]

- [ ] CFDシミュレーション入門チュートリアル（具体的なソルバー/ケース要選定）
- [ ] GISデータ処理入門チュートリアル（具体的なデータセット/ツール要選定）

#### concepts/（Tier 4）

**Phase 12で作成予定**:

- [ ] `framework-design.md` - 3docaフレームワークの設計思想
  - 3軸構造の設計根拠、Diátaxis/運用/C4の統合意図
  - ソース: `docs/archives/source-materials/9251207claude-2.md`
- [ ] `diataxis-adoption.md` - Diátaxis採用の根拠
  - 読者中心設計の原則、4象限分類の利点
  - ソース: `docs/archives/source-materials/9251129claude.md`
- [ ] `cognitive-foundation.md` - 5ティア設計の認知科学的基盤
  - 認知負荷理論、段階的詳細化の原則
  - ソース: `docs/archives/source-materials/9251206claude.md`

### C4軸（03_architecture）

#### context/（Tier 0）

**現状**: 既存の `3doca-framework-context.md` で基本的なコンテキスト図は作成済み。

**Phase 13で検討（必要に応じて）**:

- [ ] フレームワーク利用シナリオ別のコンテキスト図（個人利用、チーム利用、組織利用）

[SME_NEEDED: ドメイン固有のコンテキスト図]

- [ ] CFDシミュレーションパイプライン全体像（ソフトウェア/データソース要選定）
- [ ] GISデータ処理システム全体像（ツールチェーン/データフォーマット要選定）

#### containers/（Tier 4）

**現状**: 既存の `3doca-framework-containers.md` でコンテナ図は作成済み。

**Phase 13で検討（必要に応じて）**:

- [ ] ツール統合アーキテクチャ（CI/CD、DevRag、Markdownlint等の連携）

#### components/（Tier 4）

[ASSUMPTION: コンポーネント図は変更が多いため、必要に応じて作成]

### テンプレート（_templates）

**現状**: `docs/_templates/` ディレクトリに基本的な運用ドキュメントテンプレートは完備（プロセス、プレイブック、ランブック、ADR、チートシート等）。

**Phase 12で作成予定（Diátaxis軸テンプレート）**:

- [ ] `concept-template.md` - 概念説明テンプレート
  - 背景、定義、重要性、関連概念のセクション構成
- [ ] `tutorial-template.md` - チュートリアルテンプレート
  - 学習目標、前提条件、手順、検証、まとめのセクション構成
- [ ] `how-to-template.md` - ハウツーテンプレート
  - 目的、前提条件、手順、トラブルシューティング、関連リンクのセクション構成
- [ ] `reference-template.md` - リファレンステンプレート
  - 概要、構文、パラメータ、例、関連項目のセクション構成

**Phase 13で検討（C4軸テンプレート）**:

- [ ] `c4-context-template.md` - C4コンテキスト図テンプレート（Mermaid flowchart代替）
- [ ] `c4-containers-template.md` - C4コンテナ図テンプレート（Mermaid flowchart代替）

---

## 移行統計サマリー

| 分類 | ファイル数 | 備考 |
|------|-----------|------|
| **MIGRATE** | 25 | 新構造に移行 |
| **ARCHIVE** | 6 | アーカイブとして保存 |
| **DEPRECATE** | 4 | 新仕様に統合済み |
| **NEW** | 15 | 新規作成必要（Phase 12: 10, Phase 13: 5） |

---

## ユーザー確認必要項目

### 1. チュートリアル題材の選定

[SME_NEEDED: ドメイン固有チュートリアルの題材]

以下のチュートリアルについて、具体的な題材を選定してください：

- CFDシミュレーション入門：どのソフトウェア/ケースを使用するか？
- GISデータ処理入門：どのデータセット/ツールを使用するか？

### 2. C4コンテキスト図の対象

[SME_NEEDED: C4コンテキスト図の対象システム]

以下のシステムについてコンテキスト図を作成すべきか確認してください：

- 3docaフレームワーク自体の全体像
- CFDシミュレーションパイプライン
- GISデータ処理システム
- その他のドメイン固有システム

### 3. 移行タイミング

以下の移行オプションから選択してください：

- [ ] **即時移行**: 全ファイルを一括で移行
- [ ] **段階的移行**: 優先度の高いファイルから段階的に移行
- [ ] **新規作成優先**: 新構造のコンテンツを先に作成し、既存ファイルは後で移行

### 4. 既存ファイルの保持

移行完了後の`01-doc-framework/`の扱い：

- [ ] **削除**: 移行完了後に削除
- [ ] **アーカイブ**: `docs/archives/legacy/`に保存
- [ ] **シンボリックリンク**: 後方互換性のためリンクを残す

---

## 移行手順（参考）

### Phase 1: アーカイブディレクトリ作成

```bash
mkdir -p docs/archives/source-materials
mkdir -p docs/archives/reports
mkdir -p docs/archives/legacy
```

### Phase 2: アーカイブファイル移動

```bash
mv 01-doc-framework/9251*.md docs/archives/source-materials/
mv 01-doc-framework/4adoption-report.md docs/archives/reports/
```

### Phase 3: テンプレート移行

```bash
for f in 01-doc-framework/templates/*.md; do
  name=$(basename "$f" | sed 's/^[0-9]*//; s/-template//')
  cp "$f" "docs/_templates/${name}-template.md"
done
```

### Phase 4: 実例移行

```bash
# プロセス
cp 01-doc-framework/examples/0*process*.md docs/02_operations/01-processes/

# プレイブック
cp 01-doc-framework/examples/1*playbook*.md docs/02_operations/02-playbooks/

# ランブック
cp 01-doc-framework/examples/2*runbook*.md docs/02_operations/03-runbooks/
cp 01-doc-framework/examples/40*.md docs/02_operations/03-runbooks/

# リファレンス
cp 01-doc-framework/examples/30*.md docs/01_knowledge/reference/
```

### Phase 5: ガイド・仕様書移行

```bash
cp 01-doc-framework/1USAGE-GUIDE.md docs/01_knowledge/03-how-to/usage-guide.md
cp 01-doc-framework/3POLICY.md docs/01_knowledge/01-concepts/policy.md
# ... 以下同様
```

---

## 関連リンク

- [ギャップマーカー仕様](./01-GAP-MARKER-SPEC.md)
- [ティア設計仕様](./02-TIER-DESIGN-SPEC.md)
- [新ディレクトリ構造](../../README.md)

---

**作成日**: 2025-12-09
**更新日**: 2025-12-10
**バージョン**: 1.1
**ステータス**: Phase 12実行可能、Phase 13は要SME確認
