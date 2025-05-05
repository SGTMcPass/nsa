#!/bin/bash
# test_tools.sh — Validate that all tools/*.py scripts execute without import or syntax errors

set -e

ROOT=$(git rev-parse --show-toplevel)
TOOLS_DIR="$ROOT/tools"

echo "🔍 Testing executable scripts in $TOOLS_DIR"
echo

failures=0

for script in "$TOOLS_DIR"/*.py; do
  script_name=$(basename "$script")
  echo "🧪 Running ./$script_name --help"

  if ! "$script" --help > /dev/null 2>&1; then
    echo "❌ $script_name FAILED to execute"
    ((failures++))
  else
    echo "✅ $script_name passed"
  fi

  echo
done

if [ $failures -eq 0 ]; then
  echo "🎉 All tools executed successfully."
  exit 0
else
  echo "❌ $failures tool(s) failed."
  exit 1
fi
