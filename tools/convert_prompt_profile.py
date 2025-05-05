#!/usr/bin/env python3
"""
convert_prompt_profile.py — Convert assistant profile between JSON, YAML, and Markdown formats.
"""

import json
import yaml
import argparse
from pathlib import Path
import textwrap

def load_profile(path: Path):
    if path.suffix == ".json":
        return json.loads(path.read_text()), "json"
    elif path.suffix in [".yaml", ".yml"]:
        return yaml.safe_load(path.read_text()), "yaml"
    else:
        raise ValueError(f"Unsupported input format: {path.suffix}")

def save_yaml(data, out_path):
    with open(out_path, "w") as f:
        yaml.dump(data, f, sort_keys=False)
    print(f"[✅] YAML saved to: {out_path}")

def save_json(data, out_path):
    with open(out_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"[✅] JSON saved to: {out_path}")

def save_markdown(data, out_path, source_name):
    md = f"# NASA Simulation Assistant Profile\n\n> Converted from `{source_name}`\n"

    def section(title):
        return f"\n## {title}\n"

    user = data.get("user_profile", {})
    md += section("👤 User Profile")
    for key, value in user.items():
        line = f"- **{key.capitalize()}**: {', '.join(value) if isinstance(value, list) else value}"
        md += line + "\n"

    pb = data.get("prompt_behavior", {})
    md += section("🎯 Prompt Behavior")

    structure = pb.get("structure", [])
    if structure:
        md += "\n**Structure:**\n"
        for item in structure:
            md += f"- {item}\n"

    reasoning = pb.get("reasoning", {})
    if reasoning:
        md += "\n**Reasoning Approach:**\n"
        for key, val in reasoning.items():
            md += f"- {key.replace('_', ' ').capitalize()}: {'✅' if val else '❌'}\n"

    tags = pb.get("tags", {})
    if tags:
        md += "\n**Tag Controls:**\n"
        for k, v in tags.items():
            md += f"- `{k}` → {v}\n"

    domains = pb.get("domains", [])
    if domains:
        md += "\n**Domains:**\n"
        for d in domains:
            md += f"- {d}\n"

    if pb.get("registry_support"):
        md += "\n**Registry Support Rules:**\n"
        for r in pb["registry_support"].get("rules", []):
            md += f"- {r}\n"

    enh = data.get("enhancements", {})
    md += section("🛠 Optional Enhancements")
    for k, v in enh.items():
        if isinstance(v, list):
            md += f"- **{k.replace('_', ' ').capitalize()}**:\n"
            for i in v:
                md += f"  - {i}\n"
        elif isinstance(v, dict):
            md += f"- **{k.replace('_', ' ').capitalize()}**:\n"
            for sub_k, sub_v in v.items():
                if isinstance(sub_v, list):
                    md += f"  - {sub_k}: {', '.join(sub_v)}\n"
                else:
                    md += f"  - {sub_k}: {sub_v}\n"
        else:
            md += f"- **{k}**: {v}\n"

    Path(out_path).write_text(md)
    print(f"[✅] Markdown saved to: {out_path}")

def main():
    parser = argparse.ArgumentParser(description="Convert assistant profile between JSON, YAML, and Markdown")
    parser.add_argument("input_file", help="Input JSON or YAML file")
    parser.add_argument("--json", help="Output JSON file (if input is YAML)")
    parser.add_argument("--yaml", help="Output YAML file (if input is JSON)")
    parser.add_argument("--markdown", help="Output Markdown file")

    args = parser.parse_args()
    input_path = Path(args.input_file)

    if not input_path.exists():
        print(f"[❌] File not found: {input_path}")
        return

    data, input_format = load_profile(input_path)

    # Default output filenames
    default_json = input_path.with_suffix(".json")
    default_yaml = input_path.with_suffix(".yaml")
    default_md = input_path.with_suffix(".md")

    if input_format == "json":
        save_yaml(data, Path(args.yaml) if args.yaml else default_yaml)
    elif input_format == "yaml":
        save_json(data, Path(args.json) if args.json else default_json)

    save_markdown(data, Path(args.markdown) if args.markdown else default_md, input_path.name)

if __name__ == "__main__":
    main()

