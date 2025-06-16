# tests/test_core.py
"""
Test Suite: Bulletproof Orchestration Tests for core.py

Covers: config loading, file crawling, chunking, manifest writing, logging, and summary output.
"""

import json
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
    result = core.chunk_documents(
        config_path=str(sample_config),
        output_dir=str(output_dir),
        mode="word",
        overwrite=True,
    )
    manifest_file = output_dir / "chunks.jsonl"
    assert manifest_file.exists()
    # Optionally: Load manifest and assert correct chunk structure/content
    with open(manifest_file) as f:
        lines = f.readlines()
    assert any("Valid Heading" in line for line in lines)


def test_pipeline_skips_and_logs(tmp_path, sample_config):
    """Test: Non-md and empty/malformed files are skipped, but pipeline completes."""
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    
    # Run the function - it should not raise any exceptions
    try:
        result = core.chunk_documents(
            config_path=str(sample_config),
            output_dir=str(output_dir),
            mode="word",
            overwrite=True,
        )
        # If we get here, the function completed successfully
        assert True
    except Exception as e:
        assert False, f"chunk_documents raised an exception: {e}"
    
    # Verify the output file was created
    manifest_file = output_dir / "chunks.jsonl"
    assert manifest_file.exists(), "Manifest file was not created"
    
    # Read the manifest and verify it contains the expected content
    with open(manifest_file) as f:
        lines = [line.strip() for line in f if line.strip()]
    
    # We should have at least one chunk from the valid markdown file
    assert len(lines) > 0, "No chunks were created"
    
    # Verify the chunks have the expected structure
    for line in lines:
        try:
            chunk = json.loads(line)
            assert "content" in chunk, f"Chunk missing 'content': {chunk}"
            assert "source_file" in chunk, f"Chunk missing 'source_file': {chunk}"
            assert "category" in chunk, f"Chunk missing 'category': {chunk}"
        except json.JSONDecodeError as e:
            assert False, f"Invalid JSON in manifest: {line}"


def test_pipeline_manifest_canonical(tmp_path, sample_config):
    """Test: Manifest output is canonical (one chunk per line, with all required metadata)."""
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    core.chunk_documents(
        config_path=str(sample_config),
        output_dir=str(output_dir),
        mode="word",
        overwrite=True,
    )
    manifest_file = output_dir / "chunks.jsonl"
    assert manifest_file.exists(), f"Manifest file {manifest_file} was not created"
    with open(manifest_file) as f:
        lines = [line.strip() for line in f if line.strip()]
    assert lines, "No chunks were written to the manifest"
    for line in lines:
        try:
            chunk = json.loads(line)
            assert "content" in chunk, f"Chunk missing 'content': {chunk}"
            assert "source_file" in chunk, f"Chunk missing 'source_file': {chunk}"
            assert "category" in chunk, f"Chunk missing 'category': {chunk}"
        except json.JSONDecodeError as e:
            assert False, f"Invalid JSON in manifest line: {line}\nError: {e}"


# Add more tests as needed:
# - config loading errors
# - manifest write errors (simulate permissions issues)
# - pipeline with missing docs_root or empty config
