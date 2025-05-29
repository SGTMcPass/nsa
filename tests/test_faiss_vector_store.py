import numpy as np
import tempfile
import os

from embedding_lib.faiss_vector_store import FaissVectorStore


def test_faiss_vector_store_add_and_search():
    # Generate dummy embeddings and IDs
    num_vecs, dim = 5, 768
    embeddings = np.random.rand(num_vecs, dim).astype(np.float32)
    ids = [f"chunk_{i}" for i in range(num_vecs)]

    # Initialize FAISS vector store
    store = FaissVectorStore(dim=dim)
    store.add(embeddings, ids)

    # Query with one of the embeddings (should return its own ID as top-1 match)
    query = embeddings[2:3]
    results = store.search(query, k=1)
    assert (
        results[0][0] == ids[2]
    ), f"Expected top match to be {ids[2]}, got {results[0][0]}"


def test_faiss_vector_store_save_and_load():
    num_vecs, dim = 3, 768
    embeddings = np.random.rand(num_vecs, dim).astype(np.float32)
    ids = [f"test_{i}" for i in range(num_vecs)]

    # Create temp dir for save/load
    with tempfile.TemporaryDirectory() as tmpdir:
        index_path = os.path.join(tmpdir, "test_vectors")
        store = FaissVectorStore(dim=dim)
        store.add(embeddings, ids)
        store.save(index_path)

        # Create a new store, load the data, and search
        new_store = FaissVectorStore(dim=dim)
        new_store.load(index_path)

        # Should match the original IDs
        query = embeddings[0:1]
        results = new_store.search(query, k=1)
        assert results[0][0] == ids[0], f"Expected {ids[0]}, got {results[0][0]}"


if __name__ == "__main__":
    test_faiss_vector_store_add_and_search()
    test_faiss_vector_store_save_and_load()
    print("✅ All FAISS vector store tests passed.")
