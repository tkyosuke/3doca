#!/usr/bin/env python3
"""
3doca Documentation Quality Verification Script
Verifies gap markers, links, frontmatter, Mermaid syntax, and cross-references
"""

import os
import re
import yaml
from pathlib import Path
from typing import Dict, List, Tuple, Set
from dataclasses import dataclass, field

@dataclass
class VerificationResult:
    """Store verification results"""
    total_files: int = 0
    gap_marker_issues: List[str] = field(default_factory=list)
    link_issues: List[str] = field(default_factory=list)
    frontmatter_issues: List[str] = field(default_factory=list)
    mermaid_issues: List[str] = field(default_factory=list)
    crossref_issues: List[str] = field(default_factory=list)

    @property
    def total_issues(self) -> int:
        return (len(self.gap_marker_issues) +
                len(self.link_issues) +
                len(self.frontmatter_issues) +
                len(self.mermaid_issues) +
                len(self.crossref_issues))

class DocumentationVerifier:
    """Verify documentation quality"""

    REQUIRED_FRONTMATTER_FIELDS = ['type', 'category', 'tags', 'summary']
    GAP_MARKERS = [
        'TODOCS:', 'NEEDS_EXAMPLE:', 'NEEDS_VERIFICATION:',
        'INCOMPLETE:', 'SME_NEEDED:', 'ASSUMPTION:',
        'OUTDATED:', 'LINK_NEEDED:'
    ]

    def __init__(self, base_path: Path):
        self.base_path = base_path
        self.result = VerificationResult()
        self.all_md_files: Set[Path] = set()

    def run_verification(self) -> VerificationResult:
        """Run all verification checks"""
        print("🔍 Starting documentation quality verification...\n")

        # Collect all markdown files
        self.all_md_files = set(self.base_path.glob('docs/**/*.md'))
        self.result.total_files = len(self.all_md_files)

        print(f"📄 Found {self.result.total_files} markdown files\n")

        # Run checks
        for md_file in sorted(self.all_md_files):
            self._verify_file(md_file)

        # Verify cross-references
        self._verify_cross_references()

        return self.result

    def _verify_file(self, file_path: Path):
        """Verify a single markdown file"""
        try:
            content = file_path.read_text(encoding='utf-8')
            rel_path = file_path.relative_to(self.base_path)

            # Check frontmatter
            self._check_frontmatter(content, rel_path)

            # Check gap markers
            self._check_gap_markers(content, rel_path)

            # Check internal links
            self._check_links(content, file_path, rel_path)

            # Check Mermaid diagrams
            self._check_mermaid(content, rel_path)

        except Exception as e:
            self.result.frontmatter_issues.append(f"{rel_path}: Error reading file - {e}")

    def _check_frontmatter(self, content: str, rel_path: Path):
        """Check YAML frontmatter"""
        # Extract frontmatter
        match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)

        if not match:
            self.result.frontmatter_issues.append(f"{rel_path}: Missing frontmatter")
            return

        try:
            frontmatter = yaml.safe_load(match.group(1))

            if not frontmatter:
                self.result.frontmatter_issues.append(f"{rel_path}: Empty frontmatter")
                return

            # Check required fields
            missing = [f for f in self.REQUIRED_FRONTMATTER_FIELDS if f not in frontmatter]
            if missing:
                self.result.frontmatter_issues.append(
                    f"{rel_path}: Missing fields: {', '.join(missing)}"
                )

            # Check empty values
            empty = [f for f in self.REQUIRED_FRONTMATTER_FIELDS
                     if f in frontmatter and not frontmatter[f]]
            if empty:
                self.result.frontmatter_issues.append(
                    f"{rel_path}: Empty fields: {', '.join(empty)}"
                )

        except yaml.YAMLError as e:
            self.result.frontmatter_issues.append(f"{rel_path}: Invalid YAML - {e}")

    def _check_gap_markers(self, content: str, rel_path: Path):
        """Check gap marker usage"""
        # Find all gap markers
        for marker in self.GAP_MARKERS:
            pattern = rf'\[{marker}\s*([^\]]*)\]'
            matches = re.finditer(pattern, content)

            for match in matches:
                description = match.group(1).strip()
                if not description:
                    self.result.gap_marker_issues.append(
                        f"{rel_path}: Gap marker [{marker}] has no description"
                    )

    def _check_links(self, content: str, file_path: Path, rel_path: Path):
        """Check internal markdown links"""
        # Pattern for markdown links: [text](path)
        link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'

        for match in re.finditer(link_pattern, content):
            link_text = match.group(1)
            link_path = match.group(2)

            # Skip external links, anchors, and images
            if link_path.startswith(('http://', 'https://', '#', 'mailto:')):
                continue

            # Remove anchor if present
            link_path_clean = link_path.split('#')[0]
            if not link_path_clean:
                continue

            # Resolve relative path
            target_path = (file_path.parent / link_path_clean).resolve()

            # Check if target exists
            if not target_path.exists():
                self.result.link_issues.append(
                    f"{rel_path}: Broken link to '{link_path}' (resolved: {target_path})"
                )

    def _check_mermaid(self, content: str, rel_path: Path):
        """Check Mermaid diagram syntax"""
        # Find all Mermaid code blocks
        mermaid_pattern = r'```mermaid\s*\n(.*?)```'

        for match in re.finditer(mermaid_pattern, content, re.DOTALL):
            diagram = match.group(1)

            # Check for dark mode theme
            if "%%{init:" not in diagram and "'theme':" not in diagram:
                self.result.mermaid_issues.append(
                    f"{rel_path}: Mermaid diagram missing dark mode theme"
                )

            # Check for common syntax issues
            if diagram.strip().startswith('graph') and 'graph' in diagram[10:]:
                self.result.mermaid_issues.append(
                    f"{rel_path}: Possible Mermaid syntax error (multiple 'graph' keywords)"
                )

    def _verify_cross_references(self):
        """Verify README files reference all documents in their directories"""
        readme_dirs = [p.parent for p in self.all_md_files if p.name == 'README.md']

        for readme_dir in readme_dirs:
            readme_path = readme_dir / 'README.md'
            if not readme_path.exists():
                continue

            try:
                readme_content = readme_path.read_text(encoding='utf-8')
                rel_readme = readme_path.relative_to(self.base_path)

                # Find all markdown files in same directory (non-recursive)
                sibling_files = [f for f in readme_dir.glob('*.md')
                                if f.name != 'README.md']

                # Check if each sibling is referenced in README
                for sibling in sibling_files:
                    sibling_name = sibling.name
                    if sibling_name not in readme_content:
                        self.result.crossref_issues.append(
                            f"{rel_readme}: Does not reference {sibling_name}"
                        )

            except Exception as e:
                self.result.crossref_issues.append(
                    f"{rel_readme}: Error checking cross-references - {e}"
                )

