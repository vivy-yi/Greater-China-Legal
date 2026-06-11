#!/usr/bin/env python3
"""
validate-skills.py — Validate SKILL.md frontmatter format

Checks each SKILL.md in the repository for:
1. Required YAML frontmatter fields
2. Legal frame identifier
3. Effective date on legal sources
4. No prohibited US law references (UCC, FRCP, Delaware law, etc.)
5. Trigger phrases present
"""

import re
import sys
from pathlib import Path

LEGAL_FRAMES = {"cn-mainland", "hk", "mo", "tw", "sg"}
PROHIBITED_TERMS = [
    "UCC", "FRCP", "FIRREA", "Delaware law", "Delaware Corporations",
    "SEC regulations", "CFTC regulations", "FINRA", "Sarbanes-Oxley",
    "ERISA", "HIPAA", "FCPA", "Bankruptcy Code", "Title11",
]

REQUIRED_FIELDS = ["name", "description", "legal_frame", "last_reviewed", "version"]


def extract_frontmatter(content: str) -> tuple[dict, str]:
    """Extract YAML frontmatter from SKILL.md content."""
    match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if not match:
        return {}, content
    import yaml
    try:
        data = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        data = {}
    body = content[match.end():]
    return data, body


def check_legal_sources(data: dict) -> list[str]:
    """Check that all legal sources have effective dates."""
    errors = []
    sources = data.get("legal_sources", [])
    if not sources:
        errors.append("Warning: no legal_sources defined")
        return errors
    for i, src in enumerate(sources):
        if not src.get("effective_date"):
            errors.append(f"  legal_sources[{i}]: missing effective_date")
    return errors


def check_prohibited_terms(body: str) -> list[str]:
    """Check for prohibited US law terms in body."""
    errors = []
    for term in PROHIBITED_TERMS:
        if term.lower() in body.lower():
            errors.append(f"Prohibited term found: '{term}'")
    return errors


def validate_file(path: Path) -> list[str]:
    """Validate a single SKILL.md file. Returns list of errors."""
    errors = []
    try:
        content = path.read_text(encoding="utf-8")
    except Exception as e:
        return [f"Cannot read file: {e}"]

    data, body = extract_frontmatter(content)

    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: {field}")

    # Check legal_frame
    frame = data.get("legal_frame", "")
    if frame not in LEGAL_FRAMES:
        if frame:
            errors.append(f"Invalid legal_frame: '{frame}' (allowed: {LEGAL_FRAMES})")
        else:
            errors.append("Missing legal_frame")

    # Check trigger phrases
    triggers = data.get("trigger_phrases", [])
    if not triggers:
        errors.append("Missing trigger_phrases")

    # Check legal sources effective dates
    if "legal_sources" in data:
        errors.extend(check_legal_sources(data))

    # Check prohibited terms
    errors.extend(check_prohibited_terms(body))

    return errors


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Validate SKILL.md files")
    parser.add_argument("--path", default=".", help="Root path to validate")
    parser.add_argument("--fix", action="store_true", help="Attempt to auto-fix issues")
    parser.add_argument("--frame", help="Filter by legal frame (e.g. cn-mainland)")
    args = parser.parse_args()

    root = Path(args.path)
    skill_files = list(root.glob("**/SKILL.md*"))

    total_errors = {}
    for f in skill_files:
        if args.frame and args.frame not in f.name:
            continue
        errors = validate_file(f)
        if errors:
            total_errors[str(f)] = errors

    if not total_errors:
        print("✅ All SKILL.md files passed validation")
        sys.exit(0)

    print(f"❌ {len(total_errors)} files with issues:\n")
    for f, errors in total_errors.items():
        print(f"  {f}:")
        for e in errors:
            print(f"    - {e}")
        print()

    sys.exit(1)


if __name__ == "__main__":
    main()