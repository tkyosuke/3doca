---
# === 必須：識別情報 ===
document_id: "ADR-DOMAIN-NNN"  # ADR-data-001, ADR-arch-001等
title: "<!-- TEMPLATE: ADR番号と決定事項タイトル（例: ADR-001: データ品質検証ツール選定） -->"
type: adr
version: "1.0"
status: <!-- TEMPLATE: proposed | accepted | rejected | deprecated | superseded -->

# === 所有権 ===
owner: "@team-name"
author: "<!-- TEMPLATE: 作成者名 -->"
created: <!-- TEMPLATE: YYYY-MM-DD -->
updated: <!-- TEMPLATE: YYYY-MM-DD -->
decision_date: <!-- TEMPLATE: YYYY-MM-DD（決定日） -->
decision_makers:
  - <!-- TEMPLATE: 決定者名1 -->
  - <!-- TEMPLATE: 決定者名2 -->

# === RAG最適化 ===
tags:
  - adr
  - <!-- TEMPLATE: カテゴリタグ（例: architecture, tooling, data-analysis） -->
  - <!-- TEMPLATE: 技術タグ（例: python, database, framework） -->
key_concepts:
  - "<!-- TEMPLATE: セマンティック用語1（例: アーキテクチャ決定、技術選定） -->"
  - "<!-- TEMPLATE: セマンティック用語2（例: 評価基準、トレードオフ） -->"
summary: "<!-- TEMPLATE: 検索結果用の一文説明（150文字以内） -->"

# === ドメインコンテキスト ===
category: decision
domain: <!-- TEMPLATE: data-analysis | cfd | gis | architecture | infrastructure -->
difficulty: <!-- TEMPLATE: beginner | intermediate | advanced -->
decision_type: <!-- TEMPLATE: strategic | tactical | technical -->
audience: <!-- TEMPLATE: developers | operators | architects | scientists -->

# === 関連ドキュメント ===
related_docs:
  - path: "<!-- TEMPLATE: /path/to/superseded-adr.md -->"
    relationship: "superseded"  # implements | governed-by | references | depends-on | superseded
supersedes: <!-- TEMPLATE: 置き換えるADR番号（該当する場合） -->
superseded_by: <!-- TEMPLATE: このADRを置き換えたADR番号（該当する場合） -->
related_decisions:
  - <!-- TEMPLATE: 関連ADR1 -->
  - <!-- TEMPLATE: 関連ADR2 -->

# === メンテナンス ===
next_review: <!-- TEMPLATE: YYYY-MM-DD -->
review_cycle_days: 365
---

# <!-- TEMPLATE: ADR番号 -->: <!-- TEMPLATE: 決定事項タイトル -->

---

## 必須セクション一覧

このテンプレートには以下の必須セクションが含まれています：

| セクション | 目的 | 省略時の影響 |
|-----------|------|-------------|
| コンテキスト | 決定の背景 | なぜその決定が必要だったか不明 |
| 検討した選択肢 | 比較検討結果 | 他の選択肢を検討したか不明 |
| 決定 | 選択した内容と理由 | 決定内容が曖昧 |
| 結果 | 影響と受け入れた制約 | 決定の影響範囲が不明 |

---

**ステータス**: <!-- TEMPLATE: 🟢 Accepted | 🟡 Proposed | 🔴 Rejected | ⚫ Deprecated | 🔵 Superseded -->
**決定日**: <!-- TEMPLATE: YYYY-MM-DD -->
**決定者**: <!-- TEMPLATE: 決定者名（カンマ区切り） -->

## 📋 背景と課題

<!--
なぜ必要か: 決定の背景と理由を記録し、将来の参照時に文脈を理解できるようにするため
省略するとどうなるか: なぜその決定が必要だったか、将来理解できなくなる
-->

### 現状の課題

<!-- TEMPLATE: 2-3文で現在直面している課題を記述 -->
<!-- 例: 現在のデータ品質検証プロセスは手動で実施されており、検証漏れや人的ミスが発生しています。データパイプラインの規模拡大に伴い、体系的な品質検証ツールの導入が必要です。 -->

