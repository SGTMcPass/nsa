import subprocess
import sys
import json
from pathlib import Path
import pytest


@pytest.fixture
def tiny_manifest(tmp_path):
    data = [
        {
            "embedding": [0.1, 0.2, 0.3, 0.4],
            "source_file": "a.md",
            "chunk_index": 0,
            "chunk_hash": "aaa",
        },
        {
            "embedding": [0.2, 0.1, 0.0, 0.9],
            "source_file": "b.md",
            "chunk_index": 1,
            "chunk_hash": "bbb",
        },
    ]
    manifest_path = tmp_path / "tiny.jsonl"
    with open(manifest_path, "w") as f:
        f.write(json.dumps({"manifest_version": "1.0"}) + "\n")
        for row in data:
            f.write(json.dumps(row) + "\n")
    return manifest_path, data


def test_cli_ingest_and_query(tmp_path, tiny_manifest):
    manifest_path, data = tiny_manifest
    outpath = tmp_path / "cli_index"
    cli_path = Path(__file__).parent.parent / "tools" / "vectorstore_cli.py"

    # Ingest
    ingest_cmd = [
        sys.executable,
        str(cli_path),
        "--loglevel",
        "INFO",
        "ingest",
        "--manifest",
        str(manifest_path),
        "--outpath",
        str(outpath),
    ]
    ingest = subprocess.run(ingest_cmd, capture_output=True, text=True)
    assert ingest.returncode == 0
    assert "Ingested 2 vectors" in ingest.stdout

    # Query
    query_cmd = [
        sys.executable,
        str(cli_path),
        "--loglevel",
        "INFO",
        "query",
        "--index",
        str(outpath),
        "--query_vec",
        "0.1,0.2,0.3,0.4",
        "--top_k",
        "1",
    ]
    query = subprocess.run(query_cmd, capture_output=True, text=True)
    assert query.returncode == 0
    output = json.loads(query.stdout)
    assert isinstance(output, list)
    assert output[0]["source_file"] == "a.md"


def test_cli_missing_args(tmp_path):
    cli_path = Path(__file__).parent.parent / "tools" / "vectorstore_cli.py"
    # Should fail due to missing required subcommand
    result = subprocess.run(
        [sys.executable, str(cli_path)], capture_output=True, text=True
    )
    assert result.returncode != 0
    assert "usage:" in result.stderr or "usage:" in result.stdout


def test_cli_bad_manifest(tmp_path):
    cli_path = Path(__file__).parent.parent / "tools" / "vectorstore_cli.py"
    bad_manifest = tmp_path / "does_not_exist.jsonl"
    outpath = tmp_path / "out"
    ingest_cmd = [
        sys.executable,
        str(cli_path),
        "ingest",
        "--manifest",
        str(bad_manifest),
        "--outpath",
        str(outpath),
    ]
    result = subprocess.run(ingest_cmd, capture_output=True, text=True)
    assert result.returncode != 0
    assert "ERROR" in result.stderr or "ERROR" in result.stdout


def test_cli_bad_query(tmp_path, tiny_manifest):
    manifest_path, data = tiny_manifest
    outpath = tmp_path / "cli_index"
    cli_path = Path(__file__).parent.parent / "tools" / "vectorstore_cli.py"
    # Ingest first
    subprocess.run(
        [
            sys.executable,
            str(cli_path),
            "ingest",
            "--manifest",
            str(manifest_path),
            "--outpath",
            str(outpath),
        ]
    )
    # Now bad query: wrong vector dim
    query_cmd = [
        sys.executable,
        str(cli_path),
        "query",
        "--index",
        str(outpath),
        "--query_vec",
        "0.9,0.8",  # Wrong dimension!
    ]
    result = subprocess.run(query_cmd, capture_output=True, text=True)
    assert result.returncode != 0
    assert "ERROR" in result.stderr or "ERROR" in result.stdout
