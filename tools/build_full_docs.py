#!/usr/bin/env python3
"""
build_full_docs.py – Merge every Trick Markdown page into **one** master file
==========================================================================
• Recursively crawls the Trick docs tree starting at docs/index.md (same logic
  as build_trick_chunks.py)
• Preserves each original file verbatim so humans can read it exactly as on the
  website (including code‑blocks, tables, images references)
• Adds lightweight **file markers** that make it trivial for an LLM retriever to
  split or filter later:
    >>> ## FILE: docs/tutorial/Tutorial.md
    >>> ## BEGIN
    …original markdown…
    >>> ## END
• Generates a hyper‑linked **Table‑of‑Contents** at the top so humans can skim.
• Safe‑decodes UTF‑8/16‑LE/16‑BE/Latin‑1, skips binary links, follows the same
  link–resolution rules we already debugged.

Run:
    export TRICK_HOME=~/repos/trick
    python tools/build_full_docs.py

Output:
    docs_full.md   (single ~3 MB file)
"""
from __future__ import annotations
import codecs, os, re, sys, pathlib, time, textwrap
from collections import deque
from typing import List

import frontmatter
from markdown_it import MarkdownIt

TRICK = pathlib.Path(os.environ["TRICK_HOME"]).expanduser().resolve()
SEED  = TRICK / "docs/index.md"
OUT   = pathlib.Path("docs_full.md")

IMAGE_EXT = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp", ".ico", ".pdf"}
md = MarkdownIt()

# ───────────────────────────────────────────────────────── safe read

def safe_read(p: pathlib.Path) -> str:
    try:
        return p.read_text("utf-8")
    except UnicodeDecodeError:
        raw = p.read_bytes()
        if raw.startswith(codecs.BOM_UTF16_LE):
            return raw.decode("utf-16-le", errors="replace")
        if raw.startswith(codecs.BOM_UTF16_BE):
            return raw.decode("utf-16-be", errors="replace")
        return raw.decode("latin-1", errors="replace")

# ───────────────────────────────────────────────────────── crawl
MD_LINK = re.compile(r"\]\(([^)#]+)\)")
HREF_RE = re.compile(r'href="([^"]+)"', re.I)

def _norm(href: str, base: pathlib.Path) -> pathlib.Path | None:
    if re.match(r"^[a-zA-Z][\w+.-]*://", href) or href.startswith("mailto:"):
        return None
    href = href.split("#", 1)[0].split("?", 1)[0].replace("\x00", "").strip()
    if not href or pathlib.Path(href).suffix.lower() in IMAGE_EXT:
        return None

    t = (base / href).resolve()
    if t.is_dir():
        t = t / "index.md"
    elif t.suffix == "":
        t = t.with_suffix(".md")
    docs_root = TRICK / "docs"
    return t if t.exists() and docs_root in t.parents else None

def crawl(seed: pathlib.Path) -> List[pathlib.Path]:
    dq, seen, order = deque([seed.resolve()]), set(), []
    while dq:
        cur = dq.popleft()
        if cur in seen or not cur.exists():
            continue
        seen.add(cur); order.append(cur)
        txt = safe_read(cur); base = cur.parent
        for tok in md.parse(txt):
            if tok.type == "image":
                continue
            if tok.type == "inline":
                for m in MD_LINK.finditer(tok.content):
                    d = _norm(m.group(1), base)
                    if d: dq.append(d)
            if tok.type.startswith("html_"):
                for m in HREF_RE.finditer(tok.content):
                    d = _norm(m.group(1), base)
                    if d: dq.append(d)
    return order

# ───────────────────────────────────────────────────────── main

def main():
    t0=time.time()
    files = crawl(SEED)
    print(f"Found {len(files)} markdown files, merging → {OUT} …")

    # Build a TOC first so humans can click around.
    toc_lines = ["# Trick Documentation — Single File Edition", "", "## Table of Contents", ""]

    for p in files:
        rel = p.relative_to(TRICK)
        anchor = str(rel).replace("/", "-").replace(".md", "")
        toc_lines.append(f"* [{rel}](#{anchor})")
    toc = "\n".join(toc_lines) + "\n\n---\n\n"

    with OUT.open("w", encoding="utf-8") as f:
        f.write(toc)
        for p in files:
            rel = p.relative_to(TRICK)
            anchor = str(rel).replace("/", "-").replace(".md", "")
            f.write(f"## FILE: {rel}\n")
            f.write(f"<a name=\"{anchor}\"></a>\n\n")
            f.write("<!-- BEGIN -->\n\n")
            f.write(safe_read(p))
            f.write("\n\n<!-- END -->\n\n\n")
    print(f"✓ {OUT} written in {time.time()-t0:.1f}s  (size {OUT.stat().st_size/1024:.0f} KB)")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("Interrupted")

