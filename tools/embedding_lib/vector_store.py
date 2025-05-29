"""
vector_store.py — Abstract vector store interface for NASA Simulation Agents.
Implements the Stark Protocol: Modular, resilient, CLI-ready.

Key features:
- Pure abstract class for vector store backends (FAISS, Chroma, etc.)
- Robust logging via Python `logging` (if shared utils are present)
- Never instantiated directly; all usage via subclassing
- Explicit contract for all vectorstore operations
"""

import abc
import logging
from typing import List, Dict, Any


def setup_logging(level=logging.INFO, name=None):
    logging.basicConfig(
        level=level, format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )
    return logging.getLogger(name or __name__)


logger = setup_logging()


class VectorStoreError(Exception):
    """Custom error for vector store pipeline."""


class AbstractVectorStore(abc.ABC):
    """Abstract base class for vector store implementations."""

    @abc.abstractmethod
    def ingest(
        self,
        embeddings: List[List[float]],
        metadata: List[Dict[str, Any]],
        outpath: str,
    ) -> None:
        """Ingest embeddings and metadata into the store."""
        pass

    @abc.abstractmethod
    def query(
        self, query_embedding: List[float], top_k: int = 5
    ) -> List[Dict[str, Any]]:
        """Query top_k vectors, returning matching metadata."""
        pass

    @abc.abstractmethod
    def save(self, outpath: str) -> None:
        """Persist index and metadata to disk."""
        pass

    @abc.abstractmethod
    def load(self, index_path: str):
        """Load index and metadata from disk."""
        pass

    @staticmethod
    def load_manifest(manifest_path: str) -> List[Dict[str, Any]]:
        """Utility to load embedding manifest (JSONL, skip version header if present)."""
        import json
        from pathlib import Path

        chunks = []
        path = Path(manifest_path)
        if not path.exists():
            logger.error(f"Manifest file does not exist: {manifest_path}")
            raise FileNotFoundError(f"Manifest file does not exist: {manifest_path}")
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    try:
                        row = json.loads(line)
                        if "manifest_version" in row:
                            continue
                        chunks.append(row)
                    except Exception as e:
                        logger.warning(f"Malformed line skipped: {e}")
        logger.info(f"Loaded {len(chunks)} chunks from {manifest_path}")
        return chunks

    # Add any common utility or validation methods here (static/classmethods).


# Usage:
# class FaissVectorStore(AbstractVectorStore):
#     ... implement all abstract methods ...
