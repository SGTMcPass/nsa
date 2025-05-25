#!/usr/bin/env python3
"""
tools/chunker_lib/cli.py

Multi-purpose CLI for crawling, chunking, and manifesting Markdown docs.
"""
import os
import argparse
from pathlib import Path

from .config import load_config
from .core import chunk_documents


def run_chunk(args):
    """Run the chunk_documents pipeline and report the number of files processed."""
    cfg = load_config(args.config)
    seed = Path(os.path.expandvars(args.seed)).resolve()
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"⚙️  Starting chunking pipeline...")
    n = chunk_documents(cfg, seed, output_dir)
    print(f"🎉  Chunking complete. Processed {n} files. Output in {output_dir}")


def run_doc(args):
    """Placeholder for future full-document generation subcommand."""
    print("🛠️  The 'doc' subcommand is not yet implemented. Stay tuned!")


def main():
    parser = argparse.ArgumentParser(
        description="Multi-purpose CLI for Trick documentation processing."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # chunk subcommand
    p_chunk = subparsers.add_parser(
        "chunk", help="Chunk Markdown docs into pieces for embedding"
    )
    p_chunk.add_argument(
        "--config",
        required=True,
        help="YAML config file (docs_root, chunk_rules, overlap_pc, etc.)",
    )
    p_chunk.add_argument(
        "--seed",
        required=True,
        help="Seed Markdown file to start crawl (e.g. $TRICK_HOME/docs/index.md)",
    )
    p_chunk.add_argument(
        "--output",
        required=True,
        help="Directory to write chunk files, JSONL index, and manifest",
    )
    p_chunk.set_defaults(func=run_chunk)

    # doc subcommand
    p_doc = subparsers.add_parser(
        "doc", help="Generate a full document from chunks (TBD)"
    )
    p_doc.add_argument("--template", help="Path to document template (optional)")
    p_doc.add_argument("--output", help="Path to write generated document")
    p_doc.set_defaults(func=run_doc)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
