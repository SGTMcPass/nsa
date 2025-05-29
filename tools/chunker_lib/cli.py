# chunker_lib/cli.py

import sys
import argparse
from pathlib import Path

from chunker_lib.core import chunk_documents, ChunkerCoreError


def main():
    parser = argparse.ArgumentParser(description="NASA Simulation Agents Chunker CLI")
    parser.add_argument(
        "--config_path",
        required=True,
        type=str,
        help="Path to chunker YAML config file",
    )
    parser.add_argument(
        "--output_dir",
        required=True,
        type=str,
        help="Directory to write manifest and outputs",
    )
    parser.add_argument(
        "--mode",
        default="word",
        choices=["word", "paragraph", "heading"],
        help="Chunking mode (default: word)",
    )
    parser.add_argument(
        "--overwrite", action="store_true", help="Overwrite manifest if it exists"
    )

    args = parser.parse_args()

    try:
        manifest = chunk_documents(
            config_path=args.config_path,
            output_dir=args.output_dir,
            mode=args.mode,
            overwrite=args.overwrite,
        )
        if not manifest:
            print(
                "[cli] WARNING: No chunks produced. Check input files and config.",
                file=sys.stderr,
            )
        else:
            print(
                f"[cli] Chunking completed. {len(manifest)} chunks written to {Path(args.output_dir) / 'chunks.jsonl'}"
            )
    except ChunkerCoreError as e:
        print(f"[cli] ERROR: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"[cli] UNEXPECTED ERROR: {e}", file=sys.stderr)
        sys.exit(2)
