# records/

プロジェクト記録を格納するディレクトリ。タスク履歴、品質レビュー、CI検証記録、Serenaメモリの参照を管理。

## ディレクトリ構成

```
records/
├── 01-tasks/       # Shrimpタスク履歴
├── 02-reviews/     # 品質レビュー記録
├── 03-ci/          # CI検証記録
├── 04-memories/    # Serenaメモリ参照
└── *.md            # プロジェクト計画・仕様
```

## 01-tasks/

Shrimp Task Managerのタスク履歴。

| ファイル | 説明 |
|----------|------|
| `tasks-summary.md` | タスクサマリー |
| `tasks-detail.md` | タスク詳細 |

## 02-reviews/

品質レビュー記録。日付付きレビューファイルとスクリプト。

| ファイル | 説明 |
|----------|------|
| `2025-12-02-*.md` | 日付付きレビューファイル |
| `check_frontmatter.py` | フロントマター検証スクリプト |
| `framework-coverage-report.md` | フレームワークカバレッジ |
| `schema-consistency-report.md` | スキーマ整合性レポート |

## 03-ci/

CI/CD検証記録。

| ファイル | 説明 |
|----------|------|
| `ci-test-report.md` | CI検証レポート |

## 04-memories/

Serenaメモリの参照用コピー。正式版は`.serena/memories/`。

| ファイル | 説明 |
|----------|------|
| `current_work_session.md` | 現在の作業セッション状態 |
| `document_framework_guide.md` | フレームワークガイド |

## プロジェクト計画・仕様

| ファイル | 説明 |
|----------|------|
| [IMPLEMENTATION-PLAN.md](./IMPLEMENTATION-PLAN.md) | 実装計画 |
| [TASK-HISTORY.md](./TASK-HISTORY.md) | タスク履歴 |
| [TASK-SPECIFICATION.md](./TASK-SPECIFICATION.md) | タスク仕様 |
| [git-history.md](./git-history.md) | Git履歴 |
| [mcp-config.md](./mcp-config.md) | MCP設定 |

---

*更新日: 2025-12-14*
