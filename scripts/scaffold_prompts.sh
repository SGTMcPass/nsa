#!/bin/bash
# scaffold_prompt.sh — Create a new prompt in next-prompts/ and register it in prompt_registry.yaml

set -e

ROOT=$(git rev-parse --show-toplevel)
REGISTRY="$ROOT/prompt_registry.yaml"

# --- Collect Metadata
read -p "Prompt ID (e.g. gnc_fault_report): " PROMPT_ID
read -p "Title (short description): " TITLE
read -p "Category (deepdive/toolbuild/overview): " CATEGORY
read -p "Tags (comma-separated): " TAGS
read -p "Domain (comma-separated): " DOMAIN
read -p "Version (e.g. 0.1): " VERSION
read -p "Output format (markdown/json/cpp): " OUTPUT_FORMAT

CATEGORY=${CATEGORY:-drafts}
DIR="next-prompts/${CATEGORY}"
FILE="${DIR}/${PROMPT_ID}.md"
REGISTRY_FILE="next-prompts/${CATEGORY}/${PROMPT_ID}.md"

mkdir -p "$DIR"

# --- Create Prompt Scaffold
cat <<EOF > "$FILE"
# ${TITLE}
**Purpose:** _TODO: Describe the problem this prompt solves_
**ID:** ${PROMPT_ID}
**Tag:** ${TAGS}
**Domain:** ${DOMAIN}
**Version:** ${VERSION}
**Status:** draft

---

## 🧠 Prompt Specification

_TODO: Describe what the AI should do. Include style, constraints, and reasoning._

---

## 📥 Example Input

\`\`\`yaml
# TODO: Define sample input format (YAML/JSON/text)
\`\`\`

---

## 📤 Output Expectation

\`\`\`plaintext
# TODO: List expected files or output format
\`\`\`

---

## 📝 Notes

_TODO: Add references, design rationale, or related prompts._
EOF

echo "✅ Created prompt file: $FILE"

# --- Append to Registry
cat <<EOF >> "$REGISTRY"

  - id: ${PROMPT_ID}
    title: "${TITLE}"
    file: ${REGISTRY_FILE}
    tags: [${TAGS//,/ }]
    domain: [${DOMAIN//,/ }]
    version: ${VERSION}
    input_format: none
    output_format: ${OUTPUT_FORMAT}
    status: draft
    notes: >
      This prompt is currently in development under next-prompts/${CATEGORY}/.
      Generated via scaffold_prompt.sh.
EOF

echo "✅ Registered in prompt_registry.yaml"
