#!/usr/bin/env python3
"""
check_staleness.py - ドキュメント陳腐化検出スクリプト

3docaフレームワークのドキュメントが陳腐化していないかを検出します。

検出ロジック:
1. next_reviewが過ぎたドキュメントを検出
2. updated + review_cycle_daysを超過したドキュメントを検出

使用例:
    # 基本的な使用
    python check_staleness.py 01-doc-framework/examples

    # JSON出力
    python check_staleness.py 01-doc-framework --format json --output report.json

    # 詳細出力
    python check_staleness.py 01-doc-framework --verbose
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

try:
    import yaml
except ImportError:
    print("Error: PyYAML is required. Install with: pip install pyyaml")
    sys.exit(1)

# デフォルトレビューサイクル（日数）
DEFAULT_REVIEW_CYCLE_DAYS = 180

# 陳腐化レベル
STALENESS_LEVELS = {
    "critical": 365,    # 1年以上
    "high": 180,        # 6ヶ月以上
    "medium": 90,       # 3ヶ月以上
    "low": 30,          # 1ヶ月以上
}


def parse_frontmatter(content: str) -> Optional[dict]:
    """フロントマターを解析"""
    pattern = r'^---\s*\n(.*?)\n---\s*\n'
    match = re.match(pattern, content, re.DOTALL)
    if not match:
        return None

    frontmatter_text = match.group(1)

    try:
        return yaml.safe_load(frontmatter_text)
    except yaml.YAMLError:
        # フォールバック: 行ベース解析
        result = {}
        for line in frontmatter_text.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip().strip('"').strip("'")
                if value and 'TEMPLATE' not in value:
                    result[key] = value
        return result if result else None


def parse_date(date_str: str) -> Optional[datetime]:
    """日付文字列をdatetimeに変換"""
    if not date_str:
        return None

    formats = [
        "%Y-%m-%d",
        "%Y/%m/%d",
        "%d-%m-%Y",
    ]

    for fmt in formats:
        try:
            return datetime.strptime(str(date_str), fmt)
        except ValueError:
            continue

    return None


def check_staleness(
    frontmatter: dict,
    reference_date: datetime
) -> dict:
    """ドキュメントの陳腐化をチェック"""
    result = {
        "is_stale": False,
        "staleness_reason": None,
        "staleness_level": None,
        "days_overdue": 0,
        "next_review": None,
        "updated": None,
        "review_cycle_days": DEFAULT_REVIEW_CYCLE_DAYS,
        "owner": frontmatter.get("owner", "unknown"),
    }

    # next_reviewをチェック
    next_review_str = frontmatter.get("next_review")
    if next_review_str:
        next_review = parse_date(next_review_str)
        if next_review:
            result["next_review"] = next_review.strftime("%Y-%m-%d")
            if next_review < reference_date:
                result["is_stale"] = True
                result["staleness_reason"] = "next_review_passed"
                result["days_overdue"] = (reference_date - next_review).days

    # updated + review_cycle_daysをチェック
    updated_str = frontmatter.get("updated") or frontmatter.get("updated_at")
    review_cycle = frontmatter.get("review_cycle_days", DEFAULT_REVIEW_CYCLE_DAYS)
    result["review_cycle_days"] = review_cycle

    if updated_str:
        updated = parse_date(updated_str)
        if updated:
            result["updated"] = updated.strftime("%Y-%m-%d")
            expected_review = updated + timedelta(days=review_cycle)
            if expected_review < reference_date:
                # next_reviewが設定されていない場合、または両方過ぎている場合
                if not result["is_stale"]:
                    result["is_stale"] = True
                    result["staleness_reason"] = "review_cycle_exceeded"
                    result["days_overdue"] = (reference_date - expected_review).days
                else:
                    # 両方の条件で陳腐化
                    result["staleness_reason"] = "both_conditions"
                    result["days_overdue"] = max(
                        result["days_overdue"],
                        (reference_date - expected_review).days
                    )

    # 陳腐化レベルを判定
    if result["is_stale"]:
        days = result["days_overdue"]
        for level, threshold in STALENESS_LEVELS.items():
            if days >= threshold:
                result["staleness_level"] = level
                break
        else:
            result["staleness_level"] = "low"

    return result


def scan_directory(
    directory: Path,
    reference_date: datetime,
    verbose: bool = False
) -> list:
    """ディレクトリ内のMarkdownファイルをスキャン"""
    results = []

    for md_file in directory.rglob("*.md"):
        # テンプレートファイルはスキップ
        if "template" in md_file.name.lower():
            if verbose:
                print(f"Skipping template: {md_file}")
            continue

        try:
            content = md_file.read_text(encoding="utf-8")
        except Exception as e:
            if verbose:
                print(f"Error reading {md_file}: {e}")
            continue

        frontmatter = parse_frontmatter(content)
        if not frontmatter:
            if verbose:
                print(f"No frontmatter: {md_file}")
            continue

        staleness = check_staleness(frontmatter, reference_date)
        staleness["file"] = str(md_file)
        staleness["title"] = frontmatter.get("title", md_file.stem)
        staleness["document_id"] = frontmatter.get("document_id", "N/A")

        results.append(staleness)

    return results


def format_text_output(results: list, show_all: bool = False) -> str:
    """テキスト形式で出力"""
    stale_docs = [r for r in results if r["is_stale"]]

    if not stale_docs:
        return "✅ No stale documents found."

    # レベル別にソート
    level_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    stale_docs.sort(key=lambda x: level_order.get(x["staleness_level"], 99))

    lines = [
        f"⚠️ Found {len(stale_docs)} stale document(s):",
        "",
        "| Level | Document | Days Overdue | Owner | Reason |",
        "|-------|----------|--------------|-------|--------|",
    ]

    for doc in stale_docs:
        level = doc["staleness_level"].upper()
        title = doc["title"][:30] + "..." if len(doc["title"]) > 30 else doc["title"]
        days = doc["days_overdue"]
        owner = doc["owner"]
        reason = doc["staleness_reason"]
        lines.append(f"| {level} | {title} | {days} | {owner} | {reason} |")

    if show_all:
        lines.extend([
            "",
            "---",
            "",
            "All scanned documents:",
        ])
        for doc in results:
            status = "❌ STALE" if doc["is_stale"] else "✅ OK"
            lines.append(f"  {status} {doc['file']}")

    return "\n".join(lines)


def format_json_output(results: list) -> str:
    """JSON形式で出力"""
    stale_docs = [r for r in results if r["is_stale"]]

    output = {
        "scan_date": datetime.now().strftime("%Y-%m-%d"),
        "total_documents": len(results),
        "stale_documents": len(stale_docs),
        "summary": {
            "critical": len([d for d in stale_docs if d["staleness_level"] == "critical"]),
            "high": len([d for d in stale_docs if d["staleness_level"] == "high"]),
            "medium": len([d for d in stale_docs if d["staleness_level"] == "medium"]),
            "low": len([d for d in stale_docs if d["staleness_level"] == "low"]),
        },
        "stale_documents_list": stale_docs,
    }

    return json.dumps(output, indent=2, ensure_ascii=False)


def format_github_issue(results: list) -> str:
    """GitHub Issue用のMarkdown形式で出力"""
    stale_docs = [r for r in results if r["is_stale"]]

    if not stale_docs:
        return ""

    lines = [
        "## 📋 Document Staleness Report",
        "",
        f"**Scan Date**: {datetime.now().strftime('%Y-%m-%d')}",
        f"**Stale Documents**: {len(stale_docs)}",
        "",
        "### 🚨 Documents Requiring Review",
        "",
    ]

    # レベル別にグループ化
    by_level = {}
    for doc in stale_docs:
        level = doc["staleness_level"]
        if level not in by_level:
            by_level[level] = []
        by_level[level].append(doc)

    level_emoji = {
        "critical": "🔴",
        "high": "🟠",
        "medium": "🟡",
        "low": "🟢",
    }

    for level in ["critical", "high", "medium", "low"]:
        if level in by_level:
            emoji = level_emoji[level]
            lines.append(f"#### {emoji} {level.upper()} ({len(by_level[level])})")
            lines.append("")
            for doc in by_level[level]:
                lines.append(f"- [ ] **{doc['title']}** ({doc['document_id']})")
                lines.append(f"  - File: `{doc['file']}`")
                lines.append(f"  - Owner: {doc['owner']}")
                lines.append(f"  - Days overdue: {doc['days_overdue']}")
                lines.append(f"  - Last updated: {doc['updated'] or 'unknown'}")
                lines.append("")

    lines.extend([
        "---",
        "",
        "**Action Required**: Please review and update the documents listed above.",
        "",
        "_This issue was automatically generated by check_staleness.py_",
    ])

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Check document staleness in 3doca framework"
    )
    parser.add_argument(
        "directories",
        nargs="+",
        help="Directories to scan for Markdown files"
    )
    parser.add_argument(
        "--format", "-f",
        choices=["text", "json", "github-issue"],
        default="text",
        help="Output format (default: text)"
    )
    parser.add_argument(
        "--output", "-o",
        help="Output file path (default: stdout)"
    )
    parser.add_argument(
        "--reference-date",
        help="Reference date for staleness check (YYYY-MM-DD, default: today)"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Verbose output"
    )
    parser.add_argument(
        "--show-all",
        action="store_true",
        help="Show all scanned documents (text format only)"
    )

    args = parser.parse_args()

    # 参照日を設定
    if args.reference_date:
        reference_date = parse_date(args.reference_date)
        if not reference_date:
            print(f"Error: Invalid date format: {args.reference_date}")
            sys.exit(1)
    else:
        reference_date = datetime.now()

    # スキャン実行
    all_results = []
    for directory in args.directories:
        dir_path = Path(directory)
        if not dir_path.exists():
            print(f"Warning: Directory not found: {directory}")
            continue

        results = scan_directory(dir_path, reference_date, args.verbose)
        all_results.extend(results)

    if not all_results:
        print("No documents found to scan.")
        sys.exit(0)

    # 出力フォーマット
    if args.format == "json":
        output = format_json_output(all_results)
    elif args.format == "github-issue":
        output = format_github_issue(all_results)
    else:
        output = format_text_output(all_results, args.show_all)

    # 出力
    if args.output:
        Path(args.output).write_text(output, encoding="utf-8")
        if args.verbose:
            print(f"Output written to: {args.output}")
    else:
        print(output)

    # 終了コード
    stale_count = len([r for r in all_results if r["is_stale"]])
    if stale_count > 0:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
