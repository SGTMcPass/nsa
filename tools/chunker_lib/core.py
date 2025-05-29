"""
chunker_lib.core
Bulletproof document chunking pipeline for NASA Simulation Agents.
Adds robust logging, warnings, and soft failure modes.
"""

import os
import json
import yaml
import warnings
from pathlib import Path
from typing import List, Dict, Any, Optional

from chunker_lib.splitter import split_markdown, ChunkerSplitterError


class ChunkerCoreError(Exception):
    """Raised for errors in chunking pipeline."""


def chunk_documents(
    config_path: str,
    output_dir: str,
    mode: str = "word",
    overwrite: bool = True,
) -> List[Dict[str, Any]]:
    """
    Orchestrate full doc chunking pipeline from config.
    Logs actions, warnings, and errors.
    Returns manifest (list of chunks).
    """
    print(f"[core] Loading config from: {config_path}")
    try:
        config = _load_config(config_path)
    except Exception as e:
        print(f"[core] ERROR: Failed to load config: {e}")
        raise ChunkerCoreError(f"Config load failed: {e}")

    files = list(_crawl_files(config))
    print(f"[core] Found {len(files)} files under docs_root.")

    manifest = []
    skipped_files = []
    chunked_files = 0

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for filepath in files:
        if not str(filepath).endswith(".md"):
            msg = f"[core] Skipping non-markdown file: {filepath}"
            print(msg)
            warnings.warn(msg, stacklevel=2)
            skipped_files.append(str(filepath))
            continue
        try:
            category = _classify_path(filepath, config)
            text = _read_file(filepath)
            if not text.strip():
                msg = f"[core] WARNING: Empty markdown file skipped: {filepath}"
                print(msg)
                warnings.warn(msg, stacklevel=2)
                skipped_files.append(str(filepath))
                continue
            chunks = split_markdown(
                text,
                mode=mode,
                category=category,
                chunk_rules=config.get("chunk_rules", {}),
                overlap_pc=config.get("overlap_pc", 0.0),
            )
            if not chunks:
                msg = f"[core] WARNING: No chunks produced for file: {filepath}"
                print(msg)
                warnings.warn(msg, stacklevel=2)
                skipped_files.append(str(filepath))
                continue
            for chunk in chunks:
                chunk.update(
                    {
                        "source_file": str(filepath),
                        "category": category,
                    }
                )
            manifest.extend(chunks)
            chunked_files += 1
            print(
                f"[core] Chunked {filepath} ({len(chunks)} chunks, category: {category})"
            )
        except ChunkerSplitterError as e:
            msg = f"[core] SplitterError on {filepath}: {e}"
            print(msg)
            warnings.warn(msg, stacklevel=2)
            skipped_files.append(str(filepath))
        except Exception as e:
            msg = f"[core] ERROR: Failed to process {filepath}: {e}"
            print(msg)
            warnings.warn(msg, stacklevel=2)
            skipped_files.append(str(filepath))

    manifest_path = output_dir / "chunks.jsonl"
    if manifest and (overwrite or not manifest_path.exists()):
        try:
            _save_jsonl(manifest, manifest_path)
            print(f"[core] Manifest written: {manifest_path} ({len(manifest)} chunks)")
        except Exception as e:
            print(f"[core] ERROR: Failed to write manifest: {e}")
            warnings.warn(f"Failed to write manifest: {e}", stacklevel=2)
    else:
        print("[core] No chunks to write, or file exists and overwrite=False.")

    print(
        f"[core] Summary: {chunked_files} files chunked, {len(skipped_files)} files skipped."
    )
    if skipped_files:
        print(f"[core] Skipped files: {skipped_files}")

    return manifest


def _load_config(config_path: str) -> dict:
    """Load chunker YAML config (with env expansion)."""
    path = Path(os.path.expandvars(config_path))
    if not path.exists():
        msg = f"Config file does not exist: {config_path}"
        warnings.warn(msg, stacklevel=2)
        raise ChunkerCoreError(msg)
    with open(path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    # Expand env vars in config values (for docs_root, etc)
    for k, v in config.items():
        if isinstance(v, str):
            config[k] = os.path.expandvars(v)
    if "docs_root" not in config or not config["docs_root"]:
        msg = "[core] Config missing docs_root."
        print(msg)
        warnings.warn(msg, stacklevel=2)
        raise ChunkerCoreError(msg)
    return config


def _crawl_files(config: dict) -> List[Path]:
    """Recursively yield all files under docs_root. Logs missing root."""
    docs_root = Path(config.get("docs_root", "."))
    if not docs_root.exists():
        msg = f"[core] docs_root path does not exist: {docs_root}"
        print(msg)
        warnings.warn(msg, stacklevel=2)
        raise ChunkerCoreError(msg)
    for root, _, files in os.walk(docs_root):
        for file in files:
            yield Path(root) / file


def _classify_path(filepath: Path, config: dict) -> str:
    """
    Map file path to category using dir_map (longest prefix first).
    Returns category string.
    """
    dir_map = config.get("dir_map", {})
    rel_path = str(filepath.relative_to(config["docs_root"])).replace("\\", "/")
    best_match = ""
    best_cat = "unknown"
    for prefix, cat in dir_map.items():
        if rel_path.startswith(prefix) and len(prefix) > len(best_match):
            best_match = prefix
            best_cat = cat
    if best_cat == "unknown":
        warnings.warn(f"[core] Could not classify file: {filepath}", stacklevel=2)
    return best_cat


def _read_file(filepath: Path) -> str:
    """Read file as UTF-8 text, logs and warns if file can't be read."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        msg = f"[core] ERROR: Failed to read {filepath}: {e}"
        print(msg)
        warnings.warn(msg, stacklevel=2)
        return ""


def _save_jsonl(data: List[dict], outpath: Path):
    """Write list of dicts to JSONL, logs on error."""
    try:
        with open(outpath, "w", encoding="utf-8") as f:
            for item in data:
                f.write(json.dumps(item, ensure_ascii=False) + "\n")
    except Exception as e:
        msg = f"[core] ERROR: Could not write JSONL to {outpath}: {e}"
        print(msg)
        warnings.warn(msg, stacklevel=2)
