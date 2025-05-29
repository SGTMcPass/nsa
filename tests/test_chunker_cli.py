# tests/test_chunker_cli.py
import subprocess
import sys
import yaml
from pathlib import Path

import pytest


@pytest.fixture
def cli_sample_docs(tmp_path):
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    (docs_dir / "good.md").write_text("# Title\nBody text.")
    (docs_dir / "skip.txt").write_text("not markdown")
    return docs_dir


@pytest.fixture
def cli_minimal_config(tmp_path, cli_sample_docs):
    config = {
        "docs_root": str(cli_sample_docs),
        "dir_map": {"": "howto"},
        "chunk_rules": {"howto": 50},
        "overlap_pc": 0.0,
    }
    config_path = tmp_path / "config.yaml"
    with open(config_path, "w") as f:
        yaml.safe_dump(config, f)
    return config_path


def test_cli_happy_path(tmp_path, cli_minimal_config):
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    cli_path = Path(__file__).parent.parent / "tools" / "chunker_cli.py"
    cmd = [
        sys.executable,
        str(cli_path),
        "--config_path",
        str(cli_minimal_config),
        "--output_dir",
        str(output_dir),
        "--mode",
        "heading",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    assert result.returncode == 0
    manifest = output_dir / "chunks.jsonl"
    assert manifest.exists()
    with open(manifest) as f:
        lines = f.readlines()
    assert any("good.md" in line for line in lines)
    # CLI should print a summary message to stdout
    assert "Chunking completed" in result.stdout


def test_cli_missing_config(tmp_path):
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    cli_path = Path(__file__).parent.parent / "tools" / "chunker_cli.py"
    cmd = [
        sys.executable,
        str(cli_path),
        "--config_path",
        str(tmp_path / "nope.yaml"),
        "--output_dir",
        str(output_dir),
        "--mode",
        "heading",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    assert result.returncode != 0
    assert (
        "ERROR" in result.stderr
        or "error" in result.stderr
        or "config" in result.stderr.lower()
    )


def test_cli_bad_output_dir(tmp_path, cli_minimal_config):
    # Point output_dir to unwritable location
    unwritable_dir = tmp_path / "no_write"
    unwritable_dir.mkdir(mode=0o400)
    cli_path = Path(__file__).parent.parent / "tools" / "chunker_cli.py"
    cmd = [
        sys.executable,
        str(cli_path),
        "--config_path",
        str(cli_minimal_config),
        "--output_dir",
        str(unwritable_dir),
        "--mode",
        "heading",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    unwritable_dir.chmod(0o700)  # Reset for cleanup
    assert result.returncode != 0
    assert (
        "ERROR" in result.stderr
        or "Failed to write manifest" in result.stderr
        or "Could not write JSONL" in result.stderr
        or "UNEXPECTED ERROR" in result.stderr
    )
