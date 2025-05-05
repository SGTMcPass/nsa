#!/usr/bin/env python3
"""
lint_prompts.py — Validate all .json, .yaml, and .md prompt files and metadata in the repo.
"""

import json
import yaml
import re
from pathlib import Path
import sys

ROOT = Path(__file__).parent.parent
SCHEMA_VERSION = "v1.0.0"
SCHEMA_FILE = ROOT / "schemas" / f"assistant_profile.schema.{SCHEMA_VERSION}.json"

def is_profile_file(path: Path) -> bool:
    return (
        "assistant" in path.name
        or "profile" in path.name
    ) and "schemas" not in str(path)

def validate_json_file(path: Path) -> bool:
    try:
        if "schemas" in str(path):
            print(f"[⏭️] Skipping schema file: {path}")
            return True

        with open(path, 'r') as f:
            data = json.load(f)

        if is_profile_file(path):
            if not SCHEMA_FILE.exists():
                print(f"[⚠️] Warning: Schema not found at {SCHEMA_FILE}. Skipping schema validation.")
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
        with open(path, 'r') as f:
            yaml.safe_load(f)
        print(f"[✅] YAML valid: {path}")
        return True
    except Exception as e:
        print(f"[❌] YAML ERROR: {path} — {e}")
        return False

def validate_markdown_links(path: Path) -> bool:
    valid = True
    link_pattern = re.compile(r'\[.*?\]\((.*?)\)')
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

def scan_and_validate():
    print(f"🔎 Using schema version: {SCHEMA_VERSION}\n")

    json_files = list(ROOT.rglob("*.json"))
    yaml_files = list(ROOT.rglob("*.yaml")) + list(ROOT.rglob("*.yml"))
    md_files = list(ROOT.rglob("*.md"))

    print("📂 Validating JSON files...")
    json_results = [validate_json_file(f) for f in json_files]

    print("\n📂 Validating YAML files...")
    yaml_results = [validate_yaml_file(f) for f in yaml_files]

    print("\n📂 Validating Markdown links...")
    md_results = [validate_markdown_links(f) for f in md_files if "README" in f.name or "prompt" in f.name]

    all_passed = all(json_results + yaml_results + md_results)
    return all_passed

if __name__ == "__main__":
    try:
        from jsonschema import validate
    except ImportError:
        print("❌ Missing dependency: jsonschema\nInstall it with:\n  pip install jsonschema")
        sys.exit(1)

    success = scan_and_validate()
    if success:
        print("\n✅ All files passed validation.")
        sys.exit(0)
    else:
        print("\n❌ One or more files failed validation.")
        sys.exit(1)

