#!/usr/bin/env python3

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import argparse
from embedding_lib.embedder import embed_documents

def main():
    parser = argparse.ArgumentParser(description="Embed chunks and output embedding manifest.")
    parser.add_argument('--config', required=True, help='Path to embedding config YAML.')
    parser.add_argument('--output_dir', required=True, help='Output directory for embeddings manifest.')
    parser.add_argument('--overwrite', action='store_true', help='Overwrite outputs if present.')
    args = parser.parse_args()

    summary = embed_documents(
        config_path=args.config,
        output_dir=args.output_dir,
        overwrite=args.overwrite
    )
    print(f"Embedded chunks: {summary.get('total_embeddings', 0)}")
    print(f"Skipped files: {summary.get('skipped_chunks', 0)}")

if __name__ == '__main__':
    main()
