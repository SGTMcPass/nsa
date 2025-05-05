# 🚀 NASA Simulation Prompt Assistant

A structured prompt engineering workspace for building, testing, and managing reusable AI prompts in aerospace simulation, control systems, GNC, and infrastructure toolchains.

---

## 📁 Project Structure

```bash
nasa-simulation-assistants/
├── prompts/                  # Prompt templates organized by function
│   ├── deepdive/
│   ├── overview/
│   └── toolbuild/
├── profiles/                # Assistant definitions (JSON/YAML/Markdown)
│   └── prompt/
├── schemas/                 # JSON schema for validating assistant profiles
├── tools/                   # CLI utilities for querying and converting prompts
├── scripts/                 # Bootstrap/local setup scripts
├── memory/                  # Session summaries (archivable memory traces)
├── .gitlab-ci.yml           # CI setup for validation
├── prompt_registry.yaml     # Master registry of all prompt files
├── .gitignore
├── README.md
└── VERSION
```

---

## 🧠 Assistant Profile

Defined in:
- `profiles/prompt/nasa_simulation_prompt_assistant.json`
- Exported to `.yaml` and `.md`

Validated against:
- `schemas/assistant_profile.schema.v1.0.0.json`

---

## 📚 Prompt Registry

All prompts are tracked in `prompt_registry.yaml`, which includes:

- `id`, `title`, `file`
- `tags`, `domain`, `version`
- `output_files` (static) or `output_pattern` (dynamic)

---

## 🛠 Tooling

### 📦 `tools/load_prompt.py`

Query and export prompt metadata from the registry.

```bash
# List all prompts
python3 tools/load_prompt.py --list

# Query by ID, tag, or domain
python3 tools/load_prompt.py --id trick_model_scaffold
python3 tools/load_prompt.py --tag deepdive

# Export a prompt to a file
python3 tools/load_prompt.py --id prompt_engineering_report --export out.md

# Validate all file paths listed in prompt_registry.yaml
python3 tools/load_prompt.py --validate
```

---

### 🧪 `tools/lint_prompts.py`

Run full project validation:

- JSON schema checks
- YAML and Markdown syntax
- Broken link detection
- Skips internal schemas

```bash
python3 tools/lint_prompts.py
```

### 🧬 `tools/convert_prompt_profile.py`

Convert assistant profiles between formats:

```bash
# Convert JSON → YAML + Markdown
python3 tools/convert_prompt_profile.py profiles/prompt/nasa_simulation_prompt_assistant.json

# Convert YAML → JSON + Markdown
python3 tools/convert_prompt_profile.py profiles/prompt/nasa_simulation_prompt_assistant.yaml
```

---

## 🧰 Makefile Targets

```bash
make lint           # Validate all prompt-related files
make list           # List registered prompts
make export ID=x FILE=out.md  # Export a specific prompt
make convert        # Convert assistant profile JSON → YAML + MD
```

---

## 🤖 Bootstrap Setup

To install dependencies and validate everything locally:

```bash
./scripts/bootstrap.sh
```

---

## ✅ CI: `.gitlab-ci.yml`

- Lints JSON/YAML/Markdown
- Validates schema + registry
- Tests prompt conversions
- Triggers only on relevant changes

---

## 📌 Versioning

- Schema version: `v1.0.0`
- Assistant profile versioning tracked in `prompt_registry.yaml`

