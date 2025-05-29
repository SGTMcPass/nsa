import faiss
import numpy as np
from embedding_lib.vector_store import VectorStore


class FaissVectorStore(VectorStore):
    def __init__(self, dim: int):
        self.index = faiss.IndexFlatL2(dim)
        self.ids = []

    def add(self, embeddings: np.ndarray, ids: list):
        assert len(embeddings) == len(ids)
        self.index.add(embeddings.astype(np.float32))
        self.ids.extend(ids)

    def search(self, query: np.ndarray, k: int = 5):
        D, I = self.index.search(query.astype(np.float32), k)
        # Map FAISS indices back to user IDs
        return [[self.ids[i] for i in idxs] for idxs in I]

    def save(self, path: str):
        faiss.write_index(self.index, path + ".index")
        # Save IDs in parallel
        with open(path + ".ids", "w") as f:
            for id_ in self.ids:
                f.write(f"{id_}\n")

    def load(self, path: str):
        self.index = faiss.read_index(path + ".index")
        with open(path + ".ids") as f:
            self.ids = [line.strip() for line in f]
