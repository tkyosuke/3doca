# Quick Fix Guide - 3doca Quality Issues

**Generated**: 2025-12-10
**Status**: Action Required
**Estimated Time**: 5-7 hours for critical fixes

## Executive Summary

The 3doca documentation framework has **98 quality issues** across 42 files. Critical fixes (frontmatter and broken links) can be completed in 5-7 hours and will improve the score from 0/100 to 45-50/100.

## Critical Issues (Must Fix Now)

### Issue 1: Missing Frontmatter (31 files)

**Impact**: Documents cannot be properly indexed, searched, or categorized.

**Files Affected**:
- 18 README.md files
- 13 template files
- 3 reference documents

**Solution**: Add standardized YAML frontmatter to all files.

#### Quick Fix Script

```bash
#!/bin/bash
# add-frontmatter.sh - Add missing frontmatter to README files

cd /mnt/j/pcloud_sync/5agent/1conf/3doca

# Function to add frontmatter to README
add_readme_frontmatter() {
    local file="$1"
    local category="$2"

    # Create temp file with frontmatter
    cat > /tmp/frontmatter.tmp << EOF
---
type: index
category: $category
tags: [navigation, index]
summary: Index of $category documents
---

EOF

    # Prepend to existing file
    cat /tmp/frontmatter.tmp "$file" > /tmp/newfile.tmp
    mv /tmp/newfile.tmp "$file"
    echo "✓ Added frontmatter to $file"
}

# Fix all README files
add_readme_frontmatter "docs/01_knowledge/01-concepts/README.md" "concepts"
add_readme_frontmatter "docs/01_knowledge/02-tutorials/README.md" "tutorials"
add_readme_frontmatter "docs/01_knowledge/03-how-to/README.md" "how-to"
add_readme_frontmatter "docs/01_knowledge/04-reference/README.md" "reference"
add_readme_frontmatter "docs/01_knowledge/README.md" "knowledge"

add_readme_frontmatter "docs/02_operations/01-processes/README.md" "processes"
add_readme_frontmatter "docs/02_operations/02-playbooks/README.md" "playbooks"
add_readme_frontmatter "docs/02_operations/03-runbooks/README.md" "runbooks"
add_readme_frontmatter "docs/02_operations/04-cheatsheets/README.md" "cheatsheets"
add_readme_frontmatter "docs/02_operations/README.md" "operations"

add_readme_frontmatter "docs/03_architecture/01-context/README.md" "context"
add_readme_frontmatter "docs/03_architecture/02-containers/README.md" "containers"
add_readme_frontmatter "docs/03_architecture/03-components/README.md" "components"
add_readme_frontmatter "docs/03_architecture/README.md" "architecture"

add_readme_frontmatter "docs/README.md" "documentation"

echo "✓ All README frontmatter added"
```

#### Manual Tasks

**Templates** (13 files):
Each template needs specific frontmatter. Edit manually:

1. `docs/_templates/01_knowledge/01-concept.md`:
   ```yaml
   ---
   type: template
   category: concept
   tags: [template, diataxis, concept]
   summary: Template for creating concept/explanation documents
   ---
   ```

2. `docs/_templates/01_knowledge/02-tutorial.md`:
   ```yaml
   ---
   type: template
   category: tutorial
   tags: [template, diataxis, tutorial]
   summary: Template for creating tutorial/learning documents
   ---
   ```

3. Similar for remaining 11 template files...

**Reference Documents** (3 files):

1. `docs/01_knowledge/04-reference/01-GAP-MARKER-SPEC.md`:
   ```yaml
   ---
   type: reference
   category: specifications
   tags: [gap-markers, quality, specifications]
   summary: Complete specification of gap marker syntax and usage
   version: 1.0
   status: active
   ---
   ```

2. `docs/01_knowledge/04-reference/02-TIER-DESIGN-SPEC.md`:
   ```yaml
   ---
   type: reference
   category: specifications
   tags: [tier-design, architecture, specifications]
   summary: Document tier design specification and hierarchy
   version: 1.0
   status: active
   ---
   ```

3. `docs/01_knowledge/04-reference/03-MIGRATION-MAP.md`:
   ```yaml
   ---
   type: reference
   category: migration
   tags: [migration, implementation, specifications]
   summary: Migration roadmap and implementation timeline
   version: 1.0
   status: active
   ---
   ```

---

### Issue 2: Broken Links (25 files)

**Impact**: Navigation fails, readers get 404 errors.

**Root Causes**:
- Directory naming inconsistency (concepts vs 01-concepts)
- File naming inconsistency (GAP-MARKER-SPEC vs 01-GAP-MARKER-SPEC)
- Non-existent files referenced

#### Quick Fix Scripts

**Script 1: Fix Directory Naming (fixes 8 issues)**

