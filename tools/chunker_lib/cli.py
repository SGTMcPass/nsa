# cli.py
#!/usr/bin/env python3
"""
CLI entrypoint for chunker_lib.
"""
import argparse
from pathlib import Path
from markdown_it import MarkdownIt
from .config import load_config
from .utils import classify
from .crawler import crawl_docs
from .splitter import extract_lineage, split_chunks
from .manifest import write_manifest


def main():
    parser = argparse.ArgumentParser(
        description='Chunk documentation into token-based segments.'
    )
    parser.add_argument('--config', required=True)
    parser.add_argument('--seed', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    cfg = load_config(args.config)
    seed = Path(args.seed)
    docs_root = Path(cfg['docs_root'])
    output_dir = Path(args.output)

    files = crawl_docs(seed, docs_root)
    metadata = []
    for f in files:
        text = f.read_text(encoding='utf-8', errors='ignore')
        doc_type = classify(f, cfg)
        tokens = MarkdownIt().parse(text)
        lineage = extract_lineage(tokens)
        size = cfg['chunk_rules'].get(doc_type, cfg['chunk_rules']['unknown'])
        overlap = int(size * cfg['overlap_pc'])
        chunks = split_chunks(text, lineage, size, overlap)
        for idx, chunk in enumerate(chunks):
            chunk_id = f"{f.stem}_{idx:02d}"
            preview = chunk[:80].replace('\n', ' ')
            metadata.append({
                'chunk_id': chunk_id,
                'type': doc_type,
                'path': str(f.relative_to(docs_root)),
                'heading': lineage,
                'preview': preview,
            })
    write_manifest(metadata, output_dir)

if __name__ == '__main__':
    main()
