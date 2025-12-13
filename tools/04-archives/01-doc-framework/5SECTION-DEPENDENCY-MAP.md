---
title: "セクション間依存関係マップ"
description: "8ドキュメントタイプのセクション間依存関係を可視化したリファレンス"
tags: [dependency, mermaid, schema, reference]
category: reference
domain: documentation
difficulty: intermediate
created_at: 2025-12-06
updated_at: 2025-12-06
version: "1.0"
author: claude-code
document_id: REF-DOC-001
---

# セクション間依存関係マップ

## 概要

このドキュメントは、3docaフレームワークの8ドキュメントタイプにおけるセクション間の依存関係を可視化します。エージェントがドキュメント構造を理解し、適切な順序でセクションを作成するためのリファレンスです。

## 1. ドキュメントタイプ間の関係

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryBorderColor': '#1E1E2E', 'lineColor': '#89B4FA'}}}%%
flowchart TB
    subgraph Governance["ガバナンス層"]
        Policy[Policy<br/>方針定義]
        ADR[ADR<br/>技術決定]
    end

    subgraph Operational["運用層"]
        SOP[SOP<br/>標準作業手順]
        Playbook[Playbook<br/>判断指針]
    end

    subgraph Tactical["実行層"]
        Runbook[Runbook<br/>実行手順]
        Troubleshooting[Troubleshooting<br/>問題解決]
    end

    subgraph Reference["参照層"]
        Process[Process<br/>プロセス全体]
        Cheatsheet[Cheatsheet<br/>クイック参照]
    end

    Policy -->|"実装"| SOP
    Policy -->|"技術選択"| ADR
    ADR -->|"決定反映"| SOP
    SOP -->|"詳細化"| Runbook
    Playbook -->|"手順参照"| Runbook
    Runbook -->|"問題発生時"| Troubleshooting
    Process -->|"詳細手順"| Runbook
    Process -->|"判断指針"| Playbook
    Troubleshooting -->|"予防策"| SOP
    Cheatsheet -.->|"要約"| Runbook
    Cheatsheet -.->|"要約"| Process

    style Policy fill:#cba6f7,stroke-width:1px,color:#000
    style ADR fill:#f5c2e7,stroke-width:1px,color:#000
    style SOP fill:#89b4fa,stroke-width:1px,color:#000
    style Playbook fill:#94e2d5,stroke-width:1px,color:#000
    style Runbook fill:#a6e3a1,stroke-width:1px,color:#000
    style Troubleshooting fill:#f9e2af,stroke-width:1px,color:#000
    style Process fill:#fab387,stroke-width:1px,color:#000
    style Cheatsheet fill:#eba0ac,stroke-width:1px,color:#000
```

## 2. プロセスドキュメント依存関係

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryBorderColor': '#1E1E2E', 'lineColor': '#89B4FA'}}}%%
flowchart LR
    subgraph Process["プロセスドキュメント"]
        P_Overview[概要]
        P_Flow[プロセスフロー<br/>Mermaid必須]
        P_Steps[ステップ詳細<br/>min 3]
        P_Gate[品質ゲート<br/>チェックリスト]
        P_Metrics[メトリクスとKPI]
    end

    P_Overview --> P_Flow
    P_Flow --> P_Steps
    P_Steps --> P_Gate
    P_Gate --> P_Metrics

    style P_Flow fill:#4ade80,stroke-width:1px,color:#000
    style P_Gate fill:#fbbf24,stroke-width:1px,color:#000
```

**依存関係ルール:**
- `ステップ詳細` → `プロセスフロー`: ステップはフローで定義されたステップに対応
- `品質ゲート` → `ステップ詳細`: 品質ゲートは各ステップの完了基準を定義
- `メトリクスとKPI` → `品質ゲート`: メトリクスは品質ゲートの達成度を測定

## 3. プレイブック依存関係

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryBorderColor': '#1E1E2E', 'lineColor': '#89B4FA'}}}%%
flowchart LR
    subgraph Playbook["プレイブック"]
        PB_Overview[概要]
        PB_Framework[意思決定<br/>フレームワーク<br/>Mermaid必須]
        PB_Scenarios[シナリオ別<br/>対応戦略<br/>min 3]
        PB_Tools[判断支援ツール]
        PB_Cases[事例集<br/>min 2]
        PB_Escalation[エスカレーション<br/>基準]
    end

    PB_Overview --> PB_Framework
    PB_Framework --> PB_Scenarios
    PB_Framework --> PB_Tools
    PB_Scenarios --> PB_Cases
    PB_Scenarios --> PB_Escalation

    style PB_Framework fill:#4ade80,stroke-width:1px,color:#000
    style PB_Scenarios fill:#fbbf24,stroke-width:1px,color:#000
