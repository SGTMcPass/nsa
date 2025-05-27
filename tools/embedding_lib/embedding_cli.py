#!/usr/bin/env python3
"""
embedding_cli.py
----------------
Batch embedding tool for NASA Trick simulation documentation chunks.
Loads configuration from YAML (with CLI overrides), processes input chunks, and saves vectorized outputs.
"""

import argparse
import yaml
import logging
import json
import os
import numpy as np
from tools.embedding_lib.embedder import Embedder


def parse_args():
    parser = argparse.ArgumentParser(
        description="Batch embedding for Trick simulation docs with modular backend."
    )
    parser.add_argument(
        "--config", default="config/embedding.yaml", help="YAML config file path"
    )
    parser.add_argument("--input", help="Input file with text chunks (e.g., JSONL)")
    parser.add_argument("--output", help="Output directory or file for embeddings")
    parser.add_argument("--model", help="Embedding model name or path")
    parser.add_argument("--pooling", help="Pooling type (mean, max, etc.)")
    parser.add_argument("--batch_size", type=int, help="Batch size for embedding")
    parser.add_argument("--device", help="Device override: 'cuda' or 'cpu'")
    parser.add_argument(
        "--format",
        default="npy",
        choices=["npy", "json", "jsonl"],
        help="Output format",
    )
    parser.add_argument(
        "--log_level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Logging level",
    )
    parser.add_argument(
        "--dry_run",
        action="store_true",
        help="Validate config and inputs, don't run embedding",
    )
    return parser.parse_args()


def load_chunks(input_file):
    """
    Load chunks from a JSONL file (one JSON object per line).
    Returns a list of dicts or strings.
    Raises FileNotFoundError or JSONDecodeError for malformed files.
    """
    chunks = []
    with open(input_file, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            try:
                obj = json.loads(line)
                chunks.append(obj)
            except json.JSONDecodeError as e:
                logging.error(f"Malformed JSON on line {i} of {input_file}: {e}")
                raise
    logging.info(f"Loaded {len(chunks)} chunks from {input_file}")
    return chunks


def save_embeddings(embeddings, output_dir, fmt):
    """
    Save embeddings to disk in the specified format.
    Supported: npy, json, jsonl.
    """
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    # Compose output file path
    out_file = os.path.join(output_dir, f"embeddings.{fmt}")
    # Save based on requested format
    if fmt == "npy":
        np.save(out_file, embeddings)
    elif fmt == "json":
        import json

        with open(out_file, "w", encoding="utf-8") as f:
            json.dump(embeddings, f)
    elif fmt == "jsonl":
        import json

        with open(out_file, "w", encoding="utf-8") as f:
            for emb in embeddings:
                f.write(json.dumps(emb) + "\n")
    else:
        raise ValueError(f"Unknown output format: {fmt}")
    logging.info(f"Embeddings saved to {out_file} ({fmt})")


# Main entrypoint
def main():
    # Parse all CLI arguments
    args = parse_args()

    # Configure logging as early as possible
    logging.basicConfig(level=getattr(logging, args.log_level.upper()))
    logging.info("Embedding CLI starting...")

    # Load configuration from YAML
    with open(args.config) as f:
        cfg = yaml.safe_load(f)

    # Override YAML settings with CLI arguments if provided
    input_file = args.input or cfg.get("input_file")
    output_dir = args.output or cfg.get("output_dir")
    model = args.model or cfg.get("model")
    pooling = args.pooling or cfg.get("pooling", "mean")
    batch_size = args.batch_size or cfg.get("batch_size", 32)
    device = args.device  # Optionally passed to Embedder
    fmt = args.format

    # Early exit if dry run requested
    if args.dry_run:
        logging.info("Dry run: config and paths validated. Exiting.")
        return

    chunks = load_chunks(input_file)

    # --- Create Embedder instance ---
    try:
        embedder = Embedder(
            model, pooling=pooling, batch_size=batch_size, device=device
        )
        logging.info(
            f"Embedder initialized: {model} (pooling={pooling}, batch={batch_size}, device={device})"
        )
    except Exception as e:
        logging.error(f"Failed to initialize Embedder: {e}")
        raise

    # --- Run embedding ---
    # Process chunks in batches using the Embedder
    try:
        embeddings = embedder.embed(chunks)
        logging.info(f"Successfully embedded {len(embeddings)} chunks.")
    except Exception as e:
        logging.error(f"Embedding failed: {e}")
        raise

    save_embeddings(embeddings, output_dir, fmt)

    # Logging final state for traceability
    logging.info(
        f"Ready to embed: {input_file} -> {output_dir} [{model}] (batch={batch_size}, pooling={pooling})"
    )


if __name__ == "__main__":
    main()
