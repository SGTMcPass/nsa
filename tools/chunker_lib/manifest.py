"""
chunker_lib.manifest
Chunk manifest I/O utilities (JSONL format).
Warns on type mismatch, robust error handling.
"""

import json
import warnings
from pathlib import Path
from typing import List, Dict, Any, Union


class ChunkerManifestError(Exception):
    """Custom exception for manifest load/save errors."""


def load_manifest(path: Union[str, Path]) -> List[Dict[str, Any]]:
    """
    Load a chunk manifest (JSONL, one dict per line) from `path`.
    Warns if path is not str or Path.
    Returns a list of dictionaries.
    Raises ChunkerManifestError on error.
    """
    if not isinstance(path, (str, Path)):
        warnings.warn(
            f"[chunker_lib.manifest] 'path' is type {type(path)}, expected str or Path.",
            stacklevel=2,
        )
    try:
        with open(path, "r", encoding="utf-8") as f:
            result = []
            for i, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    result.append(json.loads(line))
                except Exception as e:
                    raise ChunkerManifestError(f"Error parsing line {i} in {path}: {e}")
            return result
    except Exception as e:
        raise ChunkerManifestError(f"Failed to load manifest from {path}: {e}")


def save_manifest(path: Union[str, Path], manifest: List[Dict[str, Any]]) -> None:
    """
    Save a chunk manifest (JSONL, one dict per line) to `path`.
    Warns if path is not str or Path, or manifest is not a list.
    Raises ChunkerManifestError on error.
    """
    if not isinstance(path, (str, Path)):
        warnings.warn(
            f"[chunker_lib.manifest] 'path' is type {type(path)}, expected str or Path.",
            stacklevel=2,
        )
    if not isinstance(manifest, list):
        warnings.warn(
            f"[chunker_lib.manifest] 'manifest' is type {type(manifest)}, expected list of dicts.",
            stacklevel=2,
        )
        raise ChunkerManifestError(
            f"Manifest argument must be a list of dicts, got {type(manifest)}."
        )
    try:
        with open(path, "w", encoding="utf-8") as f:
            for i, item in enumerate(manifest, 1):
                if not isinstance(item, dict):
                    raise ChunkerManifestError(
                        f"Manifest item at index {i-1} is not a dict (type={type(item)})."
                    )
                f.write(json.dumps(item) + "\n")
    except Exception as e:
        raise ChunkerManifestError(f"Failed to save manifest to {path}: {e}")
