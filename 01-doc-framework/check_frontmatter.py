#!/usr/bin/env python3
"""
check_frontmatter.py - 9251205claude.mdフレームワーク準拠フロントマター検証スクリプト

機能:
- document_id形式検証（TYPE-DOMAIN-NNN）
- key_concepts配列検証
- related_docs配列とrelationship値検証
- next_review/review_cycle_days整合性検証
- ドキュメントタイプ別必須セクション検証
- CI/CD連携対応（終了コード、JSON出力）

終了コード:
- 0: 成功（エラーなし）
- 1: エラーあり（必須フィールド欠落、形式不正）
- 2: 警告あり（推奨フィールド欠落）

使用方法:
  python check_frontmatter.py [--format json] [--schema-dir PATH] [--check-sections]
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

import yaml

# =============================================================================
# 定数定義
# =============================================================================

# document_id形式: TYPE-DOMAIN-NNN (例: PRC-DATA-001, PLB-INC-002)
DOCUMENT_ID_PATTERN = re.compile(r'^[A-Z]{2,4}-[A-Z]{2,4}-\d{3}$')

# ADR形式も許容: ADR-NNNN
ADR_ID_PATTERN = re.compile(r'^ADR-\d{4}$')

# 有効なドキュメントタイプ
VALID_TYPES = ['policy', 'sop', 'playbook', 'runbook', 'cheatsheet', 'adr',
               'process', 'troubleshooting', 'guide', 'specification']

# 有効なステータス
VALID_STATUSES = ['draft', 'review', 'approved', 'active', 'deprecated', 'superseded']

# 有効なrelationship値
VALID_RELATIONSHIPS = [
    'implements',      # このドキュメントがそのドキュメントを実装
    'governed-by',     # このドキュメントがそのドキュメントの管理下
    'references',      # 単純な参照関係
    'depends-on',      # 前提条件として依存
    'escalates-to',    # 失敗時のエスカレーション先
    'supersedes',      # このドキュメントが置き換える
    'superseded-by'    # このドキュメントを置き換えるもの
]

# 有効なドメイン
VALID_DOMAINS = ['infrastructure', 'security', 'data', 'application',
                 'scientific', 'operations', 'documentation',
                 'data-analysis', 'cfd', 'gis', 'visualization']  # 後方互換性

# 有効なオーディエンス
VALID_AUDIENCES = ['developers', 'operators', 'architects', 'scientists', 'all']

# 必須フィールド（9251205claude.md準拠）
REQUIRED_FIELDS = [
    'document_id', 'title', 'type', 'version', 'status',
    'owner', 'author', 'created', 'updated',
    'tags', 'key_concepts', 'summary',
    'domain', 'audience'
]

# 推奨フィールド
RECOMMENDED_FIELDS = [
    'next_review', 'review_cycle_days', 'related_docs',
    'difficulty', 'priority'
]

# 後方互換性マッピング
LEGACY_FIELD_MAPPING = {
    'category': 'type',
    'created_at': 'created',
    'updated_at': 'updated',
    'description': 'summary'
}

# =============================================================================
# YAML解析
# =============================================================================

def extract_frontmatter(file_path: Path) -> tuple[dict | None, str]:
    """YAMLフロントマターを抽出して解析する"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if not content.startswith('---'):
        return None, content

    parts = content.split('---', 2)
    if len(parts) < 3:
        return None, content

    frontmatter_text = parts[1]
    body = parts[2] if len(parts) > 2 else ''

    try:
        # YAMLとして解析（コメント付きでも対応）
        frontmatter = yaml.safe_load(frontmatter_text)
        if frontmatter is None:
            frontmatter = {}
        return frontmatter, body
    except yaml.YAMLError:
        # YAMLパースエラー時は簡易的な行解析にフォールバック
        frontmatter = parse_frontmatter_fallback(frontmatter_text)
        return frontmatter, body


