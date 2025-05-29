#!/usr/bin/env python3
"""
vectorstore_cli.py — CLI for FAISS vector store operations.
Implements the Stark Protocol.
"""

import sys
import argparse
import logging
from embedding_lib.faiss_vector_store import FaissVectorStore, VectorStoreError


def setup_logging(level=logging.INFO):
    logging.basicConfig(
        level=level, format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )


def main():
    parser = argparse.ArgumentParser(
        description="FAISS Vector Store CLI (Stark Protocol)"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    ingest_parser = subparsers.add_parser(
        "ingest", help="Ingest manifest and build FAISS index"
    )
    ingest_parser.add_argument(
        "--manifest", required=True, help="Path to embeddings manifest JSONL"
    )
    ingest_parser.add_argument(
        "--outpath", required=True, help="Output prefix for FAISS index and metadata"
    )

    query_parser = subparsers.add_parser("query", help="Query FAISS index")
    query_parser.add_argument(
        "--index", required=True, help="Base path for FAISS index/metadata"
    )
    query_parser.add_argument(
        "--query_vec",
        required=True,
        help="Comma-separated float vector, e.g. 0.1,0.2,0.3",
    )
    query_parser.add_argument(
        "--top_k", type=int, default=3, help="How many top matches to return"
    )

    parser.add_argument(
        "--loglevel", default="INFO", help="Log level (DEBUG, INFO, WARNING, ERROR)"
    )

    args = parser.parse_args()
    setup_logging(getattr(logging, args.loglevel.upper(), logging.INFO))

    if args.command == "ingest":
        store = FaissVectorStore()
        try:
            import json

            # Load manifest
            with open(args.manifest) as f:
                embeddings = []
                metadata = []
                for line in f:
                    if not line.strip():
                        continue
                    chunk = json.loads(line)
                    if "manifest_version" in chunk:
                        continue
                    embeddings.append(chunk["embedding"])
                    metadata.append(chunk)
            store.ingest(embeddings, metadata, args.outpath)
            print(
                f"[vectorstore_cli] Ingested {len(embeddings)} vectors to {args.outpath}.faiss"
            )
        except Exception as e:
            print(f"[vectorstore_cli] ERROR (ingest): {e}", file=sys.stderr)
            sys.exit(1)

    elif args.command == "query":
        store = FaissVectorStore()
        try:
            store.load(args.index)
            query_vec = [float(x) for x in args.query_vec.split(",")]
            results = store.query(query_vec, top_k=args.top_k)
            import json

            print(json.dumps(results, indent=2, ensure_ascii=False))
        except Exception as e:
            print(f"[vectorstore_cli] ERROR (query): {e}", file=sys.stderr)
            sys.exit(2)


if __name__ == "__main__":
    main()