def print_results(result: VerificationResult):
    """Print verification results"""
    print("\n" + "="*80)
    print("📊 VERIFICATION RESULTS")
    print("="*80)

    # Summary table
    print("\n## Summary")
    print(f"Total files verified: {result.total_files}")
    print(f"Total issues found: {result.total_issues}")

    # Criteria table
    print("\n## Verification Criteria Results")
    print("| Criterion | Issues | Status |")
    print("|-----------|--------|--------|")

    criteria = [
        ("Gap Markers", len(result.gap_marker_issues)),
        ("Link Integrity", len(result.link_issues)),
        ("Frontmatter Compliance", len(result.frontmatter_issues)),
        ("Mermaid Syntax", len(result.mermaid_issues)),
        ("Cross-references", len(result.crossref_issues)),
    ]

    for name, count in criteria:
        status = "✅ PASS" if count == 0 else f"❌ FAIL ({count})"
        print(f"| {name} | {count} | {status} |")

    # Detailed issues
    if result.total_issues > 0:
        print("\n## Detailed Issues")

        if result.frontmatter_issues:
            print(f"\n### ❌ Frontmatter Issues ({len(result.frontmatter_issues)})")
            for issue in sorted(result.frontmatter_issues)[:20]:
                print(f"- {issue}")
            if len(result.frontmatter_issues) > 20:
                print(f"... and {len(result.frontmatter_issues) - 20} more")

        if result.link_issues:
            print(f"\n### ❌ Link Issues ({len(result.link_issues)})")
            for issue in sorted(result.link_issues)[:20]:
                print(f"- {issue}")
            if len(result.link_issues) > 20:
                print(f"... and {len(result.link_issues) - 20} more")

        if result.gap_marker_issues:
            print(f"\n### ⚠️ Gap Marker Issues ({len(result.gap_marker_issues)})")
            for issue in sorted(result.gap_marker_issues)[:10]:
                print(f"- {issue}")
            if len(result.gap_marker_issues) > 10:
                print(f"... and {len(result.gap_marker_issues) - 10} more")

        if result.mermaid_issues:
            print(f"\n### ⚠️ Mermaid Issues ({len(result.mermaid_issues)})")
            for issue in sorted(result.mermaid_issues)[:10]:
                print(f"- {issue}")
            if len(result.mermaid_issues) > 10:
                print(f"... and {len(result.mermaid_issues) - 10} more")

        if result.crossref_issues:
            print(f"\n### ⚠️ Cross-reference Issues ({len(result.crossref_issues)})")
            for issue in sorted(result.crossref_issues)[:10]:
                print(f"- {issue}")
            if len(result.crossref_issues) > 10:
                print(f"... and {len(result.crossref_issues) - 10} more")

    # Quality score
    print("\n## Overall Quality Score")

    # Calculate score (100 points total)
    # Deduct points based on issue severity
    score = 100
    score -= len(result.frontmatter_issues) * 2  # Critical: -2 each
    score -= len(result.link_issues) * 2  # Critical: -2 each
    score -= len(result.gap_marker_issues) * 0.5  # Minor: -0.5 each
    score -= len(result.mermaid_issues) * 1  # Medium: -1 each
    score -= len(result.crossref_issues) * 1  # Medium: -1 each

    score = max(0, round(score))

    if score >= 90:
        grade = "A (Excellent)"
    elif score >= 80:
        grade = "B (Good)"
    elif score >= 70:
        grade = "C (Fair)"
    elif score >= 60:
        grade = "D (Poor)"
    else:
        grade = "F (Needs Major Improvement)"

    print(f"**Score: {score}/100 ({grade})**")

    # Recommendations
    print("\n## Recommendations")

    if result.frontmatter_issues:
        print("- 🔴 **HIGH PRIORITY**: Fix frontmatter issues to ensure proper metadata")
    if result.link_issues:
        print("- 🔴 **HIGH PRIORITY**: Fix broken internal links to maintain navigation")
    if result.mermaid_issues:
        print("- 🟡 **MEDIUM PRIORITY**: Add dark mode theme to Mermaid diagrams")
    if result.crossref_issues:
        print("- 🟡 **MEDIUM PRIORITY**: Update README files to reference all sibling documents")
    if result.gap_marker_issues:
        print("- 🟢 **LOW PRIORITY**: Add descriptions to gap markers for better tracking")

    if result.total_issues == 0:
        print("✅ **Excellent!** All quality criteria passed. No improvements needed.")

    print("\n" + "="*80)

def main():
    """Main entry point"""
    base_path = Path(__file__).parent
    verifier = DocumentationVerifier(base_path)
    result = verifier.run_verification()
    print_results(result)

    # Exit with error code if critical issues found
    critical_issues = len(result.frontmatter_issues) + len(result.link_issues)
    return 1 if critical_issues > 0 else 0

if __name__ == '__main__':
    exit(main())
