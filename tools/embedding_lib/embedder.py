# tools/embedding_lib/embedder.py

import logging
from typing import List, Optional
import torch


class Embedder:
    def __init__(
        self,
        model_name: str,
        pooling: str = "mean",
        batch_size: int = 32,
        device: Optional[str] = None,
        backend: Optional[object] = None,
    ):
        """
        Initialize the Embedder.
        Args:
            model_name (str): HuggingFace model name or path.
            pooling (str): Pooling strategy ('mean', 'max', etc.).
            batch_size (int): Batch size for encoding.
            device (str, optional): 'cpu', 'cuda', 'auto', or None for auto-detect.
            backend (object, optional): Pluggable backend adapter (for future models).
        """
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)
        self.model_name = model_name
        self.pooling = pooling
        self.batch_size = batch_size

        # Device selection: if not specified, auto-detect CUDA
        if device is None or device == "auto":
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
        else:
            self.device = device
        self.logger.info(f"Using device: {self.device}")

        # Model backend: default to SentenceTransformers if not provided
        if backend is not None:
            self.backend = backend
            self.logger.info(f"Using custom backend for {model_name}")
        else:
            from sentence_transformers import SentenceTransformer

            # Loads the model to the specified device
            self.backend = SentenceTransformer(model_name, device=self.device)
            self.logger.info(f"Loaded model: {model_name}")

    def encode_chunks(
        self, chunks: List[str], prefix: Optional[str] = "passage:"
    ) -> List[List[float]]:
        """
        Embed a list of text chunks.
        Args:
            chunks (List[str]): List of input strings (docs/chunks).
            prefix (str, optional): Prefix for optimal model usage (e5 expects 'passage:' or 'query:').
        Returns:
            List[List[float]]: List of embedding vectors.
        """
        # Add prefix to each chunk if required by the model (e5 best practice)
        inputs = [f"{prefix} {chunk}" if prefix else chunk for chunk in chunks]
        self.logger.info(
            f"Encoding {len(inputs)} chunks (batch size: {self.batch_size})..."
        )
        # Batch encode all inputs (efficient for CUDA)
        embeddings = self.backend.encode(
            inputs, batch_size=self.batch_size, convert_to_numpy=True
        )
        self.logger.info(f"Generated embeddings with shape {embeddings.shape}")
        return embeddings

    # Additional methods for saving embeddings, changing pooling, etc., can be added here