def parse_frontmatter_fallback(text: str) -> dict:
    """YAMLパースエラー時のフォールバック解析"""
    result = {}
    current_key = None
    current_array = None

    for line in text.split('\n'):
        # コメント行をスキップ
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue

        # 配列アイテムの処理
        if stripped.startswith('- '):
            if current_array is not None:
                value = stripped[2:].strip().strip('"\'')
                # ネストされたオブジェクト（例: path:, relationship:）
                if ':' in value and not value.startswith('<!--'):
                    # 簡易的にオブジェクトとして処理
                    obj = {}
                    for part in stripped[2:].split(','):
                        if ':' in part:
                            k, v = part.split(':', 1)
                            obj[k.strip()] = v.strip().strip('"\'')
                    result[current_array].append(obj)
                else:
                    result[current_array].append(value)
            continue

        # キー: 値の処理
        if ':' in line:
            key_part, value_part = line.split(':', 1)
            key = key_part.strip()

            # コメントを除去
            if not key.startswith('#'):
                value = value_part.strip()
                # インラインコメントを除去
                if '#' in value and not value.startswith('"'):
                    value = value.split('#')[0].strip()

                # 配列の開始を検出
                if value == '' or value == '[]':
                    result[key] = []
                    current_array = key
                    current_key = None
                else:
                    value = value.strip('"\'')
                    result[key] = value
                    current_key = key
                    current_array = None

    return result

def extract_sections(body: str) -> list[str]:
    """Markdown本文からH2セクション名を抽出"""
    sections = []
    for line in body.split('\n'):
        if line.startswith('## '):
            # 絵文字やマークを除去してセクション名を取得
            section_name = line[3:].strip()
            # 絵文字を除去
            section_name = re.sub(r'^[\U0001F300-\U0001F9FF\u2600-\u26FF\u2700-\u27BF]+\s*', '', section_name)
            sections.append(section_name)
    return sections

# =============================================================================
# 検証関数
# =============================================================================

def validate_document_id(value: str) -> tuple[bool, str]:
    """document_id形式を検証"""
    if not value:
        return False, "document_id is empty"

    # TEMPLATEプレースホルダーをスキップ
    if 'TEMPLATE' in value or 'DOMAIN-NNN' in value:
        return True, "template placeholder (skipped)"

    if DOCUMENT_ID_PATTERN.match(value) or ADR_ID_PATTERN.match(value):
        return True, "valid"

    return False, f"invalid format: expected TYPE-DOMAIN-NNN (e.g., PRC-DATA-001), got '{value}'"

def validate_type(value: str) -> tuple[bool, str]:
    """typeフィールドを検証"""
    if not value:
        return False, "type is empty"

    if value.lower() in VALID_TYPES:
        return True, "valid"

    return False, f"invalid type: expected one of {VALID_TYPES}, got '{value}'"

def validate_status(value: str) -> tuple[bool, str]:
    """statusフィールドを検証"""
    if not value:
        return False, "status is empty"

    # TEMPLATEプレースホルダーをスキップ
    if 'TEMPLATE' in value:
        return True, "template placeholder (skipped)"

    if value.lower() in VALID_STATUSES:
        return True, "valid"

    return False, f"invalid status: expected one of {VALID_STATUSES}, got '{value}'"

def validate_owner(value: str) -> tuple[bool, str]:
    """ownerフィールドを検証（@team-name形式）"""
    if not value:
        return False, "owner is empty"

    # TEMPLATEプレースホルダーをスキップ
    if 'TEMPLATE' in value or value == '@team-name':
        return True, "template placeholder (skipped)"

    if value.startswith('@'):
        return True, "valid"

    return False, f"invalid owner format: expected @team-name, got '{value}'"

def validate_date(value: Any, field_name: str) -> tuple[bool, str]:
    """日付フィールドを検証"""
    if not value:
        return False, f"{field_name} is empty"

    # TEMPLATEプレースホルダーをスキップ
    if isinstance(value, str) and 'TEMPLATE' in value:
        return True, "template placeholder (skipped)"

    # datetimeオブジェクトの場合
    if isinstance(value, datetime):
        return True, "valid"

    # 文字列の場合
    if isinstance(value, str):
        try:
            datetime.strptime(value, '%Y-%m-%d')
            return True, "valid"
        except ValueError:
            return False, f"invalid date format: expected YYYY-MM-DD, got '{value}'"

    return True, "valid (non-string)"

