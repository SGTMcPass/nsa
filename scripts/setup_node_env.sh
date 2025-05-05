#!/usr/bin/env bash
# setup_node_env.sh — Configures user-local npm global install and installs markdownlint-cli

set -e

echo "📦 Setting up user-local npm global install path..."

# Step 1: Configure npm to use a user-local directory
NPM_GLOBAL_DIR="${HOME}/.npm-global"
mkdir -p "$NPM_GLOBAL_DIR"
npm config set prefix "$NPM_GLOBAL_DIR"

# Step 2: Ensure ~/.npm-global/bin is in PATH
PROFILE_FILE="${HOME}/.bashrc"
EXPORT_LINE='export PATH="$HOME/.npm-global/bin:$PATH"'

if ! grep -Fxq "$EXPORT_LINE" "$PROFILE_FILE"; then
    echo "$EXPORT_LINE" >> "$PROFILE_FILE"
    echo "✅ Added npm global bin path to $PROFILE_FILE"
else
    echo "✅ npm global bin path already in $PROFILE_FILE"
fi

# Step 3: Apply path change to current session
export PATH="$HOME/.npm-global/bin:$PATH"

# Step 4: Install markdownlint-cli
echo "📥 Installing markdownlint-cli..."
npm install -g markdownlint-cli

echo "✅ markdownlint-cli installed to $NPM_GLOBAL_DIR/bin"
echo "ℹ️  You may need to restart your shell if the command is not found."
