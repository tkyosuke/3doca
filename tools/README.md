# tools/

ツール、設定、アーカイブを格納するディレクトリ。

## ディレクトリ構成

```
tools/
├── 01-scripts/     # Pythonスクリプト
├── 02-models/      # DevRag用モデル
├── 03-styles/      # Vale用スタイル
└── 04-archives/    # アーカイブ・バックアップ
```

## 01-scripts/

ドキュメント品質検証用のPythonスクリプト。

| ファイル | 説明 |
|----------|------|
| `01-check_frontmatter.py` | フロントマター検証スクリプト |
| `02-coverage_report.py` | ドキュメントカバレッジレポート生成 |
| `03-verify_quality.py` | 品質検証スクリプト |

### 使用方法

```bash
# フロントマター検証
python tools/01-scripts/01-check_frontmatter.py docs/

# カバレッジレポート
python tools/01-scripts/02-coverage_report.py

# 品質検証
python tools/01-scripts/03-verify_quality.py docs/
```

## 02-models/

DevRag用の埋め込みモデルと設定ファイル。

| ファイル | 説明 |
|----------|------|
| `model.onnx` | ONNX形式の埋め込みモデル |
| `tokenizer.json` | トークナイザー設定 |
| `config.json` | モデル設定 |
| `devrag-config.json` | DevRag設定 |

## 03-styles/

Vale用のカスタムスタイル定義。

```
03-styles/
└── 3doca/
    ├── Frontmatter.yml   # フロントマター検証ルール
    └── Headings.yml      # 見出し検証ルール
```

### Vale設定

`.vale.ini`の`StylesPath`がこのディレクトリを参照：

```ini
StylesPath = tools/03-styles
```

## 04-archives/

旧バージョンのドキュメント、バックアップ、参照用ファイル。

| ファイル/フォルダ | 説明 |
|-------------------|------|
| `01-doc-framework/` | 旧フレームワーク定義（参照用） |
| `01-doc-framework.7z` | フレームワークのアーカイブ |
| `CLAUDE2.md` | 旧Claude設定 |
| `migration-log.md` | 移行ログ |
| `shrimp-rules.md` | Shrimpルール定義 |

---

*更新日: 2025-12-14*