def validate_array(value: Any, field_name: str, min_items: int = 1) -> tuple[bool, str]:
    """配列フィールドを検証"""
    if not value:
        return False, f"{field_name} is empty"

    if not isinstance(value, list):
        return False, f"{field_name} should be an array, got {type(value).__name__}"

    if len(value) < min_items:
        return False, f"{field_name} should have at least {min_items} items, got {len(value)}"

    return True, "valid"

def validate_related_docs(value: Any) -> tuple[bool, str, list[str]]:
    """related_docs配列を検証"""
    warnings = []

    if not value:
        return True, "not specified (optional)", warnings

    if not isinstance(value, list):
        return False, "related_docs should be an array", warnings

    for i, item in enumerate(value):
        if isinstance(item, dict):
            # path検証
            if 'path' not in item:
                warnings.append(f"related_docs[{i}]: missing 'path'")

            # relationship検証
            if 'relationship' in item:
                rel = item['relationship']
                if rel not in VALID_RELATIONSHIPS:
                    return False, f"related_docs[{i}]: invalid relationship '{rel}', expected one of {VALID_RELATIONSHIPS}", warnings
        elif isinstance(item, str):
            # 旧形式（文字列のみ）も許容
            warnings.append(f"related_docs[{i}]: legacy format (string only), consider using {{path, relationship}} format")

    return True, "valid", warnings

def validate_review_consistency(frontmatter: dict) -> tuple[bool, str]:
    """next_reviewとreview_cycle_daysの整合性を検証"""
    next_review = frontmatter.get('next_review')
    review_cycle = frontmatter.get('review_cycle_days', 180)
    updated = frontmatter.get('updated')

    if not next_review or not updated:
        return True, "skipped (missing next_review or updated)"

    # TEMPLATEプレースホルダーをスキップ
    if isinstance(next_review, str) and 'TEMPLATE' in next_review:
        return True, "template placeholder (skipped)"

    try:
        if isinstance(next_review, str):
            next_review_date = datetime.strptime(next_review, '%Y-%m-%d')
        else:
            next_review_date = next_review

        if isinstance(updated, str):
            updated_date = datetime.strptime(updated, '%Y-%m-%d')
        else:
            updated_date = updated

        expected_review = updated_date + timedelta(days=review_cycle)

        # 30日以内の差は許容
        diff = abs((next_review_date - expected_review).days)
        if diff > 30:
            return False, f"next_review ({next_review}) differs from expected ({expected_review.strftime('%Y-%m-%d')}) by {diff} days"

        return True, "valid"
    except (ValueError, TypeError):
        return True, "skipped (date parse error)"

# =============================================================================
# スキーマ検証
# =============================================================================