```bash
#!/bin/bash
# fix-directory-links.sh - Update all directory references

cd /mnt/j/pcloud_sync/5agent/1conf/3doca

echo "Fixing directory references in all markdown files..."

find docs -name "*.md" -type f -exec sed -i \
  's|/concepts/|/01-concepts/|g; \
   s|/tutorials/|/02-tutorials/|g; \
   s|/how-to/|/03-how-to/|g; \
   s|/reference/|/04-reference/|g; \
   s|/processes/|/01-processes/|g; \
   s|/playbooks/|/02-playbooks/|g; \
   s|/runbooks/|/03-runbooks/|g; \
   s|/cheatsheets/|/04-cheatsheets/|g' {} \;

echo "✓ Directory references updated"
echo "Fixed patterns:"
echo "  - concepts/ → 01-concepts/"
echo "  - tutorials/ → 02-tutorials/"
echo "  - how-to/ → 03-how-to/"
echo "  - reference/ → 04-reference/"
echo "  - processes/ → 01-processes/"
echo "  - playbooks/ → 02-playbooks/"
echo "  - runbooks/ → 03-runbooks/"
echo "  - cheatsheets/ → 04-cheatsheets/"
```

**Script 2: Fix Reference Document Links (fixes 10 issues)**

```bash
#!/bin/bash
# fix-reference-links.sh - Update reference document cross-links

cd /mnt/j/pcloud_sync/5agent/1conf/3doca/docs/01_knowledge/04-reference

echo "Fixing reference document cross-links..."

find . -name "*.md" -type f -exec sed -i \
  's|GAP-MARKER-SPEC\.md|01-GAP-MARKER-SPEC.md|g; \
   s|TIER-DESIGN-SPEC\.md|02-TIER-DESIGN-SPEC.md|g; \
   s|MIGRATION-MAP\.md|03-MIGRATION-MAP.md|g; \
   s|FRONTMATTER-EXTENSION-SPEC\.md|04-FRONTMATTER-REFERENCE.md|g' {} \;

echo "✓ Reference cross-links updated"
echo "Fixed patterns:"
echo "  - GAP-MARKER-SPEC.md → 01-GAP-MARKER-SPEC.md"
echo "  - TIER-DESIGN-SPEC.md → 02-TIER-DESIGN-SPEC.md"
echo "  - MIGRATION-MAP.md → 03-MIGRATION-MAP.md"
echo "  - FRONTMATTER-EXTENSION-SPEC.md → 04-FRONTMATTER-REFERENCE.md"
```

**Script 3: Create Missing Concept Documents (fixes 2 issues)**

```bash
#!/bin/bash
# create-missing-concepts.sh - Create referenced but missing concept documents

cd /mnt/j/pcloud_sync/5agent/1conf/3doca

echo "Creating missing concept documents..."

# Create framework-overview.md
cat > docs/01_knowledge/01-concepts/01-framework-overview.md << 'EOF'
---
type: concept
category: framework
tags: [overview, introduction, diataxis, operations, architecture]
summary: High-level overview of the 3doca three-axis documentation framework
created: 2025-12-10
updated: 2025-12-10
---

# 3doca Framework Overview

[TODOCS: Add complete framework overview content]

## Three-Axis Structure

The 3doca framework organizes documentation along three complementary axes:

1. **Diátaxis Axis** (01_knowledge/) - For understanding and learning
2. **Operations Axis** (02_operations/) - For execution and procedures
3. **C4 Architecture Axis** (03_architecture/) - For system structure

## Key Benefits

[NEEDS_EXAMPLE: Add benefits and use cases]

## Related Documents

- [Three-Axis Structure](./three-axis-structure-concept.md)
- [Document Creation Process](../../02_operations/01-processes/01-document-creation-process.md)
EOF

# Create three-axis-structure-concept.md
cat > docs/01_knowledge/01-concepts/three-axis-structure-concept.md << 'EOF'
---
type: concept
category: architecture
tags: [structure, three-axis, diataxis, operations, c4]
summary: Detailed explanation of the three-axis documentation structure
created: 2025-12-10
updated: 2025-12-10
---

# Three-Axis Documentation Structure

[TODOCS: Add detailed explanation of the three-axis structure]

## The Three Axes

### 1. Diátaxis Axis (Knowledge)

[NEEDS_EXAMPLE: Add Diátaxis explanation]

### 2. Operations Axis (Execution)

[NEEDS_EXAMPLE: Add operations explanation]

### 3. C4 Axis (Architecture)

[NEEDS_EXAMPLE: Add C4 explanation]

## How the Axes Interact

[TODOCS: Add interaction patterns]

## Related Documents

- [Framework Overview](./01-framework-overview.md)
- [Gap Marker Specification](../04-reference/01-GAP-MARKER-SPEC.md)
EOF

echo "✓ Created missing concept documents"
echo "Created files:"
echo "  - docs/01_knowledge/01-concepts/01-framework-overview.md"
echo "  - docs/01_knowledge/01-concepts/three-axis-structure-concept.md"
```

