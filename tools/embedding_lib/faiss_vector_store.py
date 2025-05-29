"""
faiss_vector_store.py — FAISS backend for NASA Simulation Agents.
Implements the Stark Protocol: Modular, resilient, CLI-ready.

Key features:
- Subclasses the abstract vector store interface
- Robust logging via Python `logging`
- All warnings/errors surfaced, soft fail on per-vector error
- All vectors linked to their full metadata for traceability
"""

import logging
import faiss
import numpy as np
import json
from pathlib import Path
from typing import List, Dict, Any, Optional

from .vector_store import AbstractVectorStore, setup_logging, VectorStoreError

logger = setup_logging()


class FaissVectorStore(AbstractVectorStore):
    def __init__(self):
        self.index = None
        self.metadata = None

    def ingest(
        self,
        embeddings: List[List[float]],
        metadata: List[Dict[str, Any]],
        outpath: str,
    ) -> None:
        """Ingest embeddings and metadata into FAISS, and save to disk."""
        try:
            self.index = self.build_faiss_index(embeddings)
            self.metadata = metadata
            self.save(outpath)
        except Exception as e:
            logger.error(f"Ingest failed: {e}")
            raise VectorStoreError(e)

    def build_faiss_index(self, embeddings: List[List[float]]):
        if not embeddings:
            logger.error("No embeddings provided to build index.")
            raise ValueError("No embeddings to index.")
        arr = np.vstack(embeddings).astype("float32")
        dim = arr.shape[1]
        index = faiss.IndexFlatL2(dim)
        index.add(arr)
        logger.info(f"FAISS index built with {arr.shape[0]} vectors (dim {dim})")
        return index

    def save(self, outpath: str) -> None:
        """Persist index and metadata to disk."""
        faiss_path = str(outpath) + ".faiss"
        meta_path = str(outpath) + ".meta.json"
        faiss.write_index(self.index, faiss_path)
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(self.metadata, f, ensure_ascii=False, indent=2)
        logger.info(f"Saved FAISS index to {faiss_path} and metadata to {meta_path}")

    def load(self, index_path: str):
        """Load index and metadata from disk."""
        faiss_path = str(index_path) + ".faiss"
        meta_path = str(index_path) + ".meta.json"
        if not Path(faiss_path).exists():
            logger.error(f"FAISS index not found: {faiss_path}")
            raise FileNotFoundError(faiss_path)
        if not Path(meta_path).exists():
            logger.error(f"FAISS metadata not found: {meta_path}")
            raise FileNotFoundError(meta_path)
        self.index = faiss.read_index(faiss_path)
        with open(meta_path, "r", encoding="utf-8") as f:
            self.metadata = json.load(f)
        logger.info(f"Loaded FAISS index ({faiss_path}) and metadata ({meta_path})")

    def query(
        self, query_embedding: List[float], top_k: int = 5
    ) -> List[Dict[str, Any]]:
        """Query the FAISS index and return top_k matches with full metadata."""
        if not isinstance(query_embedding, np.ndarray):
            query_embedding = np.array(query_embedding, dtype="float32").reshape(1, -1)
        D, I = self.index.search(query_embedding, top_k)
        results = []
        for idx in I[0]:
            if idx < 0 or idx >= len(self.metadata):
                logger.warning(f"Query returned invalid index: {idx}")
                continue
            results.append(self.metadata[idx])
        logger.info(f"FAISS query returned {len(results)} results (top_k={top_k})")
        return results