### ビジネス要件

- <!-- TEMPLATE: ビジネス要件1 -->
- <!-- TEMPLATE: ビジネス要件2 -->
- <!-- TEMPLATE: ビジネス要件3 -->

### 技術的制約

- <!-- TEMPLATE: 技術的制約1（例: Python 3.9以上で動作すること） -->
- <!-- TEMPLATE: 技術的制約2 -->
- <!-- TEMPLATE: 技術的制約3 -->

### 決定が必要な理由

<!-- TEMPLATE: なぜ今この決定が必要なのかを説明 -->

## 🎯 評価基準

<!--
なぜ必要か: 選択肢の評価基準を明確化し、客観的な比較を可能にするため
省略するとどうなるか: 主観的な判断で一貫性のない選択になる
-->

**⚠️ [重要]** 選択肢の評価に使用する基準を明確化

| 基準 | 重要度 | 説明 |
|------|--------|------|
| **<!-- TEMPLATE: 基準1（例: 精度） -->** | <!-- TEMPLATE: 高 / 中 / 低 --> | <!-- TEMPLATE: 基準の説明 --> |
| **<!-- TEMPLATE: 基準2（例: 処理速度） -->** | <!-- TEMPLATE: 高 / 中 / 低 --> | <!-- TEMPLATE: 基準の説明 --> |
| **<!-- TEMPLATE: 基準3（例: 保守性） -->** | <!-- TEMPLATE: 高 / 中 / 低 --> | <!-- TEMPLATE: 基準の説明 --> |
| **<!-- TEMPLATE: 基準4（例: コスト） -->** | <!-- TEMPLATE: 高 / 中 / 低 --> | <!-- TEMPLATE: 基準の説明 --> |
| **<!-- TEMPLATE: 基準5（例: 学習コスト） -->** | <!-- TEMPLATE: 高 / 中 / 低 --> | <!-- TEMPLATE: 基準の説明 --> |

### 重み付け

重要度が「高」の基準を優先的に評価します。

## 🔍 検討した選択肢

<!--
なぜ必要か: 複数の選択肢を検討したことを示し、決定の妥当性を証明するため
省略するとどうなるか: 他の選択肢を検討したか不明で、決定の根拠が弱くなる
-->

### 選択肢1: <!-- TEMPLATE: 選択肢名 -->

<!--
なぜ必要か: 各選択肢の特徴を明確化
省略するとどうなるか: 選択肢の比較ができない
-->

**概要**: <!-- TEMPLATE: 選択肢の概要 -->

**長所**:
- ✅ <!-- TEMPLATE: 長所1 -->
- ✅ <!-- TEMPLATE: 長所2 -->
- ✅ <!-- TEMPLATE: 長所3 -->

**短所**:
- ❌ <!-- TEMPLATE: 短所1 -->
- ❌ <!-- TEMPLATE: 短所2 -->
- ❌ <!-- TEMPLATE: 短所3 -->

**コスト**: <!-- TEMPLATE: 初期コスト、運用コスト -->

**参考**: <!-- TEMPLATE: 公式サイトURL、ドキュメントURL -->

---

### 選択肢2: <!-- TEMPLATE: 選択肢名 -->

**概要**: <!-- TEMPLATE: 選択肢の概要 -->

**長所**:
- ✅ <!-- TEMPLATE: 長所1 -->
- ✅ <!-- TEMPLATE: 長所2 -->
- ✅ <!-- TEMPLATE: 長所3 -->

**短所**:
- ❌ <!-- TEMPLATE: 短所1 -->
- ❌ <!-- TEMPLATE: 短所2 -->
- ❌ <!-- TEMPLATE: 短所3 -->

**コスト**: <!-- TEMPLATE: 初期コスト、運用コスト -->

**参考**: <!-- TEMPLATE: 公式サイトURL、ドキュメントURL -->

---

### 選択肢3: <!-- TEMPLATE: 選択肢名 -->

**⚠️ 最低3つの選択肢を検討することを推奨**

