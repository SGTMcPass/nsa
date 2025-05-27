#!/bin/bash

# Move to the directory where the script lives
cd "$(dirname "$0")"

# Go to the project root (parent of 'scripts')
cd ..

# Set directories and files to include
CHUNKER_LIB="tools/chunker_lib"
TESTS="tests"
CONFIG_DIR="config"
EXTRA_FILES="README.md setup.py requirements.txt"
OUTPUT_DIR="scripts"  # Where to place the zip

# Name the zip with a timestamp
OUTPUT_ZIP="$OUTPUT_DIR/chunker_package_$(date +%Y%m%d_%H%M%S).zip"

# Create the zip archive from project root
zip -r "$OUTPUT_ZIP" \
    "$CHUNKER_LIB" \
    "$TESTS" \
    "$CONFIG_DIR" \
    $EXTRA_FILES \
    -x "*.pyc" -x "__pycache__/*" -x "*.egg-info/*"

echo "Zipped files into $OUTPUT_ZIP"
