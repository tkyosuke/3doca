# MCP設定メモ (Codex / Claude 共通)

本ファイルはMCP設定の参照場所と同期手順をまとめたドキュメントです。設定ファイルそのものは本メモでは変更しません。

## 主な設定ファイルとデータ置き場
- Codex設定: `~/.codex/config.toml`
- 共通MCP設定: `~/.mmcp.json`
- Claude設定: `~/.claude.json`
- Shrimpローカル設定: `~/.shrimp-task-manager/.env` (例: `DATA_DIR=/home/tkyosuke/.shrimp-task-manager/data`, `TEMPLATES_USE=ja`, `ENABLE_GUI=true`)
- Shrimpタスク保存先: `~/.shrimp-task-manager/data/` 配下（グローバル `tasks.json` が現行の37件 pendingを保持）

## 主要MCPサーバー (command/args/env)
- shrimp-task-manager: `npx mcp-shrimp-task-manager`（env: `DATA_DIR`, `TEMPLATES_USE`, `ENABLE_GUI`）
- serena: `uvx --from git+https://github.com/oraios/serena serena start-mcp-server --context ide-assistant`
- filesystem: `uvx @modelcontextprotocol/server-filesystem` ※Codex側もuvxに統一済み
- brave-search: `mcp-server-brave-search`（env: `BRAVE_API_KEY` プレースホルダのまま）
- gitlab: `mcp-server-gitlab`（env: `GITLAB_TOKEN`, `GITLAB_API_URL=https://gitlab.com/api/v4`）
- その他: redis, context7, everything-search, postgres, obsidian, sequential-thinking

## 差分・整合状況
- `~/.codex/config.toml` の filesystem サーバーを `uvx @modelcontextprotocol/server-filesystem` に変更し、`~/.claude.json` / `~/.mmcp.json` と一致させています。
- `~/.mmcp.json` と `~/.claude.json` は同じサーバー定義を保持（参照のみ）。
- 設定ファイル編集は行わず、参照と同期手順を記録する方針です。

## 同期手順（別ホスト・別ユーザーで合わせたい場合）
1. `~/.mmcp.json` と `~/.claude.json` を比較し、必要なら同一内容にコピー（もしくはシンボリックリンクで共通化）。
2. Codex用は `~/.codex/config.toml` の `mcpServers` を参照し、Claude側とcommand/args/envが一致していることを確認（filesystemはuvxを使用）。
3. Shrimpのデータを共有する場合、`~/.shrimp-task-manager/.env` の `DATA_DIR` を同じパスに設定する。

## Brave APIキー設定（web検索復旧）
- 必要な環境変数: `BRAVE_API_KEY`
- 推奨設定例: シェルの秘密管理 (例: `pass`/`gopass`/`1password`/`aws secretsmanager`) から読み出すか、ログインシェルの rc ではなく専用の秘密ファイルに `export BRAVE_API_KEY=...` を置き、権限を600で管理。
- 直接ファイルへ平文を書かない。Gitなどにコミットしない。