```

**依存関係ルール:**
- `シナリオ別対応戦略` → `意思決定フレームワーク`: シナリオはフローの分岐先
- `事例集` → `シナリオ別対応戦略`: 事例はシナリオに対応した記録
- `判断支援ツール` → `意思決定フレームワーク`: ツールはフレームワークでの判断を補助

## 4. ランブック依存関係

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryBorderColor': '#1E1E2E', 'lineColor': '#89B4FA'}}}%%
flowchart LR
    subgraph Runbook["ランブック"]
        RB_Overview[概要]
        RB_Pre[前提条件]
        RB_Check[事前確認<br/>チェックリスト]
        RB_Exec[実行手順<br/>コード必須]
        RB_Verify[検証<br/>チェックリスト]
        RB_Trouble[トラブル<br/>シューティング<br/>min 2]
        RB_Rollback[ロールバック<br/>手順]
    end

    RB_Overview --> RB_Pre
    RB_Pre --> RB_Check
    RB_Check --> RB_Exec
    RB_Exec --> RB_Verify
    RB_Exec --> RB_Trouble
    RB_Exec --> RB_Rollback

    style RB_Exec fill:#4ade80,stroke-width:1px,color:#000
    style RB_Rollback fill:#f87171,stroke-width:1px,color:#000
```

**依存関係ルール:**
- `実行手順` → `前提条件`: 手順は前提条件が満たされた状態で実行
- `検証チェックリスト` → `実行手順`: 検証は実行手順の完了を確認
- `トラブルシューティング` → `実行手順`: 実行中の問題に対応
- `ロールバック手順` → `実行手順`: ロールバックは実行手順の逆操作

## 5. トラブルシューティング依存関係

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryBorderColor': '#1E1E2E', 'lineColor': '#89B4FA'}}}%%
flowchart LR
    subgraph Troubleshooting["トラブルシューティング"]
        TS_Overview[概要]
        TS_Symptom[症状<br/>エラーメッセージ]
        TS_Root[根本原因]
        TS_Solution[解決手順<br/>コード必須]
        TS_Verify[検証方法<br/>チェックリスト]
        TS_Prevent[予防策]
        TS_Lesson[教訓と改善点]
    end

    TS_Overview --> TS_Symptom
    TS_Symptom --> TS_Root
    TS_Root --> TS_Solution
    TS_Root --> TS_Prevent
    TS_Solution --> TS_Verify
    TS_Root --> TS_Lesson
    TS_Solution --> TS_Lesson

    style TS_Symptom fill:#f87171,stroke-width:1px,color:#000
    style TS_Root fill:#fbbf24,stroke-width:1px,color:#000
    style TS_Solution fill:#4ade80,stroke-width:1px,color:#000
```

**依存関係ルール:**
- `根本原因` → `症状`: 原因分析は症状の観察に基づく
- `解決手順` → `根本原因`: 解決策は原因に対処
- `検証方法` → `解決手順`: 検証は解決手順の効果を確認
- `予防策` → `根本原因`: 予防策は原因の再発を防ぐ
- `教訓と改善点` → `根本原因`, `解決手順`: 原因分析と解決過程から導出

## 6. ADR依存関係

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryBorderColor': '#1E1E2E', 'lineColor': '#89B4FA'}}}%%
flowchart LR
    subgraph ADR["ADR（技術決定記録）"]
        ADR_Context[背景と課題]
        ADR_Criteria[評価基準]
        ADR_Options[検討した選択肢<br/>min 2]
        ADR_Compare[選択肢比較表<br/>テーブル必須]
        ADR_Decision[決定]
        ADR_Impact[影響]
        ADR_Impl[実装計画]
    end

    ADR_Context --> ADR_Criteria
    ADR_Context --> ADR_Options
    ADR_Criteria --> ADR_Compare
    ADR_Options --> ADR_Compare
    ADR_Compare --> ADR_Decision
    ADR_Decision --> ADR_Impact
    ADR_Decision --> ADR_Impl

    style ADR_Compare fill:#89b4fa,stroke-width:1px,color:#000
    style ADR_Decision fill:#4ade80,stroke-width:1px,color:#000
```

**依存関係ルール:**
- `評価基準` → `背景と課題`: 評価基準は課題に基づいて定義
- `検討した選択肢` → `背景と課題`: 選択肢は課題を解決するためのもの
- `選択肢比較表` → `評価基準`, `検討した選択肢`: 比較表は評価基準で選択肢を評価
- `決定` → `選択肢比較表`: 決定は比較結果に基づく
- `影響` → `決定`: 影響は決定の結果として発生
- `実装計画` → `決定`: 実装は決定内容を具体化

