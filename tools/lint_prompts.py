#!/usr/bin/env python3
"""
lint_prompts.py — Validate all .json, .yaml, and .md prompt files and metadata in the repo.
"""

from pathlib import Path
import sys

# ✅ Allow relative imports when running as script
if __name__ == "__main__" and __package__ is None:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import json
import yaml
import re
import argparse

ROOT = Path(__file__).parent.parent
SCHEMA_VERSION = "v1.0.0"
SCHEMA_FILE = ROOT / "schemas" / f"assistant_profile.schema.{SCHEMA_VERSION}.json"


def parse_args():
    parser = argparse.ArgumentParser(
        description="Validate prompt files: JSON schema, YAML, Markdown structure, and prompt metadata."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Optional: list of files to lint. If omitted, all prompt files will be validated.",
    )
    return parser.parse_args()


def is_profile_file(path: Path) -> bool:
    return (
        "assistant" in path.name or "profile" in path.name
    ) and "schemas" not in str(path)


def validate_json_file(path: Path) -> bool:
    try:
        if "schemas" in str(path):
            print(f"[⏭️] Skipping schema file: {path}")
            return True

        with open(path, "r") as f:
            data = json.load(f)

        if is_profile_file(path):
            if not SCHEMA_FILE.exists():
                print(
                    f"[⚠️] Warning: Schema not found at {SCHEMA_FILE}. Skipping schema validation."
                )
            else:
                from jsonschema import validate

                schema = json.loads(SCHEMA_FILE.read_text())
                validate(instance=data, schema=schema)
                print(f"[✅] JSON schema valid: {path}")
        else:
            print(f"[✅] JSON syntax valid: {path}")
        return True

    except Exception as e:
        print(f"[❌] JSON ERROR: {path} — {e}")
        return False


def validate_yaml_file(path: Path) -> bool:
    try:
        with open(path, "r") as f:
            yaml.safe_load(f)
        print(f"[✅] YAML valid: {path}")
        return True
    except Exception as e:
        print(f"[❌] YAML ERROR: {path} — {e}")
        return False


def validate_markdown_links(path: Path) -> bool:
    valid = True
    link_pattern = re.compile(r"\[.*?\]\((.*?)\)")
    for i, line in enumerate(path.read_text().splitlines()):
        for match in link_pattern.findall(line):
            if match.startswith("http"):
                continue
            target = (path.parent / match).resolve()
            if not target.exists():
                print(f"[❌] Broken link in {path}:{i + 1} → {match}")
                valid = False
    if valid:
        print(f"[✅] Markdown links valid: {path}")
    return valid


def scan_and_validate(paths=None):
    print(f"🔎 Using schema version: {SCHEMA_VERSION}\n")

    # If specific paths were passed, filter files by suffix
    if paths:
        json_files = [f for f in paths if f.endswith(".json")]
        yaml_files = [f for f in paths if f.endswith((".yaml", ".yml"))]
        md_files = [f for f in paths if f.endswith(".md")]
    else:
        json_files = list(ROOT.rglob("*.json"))
        yaml_files = list(ROOT.rglob("*.yaml")) + list(ROOT.rglob("*.yml"))
        md_files = list(ROOT.rglob("*.md"))

    print("📂 Validating JSON files...")
    json_results = [validate_json_file(Path(f)) for f in json_files]

    print("\n📂 Validating YAML files...")
    yaml_results = [validate_yaml_file(Path(f)) for f in yaml_files]

    print("\n📂 Validating Markdown links...")
    md_results = [
        validate_markdown_links(Path(f))
        for f in md_files
        if "README" in f or "prompt" in f
    ]

    # Only run prompt structure validation if scanning all or any .mds
    run_prompt_check = not paths or any(f.endswith(".md") for f in paths)
    if run_prompt_check:
        print("\n📂 Validating Prompt Markdown Structure...")
        from tools.validate_prompt_files import scan_all_prompts

        prompt_structure_results = scan_all_prompts()
    else:
        prompt_structure_results = True

    return all(json_results + yaml_results + md_results) and prompt_structure_results


if __name__ == "__main__":
    args = parse_args()
    try:
        from jsonschema import validate
    except ImportError:
        print(
            "❌ Missing dependency: jsonschema\nInstall it with:\n  pip install jsonschema"
        )
        sys.exit(1)

    success = scan_and_validate(paths=args.paths)
    sys.exit(0 if success else 1)
