"""
embedder.py — Embedding pipeline core for NASA Simulation Agents.
Implements the Stark Protocol: Modular, resilient, CLI-ready.

Key features:
- Modular functions for loading, embedding, and saving
- Robust logging via Python `logging`
- All errors/warnings surfaced; per-file failures do not stop the batch
- Outputs canonical, traceable embedding manifest
"""

import os
import json
import yaml
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional

import numpy as np
from sentence_transformers import SentenceTransformer

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)
logger = logging.getLogger("embedding_lib.embedder")

logger = logging.getLogger("embedding_lib.embedder")
logger.setLevel(logging.INFO)


def load_config(config_path: str) -> Dict[str, Any]:
    """Load YAML config with environment variable expansion and validation."""
    path = Path(os.path.expandvars(config_path))
    if not path.exists():
        logger.error(f"Config file does not exist: {config_path}")
        raise FileNotFoundError(f"Config file does not exist: {config_path}")
    with open(path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    # Expand env vars in string fields
    for k, v in config.items():
        if isinstance(v, str):
            config[k] = os.path.expandvars(v)
    if "input_chunks" not in config or not config["input_chunks"]:
        logger.error("Config missing input_chunks path.")
        raise ValueError("Config missing input_chunks path.")
    if "embedding_model" not in config or not config["embedding_model"]:
        logger.warning("No embedding_model specified. Using 'all-MiniLM-L6-v2'.")
        config["embedding_model"] = "all-MiniLM-L6-v2"
    if "output_name" not in config or not config["output_name"]:
        config["output_name"] = "embeddings.jsonl"
    return config


def load_chunks(chunks_path: str) -> List[Dict[str, Any]]:
    """Load input chunks from JSONL file."""
    chunks = []
    path = Path(chunks_path)
    if not path.exists():
        logger.error(f"Chunks file does not exist: {chunks_path}")
        raise FileNotFoundError(f"Chunks file does not exist: {chunks_path}")
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                try:
                    chunks.append(json.loads(line))
                except Exception as e:
                    logger.warning(f"Malformed chunk skipped: {e}")
    logger.info(f"Loaded {len(chunks)} input chunks from {chunks_path}")
    return chunks


def save_jsonl(data: List[Dict[str, Any]], outpath: str, overwrite: bool = True):
    """Write list of dicts to JSONL, logs on error."""
    path = Path(outpath)
    if path.exists() and not overwrite:
        logger.warning(f"File {outpath} exists and overwrite=False. Skipping write.")
        return
    try:
        with open(path, "w", encoding="utf-8") as f:
            for item in data:
                f.write(json.dumps(item, ensure_ascii=False) + "\n")
        logger.info(f"Manifest written: {outpath} ({len(data)} embeddings)")
    except Exception as e:
        logger.error(f"Could not write JSONL to {outpath}: {e}")


def generate_embedding(model, text: str) -> List[float]:
    """Generate embedding for a single chunk of text."""
    try:
        emb = model.encode(text)
        return emb.tolist() if isinstance(emb, np.ndarray) else list(emb)
    except Exception as e:
        logger.warning(f"Embedding failed for text: {e}")
        raise


def embed_documents(
    config_path: str,
    output_dir: str,
    overwrite: bool = True,
) -> Dict[str, Any]:
    """
    Orchestrate the full embedding pipeline.
    Implements the Stark Protocol.
    Returns summary dict: {manifest, skipped_chunks, total_embeddings}
    """
    logger.info(f"Loading config from: {config_path}")
    try:
        config = load_config(config_path)
    except Exception as e:
        logger.error(f"Failed to load config: {e}")
        raise

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest = []
    skipped_chunks = []

    logger.info(f"Loading embedding model: {config['embedding_model']}")
    try:
        model = SentenceTransformer(config["embedding_model"])
    except Exception as e:
        logger.error(f"Failed to load embedding model: {e}")
        raise

    chunks = load_chunks(config["input_chunks"])
    for idx, chunk in enumerate(chunks):
        # Defensive: ensure required fields are present
        if not chunk.get("content"):
            logger.warning(
                f"Chunk missing 'content', skipped: {chunk.get('source_file', '')}:{chunk.get('chunk_index', idx)}"
            )
            skipped_chunks.append(chunk.get("source_file", "unknown"))
            continue
        try:
            emb = generate_embedding(model, chunk["content"])
            chunk_out = dict(chunk)  # Copy original metadata
            chunk_out["embedding"] = emb
            manifest.append(chunk_out)
        except Exception as e:
            logger.warning(
                f"Embedding failed for {chunk.get('source_file', '')}:{chunk.get('chunk_index', idx)}: {e}"
            )
            skipped_chunks.append(chunk.get("source_file", "unknown"))
            continue

    manifest_path = output_dir / config["output_name"]
    if manifest:
        save_jsonl(manifest, manifest_path, overwrite=overwrite)
    else:
        logger.warning("No embeddings to write.")

    logger.info(
        f"Embedding summary: {len(manifest)} chunks embedded, {len(skipped_chunks)} skipped."
    )
    return {
        "manifest": manifest,
        "skipped_chunks": skipped_chunks,
        "total_embeddings": len(manifest),
    }
