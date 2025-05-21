# splitter.py
from typing import List
import tiktoken


def extract_lineage(tokens) -> str:
    """
    Build a heading lineage (top 3 levels) from Markdown-It tokens.
    """
    stack: List[str] = []
    lineage: List[str] = []
    for i, tok in enumerate(tokens):
        if tok.type == 'heading_open':
            lvl = int(tok.tag[1])
            title = tokens[i + 1].content
            stack = stack[:lvl-1] + [title]
            lineage = stack[:3]
    return ' > '.join(lineage) if lineage else 'Root'


def split_chunks(content: str, lineage: str, size: int, overlap: int) -> List[str]:
    """
    Tokenize `content` and split into windows of `size` with `overlap`.
    Prefix each chunk with '### {lineage}'.
    """
    encoder = tiktoken.get_encoding('cl100k_base')
    ids = encoder.encode(content)
    chunks: List[str] = []
    start = 0
    while start < len(ids):
        end = min(start + size, len(ids))
        text = encoder.decode(ids[start:end])
        chunks.append(f"### {lineage}\n\n{text}")
        if end == len(ids):
            break
        start = end - overlap
    return chunks
