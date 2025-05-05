#!/usr/bin/env python3
"""
load_prompt.py — CLI tool to query, list, validate, and export prompts from prompt_registry.yaml
"""

from pathlib import Path
import sys

# ✅ Allow relative imports when run as script
if __name__ == "__main__" and __package__ is None:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# (your actual imports follow here)
import argparse
import yaml
import json
from pathlib import Path

# Constants
REGISTRY_PATH = Path(__file__).parent.parent / "prompt_registry.yaml"
ROOT = Path(__file__).parent.parent


def load_registry():
    if not REGISTRY_PATH.exists():
        print(f"[ERROR] Registry not found at {REGISTRY_PATH}")
        return []
    with open(REGISTRY_PATH, "r") as f:
        data = yaml.safe_load(f)
    return data.get("registry", [])


def list_prompts(registry):
    print("📘 Registered Prompts:\n")
    for entry in registry:
        print(f"- ID: {entry['id']}")
        print(f"  Title: {entry['title']}")
        print(f"  File: {entry['file']}")
        print(f"  Tags: {', '.join(entry.get('tags', []))}")
        print(f"  Version: {entry.get('version', 'N/A')}")
        print()


def query_prompt(registry, query_id=None, tag=None, domain=None):
    results = []

    for entry in registry:
        if query_id and entry["id"] == query_id:
            results.append(entry)
        elif tag and tag in entry.get("tags", []):
            results.append(entry)
        elif domain and domain in entry.get("domain", []):
            results.append(entry)

    return results


def display_prompt(entry, format_json=False):
    if format_json:
        print(json.dumps(entry, indent=2))
        return

    print(f"\n📄 {entry['title']} ({entry['id']})")
    print(f"File: {entry['file']}")
    print(f"Tags: {', '.join(entry.get('tags', []))}")
    print(f"Version: {entry.get('version', 'N/A')}")
    print("Notes:\n" + textwrap.indent(entry.get("notes", ""), "  "))

    prompt_file = ROOT / entry["file"]
    if prompt_file.exists():
        print("\n🔍 Prompt Content:\n")
        print(prompt_file.read_text())
    else:
        print(f"[WARNING] Prompt file not found: {prompt_file}")


def export_prompt(entry, export_path):
    prompt_file = ROOT / entry["file"]
    export_path = Path(export_path)
    if not prompt_file.exists():
        print(f"[ERROR] Cannot export, source file missing: {prompt_file}")
        return
    export_path.write_text(prompt_file.read_text())
    print(f"[✅] Exported to {export_path}")


def validate_registry(registry):
    print("🔍 Validating prompt registry file paths...")
    all_valid = True
    for entry in registry:
        prompt_file = ROOT / entry["file"]
        if not prompt_file.exists():
            print(f"[❌] Missing file: {entry['file']} ({entry['id']})")
            all_valid = False
        else:
            print(f"[✅] Found: {entry['file']}")
    if all_valid:
        print("✅ All files referenced in the registry exist.")
    else:
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Prompt Registry CLI Tool")
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--list", action="store_true", help="List all registered prompts"
    )
    group.add_argument("--id", help="Query a prompt by ID")
    group.add_argument("--tag", help="Query prompts by tag")
    group.add_argument("--domain", help="Query prompts by domain")
    parser.add_argument(
        "--export", help="Export prompt content to a file (only works with --id)"
    )
    parser.add_argument("--format", choices=["json"], help="Format metadata as JSON")
    parser.add_argument(
        "--validate", action="store_true", help="Validate that all files exist"
    )

    args = parser.parse_args()
    registry = load_registry()

    if args.validate:
        validate_registry(registry)
    elif args.list:
        list_prompts(registry)
    elif args.id or args.tag or args.domain:
        results = query_prompt(registry, args.id, args.tag, args.domain)
        if not results:
            print("No matching prompts found.")
            return
        for entry in results:
            if args.export and args.id:
                export_prompt(entry, args.export)
            else:
                display_prompt(entry, format_json=(args.format == "json"))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