## 7. チートシート依存関係

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryBorderColor': '#1E1E2E', 'lineColor': '#89B4FA'}}}%%
flowchart LR
    subgraph Cheatsheet["チートシート"]
        CS_Top5[最頻出コマンド<br/>TOP 5<br/>テーブル必須]
        CS_Quick[クイックスタート<br/>max 200語]
        CS_Basic[基本コマンド<br/>テーブル必須]
        CS_Pattern[頻出パターン]
        CS_Trouble[クイック<br/>トラブルシュート]
        CS_Advanced[応用例]
    end

    CS_Top5 --> CS_Quick
    CS_Quick --> CS_Basic
    CS_Basic --> CS_Pattern
    CS_Basic --> CS_Trouble
    CS_Basic --> CS_Advanced

    style CS_Top5 fill:#4ade80,stroke-width:1px,color:#000
    style CS_Basic fill:#89b4fa,stroke-width:1px,color:#000
```

**依存関係ルール:**
- `頻出パターン` → `基本コマンド`: パターンは基本コマンドの組み合わせ
- `応用例` → `基本コマンド`: 応用例は基本コマンドを使用
- `クイックトラブルシュート` → `基本コマンド`: トラブルシュートは基本操作の問題を扱う

## 8. Policy / SOP 依存関係

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryBorderColor': '#1E1E2E', 'lineColor': '#89B4FA'}}}%%
flowchart TB
    subgraph Policy["ポリシー"]
        POL_Purpose[目的]
        POL_Scope[適用範囲]
        POL_Roles[役割と責任<br/>テーブル必須]
        POL_Statements[ポリシー声明<br/>番号リスト]
        POL_Compliance[コンプライアンス]
        POL_Enforce[執行]
    end

    subgraph SOP["標準作業手順書"]
        SOP_Purpose[目的]
        SOP_Scope[適用範囲]
        SOP_Pre[前提条件<br/>テーブル必須]
        SOP_Steps[手順<br/>番号ステップ]
        SOP_Quality[品質メトリクス<br/>テーブル必須]
        SOP_Trouble[トラブル<br/>シューティング]
        SOP_Rollback[ロールバック]
    end

    POL_Purpose --> POL_Scope
    POL_Scope --> POL_Roles
    POL_Roles --> POL_Statements
    POL_Statements --> POL_Compliance
    POL_Compliance --> POL_Enforce

    SOP_Purpose --> SOP_Scope
    SOP_Scope --> SOP_Pre
    SOP_Pre --> SOP_Steps
    SOP_Steps --> SOP_Quality
    SOP_Steps --> SOP_Trouble
    SOP_Steps --> SOP_Rollback

    POL_Statements -->|"実装"| SOP_Steps

    style POL_Statements fill:#cba6f7,stroke-width:1px,color:#000
    style SOP_Steps fill:#89b4fa,stroke-width:1px,color:#000
```

## 9. 統合依存関係マップ

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'primaryBorderColor': '#1E1E2E', 'lineColor': '#89B4FA'}}}%%
stateDiagram-v2
    direction LR

    [*] --> Policy: ガバナンス定義
    Policy --> ADR: 技術選択
    Policy --> SOP: 実装手順化

    ADR --> SOP: 決定反映

    SOP --> Runbook: 詳細化
    SOP --> Playbook: 判断指針

    Playbook --> Runbook: 手順参照
    Runbook --> Troubleshooting: 問題発生

    Troubleshooting --> SOP: 予防策反映

    Process --> Runbook: 詳細手順
    Process --> Playbook: 判断指針

    Cheatsheet --> Process: 要約
    Cheatsheet --> Runbook: 要約
```

## 10. ドキュメント作成フロー（推奨順序）

| 順序 | ドキュメントタイプ | 前提条件 | 成果物 |
|------|-------------------|---------|--------|
| 1 | Policy | なし | 組織方針 |
| 2 | ADR | Policy（該当する場合） | 技術決定記録 |
| 3 | Process | なし | 全体フロー |
| 4 | SOP | Policy, ADR | 標準手順 |
| 5 | Playbook | Process | 判断指針 |
| 6 | Runbook | SOP, Playbook | 実行手順 |
| 7 | Cheatsheet | Process, Runbook | 参照カード |
| 8 | Troubleshooting | 運用実績後 | 問題解決記録 |

## 関連ドキュメント

- [USAGE-GUIDE.md](./1USAGE-GUIDE.md) - テンプレート使用ガイド
- [schema/README.md](./schema/README.md) - スキーマ定義リファレンス
- [POLICY.md](./3POLICY.md) - プロジェクトポリシー
