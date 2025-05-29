import pytest
import numpy as np
from pathlib import Path
import json

from embedding_lib.faiss_vector_store import FaissVectorStore, VectorStoreError


@pytest.fixture
def sample_embeddings_and_meta(tmp_path):
    # 3 random vectors, dim=4
    embeddings = [
        [0.1, 0.2, 0.3, 0.4],
        [0.2, 0.1, 0.0, 0.9],
        [0.9, 0.8, 0.7, 0.6],
    ]
    meta = [
        {"source_file": "a.md", "chunk_index": 0, "chunk_hash": "aaa"},
        {"source_file": "b.md", "chunk_index": 0, "chunk_hash": "bbb"},
        {"source_file": "c.md", "chunk_index": 1, "chunk_hash": "ccc"},
    ]
    index_path = tmp_path / "my_index"
    return embeddings, meta, index_path


def test_faiss_build_ingest_and_query(tmp_path, sample_embeddings_and_meta):
    embeddings, meta, index_path = sample_embeddings_and_meta
    store = FaissVectorStore()
    # Ingest/build and save index
    store.ingest(embeddings, meta, str(index_path))
    # Reload from disk
    new_store = FaissVectorStore()
    new_store.load(str(index_path))
    # Query with close vector to embedding[0]
    query = [0.1, 0.2, 0.3, 0.4]
    results = new_store.query(query, top_k=2)
    # Should return at least one result, with correct metadata
    assert len(results) >= 1
    assert "source_file" in results[0]
    assert "chunk_hash" in results[0]
    assert results[0]["source_file"] == "a.md"


def test_save_and_load_metadata_file(tmp_path, sample_embeddings_and_meta):
    embeddings, meta, index_path = sample_embeddings_and_meta
    store = FaissVectorStore()
    store.ingest(embeddings, meta, str(index_path))
    # Check .meta.json exists and is valid
    meta_path = str(index_path) + ".meta.json"
    assert Path(meta_path).exists()
    with open(meta_path) as f:
        loaded = json.load(f)
    assert loaded == meta


def test_missing_index_file_raises(tmp_path):
    store = FaissVectorStore()
    with pytest.raises(FileNotFoundError):
        store.load(str(tmp_path / "nope_index"))


def test_query_invalid_embedding_shape(tmp_path, sample_embeddings_and_meta):
    embeddings, meta, index_path = sample_embeddings_and_meta
    store = FaissVectorStore()
    store.ingest(embeddings, meta, str(index_path))
    store.load(str(index_path))
    # Query with wrong shape should be handled or logged
    with pytest.raises(Exception):
        # Query with a vector of wrong dimension (dim=3 instead of 4)
        store.query([0.1, 0.2, 0.3])


def test_ingest_fails_on_empty_embeddings(tmp_path):
    store = FaissVectorStore()
    with pytest.raises(VectorStoreError):
        store.ingest([], [], str(tmp_path / "idx"))


def test_soft_fail_on_bad_metadata(tmp_path):
    # Bad metadata: missing chunk_hash, should still index and log
    embeddings = [[0.5, 0.5, 0.5, 0.5]]
    meta = [{"source_file": "bad.md", "chunk_index": 9}]  # No chunk_hash
    index_path = tmp_path / "weird"
    store = FaissVectorStore()
    store.ingest(embeddings, meta, str(index_path))
    # Should have saved the file, with missing field (but not fail)
    meta_path = str(index_path) + ".meta.json"
    assert Path(meta_path).exists()
    with open(meta_path) as f:
        loaded = json.load(f)
    assert loaded[0]["source_file"] == "bad.md"