**Script 4: Fix Playbook Directory Link (fixes 1 issue)**

```bash
#!/bin/bash
# fix-playbook-link.sh - Update directory link to file link

cd /mnt/j/pcloud_sync/5agent/1conf/3doca

# In how-to guide, change directory link to README link
sed -i 's|../../02_operations/playbooks/|../../02_operations/02-playbooks/README.md|g' \
  docs/01_knowledge/03-how-to/01-template-usage-guide.md

echo "✓ Fixed playbook directory link"
```

---

## Medium Priority: Mermaid Dark Mode (18 files)

**Impact**: Visual inconsistency, diagrams don't match dark theme.

**Solution**: Add `%%{init: {'theme': 'dark'}}%%` to all Mermaid diagrams.

### Quick Fix Script

```bash
#!/bin/bash
# add-mermaid-dark-mode.sh - Add dark mode theme to all Mermaid diagrams

cd /mnt/j/pcloud_sync/5agent/1conf/3doca

echo "Adding dark mode theme to Mermaid diagrams..."

count=0
find docs -name "*.md" -type f | while read file; do
  # Check if file contains Mermaid without theme
  if grep -q '```mermaid' "$file" && ! grep -q "%%{init:" "$file"; then
    # Create backup
    cp "$file" "$file.bak"

    # Add theme after ```mermaid
    sed -i '/```mermaid/a %%{init: {'"'"'theme'"'"': '"'"'dark'"'"'}}%%' "$file"

    echo "  ✓ Updated: $file"
    ((count++))
  fi
done

echo ""
echo "✓ Added dark mode theme to $count files"
echo "✓ Backup files created with .bak extension"
```

---

## Execution Checklist

### Phase 1: Critical Fixes (5-7 hours)

- [ ] **Step 1**: Run `add-frontmatter.sh` (auto: 15 README files)
- [ ] **Step 2**: Manually add frontmatter to 13 template files
- [ ] **Step 3**: Manually add frontmatter to 3 reference documents
- [ ] **Step 4**: Run `fix-directory-links.sh`
- [ ] **Step 5**: Run `fix-reference-links.sh`
- [ ] **Step 6**: Run `create-missing-concepts.sh`
- [ ] **Step 7**: Run `fix-playbook-link.sh`
- [ ] **Step 8**: Verify with `python3 verify_quality.py`

**Expected Result**: Score improves to 45-50/100

### Phase 2: Visual Consistency (1-2 hours)

- [ ] **Step 9**: Run `add-mermaid-dark-mode.sh`
- [ ] **Step 10**: Verify diagrams render correctly in preview
- [ ] **Step 11**: Re-run verification

**Expected Result**: Score improves to 65-70/100

---

## Verification Commands

After each phase, verify improvements:

```bash
# Run full verification
cd /mnt/j/pcloud_sync/5agent/1conf/3doca
python3 verify_quality.py

# Quick check: count remaining issues
echo "Frontmatter issues:"
grep -r "^---" docs --include="*.md" -L | wc -l

echo "Broken links:"
python3 -c "
import re
from pathlib import Path

issues = 0
for f in Path('docs').glob('**/*.md'):
    content = f.read_text()
    for match in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', content):
        link = match.group(2)
        if not link.startswith(('http', '#', 'mailto:')):
            target = (f.parent / link.split('#')[0]).resolve()
            if not target.exists():
                issues += 1
print(f'{issues} broken links')
"

echo "Mermaid without dark mode:"
grep -r "^\`\`\`mermaid" docs --include="*.md" | wc -l
grep -r "%%{init:" docs --include="*.md" | wc -l
```

---

## Rollback Plan

If any script causes issues:

```bash
# Restore from backups
find docs -name "*.bak" -exec sh -c 'mv "$1" "${1%.bak}"' _ {} \;

# Or use git
git checkout docs/
```

---

## Next Steps After Critical Fixes

1. **Content Quality** (3-5 hours):
   - Review and improve gap marker descriptions
   - Add concrete examples where marked
   - Verify technical claims

2. **Continuous Monitoring**:
   - Run verification before commits
   - Set up pre-commit hooks
   - Monthly quality reviews

3. **Automation**:
   - Integrate verification into CI/CD
   - Add automated link checking
   - Template validation on creation

---

## Support

For detailed analysis and recommendations, see:
- `reports/quality-verification-report-20251210.md` (full report)
- `verify_quality.py` (verification script source)

**Questions or Issues?** Review the detailed report for specific file-by-file analysis.