**概要**: <!-- TEMPLATE: 選択肢の概要 -->

**長所**:
- ✅ <!-- TEMPLATE: 長所1 -->
- ✅ <!-- TEMPLATE: 長所2 -->
- ✅ <!-- TEMPLATE: 長所3 -->

**短所**:
- ❌ <!-- TEMPLATE: 短所1 -->
- ❌ <!-- TEMPLATE: 短所2 -->
- ❌ <!-- TEMPLATE: 短所3 -->

**コスト**: <!-- TEMPLATE: 初期コスト、運用コスト -->

**参考**: <!-- TEMPLATE: 公式サイトURL、ドキュメントURL -->

## 📊 選択肢比較表

| 評価基準 | 選択肢1 | 選択肢2 | 選択肢3 |
|---------|---------|---------|---------|
| **<!-- TEMPLATE: 基準1 -->** | <!-- TEMPLATE: ◎/○/△/× --> | <!-- TEMPLATE: ◎/○/△/× --> | <!-- TEMPLATE: ◎/○/△/× --> |
| **<!-- TEMPLATE: 基準2 -->** | <!-- TEMPLATE: ◎/○/△/× --> | <!-- TEMPLATE: ◎/○/△/× --> | <!-- TEMPLATE: ◎/○/△/× --> |
| **<!-- TEMPLATE: 基準3 -->** | <!-- TEMPLATE: ◎/○/△/× --> | <!-- TEMPLATE: ◎/○/△/× --> | <!-- TEMPLATE: ◎/○/△/× --> |
| **<!-- TEMPLATE: 基準4 -->** | <!-- TEMPLATE: ◎/○/△/× --> | <!-- TEMPLATE: ◎/○/△/× --> | <!-- TEMPLATE: ◎/○/△/× --> |
| **<!-- TEMPLATE: 基準5 -->** | <!-- TEMPLATE: ◎/○/△/× --> | <!-- TEMPLATE: ◎/○/△/× --> | <!-- TEMPLATE: ◎/○/△/× --> |
| **総合評価** | <!-- TEMPLATE: 点数 --> | <!-- TEMPLATE: 点数 --> | <!-- TEMPLATE: 点数 --> |

**凡例**: ◎ 優秀 / ○ 良好 / △ 可 / × 不可

## ✅ 決定

<!--
なぜ必要か: 最終決定内容と理由を明確に記録するため
省略するとどうなるか: 決定内容が曖昧で、実装時に混乱する
-->

### 選択した解決策

**選択**: **<!-- TEMPLATE: 選択した選択肢名 -->**

### 選択理由

**[重要]** なぜこの選択肢を選んだのか、具体的な理由を記述

<!-- TEMPLATE: 選択理由を詳細に記述 -->
<!-- 例: Great Expectationsを選定した理由は以下の通りです。
1. 宣言的な品質ルール定義により、保守性が高い
2. Pythonネイティブで既存のパイプラインと統合が容易
3. コミュニティが活発で、ドキュメントが充実している
4. データプロファイリング機能により、ルール作成の学習コストが低い
-->

### 評価基準との整合性

- **<!-- TEMPLATE: 基準1 -->**: <!-- TEMPLATE: この基準に対する選択肢の評価 -->
- **<!-- TEMPLATE: 基準2 -->**: <!-- TEMPLATE: この基準に対する選択肢の評価 -->
- **<!-- TEMPLATE: 基準3 -->**: <!-- TEMPLATE: この基準に対する選択肢の評価 -->

## 📈 影響

<!--
なぜ必要か: 決定の影響範囲を明確化し、受け入れるトレードオフを記録するため
省略するとどうなるか: 決定の影響が理解されず、予期しない問題が発生する
-->

### ポジティブな影響

**✅ Good**:
- <!-- TEMPLATE: ポジティブな影響1 -->
- <!-- TEMPLATE: ポジティブな影響2 -->
- <!-- TEMPLATE: ポジティブな影響3 -->

### ネガティブな影響

