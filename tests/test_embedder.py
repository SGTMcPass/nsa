import pytest
import yaml
import json
from pathlib import Path

from embedding_lib.embedder import embed_documents


@pytest.fixture
def test_chunks(tmp_path):
    """Creates a JSONL file with test chunks, including a bad/empty one."""
    chunks = [
        {
            "source_file": "good.md",
            "chunk_index": 0,
            "category": "howto",
            "content": "Hello world, this is a test chunk.",
        },
        {"source_file": "bad.md", "chunk_index": 1, "category": "howto", "content": ""},
        {
            "source_file": "malformed.md",
            "chunk_index": 2,
            "category": "howto",
            # missing 'content'
        },
    ]
    chunks_path = tmp_path / "chunks.jsonl"
    with open(chunks_path, "w") as f:
        for chunk in chunks:
            f.write(json.dumps(chunk) + "\n")
    return chunks_path


@pytest.fixture
def test_config(tmp_path, test_chunks):
    """Create a minimal config referencing the chunk file."""
    config = {
        "input_chunks": str(test_chunks),
        "embedding_model": "all-MiniLM-L6-v2",
        "output_name": "test_embeddings.jsonl",
    }
    config_path = tmp_path / "config.yaml"
    with open(config_path, "w") as f:
        yaml.safe_dump(config, f)
    return config_path


def test_embed_documents_happy_path(tmp_path, test_config):
    """Test: All valid chunks processed, manifest written, output as expected."""
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    result = embed_documents(
        config_path=str(test_config), output_dir=str(output_dir), overwrite=True
    )
    # Manifest should include only chunks with non-empty content
    assert "manifest" in result
    assert "skipped_chunks" in result
    assert "total_embeddings" in result
    assert result["total_embeddings"] == 1  # Only 'good.md' is valid
    manifest_path = output_dir / "test_embeddings.jsonl"
    assert manifest_path.exists()
    with open(manifest_path) as f:
        lines = f.readlines()
    # Only one valid output
    assert len(lines) == 1
    chunk = json.loads(lines[0])
    assert "embedding" in chunk
    assert "content" in chunk
    assert chunk["source_file"] == "good.md"


def test_embed_documents_missing_config(tmp_path):
    """Test: Missing config file should raise FileNotFoundError."""
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    with pytest.raises(FileNotFoundError):
        embed_documents(
            config_path=str(tmp_path / "nope.yaml"),
            output_dir=str(output_dir),
            overwrite=True,
        )


def test_embed_documents_missing_model(tmp_path, test_chunks):
    """Test: Missing model in config should fall back to default."""
    config = {"input_chunks": str(test_chunks), "output_name": "out.jsonl"}
    config_path = tmp_path / "config.yaml"
    with open(config_path, "w") as f:
        yaml.safe_dump(config, f)
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    result = embed_documents(
        config_path=str(config_path), output_dir=str(output_dir), overwrite=True
    )
    assert result["total_embeddings"] == 1


def test_embed_documents_fails_on_bad_chunks_file(tmp_path, test_config):
    """Test: Nonexistent chunks file raises FileNotFoundError."""
    # Patch config to reference a bad chunks file
    bad_config = {
        "input_chunks": str(tmp_path / "nope_chunks.jsonl"),
        "embedding_model": "all-MiniLM-L6-v2",
    }
    bad_config_path = tmp_path / "bad_config.yaml"
    with open(bad_config_path, "w") as f:
        yaml.safe_dump(bad_config, f)
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    with pytest.raises(FileNotFoundError):
        embed_documents(
            config_path=str(bad_config_path), output_dir=str(output_dir), overwrite=True
        )


def test_embed_documents_manifest_traceability(tmp_path, test_config):
    """Test: Each output includes traceable metadata (source_file, chunk_index, embedding)."""
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    result = embed_documents(
        config_path=str(test_config), output_dir=str(output_dir), overwrite=True
    )
    manifest_path = output_dir / "test_embeddings.jsonl"
    with open(manifest_path) as f:
        lines = f.readlines()
    chunk = json.loads(lines[0])
    assert "source_file" in chunk
    assert "chunk_index" in chunk
    assert "embedding" in chunk
    assert isinstance(chunk["embedding"], list)
