#!/usr/bin/env python3
"""
tools/chunker_lib/core.py

Core functionality for crawling, chunking, and manifesting Markdown docs.
Provides a function that can be used in both CLI and tests.
"""
from pathlib import Path
from markdown_it import MarkdownIt

from .config import load_config
from .utils import safe_read, classify
from .crawler import crawl_docs
from .splitter import extract_lineage, split_chunks
from .manifest import write_manifest


def chunk_documents(cfg: dict, seed: Path, output_dir: Path) -> int:
    """
    Crawl the docs tree, split each Markdown file into chunks,
    write chunk files, JSONL index, and Markdown manifest.

    Args:
        cfg: Configuration dictionary loaded from YAML.
        seed: Entry-point Markdown file Path.
        output_dir: Directory Path to write outputs.

    Returns:
        Number of Markdown files processed.
    """
    docs_root = Path(cfg["docs_root"]).expanduser().resolve()
    # Crawl markdown files
    files = crawl_docs(seed, docs_root)

    md_parser = MarkdownIt()
    metadata = []
    for path in files:
        text = safe_read(path)
        doc_type = classify(path, cfg)
        tokens = md_parser.parse(text)
        lineage = extract_lineage(tokens)

        size = cfg.get("chunk_rules", {}).get(
            doc_type, cfg.get("chunk_rules", {}).get("unknown", 500)
        )
        overlap = int(size * cfg.get("overlap_pc", 0.15))
        chunks = split_chunks(text, lineage, size, overlap)

        # Write individual chunk files
        chunk_subdir = output_dir / doc_type
        chunk_subdir.mkdir(parents=True, exist_ok=True)

        rel_path = str(path.relative_to(docs_root))
        for idx, chunk in enumerate(chunks):
            chunk_id = f"{path.stem}_{idx:02d}"
            # write markdown file
            (chunk_subdir / f"{chunk_id}.md").write_text(chunk, encoding="utf-8")
            # collect metadata
            preview = chunk[:80].replace("\n", " ")
            metadata.append(
                {
                    "chunk_id": chunk_id,
                    "type": doc_type,
                    "path": rel_path,
                    "heading": lineage,
                    "preview": preview,
                }
            )

    # Write index and manifest
    write_manifest(metadata, output_dir)
    return len(files)
