import pytest
import yaml
from pathlib import Path

from chunker_lib.core import chunk_documents


def test_chunk_documents_creates_expected_files(tmp_path):
    # 1. Arrange: create a small docs tree
    docs_root = tmp_path / "docs"
    docs_root.mkdir()

    # Sample Markdown file with guide layout -> classified as howto
    intro_md = docs_root / "intro.md"
    intro_md.write_text(
        """
---
layout: guide
title: Introduction
---
# Intro
This is the introduction.
"""
    )

    # 2. Create minimal config dict
    cfg = {
        "docs_root": str(docs_root),
        "chunk_rules": {"howto": 10, "unknown": 10},
        "overlap_pc": 0.1,
        "dir_map": {"docs": "howto"},
        "image_ext": [],
    }

    # 3. Act: run chunk_documents
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    processed_files = chunk_documents(cfg, intro_md, output_dir)

    # 4. Assert: one file processed
    assert processed_files == 1

    # Manifest and JSONL index should be created
    manifest = output_dir / "chunks_manifest.md"
    jsonl = output_dir / "chunks.jsonl"
    assert manifest.exists(), "chunks_manifest.md should exist"
    assert jsonl.exists(), "chunks.jsonl should exist"

    # The howto subdirectory should contain at least one chunk file
    howto_dir = output_dir / "howto"
    assert howto_dir.exists(), "howto directory should exist"
    chunk_files = list(howto_dir.glob("intro_*.md"))
    assert chunk_files, "Expected at least one chunk file for intro.md"

    # Manifest should list the chunk_id and preview of the intro chunk
    manifest_text = manifest.read_text()
    assert "intro_00" in manifest_text
    assert "Introduction" in manifest_text
