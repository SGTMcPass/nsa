"""
chunker_lib.utils
Reusable utility functions for chunking workflows.
Warns on argument type mismatch. Robust, reusable, error-safe.
"""

import os
import re
import json
import warnings
from pathlib import Path
from typing import List, Any, Optional, Union


class ChunkerUtilsError(Exception):
    """Custom exception for all chunker utility errors."""


def read_file(path: Union[str, Path]) -> str:
    """
    Read text from a file at `path`.
    Warns if the path is not a str or Path.
    """
    if not isinstance(path, (str, Path)):
        warnings.warn(
            f"[chunker_lib.utils] 'path' is type {type(path)}, expected str or Path.",
            stacklevel=2,
        )
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        raise ChunkerUtilsError(f"Failed to read file {path}: {e}")


def write_file(path: Union[str, Path], data: str) -> None:
    """
    Write text to a file at `path`.
    Warns if the path is not a str or Path.
    """
    if not isinstance(path, (str, Path)):
        warnings.warn(
            f"[chunker_lib.utils] 'path' is type {type(path)}, expected str or Path.",
            stacklevel=2,
        )
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(data)
    except Exception as e:
        raise ChunkerUtilsError(f"Failed to write file {path}: {e}")


def find_markdown_files(root: Union[str, Path]) -> List[str]:
    """
    Recursively find all `.md` files under a directory.
    Warns if the root is not a str or Path.
    """
    if not isinstance(root, (str, Path)):
        warnings.warn(
            f"[chunker_lib.utils] 'root' is type {type(root)}, expected str or Path.",
            stacklevel=2,
        )
    md_files = []
    for dirpath, _, filenames in os.walk(root):
        for fname in filenames:
            if fname.endswith(".md"):
                md_files.append(os.path.join(dirpath, fname))
    return md_files


def load_json(path: Union[str, Path]) -> Any:
    """
    Load JSON from a file at `path`.
    Warns if the path is not a str or Path.
    """
    if not isinstance(path, (str, Path)):
        warnings.warn(
            f"[chunker_lib.utils] 'path' is type {type(path)}, expected str or Path.",
            stacklevel=2,
        )
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        raise ChunkerUtilsError(f"Failed to load JSON file {path}: {e}")


def save_json(path: Union[str, Path], obj: Any) -> None:
    """
    Save JSON to a file at `path`.
    Warns if the path is not a str or Path.
    """
    if not isinstance(path, (str, Path)):
        warnings.warn(
            f"[chunker_lib.utils] 'path' is type {type(path)}, expected str or Path.",
            stacklevel=2,
        )
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(obj, f, indent=2)
    except Exception as e:
        raise ChunkerUtilsError(f"Failed to save JSON file {path}: {e}")
