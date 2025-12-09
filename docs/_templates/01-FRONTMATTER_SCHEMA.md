# フロントマタースキーマ定義

devrag/RAG検索に最適化されたフロントマター仕様。

## 共通フィールド（全ドキュメント必須）

```yaml
---
title: "ドキュメントタイトル"           # 必須: 検索・表示用
type: concept                           # 必須: ドキュメントタイプ（下記参照）
category: "カテゴリ名"                  # 必須: 分類用
tags: [tag1, tag2]                      # 必須: 検索タグ（配列）
summary: |                              # 必須: 2-3文の要約（RAG検索コンテキスト用）
  このドキュメントの簡潔な説明。
  何について書かれているか、何ができるようになるか。
keywords:                               # 推奨: 検索キーワード
  - キーワード1
  - キーワード2
related:                                # 推奨: 関連ドキュメントへのパス
  - path/to/related-doc.md
version: "1.0.0"                        # 必須: ドキュメントバージョン
status: draft | review | published      # 必須: ステータス
created: "YYYY-MM-DD"                   # 必須: 作成日
updated: "YYYY-MM-DD"                   # 必須: 最終更新日
---
```

## typeフィールドの値

### Diátaxis軸 (01_knowledge/)

| type | 説明 | 用途 |
|------|------|------|
| `concept` | 説明・概念 | 背景、理論、設計意図 |
| `tutorial` | チュートリアル | 学習目的の手順 |
| `how-to` | ハウツーガイド | タスク遂行手順 |
| `reference` | リファレンス | 仕様、パラメータ一覧 |

### 運用軸 (02_operations/)

| type | 説明 | 用途 |
|------|------|------|
| `process` | プロセス定義 | ワークフロー全体 |
| `playbook` | プレイブック | 状況対応手順 |
| `runbook` | ランブック | 定常作業手順 |
| `cheatsheet` | チートシート | クイックリファレンス |

### C4軸 (03_architecture/)

| type | 説明 | 用途 |
|------|------|------|
| `architecture` | アーキテクチャ | 構造図・設計図 |

C4軸では追加で `level` フィールドを使用:
```yaml
level: context | container | component
```

## タイプ別追加フィールド

### tutorial

```yaml
estimated_time: "15分"                  # 所要時間の目安
difficulty: beginner | intermediate | advanced
prerequisites:                          # 前提となるドキュメント
  - path/to/prereq.md
```

### how-to / runbook

```yaml
prerequisites:                          # 前提条件
  - path/to/prereq.md
```

### playbook

```yaml
severity: high | medium | low           # 重要度
triggers:                               # 起動条件
  - "条件1"
  - "条件2"
owner: "責任者/チーム"
last_tested: "YYYY-MM-DD"               # 最終テスト日
```

### runbook

```yaml
frequency: "日次 | 週次 | 月次 | 随時"   # 実行頻度
estimated_time: "30分"                  # 所要時間
owner: "責任者"
executor: "実行者のロール"
```

### process

```yaml
owner: "責任者"
stakeholders:                           # 関係者
  - "関係者1"
triggers:                               # 開始トリガー
  - "トリガー条件"
frequency: "実行頻度"
```

### reference

```yaml
applies_to: "v1.0.0 - v2.0.0"          # 適用バージョン範囲
```

### architecture

```yaml
level: context | container | component  # C4レベル
parent_container: "親コンテナ名"        # Level 3の場合
```

## RAG最適化のポイント

### summaryフィールドの書き方

```yaml
# 良い例
summary: |
  iRIC Nays2DFloodでメッシュを生成する方法を説明します。
  河川形状データから計算用メッシュを作成し、品質検証まで行います。

# 悪い例
summary: "メッシュ生成について"
```

**ポイント**:
- 2-3文で具体的に
- 何ができるようになるか / 何が書かれているかを明記
- 検索されそうなキーワードを含める

### keywordsフィールドの選定

```yaml
keywords:
  - メッシュ生成
  - iRIC
  - Nays2DFlood
  - 河川シミュレーション
  - 格子生成
```

**ポイント**:
- 同義語・別名を含める
- 英語/日本語両方を検討
- 5-10個程度

### tagsとkeywordsの使い分け

| フィールド | 用途 | 例 |
|------------|------|-----|
| tags | カテゴリ分類、フィルタリング | `[mesh, iric, simulation]` |
| keywords | 全文検索、類似検索 | `[メッシュ, 格子, grid, mesh generation]` |

## チャンクサイズの考慮

devragのデフォルトチャンクサイズは500トークン。以下を意識:

- 各セクション（## 見出し）が独立して意味を持つように
- 前のセクションを読まなくても理解できる自己完結性
- 重要な用語は繰り返し記述してもOK

## 検証チェックリスト

ドキュメント作成時に確認:

- [ ] title: 検索結果で意味がわかるか
- [ ] type: 正しいタイプが指定されているか
- [ ] summary: 2-3文で具体的に書かれているか
- [ ] keywords: 検索されそうな用語が含まれているか
- [ ] related: 関連ドキュメントがリンクされているか
- [ ] status: 正しいステータスか
- [ ] updated: 最終更新日が正しいか
