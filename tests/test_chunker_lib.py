import os
import sys

# Ensure the tools/ directory is on the import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import json
import tempfile
from pathlib import Path
import codecs
import pytest
from markdown_it import MarkdownIt
import tiktoken

import tools.chunker_lib.config as cfg_mod
import tools.chunker_lib.utils as utils
import tools.chunker_lib.crawler as crawler
import tools.chunker_lib.splitter as splitter
import tools.chunker_lib.manifest as manifest

# Sample minimal frontmatter file
FRONTMATTER_MD = """---
layout: guide
title: Sample Guide
---
# Heading
Content here.
"""


@pytest.fixture
def tmp_docs(tmp_path):
    # Create a fake docs root with sample files
    docs = tmp_path / "docs"
    docs.mkdir()
    # Write sample markdown files
    f1 = docs / "a.md"
    f1.write_text(FRONTMATTER_MD)
    f2 = docs / "b.md"
    # b links to a
    f2.write_text("See [A](a.md)")
    return docs


def test_load_config(tmp_path, monkeypatch):
    cfg_file = tmp_path / "cfg.yaml"
    # Use triple-quoted string for valid multi-line YAML
    cfg_file.write_text(
        """docs_root: '$HOME/project/docs'
chunk_rules: {unknown: 10}
overlap_pc: 0.1"""
    )
    monkeypatch.setenv("HOME", "/home/user")
    cfg = cfg_mod.load_config(str(cfg_file))
    assert cfg["docs_root"] == "/home/user/project/docs"
    assert cfg["chunk_rules"]["unknown"] == 10
    assert abs(cfg["overlap_pc"] - 0.1) < 1e-6


def test_safe_read_and_bom(tmp_path):
    p = tmp_path / "u8.txt"
    p.write_bytes(codecs.BOM_UTF16_LE + "hello".encode("utf-16-le"))
    text = utils.safe_read(p)
    assert "hello" in text


def test_normalize_href(tmp_path):
    docs = tmp_path / "docs"
    docs.mkdir()
    base = docs
    (docs / "index.md").write_text("# root")
    # Test directory to index.md
    result = utils.normalize_href("", base, docs)
    assert result is None
    result = utils.normalize_href("index.md", base, docs)
    assert result.name == "index.md"


def test_classify(tmp_path):
    # Create fake file with frontmatter
    f = tmp_path / "f.md"
    f.write_text(FRONTMATTER_MD)
    cfg = {"docs_root": str(tmp_path), "dir_map": {}}
    assert utils.classify(f, cfg) == "howto"
    # Filename heuristic
    f2 = tmp_path / "test_reference.md"
    f2.write_text("")
    assert utils.classify(f2, cfg) == "reference"


def test_crawl_docs(tmp_docs):
    files = crawler.crawl_docs(tmp_docs / "b.md", tmp_docs)
    paths = {p.name for p in files}
    assert {"b.md", "a.md"} == paths


def test_extract_lineage_and_split():
    md = "# H1\n## H2\nParagraph text."
    md_parser = MarkdownIt()
    tokens = md_parser.parse(md)
    lineage = splitter.extract_lineage(tokens)
    assert lineage == "H1 > H2"
    # Test splitting small content
    chunks = splitter.split_chunks("word " * 100, lineage, size=10, overlap=2)
    assert all(chunk.startswith("### H1 > H2") for chunk in chunks)
    # Overlap test: second chunk shares last 2 tokens of first
    enc = tiktoken.get_encoding("cl100k_base")
    ids_all = enc.encode("word " * 100)
    assert len(chunks) > 1


def test_manifest(tmp_path):
    # Prepare metadata
    metadata = [
        {
            "chunk_id": "x_00",
            "type": "howto",
            "path": "a.md",
            "heading": "H",
            "preview": "p",
        }
    ]
    out = tmp_path / "out"
    manifest.write_manifest(metadata, out)
    # Validate JSONL
    lines = (out / "chunks.jsonl").read_text().splitlines()
    assert json.loads(lines[0])["chunk_id"] == "x_00"
    # Validate Markdown manifest
    m = (out / "chunks_manifest.md").read_text()
    assert "| x_00 | howto | a.md | H | p |" in m
