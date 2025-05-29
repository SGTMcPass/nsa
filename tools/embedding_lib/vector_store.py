# embedding_lib/vector_store.py

from abc import ABC, abstractmethod
import numpy as np


class VectorStore(ABC):
    @abstractmethod
    def add(self, embeddings: np.ndarray, ids: list):
        pass

    @abstractmethod
    def search(self, query: np.ndarray, k: int = 5):
        pass

    @abstractmethod
    def save(self, path: str):
        pass

    @abstractmethod
    def load(self, path: str):
        pass