**❌ Bad**:
- <!-- TEMPLATE: ネガティブな影響1 -->
- <!-- TEMPLATE: ネガティブな影響2 -->
- <!-- TEMPLATE: ネガティブな影響3 -->

### リスクと軽減策

| リスク | 影響度 | 確率 | 軽減策 |
|--------|--------|------|--------|
| <!-- TEMPLATE: リスク1 --> | <!-- TEMPLATE: 高/中/低 --> | <!-- TEMPLATE: 高/中/低 --> | <!-- TEMPLATE: 軽減策 --> |
| <!-- TEMPLATE: リスク2 --> | <!-- TEMPLATE: 高/中/低 --> | <!-- TEMPLATE: 高/中/低 --> | <!-- TEMPLATE: 軽減策 --> |

### 影響を受けるステークホルダー

- **<!-- TEMPLATE: ステークホルダー1（例: データエンジニア） -->**: <!-- TEMPLATE: 影響内容 -->
- **<!-- TEMPLATE: ステークホルダー2（例: データアナリスト） -->**: <!-- TEMPLATE: 影響内容 -->
- **<!-- TEMPLATE: ステークホルダー3 -->**: <!-- TEMPLATE: 影響内容 -->

## 🔧 実装計画

### 検証期間

- **開始日**: <!-- TEMPLATE: YYYY-MM-DD -->
- **終了日**: <!-- TEMPLATE: YYYY-MM-DD -->
- **期間**: <!-- TEMPLATE: X週間 -->

### 実装ステップ

1. **フェーズ1**: <!-- TEMPLATE: フェーズ名（例: PoC実施） -->
   - <!-- TEMPLATE: タスク1 -->
   - <!-- TEMPLATE: タスク2 -->

2. **フェーズ2**: <!-- TEMPLATE: フェーズ名（例: パイロット導入） -->
   - <!-- TEMPLATE: タスク1 -->
   - <!-- TEMPLATE: タスク2 -->

3. **フェーズ3**: <!-- TEMPLATE: フェーズ名（例: 本番展開） -->
   - <!-- TEMPLATE: タスク1 -->
   - <!-- TEMPLATE: タスク2 -->

### 成功基準

- [ ] <!-- TEMPLATE: 成功基準1（例: 品質検証時間が50%削減） -->
- [ ] <!-- TEMPLATE: 成功基準2（例: 検証漏れゼロを3ヶ月達成） -->
- [ ] <!-- TEMPLATE: 成功基準3 -->

## 📝 補足情報

### 検証結果

<!-- TEMPLATE: 検証期間中に実施したテストや評価の結果 -->

### 代替案検討の経緯

<!-- TEMPLATE: 各選択肢を検討した経緯や議論の内容 -->

### 参考資料

- <!-- TEMPLATE: 参考資料1（公式ドキュメント、論文等） -->
- <!-- TEMPLATE: 参考資料2 -->
- <!-- TEMPLATE: 参考資料3 -->

### 関連ADR

- [<!-- TEMPLATE: 関連ADR番号 -->](<!-- TEMPLATE: パス -->) - <!-- TEMPLATE: 関連内容 -->

## 🔄 レビューと更新

### レビュー履歴

| 日付 | レビュアー | コメント | アクション |
|------|-----------|---------|----------|
| <!-- TEMPLATE: YYYY-MM-DD --> | <!-- TEMPLATE: 名前 --> | <!-- TEMPLATE: コメント --> | <!-- TEMPLATE: 対応内容 --> |

### 再評価トリガー

以下の条件が発生した場合、この決定を再評価します：

- <!-- TEMPLATE: トリガー1（例: 選定ツールの重大な脆弱性発見） -->
- <!-- TEMPLATE: トリガー2（例: ビジネス要件の大幅な変更） -->
- <!-- TEMPLATE: トリガー3（例: 1年経過後の定期レビュー） -->

### 次回レビュー予定

**予定日**: <!-- TEMPLATE: YYYY-MM-DD -->

---

**承認**: <!-- TEMPLATE: 承認者名、承認日 -->
**最終更新**: <!-- TEMPLATE: YYYY-MM-DD -->
**バージョン**: 1.0