def load_schema(schema_dir: Path, doc_type: str) -> dict | None:
    """ドキュメントタイプに対応するスキーマを読み込む"""
    schema_file = schema_dir / f"{doc_type}.yaml"

    if not schema_file.exists():
        return None

    with open(schema_file, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def validate_sections(body: str, schema: dict) -> tuple[bool, list[str], list[str]]:
    """必須セクションの存在を検証"""
    if not schema or 'sections' not in schema:
        return True, [], []

    actual_sections = extract_sections(body)
    actual_sections_lower = [s.lower() for s in actual_sections]

    missing = []
    found = []

    required_sections = schema.get('sections', {}).get('required', [])

    for section in required_sections:
        section_name = section.get('name', '') if isinstance(section, dict) else section
        # 部分一致で検索
        if any(section_name.lower() in s for s in actual_sections_lower):
            found.append(section_name)
        else:
            missing.append(section_name)

    return len(missing) == 0, missing, found

# =============================================================================
# メイン検証ロジック
# =============================================================================

def validate_file(file_path: Path, schema_dir: Path | None = None, check_sections: bool = False) -> dict:
    """単一ファイルを検証"""
    result = {
        'file': str(file_path),
        'has_frontmatter': False,
        'errors': [],
        'warnings': [],
        'info': []
    }

    frontmatter, body = extract_frontmatter(file_path)

    if frontmatter is None:
        result['errors'].append("No frontmatter found")
        return result

    if '_parse_error' in frontmatter:
        result['errors'].append(f"YAML parse error: {frontmatter['_parse_error']}")
        return result

    result['has_frontmatter'] = True

    # 後方互換性: レガシーフィールドをマッピング
    for legacy, new in LEGACY_FIELD_MAPPING.items():
        if legacy in frontmatter and new not in frontmatter:
            frontmatter[new] = frontmatter[legacy]
            result['info'].append(f"Legacy field '{legacy}' mapped to '{new}'")

    # === 必須フィールド検証 ===
    for field in REQUIRED_FIELDS:
        if field not in frontmatter:
            result['errors'].append(f"Missing required field: {field}")

    # === 個別フィールド検証 ===

    # document_id
    if 'document_id' in frontmatter:
        valid, msg = validate_document_id(frontmatter['document_id'])
        if not valid:
            result['errors'].append(f"document_id: {msg}")

    # type
    if 'type' in frontmatter:
        valid, msg = validate_type(frontmatter['type'])
        if not valid:
            result['errors'].append(f"type: {msg}")

    # status
    if 'status' in frontmatter:
        valid, msg = validate_status(frontmatter['status'])
        if not valid:
            result['errors'].append(f"status: {msg}")

    # owner
    if 'owner' in frontmatter:
        valid, msg = validate_owner(frontmatter['owner'])
        if not valid:
            result['errors'].append(f"owner: {msg}")

    # dates
    for date_field in ['created', 'updated', 'next_review']:
        if date_field in frontmatter:
            valid, msg = validate_date(frontmatter[date_field], date_field)
            if not valid:
                result['errors'].append(f"{date_field}: {msg}")

    # arrays
    if 'tags' in frontmatter:
        valid, msg = validate_array(frontmatter['tags'], 'tags', min_items=2)
        if not valid:
            result['errors'].append(f"tags: {msg}")

    if 'key_concepts' in frontmatter:
        valid, msg = validate_array(frontmatter['key_concepts'], 'key_concepts', min_items=1)
        if not valid:
            result['errors'].append(f"key_concepts: {msg}")

    # related_docs
    if 'related_docs' in frontmatter:
        valid, msg, warnings = validate_related_docs(frontmatter['related_docs'])
        if not valid:
            result['errors'].append(f"related_docs: {msg}")
        result['warnings'].extend(warnings)

    # review consistency
    valid, msg = validate_review_consistency(frontmatter)
    if not valid:
        result['warnings'].append(f"Review consistency: {msg}")

    # === 推奨フィールド検証 ===
    for field in RECOMMENDED_FIELDS:
        if field not in frontmatter:
            result['warnings'].append(f"Missing recommended field: {field}")

    # === セクション検証 ===
    if check_sections and schema_dir:
        doc_type = frontmatter.get('type', '').lower()
        schema = load_schema(schema_dir, doc_type)

        if schema:
            valid, missing, found = validate_sections(body, schema)
            if not valid:
                result['errors'].append(f"Missing required sections: {', '.join(missing)}")
            if found:
                result['info'].append(f"Found required sections: {', '.join(found)}")

    return result

def check_files(base_dir: Path, schema_dir: Path | None = None, check_sections: bool = False) -> list[dict]:
    """指定ディレクトリ内のMarkdownファイルを検証"""
    results = []

    for subdir in ['templates', 'examples']:
        dir_path = base_dir / subdir
        if not dir_path.exists():
            continue

        for md_file in sorted(dir_path.glob('*.md')):
            if md_file.name == 'README.md':
                continue

            result = validate_file(md_file, schema_dir, check_sections)
            result['file'] = str(md_file.relative_to(base_dir))
            results.append(result)

    return results

# =============================================================================
# 出力フォーマット
# =============================================================================

def print_text_report(results: list[dict]) -> int:
    """テキスト形式でレポートを出力"""
    total = len(results)
    with_frontmatter = sum(1 for r in results if r['has_frontmatter'])
    error_count = sum(1 for r in results if r['errors'])
    warning_count = sum(1 for r in results if r['warnings'] and not r['errors'])

    print(f"検証対象ファイル数: {total}")
    print(f"フロントマター有: {with_frontmatter}/{total}")
    print(f"エラーあり: {error_count}/{total}")
    print(f"警告のみ: {warning_count}/{total}")
    print()

    print("=" * 80)

    for r in results:
        print(f"\nファイル: {r['file']}")

        if not r['has_frontmatter']:
            print("  ❌ フロントマターなし")
            continue

        if r['errors']:
            print("  ❌ エラー:")
            for err in r['errors']:
                print(f"     - {err}")
        else:
            print("  ✅ 必須フィールド・形式OK")

        if r['warnings']:
            print("  ⚠️  警告:")
            for warn in r['warnings']:
                print(f"     - {warn}")

        if r['info']:
            print("  ℹ️  情報:")
            for info in r['info']:
                print(f"     - {info}")

    print("\n" + "=" * 80)

    # ベストプラクティス提案
    if error_count > 0:
        print("\n📚 ベストプラクティス:")
        print("   - document_id形式: TYPE-DOMAIN-NNN (例: PRC-DATA-001)")
        print("   - relationship値: implements, governed-by, references, depends-on, escalates-to, supersedes, superseded-by")
        print("   - 詳細は 1USAGE-GUIDE.md を参照してください")

    # 終了コード決定
    if error_count > 0:
        print(f"\n❌ 検証失敗: {error_count}件のエラー")
        return 1
    elif warning_count > 0:
        print(f"\n⚠️  検証成功（警告あり）: {warning_count}件の警告")
        return 2
    else:
        print(f"\n✅ 検証成功: 全{total}ファイルが準拠")
        return 0

def print_json_report(results: list[dict]) -> int:
    """JSON形式でレポートを出力"""
    total = len(results)
    error_count = sum(1 for r in results if r['errors'])
    warning_count = sum(1 for r in results if r['warnings'] and not r['errors'])

    report = {
        'summary': {
            'total_files': total,
            'with_frontmatter': sum(1 for r in results if r['has_frontmatter']),
            'error_count': error_count,
            'warning_count': warning_count,
            'success': error_count == 0
        },
        'results': results
    }

    print(json.dumps(report, indent=2, ensure_ascii=False))

    if error_count > 0:
        return 1
    elif warning_count > 0:
        return 2
    return 0

# =============================================================================
# メイン
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='9251205claude.mdフレームワーク準拠フロントマター検証'
    )
    parser.add_argument(
        '--format', choices=['text', 'json'], default='text',
        help='出力形式 (default: text)'
    )
    parser.add_argument(
        '--schema-dir', type=Path,
        help='スキーマディレクトリへのパス'
    )
    parser.add_argument(
        '--check-sections', action='store_true',
        help='必須セクションも検証する'
    )
    parser.add_argument(
        '--base-dir', type=Path,
        default=Path('/mnt/j/pcloud_sync/5agent/1conf/3doca/01-doc-framework'),
        help='検証対象のベースディレクトリ'
    )

    args = parser.parse_args()

    # デフォルトスキーマディレクトリ
    if args.check_sections and not args.schema_dir:
        args.schema_dir = args.base_dir / 'schema'

    results = check_files(args.base_dir, args.schema_dir, args.check_sections)

    if args.format == 'json':
        exit_code = print_json_report(results)
    else:
        exit_code = print_text_report(results)

    sys.exit(exit_code)

if __name__ == '__main__':
    main()
