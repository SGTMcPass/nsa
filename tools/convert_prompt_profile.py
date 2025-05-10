#!/usr/bin/env python3
"""
convert_prompt_profile.py — Converts a YAML assistant profile to JSON and Markdown.
Validates JSON against the assistant schema.
"""

import yaml
import json
import sys
from textwrap import fill
from jsonschema import validate, ValidationError
from pathlib import Path

# Constants
SCHEMA_PATH = (
    Path(__file__).parent.parent / "schemas/assistant_profile.schema.v1.0.0.json"
)


def load_schema():
    """Load the JSON schema for assistant profile validation."""
    try:
        with open(SCHEMA_PATH, "r") as f:
            schema = json.load(f)
        return schema
    except FileNotFoundError:
        print(f"[ERROR] Schema file not found at {SCHEMA_PATH}")
        sys.exit(1)


def wrap_text(text, width=80):
    """Wraps text to a specified width for Markdown compatibility."""
    return "\n".join([fill(line, width) for line in text.splitlines()])


def yaml_to_json(yaml_data):
    """Converts the loaded YAML to structured JSON"""
    required_sections = ["prompt_behavior", "enhancements", "user_profile"]
    for section in required_sections:
        if section not in yaml_data:
            raise ValueError(f"[❌] Missing required section: {section}")

    json_data = {
        "name": yaml_data.get("name"),
        "description": yaml_data.get("description"),
        "user_profile": yaml_data.get("user_profile"),
        "prompt_behavior": yaml_data.get("prompt_behavior"),
        "enhancements": yaml_data.get("enhancements"),
        "memory_summary_format": yaml_data.get("memory_summary_format"),
        "output_files": yaml_data.get("output_files"),
        "output_pattern": yaml_data.get("output_pattern"),
        "notes": yaml_data.get("notes", ""),
    }

    return json_data


def yaml_to_markdown(yaml_data):
    """Converts the loaded YAML to Markdown format with lint compliance"""
    return f"""
# {yaml_data.get('name')}

**Description:**
{wrap_text(yaml_data.get('description'))}

---

## 🧑‍🚀 User Profile

- **Role:** {yaml_data['user_profile']['role']}
- **Background:** {wrap_text(yaml_data['user_profile']['background'])}

- **Languages:**
  {wrap_text(", ".join(yaml_data['user_profile']['languages']))}

- **Tools:**
  {wrap_text(", ".join(yaml_data['user_profile']['tools']))}

- **Formats:**
  {wrap_text(", ".join(yaml_data['user_profile']['formats']))}

- **Platforms:**
  {wrap_text(", ".join(yaml_data['user_profile']['platforms']))}

- **Style:** {yaml_data['user_profile']['style']}

---

## 🔍 Prompt Behavior

- **Structure:**
  {wrap_text(", ".join(yaml_data['prompt_behavior']['structure']))}

- **Reasoning Style:**
  {wrap_text(", ".join(f"{k}: {v}" for k, v in yaml_data['prompt_behavior']['reasoning'].items()))}

- **Tags:**
  {wrap_text(", ".join(yaml_data['prompt_behavior']['tags'].keys()))}

- **Domains:**
  {wrap_text(", ".join(yaml_data['prompt_behavior']['domains']))}

---

## 🚀 Enhancements

- **Formats:**
  {wrap_text(", ".join(yaml_data['enhancements']['formats']))}

- **Styles:**
  {wrap_text(", ".join(yaml_data['enhancements']['styles']))}

- **Modes:**
  {wrap_text(", ".join(yaml_data['enhancements']['modes']))}

- **Tooling Integration:**
  - CLI Tool: {yaml_data['enhancements']['tooling_integration']['cli_tool']}
  - Registry: {yaml_data['enhancements']['tooling_integration']['prompt_registry_yaml']}
  - Makefile Commands:
    {wrap_text(", ".join(yaml_data['enhancements']['tooling_integration']['makefile_commands']))}

---

## 📝 Notes

{wrap_text(yaml_data.get('notes', 'N/A'))}
    """


def convert(yaml_file):
    """Main conversion logic"""
    try:
        yaml_path = Path(yaml_file)
        if not yaml_path.exists():
            print(f"[❌] YAML file not found: {yaml_file}")
            sys.exit(1)

        with open(yaml_path, "r") as f:
            data = yaml.safe_load(f)

        # Generate filenames
        json_file = yaml_path.with_suffix(".json")
        md_file = yaml_path.with_suffix(".md")

        # Convert to JSON
        json_data = yaml_to_json(data)

        # Validate JSON
        schema = load_schema()
        validate(instance=json_data, schema=schema)
        print("✅ JSON is valid against the schema.")

        # Write JSON
        with open(json_file, "w") as f:
            json.dump(json_data, f, indent=4)
        print(f"✅ Successfully converted to '{json_file}'")

        # Convert to Markdown
        markdown_data = yaml_to_markdown(data)

        # Write Markdown
        with open(md_file, "w") as f:
            f.write(markdown_data.strip() + "\n")  # Ensure newline at EOF
        print(f"✅ Successfully converted to '{md_file}'")

    except ValidationError as ve:
        print(f"[❌] Schema Validation Error: {ve.message}")
        sys.exit(1)
    except Exception as e:
        print(f"[❌] Conversion failed: {e}")
        sys.exit(1)


# Command-line usage
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convert_prompt_profile.py <input_yaml>")
    else:
        convert(sys.argv[1])
