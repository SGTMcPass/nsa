#!/usr/bin/env python3
import os, sys, shutil
from pathlib import Path
import yaml

# Make sure our library is importable
sys.path.insert(0, os.path.abspath("tools"))

from chunker_lib.config import load_config
from chunker_lib.crawler import crawl_docs
from chunker_lib.utils import classify
from chunker_lib.splitter import extract_lineage, split_chunks
from chunker_lib.manifest import write_manifest
from markdown_it import MarkdownIt

# Use a local sample directory under the repo
sample_root = Path("sample_docs")
docs_dir = sample_root / "docs"
output_dir = sample_root / "chunks"

# Clean start
if sample_root.exists():
    shutil.rmtree(sample_root)
docs_dir.mkdir(parents=True)
output_dir.mkdir(parents=True, exist_ok=True)

# Create sample files
file1 = docs_dir / "intro.md"
file1.write_text(
    """---
layout: guide
title: Introduction
---
# Intro
This is the introduction to the sample docs.
""",
    encoding="utf-8",
)

file2 = docs_dir / "setup.md"
file2.write_text(
    """---
layout: reference
title: Setup
---
# Setup
Follow these steps to set up the environment.
See [Intro](intro.md) for context.
""",
    encoding="utf-8",
)

# Create a config.yaml for this sample
config = {
    "docs_root": str(docs_dir),
    "dir_map": {
        "docs": "howto",
    },
    "chunk_rules": {
        "howto": 20,
        "reference": 20,
        "unknown": 20,
    },
    "overlap_pc": 0.1,
    "image_ext": [
        ".png",
        ".jpg",
        ".jpeg",
        ".gif",
        ".svg",
        ".webp",
        ".bmp",
        ".ico",
        ".pdf",
    ],
}

config_path = sample_root / "config.yaml"
with open(config_path, "w", encoding="utf-8") as f:
    yaml.safe_dump(config, f)

# Run the chunker
cfg = load_config(str(config_path))
seed = docs_dir / "intro.md"
files = crawl_docs(seed, docs_dir)

md_parser = MarkdownIt()
metadata = []

for f in files:
    text = f.read_text(encoding="utf-8", errors="ignore")
    doc_type = classify(f, cfg)
    tokens = md_parser.parse(text)
    lineage = extract_lineage(tokens)
    size = cfg["chunk_rules"].get(doc_type, cfg["chunk_rules"]["unknown"])
    overlap = int(size * cfg["overlap_pc"])
    chunks = split_chunks(text, lineage, size, overlap)

    for idx, chunk in enumerate(chunks):
        chunk_id = f"{f.stem}_{idx:02d}"
        preview = chunk[:60].replace("\n", " ")
        metadata.append(
            {
                "chunk_id": chunk_id,
                "type": doc_type,
                "path": str(f.resolve().relative_to(docs_dir.resolve())),
                "heading": lineage,
                "preview": preview,
            }
        )

write_manifest(metadata, output_dir)

# Print out the manifest for inspection
print((output_dir / "chunks_manifest.md").read_text(encoding="utf-8"))
