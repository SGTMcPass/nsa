#!/usr/bin/env python3
"""
validate_prompt_files.py — Ensure all .md prompts meet structural and metadata expectations.
"""

import re
from pathlib import Path
import sys
import argparse

# ✅ Add project root to path if run directly
if __name__ == "__main__" and __package__ is None:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

ROOT = Path(__file__).parent.parent
PROMPT_DIRS = ["prompts", "next-prompts"]
REQUIRED_SECTIONS = [
    "## 🧠 Prompt Specification",
    "## 📥 Example Input",
    "## 📤 Output Expectation",
    "## 📝 Notes",
]

REQUIRED_METADATA = [
    "**Purpose:**",
    "**ID:**",
    "**Tag:**",
    "**Domain:**",
    "**Version:**",
    "**Status:**",
]


def validate_prompt_md(file: Path) -> bool:
    if "README" in file.name:
        print(f"[⏭️] Skipping README file: {file}")
        return True

    content = file.read_text(encoding="utf-8")
    valid = True

    # Check required metadata fields
    for meta in REQUIRED_METADATA:
        if meta not in content:
            print(f"[❌] {file}: missing metadata field: {meta}")
            valid = False

    # Check required section headers
    for section in REQUIRED_SECTIONS:
        if section not in content:
            print(f"[❌] {file}: missing section: {section}")
            valid = False

    # Check that ID matches filename
    id_match = re.search(r"\*\*ID:\*\*\s*(\S+)", content)
    if id_match:
        declared_id = id_match.group(1).strip()
        if file.stem != declared_id:
            print(
                f"[❌] {file}: ID '{declared_id}' does not match filename '{file.stem}'"
            )
            valid = False
    else:
        print(f"[❌] {file}: missing or malformed ID")
        valid = False

    if valid:
        print(f"[✅] Prompt valid: {file}")
    return valid


def scan_all_prompts():
    prompt_files = []
    for folder in PROMPT_DIRS:
        prompt_files.extend(Path(ROOT / folder).rglob("*.md"))

    results = [validate_prompt_md(f) for f in prompt_files]
    return all(results)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Validate prompt Markdown files for required metadata and structure."
    )
    parser.parse_args()  # support --help
    if scan_all_prompts():
        print("\n✅ All prompts passed structural validation.")
        sys.exit(0)
    else:
        print("\n❌ Prompt validation failed.")
        sys.exit(1)
