import os
import shutil
import yaml
from pathlib import Path
from markdown_it import MarkdownIt

import tools.chunker_lib.config   as cfg_mod
import tools.chunker_lib.crawler  as crawler
import tools.chunker_lib.utils    as utils
import tools.chunker_lib.splitter as splitter
import tools.chunker_lib.manifest as manifest

def test_sample_docs_integration(tmp_path):
    # 1. Arrange: create a small sample_docs tree
    sample_root = tmp_path / "sample_docs"
    docs_dir    = sample_root / "docs"
    out_dir     = sample_root / "chunks"
    docs_dir.mkdir(parents=True)
    out_dir.mkdir()

    # intro.md (howto) and setup.md (reference) linking back to intro
    (docs_dir/"intro.md").write_text(
        """---
layout: guide
title: Introduction
---
# Intro
This is the introduction."""
    )
    (docs_dir/"setup.md").write_text(
        """---
layout: reference
title: Setup
---
# Setup
Follow steps; see [Intro](intro.md)."""
    )

    # 2. Write config.yaml
    cfg = {
        "docs_root": str(docs_dir.resolve()),
        "dir_map": {"docs": "howto"},
        "chunk_rules": {"howto": 20, "reference": 20, "unknown": 20},
        "overlap_pc": 0.1,
        "image_ext": []
    }
    cfg_path = sample_root / "config.yaml"
    cfg_path.write_text(yaml.safe_dump(cfg))

    # 3. Act: run each stage
    config = cfg_mod.load_config(str(cfg_path))
    seed   = docs_dir / "setup.md"
    files  = crawler.crawl_docs(seed, Path(config["docs_root"]))
    mdp    = MarkdownIt()

    metadata = []
    for f in files:
        text     = f.read_text(encoding="utf-8", errors="ignore")
        doc_type = utils.classify(f, config)
        tokens   = mdp.parse(text)
        lineage  = splitter.extract_lineage(tokens)
        size     = config["chunk_rules"].get(doc_type, config["chunk_rules"]["unknown"])
        overlap  = int(size * config["overlap_pc"])
        chunks   = splitter.split_chunks(text, lineage, size, overlap)

        for idx, chunk in enumerate(chunks):
            cid    = f"{f.stem}_{idx:02d}"
            preview = chunk[:60].replace("\n", " ")
            metadata.append({
                "chunk_id": cid,
                "type":     doc_type,
                "path":     str(f.relative_to(docs_dir)),
                "heading":  lineage,
                "preview":  preview,
            })

    manifest.write_manifest(metadata, out_dir)

    # 4. Assert: check that the manifest has both intro and setup entries
    md = (out_dir / "chunks_manifest.md").read_text()
    # intro should produce at least two chunks (title+body), type=howto
    assert "| intro_00 | howto | intro.md | Intro |" in md
    # setup produces at least one chunk, type=reference
    assert "| setup_00 | reference | setup.md | Setup |" in md

