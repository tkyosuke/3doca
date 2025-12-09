#!/usr/bin/env python3
"""
フロントマター検証スクリプト

01-doc-framework/templates/およびexamples/の全Markdownファイルの
フロントマターを検証し、RAG対応標準との適合性をチェックします。
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

# USAGE-GUIDE.mdへの参照URL
USAGE_GUIDE_URL = "../USAGE-GUIDE.md"

# 必須フィールドとUSAGE-GUIDEのセクション参照
REQUIRED_FIELDS = {
    'title': f"See {USAGE_GUIDE_URL}#フロントマター必須項目",
    'description': f"See {USAGE_GUIDE_URL}#フロントマター必須項目",
    'tags': f"See {USAGE_GUIDE_URL}#フロントマター必須項目",
    'category': f"See {USAGE_GUIDE_URL}#フロントマター必須項目",
    'domain': f"See {USAGE_GUIDE_URL}#フロントマター必須項目"
}

# 固定categoryリスト
VALID_CATEGORIES = ['process', 'playbook', 'runbook', 'reference', 'guide', 'concepts']


def extract_frontmatter(content: str) -> Tuple[Dict[str, str], bool]:
    """Markdownファイルからフロントマッターを抽出"""
    pattern = r'^---\s*\n(.*?)\n---'
    match = re.match(pattern, content, re.DOTALL)

    if not match:
        return {}, False

    frontmatter = {}
    for line in match.group(1).split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            frontmatter[key.strip()] = value.strip()

    return frontmatter, True


def check_required_fields(frontmatter: Dict[str, str], filename: str) -> List[str]:
    """必須フィールドの存在確認"""
    errors = []

    for field, guide_ref in REQUIRED_FIELDS.items():
        if field not in frontmatter or not frontmatter[field]:
            errors.append(f"  ❌ Missing required field: '{field}' → {guide_ref}")

    return errors


def check_category_validity(frontmatter: Dict[str, str]) -> List[str]:
    """categoryフィールドの妥当性確認"""
    warnings = []

    if 'category' in frontmatter:
        category = frontmatter['category'].strip('"\'')
        if category not in VALID_CATEGORIES:
            warnings.append(
                f"  ⚠️  Invalid category: '{category}' "
                f"(Valid: {', '.join(VALID_CATEGORIES)}) "
                f"→ {USAGE_GUIDE_URL}#よくある落とし穴"
            )

    return warnings


def check_description_length(frontmatter: Dict[str, str]) -> List[str]:
    """descriptionの長さ確認（150文字推奨）"""
    warnings = []

    if 'description' in frontmatter:
        desc = frontmatter['description'].strip('"\'')
        if len(desc) > 150:
            warnings.append(
                f"  ⚠️  Description too long: {len(desc)} chars (recommended: ≤150) "
                f"→ {USAGE_GUIDE_URL}#フロントマター必須項目"
            )

    return warnings


def print_best_practices():
    """ベストプラクティス提案を表示"""
    print("\n💡 Best Practices:")
    print(f"  - Keep chunk size under 500 lines ({USAGE_GUIDE_URL}#よくある落とし穴)")
    print(f"  - Add 'related_docs' for knowledge graph ({USAGE_GUIDE_URL}#よくある落とし穴)")
    print(f"  - Avoid pronouns like '「これは」「それは」' ({USAGE_GUIDE_URL}#よくある落とし穴)")
    print(f"  - Place keywords at the beginning of paragraphs ({USAGE_GUIDE_URL}#よくある落とし穴)")
    print(f"  - Use 'git mv' to preserve history ({USAGE_GUIDE_URL}#よくある落とし穴)")


def check_files(base_dir: str) -> Tuple[int, int, List[str]]:
    """指定ディレクトリ内の全Markdownファイルを検証"""
    templates_dir = Path(base_dir) / "templates"
    examples_dir = Path(base_dir) / "examples"

    total_files = 0
    passed_files = 0
    all_issues = []

    for directory in [templates_dir, examples_dir]:
        if not directory.exists():
            continue

        for md_file in sorted(directory.glob("*.md")):
            if md_file.name == "README.md":
                continue

            total_files += 1

            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            frontmatter, has_frontmatter = extract_frontmatter(content)

            if not has_frontmatter:
                all_issues.append(f"\n📄 {md_file.relative_to(base_dir)}")
                all_issues.append(f"  ❌ No frontmatter found → {USAGE_GUIDE_URL}#フロントマター必須項目")
                continue

            errors = check_required_fields(frontmatter, md_file.name)
            warnings = check_category_validity(frontmatter)
            warnings.extend(check_description_length(frontmatter))

            if errors or warnings:
                all_issues.append(f"\n📄 {md_file.relative_to(base_dir)}")
                all_issues.extend(errors)
                all_issues.extend(warnings)
            else:
                passed_files += 1

    return total_files, passed_files, all_issues


def main():
    """メイン処理"""
    # 01-doc-frameworkディレクトリを検索
    current_dir = Path(__file__).parent
    base_dir = current_dir.parent.parent / "01-doc-framework"

    if not base_dir.exists():
        print(f"❌ Error: Directory not found: {base_dir}")
        sys.exit(1)

    print("🔍 Checking frontmatter in 01-doc-framework/templates/ and examples/\n")

    total_files, passed_files, all_issues = check_files(base_dir)

    # 結果表示
    if all_issues:
        print("❌ Issues found:\n")
        for issue in all_issues:
            print(issue)

    # サマリー表示
    compliance_rate = (passed_files / total_files * 100) if total_files > 0 else 0

    print("\n" + "="*60)
    print("📊 Summary:")
    print(f"  Total files checked: {total_files}")
    print(f"  Files passed: {passed_files}")
    print(f"  Files with issues: {total_files - passed_files}")
    print(f"  Compliance rate: {compliance_rate:.1f}% (Goal: 100%)")
    print("="*60)

    # ベストプラクティス提案（検証成功時も表示）
    if compliance_rate == 100:
        print("\n✅ All checks passed!")

    print_best_practices()

    # よくある落とし穴トップ3
    print(f"\n⚠️  Common Pitfalls (see {USAGE_GUIDE_URL}#よくある落とし穴):")
    print("  1. description欠落 → RAG検索失敗")
    print("  2. チャンクサイズ過大（500行超） → 検索精度低下")
    print("  3. related_docs未設定 → ナレッジグラフ構築不可")

    # 終了コード（エラーがあれば1、なければ0）
    sys.exit(0 if compliance_rate == 100 else 1)


if __name__ == "__main__":
    main()
