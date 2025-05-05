#!/bin/bash
# tag-and-release.sh — Tag your assistant project as v1.0.0

set -e

VERSION="v1.0.0"

echo "🔖 Tagging release: $VERSION"

# Check for uncommitted changes
if ! git diff-index --quiet HEAD --; then
  echo "⚠️ You have uncommitted changes. Please commit or stash first."
  exit 1
fi

# Create tag
git tag -a $VERSION -m "Release $VERSION: Initial prompt assistant milestone"
git push origin $VERSION

echo "✅ Tagged and pushed as $VERSION"

