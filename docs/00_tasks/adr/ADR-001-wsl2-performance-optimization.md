---
title: "ADR-001: WSL2パフォーマンス最適化とOOMクラッシュ対策"
type: adr
category: architecture-decision
tags: [adr, wsl2, performance, memory, oom]
summary: WSL2環境でのOOMクラッシュと連鎖障害を防ぐための.wslconfig最適化設定を決定。
status: accepted
created: "2024-12-10"
updated: "2024-12-10"
---

# ADR-001: WSL2パフォーマンス最適化とOOMクラッシュ対策

## ステータス

**採用** - 2024-12-10

## コンテキスト

WSL2環境でWindsurfおよびClaude Codeを使用中に以下の問題が発生していた：

1. **動作が遅い** - CPU/メモリリソースがデフォルト設定で不足
2. **連鎖クラッシュ** - Windsurf上でWSLを起動中、全プロセスが連鎖的に終了する
3. **OOM Killer発動** - メモリ不足によりnodeプロセスが強制終了される

### 診断結果

```
=== OOM Killer履歴 ===
claude invoked oom-killer → node killed (total-vm:35MB, anon-rss:2.3GB)
```

| 項目 | 問題発覚時の値 |
|------|----------------|
| CPU割当 | 4コア（12コア24スレッド中） |
| スワップ | 2GB（使用率33%） |
| .wslconfig | 未作成（デフォルト設定） |
| Cドライブ | 86%使用 |

### 連鎖クラッシュの原因分析

```
OOM発生 → nodeプロセスkill → Windsurf Server停止 → 全ターミナル終了
```

主な原因：
- WSL2のデフォルトメモリ割当が不十分
- 複数のextensionHostプロセスがメモリを蓄積（4日間で6個以上、計3GB+）
- スワップ領域が小さくOOM回避の余地がない

## 決定

`.wslconfig`を作成し、以下の設定を適用する：

```ini
[wsl2]
# CPU: 12論理プロセッサを割当（24スレッド中の半分）
processors=12

# メモリ: 20GBに増加（OOM対策強化）
memory=20GB

# スワップ: 6GB
swap=6GB

# ページレポーティング: メモリ解放を有効化
pageReporting=true

# ネストされた仮想化
nestedVirtualization=true

# カーネルのメモリ回収を積極的に
[experimental]
autoMemoryReclaim=gradual
```

### 設定値の根拠

| 項目 | 値 | 根拠 |
|------|-----|------|
| processors | 12 | Ryzen 9 5900X（24スレッド）の半分。Windows側にも余裕を残す |
| memory | 20GB | 物理メモリ32GB想定。OOM発生時のログからnodeが2.3GB使用しており、複数プロセスで10GB以上必要 |
| swap | 6GB | メモリ逼迫時のバッファ。OOM発生を遅延させる |
| autoMemoryReclaim | gradual | 未使用メモリを段階的に解放し、Windows側に返却 |

## 結果

### 期待される効果

1. **OOM発生の大幅抑制** - メモリ20GB + スワップ6GBで十分な余裕
2. **処理速度向上** - CPU 4→12で3倍の並列処理能力
3. **連鎖クラッシュの防止** - OOMが発生しにくくなりnodeプロセスが安定

### 適用手順

```powershell
# PowerShell（管理者）またはcmdで実行
wsl --shutdown

# その後WSLを再起動
wsl
```

### 追加の推奨対策

1. **ログのクリーンアップ**（古いプロセス蓄積防止）
   ```bash
   rm -rf ~/.windsurf-server/data/logs/*
   rm -rf ~/.vscode-server/data/logs/*
   ```

2. **定期的なWSL再起動** - 週1回程度でメモリリセット

3. **不要な拡張機能の無効化** - extensionHostプロセスの削減

## 参考資料

- [VSCode remote server OOM issue #221722](https://github.com/microsoft/vscode/issues/221722)
- [WSL crashes with Catastrophic failure #13263](https://github.com/microsoft/WSL/issues/13263)
- [WSL crash recovery issue #265301](https://github.com/microsoft/vscode/issues/265301)
- [Microsoft WSL Troubleshooting](https://learn.microsoft.com/en-us/windows/wsl/troubleshooting)
- [How to fix WSL2 crashing mid compile](https://blog.tymscar.com/posts/wsloom/)

## 変更履歴

| 日付 | 変更内容 |
|------|----------|
| 2024-12-10 | 初版作成。.wslconfig設定を決定 |
