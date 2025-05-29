# tests/test_core.py
"""
Test Suite: Bulletproof Orchestration Tests for core.py

Covers: config loading, file crawling, chunking, manifest writing, logging, and summary output.
"""

import pytest
from pathlib import Path
import shutil
import yaml

from chunker_lib import core  # Adjust import path as needed


@pytest.fixture
def sample_docs(tmp_path):
    """Create a test docs tree with various edge cases."""
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()

    # Valid Markdown
    valid_md = docs_dir / "valid.md"
    valid_md.write_text("# Valid Heading\nSome valid content.")

    # Empty Markdown
    empty_md = docs_dir / "empty.md"
    empty_md.write_text("")

    # Malformed Markdown (simulate with nonsense)
    malformed_md = docs_dir / "malformed.md"
    malformed_md.write_text("\x00\x01\x02")

    # Non-markdown file
    not_md = docs_dir / "not_a_markdown.txt"
    not_md.write_text("This should be skipped.")

    return docs_dir


@pytest.fixture
def sample_config(tmp_path, sample_docs):
    """Generate a valid config.yaml with minimal rules."""
    config = {
        "docs_root": str(sample_docs),
        "dir_map": {"": "howto"},
        "chunk_rules": {"howto": 100},
        "overlap_pc": 0.0,
    }
    config_path = tmp_path / "config.yaml"
    with open(config_path, "w") as f:
        yaml.dump(config, f)
    return config_path


def test_pipeline_happy_path(tmp_path, sample_config):
    """Test: All valid .md files processed, manifest written, summary/output as expected."""
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    result = core.run_pipeline(
        config_path=str(sample_config),
        output_dir=str(output_dir),
        mode="heading",
        overwrite=True,
    )
    manifest_file = output_dir / "chunks.jsonl"
    assert manifest_file.exists()
    # Optionally: Load manifest and assert correct chunk structure/content
    with open(manifest_file) as f:
        lines = f.readlines()
    assert any("Valid Heading" in line for line in lines)


def test_pipeline_skips_and_logs(tmp_path, sample_config, caplog):
    """Test: Non-md and empty/malformed files are skipped/warned, but pipeline completes."""
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    core.run_pipeline(
        config_path=str(sample_config),
        output_dir=str(output_dir),
        mode="heading",
        overwrite=True,
    )
    logs = caplog.text
    assert "Skipped" in logs or "Warning" in logs
    assert "empty.md" in logs
    assert "malformed.md" in logs
    assert "not_a_markdown.txt" in logs


def test_pipeline_manifest_canonical(tmp_path, sample_config):
    """Test: Manifest output is canonical (one chunk per line, with all required metadata)."""
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    core.run_pipeline(
        config_path=str(sample_config),
        output_dir=str(output_dir),
        mode="heading",
        overwrite=True,
    )
    manifest_file = output_dir / "chunks.jsonl"
    with open(manifest_file) as f:
        for line in f:
            chunk = yaml.safe_load(line)  # or json.loads(line)
            assert "content" in chunk
            assert "source_file" in chunk
            assert "category" in chunk


# Add more tests as needed:
# - config loading errors
# - manifest write errors (simulate permissions issues)
# - pipeline with missing docs_root or empty config
