# utils.py
from pathlib import Path
import codecs
import re
import os
from typing import Dict
from frontmatter import load as load_frontmatter


def safe_read(path: Path) -> str:
    """
    Read a file at `path` into a string, handling UTF-8/16 BOMs and fallback encodings.
    """
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        raw = path.read_bytes()
        if raw.startswith(codecs.BOM_UTF16_LE):
            return raw.decode("utf-16-le", errors="replace")
        if raw.startswith(codecs.BOM_UTF16_BE):
            return raw.decode("utf-16-be", errors="replace")
        return raw.decode("latin-1", errors="replace")


def normalize_href(href: str, base: Path, docs_root: Path) -> Path | None:
    """
    Normalize a Markdown or HTML link `href` to a local markdown file under `docs_root`.
    Returns a Path if valid, otherwise None.
    """
    # Skip external URLs and mailto links
    if re.match(r"^[a-zA-Z]+://", href) or href.startswith("mailto:"):
        return None

    # Strip anchors and query params
    clean = href.split("#", 1)[0].split("?", 1)[0].strip()
    if not clean:
        return None

    # Reject suspicious or non-path links
    if not re.match(r"^[\w\-\./]+$", clean):
        return None

    # Skip common non-markdown file extensions
    if Path(clean).suffix.lower() in {
        ".png",
        ".jpg",
        ".jpeg",
        ".gif",
        ".svg",
        ".webp",
        ".bmp",
        ".ico",
        ".pdf",
    }:
        return None

    # Now resolve and check under docs_root
    target = (base / clean).resolve()
    if target.is_dir():
        target = target / "index.md"
    if target.suffix == "":
        target = target.with_suffix(".md")

    try:
        if target.is_file() and target.resolve().is_relative_to(
            Path(docs_root).resolve()
        ):
            return target
    except AttributeError:
        if Path(docs_root).resolve() in target.parents:
            return target

    return None


def classify(path: Path, cfg: Dict) -> str:
    """
    Determine the document type for `path` based on:
      1. Front-matter 'layout' or 'type'
      2. Longest-prefix match in cfg['dir_map']
      3. Filename regex patterns
      4. Default to 'unknown'
    """
    # 1. Front-matter
    try:
        post = load_frontmatter(path)
        layout = (post.get("layout") or post.get("type") or "").lower()
        if layout in {"howto", "guide"}:
            return "howto"
        if layout == "reference":
            return "reference"
        if layout == "faq":
            return "troubleshoot"
    except Exception:
        pass
    # 2. Directory mapping
    rel = str(path.relative_to(cfg["docs_root"])).replace("\\", "/").lower()
    for prefix, kind in cfg.get("dir_map", {}).items():
        if rel.startswith(prefix.lower()):
            return kind
    # 3. Filename-based heuristics
    name = path.name.lower()
    if any(tok in name for tok in ("howto", "tutorial", "guide")):
        return "howto"
    if any(
        tok in name for tok in ("overview", "introduction", "architecture", "concept")
    ):
        return "concept"
    if any(tok in name for tok in ("api", "reference", "class_", "web")):
        return "reference"
    if any(tok in name for tok in ("faq", "trouble", "checkpoint")):
        return "troubleshoot"
    # 4. Default
    return "unknown"
