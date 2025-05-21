# tools/chunker_lib/crawler.py
from pathlib import Path
from typing import List
from markdown_it import MarkdownIt
import re
from .utils import safe_read, normalize_href


def crawl_docs(seed: Path, docs_root: Path) -> List[Path]:
    """
    Depth-first crawl starting at `seed`, following Markdown and HTML links within `docs_root`.
    Returns a list of resolved Markdown file Paths.
    """
    parser = MarkdownIt()
    stack: List[Path] = [seed.resolve()]
    seen: set[Path] = set()
    result: List[Path] = []

    # Regex for Markdown links: [text](url)
    md_link_re = re.compile(r"\]\(([^)#]+)\)")
    # Regex for HTML href attributes: href="url"
    html_href_re = re.compile(r'href=["\']([^"\']+)["\']', re.IGNORECASE)

    while stack:
        cur = stack.pop()
        if cur in seen or not cur.exists():
            continue
        seen.add(cur)
        result.append(cur)

        text = safe_read(cur)
        base = cur.parent
        tokens = parser.parse(text)

        for tok in tokens:
            # 1) Markdown-style links
            if tok.type == 'inline':
                for m in md_link_re.finditer(tok.content):
                    href = m.group(1)
                    dst = normalize_href(href, base, docs_root)
                    if dst and dst not in seen:
                        stack.append(dst)

            # 2) HTML <a href="..."> links within raw HTML tokens
            if tok.type.startswith('html_') or tok.type == 'html_inline':
                for m in html_href_re.finditer(tok.content):
                    href = m.group(1)
                    dst = normalize_href(href, base, docs_root)
                    if dst and dst not in seen:
                        stack.append(dst)

    return result

