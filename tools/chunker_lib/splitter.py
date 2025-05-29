"""
chunker_lib.splitter
Modular, mode-driven markdown chunking utilities.
Supports: word, paragraph, heading (with recursive fallback).
"""

import re
import warnings
from typing import List, Dict, Any, Optional


class ChunkerSplitterError(Exception):
    """Raised for invalid input or unsupported mode."""


def split_markdown(
    text: str,
    mode: str = "word",
    category: Optional[str] = None,
    chunk_rules: Optional[Dict[str, int]] = None,
    overlap_pc: float = 0.0,
) -> List[Dict[str, Any]]:
    """
    Split markdown text using the specified mode.
    mode: "word" | "paragraph" | "heading"
    """
    if not isinstance(text, str):
        warnings.warn(
            f"[chunker_lib.splitter] 'text' is type {type(text)}, expected str.",
            stacklevel=2,
        )
        raise ChunkerSplitterError(f"Input must be a string, got {type(text)}.")

    if mode == "word":
        return _split_by_word(text, category, chunk_rules, overlap_pc)
    elif mode == "paragraph":
        return _split_by_paragraph(text, category, chunk_rules)
    elif mode == "heading":
        return _split_by_heading(text, category, chunk_rules, overlap_pc)
    else:
        raise ChunkerSplitterError(
            f"Unsupported mode '{mode}'. Use 'word', 'paragraph', or 'heading'."
        )


def _get_chunk_size(category, chunk_rules):
    if chunk_rules and category:
        if category in chunk_rules:
            return chunk_rules[category]
        else:
            warnings.warn(
                f"No chunk rule for category '{category}'. Using default.", stacklevel=2
            )
    return 500  # Default chunk size


def _split_by_word(text, category, chunk_rules, overlap_pc):
    chunk_size = _get_chunk_size(category, chunk_rules)
    overlap_tokens = int(chunk_size * overlap_pc) if chunk_size > 0 else 0

    words = text.split()
    if not words:
        return []
    chunks = []
    i = 0
    while i < len(words):
        start = max(i - overlap_tokens, 0)
        end = min(i + chunk_size, len(words))
        chunk_words = words[start:end]
        chunk_text = " ".join(chunk_words).strip()
        if not chunk_text:
            break
        chunk = {
            "id": len(chunks),
            "content": chunk_text,
            "start_word": start,
            "end_word": end,
            "category": category or "unknown",
            "chunk_size": len(chunk_words),
            "token_estimate": len(chunk_words),
            "mode": "word",
        }
        chunks.append(chunk)
        i += chunk_size - overlap_tokens if chunk_size > overlap_tokens else 1
    return chunks


def _split_by_paragraph(text, category, chunk_rules):
    chunk_size = _get_chunk_size(category, chunk_rules)
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    temp_chunk = []
    temp_tokens = 0
    chunks = []
    for p in paragraphs:
        tokens = len(p.split())
        if temp_tokens + tokens > chunk_size and temp_chunk:
            chunk_text = "\n\n".join(temp_chunk)
            chunks.append(
                {
                    "id": len(chunks),
                    "content": chunk_text,
                    "category": category or "unknown",
                    "chunk_size": temp_tokens,
                    "token_estimate": temp_tokens,
                    "mode": "paragraph",
                }
            )
            temp_chunk = []
            temp_tokens = 0
        temp_chunk.append(p)
        temp_tokens += tokens
    # Add the last chunk
    if temp_chunk:
        chunk_text = "\n\n".join(temp_chunk)
        chunks.append(
            {
                "id": len(chunks),
                "content": chunk_text,
                "category": category or "unknown",
                "chunk_size": temp_tokens,
                "token_estimate": temp_tokens,
                "mode": "paragraph",
            }
        )
    return chunks


def _split_by_heading(text, category, chunk_rules, overlap_pc):
    chunk_size = _get_chunk_size(category, chunk_rules)
    # Split at markdown headings (# ... or ## ...)
    sections = re.split(r"(?m)^#{1,6}\s+", text)
    if sections[0].strip() == "":
        sections = sections[1:]  # Remove empty section if text starts with heading
    chunks = []
    for i, section in enumerate(sections):
        section = section.strip()
        if not section:
            continue
        tokens = len(section.split())
        # If section is too big, split further by word
        if tokens > chunk_size:
            subchunks = _split_by_word(section, category, chunk_rules, overlap_pc)
            for c in subchunks:
                c["mode"] = "heading+word"
                chunks.append(c)
        else:
            chunks.append(
                {
                    "id": len(chunks),
                    "content": section,
                    "category": category or "unknown",
                    "chunk_size": tokens,
                    "token_estimate": tokens,
                    "mode": "heading",
                }
            )
    return chunks
