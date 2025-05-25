import sys
import pytest
from pathlib import Path
import yaml

from chunker_lib.cli import main as cli_main


def test_cli_chunk_end_to_end(tmp_path, monkeypatch, capsys):
    # Arrange: create docs tree
    root = tmp_path / "trick_home"
    docs = root / "docs"
    docs.mkdir(parents=True)
    intro = docs / "intro.md"
    intro.write_text(
        """
---
layout: guide
title: Introduction
---
# Intro
Sample intro text for CLI test.
"""
    )

    # Write config.yaml
    cfg = {
        "docs_root": str(docs),
        "chunk_rules": {"howto": 8, "unknown": 8},
        "overlap_pc": 0.1,
        "dir_map": {"docs": "howto"},
        "image_ext": [],
    }
    cfg_path = tmp_path / "config.yaml"
    cfg_path.write_text(yaml.safe_dump(cfg))

    # Output directory
    output_dir = tmp_path / "output"

    # Monkeypatch environment for seed expansion
    monkeypatch.setenv("TRICK_HOME", str(root))

    # Act: simulate CLI invocation
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "chunker",
            "chunk",
            "--config",
            str(cfg_path),
            "--seed",
            "$TRICK_HOME/docs/intro.md",
            "--output",
            str(output_dir),
        ],
    )
    # Run CLI main
    cli_main()

    # Capture CLI output
    captured = capsys.readouterr()
    assert "Starting chunking pipeline" in captured.out
    assert "Chunking complete" in captured.out

    # Assert: outputs exist
    manifest = output_dir / "chunks_manifest.md"
    jsonl = output_dir / "chunks.jsonl"
    assert manifest.exists()
    assert jsonl.exists()

    # Assert: chunk file written under howto
    chunk_dir = output_dir / "howto"
    assert chunk_dir.exists() and any(chunk_dir.iterdir())


def test_cli_doc_stub(capsys):
    # Act: test 'doc' stub prints placeholder
    args = ["chunker", "doc"]
    monkeypatch = pytest.MonkeyPatch()
    monkeypatch.setattr(sys, "argv", args)
    try:
        cli_main()
    finally:
        monkeypatch.undo()
    captured = capsys.readouterr()
    assert "not yet implemented" in captured.out
