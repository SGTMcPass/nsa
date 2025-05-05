#!/bin/bash
# bootstrap.sh — Local setup and validation script for prompt assistant repo

set -e

echo "🔧 Setting up local environment..."

# Step 1: Create virtual environment
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
  echo "✅ Virtual environment created."
else
  echo "🔁 Virtual environment already exists."
fi

# Step 2: Activate and install dependencies
source .venv/bin/activate
pip install --quiet --upgrade pip
pip install --quiet pyyaml jsonschema

echo "📦 Dependencies installed."

# Step 3: Run validations
echo ""
echo "🔍 Running prompt file validation..."
python tools/lint_prompts.py

echo ""
echo "🧪 Testing prompt profile conversion..."
python tools/convert_prompt_profile.py profiles/prompt/nasa_simulation_prompt_assistant.json --markdown /dev/null

echo ""
echo "📦 Validating prompt registry paths..."
python tools/load_prompt.py --validate

echo ""
echo "✅ Bootstrap complete. Local environment is ready."
