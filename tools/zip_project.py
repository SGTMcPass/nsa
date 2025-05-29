#!/usr/bin/env python3
"""
zip_project_fixed.py
------------------------------------
Archive your project with flexible inclusion/exclusion, and [bash]$ tree preview.

Supports a YAML-based ignore config:
- Use --ignore_file <path> to specify.
- Or just put .zipignore.yaml or .zipignore at your project root.

YAML format:
  exclude:
    - "*.pyc"
    - "__pycache__"
    - ".git"
    - ".private"
    - "artifacts"
    - ".venv"
    - "node_modules"
    - "*.log"
    - "*.swp"
  include:
    # Optional: specify dirs/files/globs to always include

Usage Examples:
  python zip_project_fixed.py --src_dir . --out_dir .private --preview
  python zip_project_fixed.py --src_dir . --out_dir .private --ignore_file zipignore.yaml
  python zip_project_fixed.py --src_dir . --out_dir .private --include tools,tests --exclude *.pyc,__pycache__
"""

import os
import argparse
import zipfile
import fnmatch
from datetime import datetime
from pathlib import Path
import yaml


def parse_args():
    parser = argparse.ArgumentParser(
        description="Zip your project with flexible ignore rules and tree preview.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "--src_dir", type=str, required=True, help="Project root directory to archive"
    )
    parser.add_argument(
        "--out_dir",
        type=str,
        default="artifacts",
        help="Output dir for zips (should be .gitignored)",
    )
    parser.add_argument(
        "--include",
        type=str,
        default="",
        help="Comma-separated list of globs/dirs/files to always include",
    )
    parser.add_argument(
        "--exclude",
        type=str,
        default="*.pyc,__pycache__,.git,.private,artifacts,.venv,node_modules",
        help="Comma-separated list of globs/dirs/files to exclude",
    )
    parser.add_argument(
        "--ignore_file",
        type=str,
        default="",
        help="YAML file with include/exclude patterns",
    )
    parser.add_argument(
        "--preview",
        action="store_true",
        help="Show a [bash]$ tree preview of what will be zipped and exit",
    )

    parser.add_argument(
        "--checkpoint",
        action="store_true",
        help="Also save a versioned archive in a .history directory",
    )
    parser.add_argument(
        "--checkpoint_keep",
        type=int,
        default=None,
        help="If set, keep only the N most recent checkpoints",
    )
    parser.add_argument(
        "--checkpoint_dir",
        type=str,
        default=".history",
        help="Subdirectory for versioned archives inside out_dir",
    )

    parser.add_argument(
        "--include_only",
        type=str,
        default="",
        help="Comma-separated list of paths to include (relative to src_dir)",
    )
    parser.add_argument(
        "--load_context_yaml",
        type=str,
        default="",
        help="YAML file specifying include_only list (under key: include_only)",
    )

    return parser.parse_args()


def load_ignore_patterns(ignore_file_path):
    try:
        with open(ignore_file_path, "r") as f:
            patterns = yaml.safe_load(f)
            include = patterns.get("include", []) or []
            exclude = patterns.get("exclude", []) or []
            print(f"[zipper] Using ignore file: {ignore_file_path}")
            return include, exclude
    except Exception as e:
        raise RuntimeError(
            f"[zipper] Failed to load ignore file {ignore_file_path}: {e}"
        )


def normalize_path(path):
    return str(path).replace(os.sep, "/")


def should_include(rel_path, include_patterns, exclude_patterns):
    path_str = normalize_path(rel_path)
    if any(fnmatch.fnmatch(path_str, pat) for pat in exclude_patterns):
        if not any(fnmatch.fnmatch(path_str, pat) for pat in include_patterns):
            return False
    return True


def gather_files(src_dir, include_patterns, exclude_patterns):
    is_git_style = isinstance(exclude_patterns, list) and all(
        isinstance(p, tuple) for p in exclude_patterns
    )

    src_dir = Path(src_dir).resolve()
    file_list = []
    for root, dirs, files in os.walk(src_dir, followlinks=False):
        rel_root = Path(root).relative_to(src_dir)
        # Filter dirs in-place
        dirs[:] = [
            d
            for d in dirs
            if should_include(rel_root / d, include_patterns, exclude_patterns)
        ]
        for file in files:
            rel_file = rel_root / file
            if (
                should_include_git(rel_file, exclude_patterns)
                if is_git_style
                else should_include(rel_file, include_patterns, exclude_patterns)
            ):
                file_list.append(rel_file)
    return file_list


def print_tree(file_list):
    import collections

    Tree = lambda: collections.defaultdict(Tree)
    tree = Tree()
    for rel_file in file_list:
        parts = rel_file.parts
        node = tree
        for part in parts:
            node = node[part]

    def _print(node, prefix=""):
        entries = sorted(node.items())
        for idx, (name, subtree) in enumerate(entries):
            connector = "└── " if idx == len(entries) - 1 else "├── "
            print(prefix + connector + name)
            if subtree:
                ext = "    " if idx == len(entries) - 1 else "│   "
                _print(subtree, prefix + ext)

    print("[bash]$ tree")
    _print(tree)


def load_gitignore_patterns(gitignore_path):
    try:
        with open(gitignore_path, "r") as f:
            lines = f.readlines()
        exclude = []
        for line in lines:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.endswith("/"):
                line = line.rstrip("/")
            exclude.append(line)
        return [], exclude
    except Exception as e:
        print(f"[zipper] Warning: Failed to read .gitignore: {e}")
        return [], []


import re


def parse_gitignore(gitignore_path, root_dir):
    """Parse .gitignore and return ordered (pattern, include/exclude) list."""
    patterns = []
    try:
        with open(gitignore_path, "r") as f:
            for line in f:
                line = line.rstrip("\n")
                if not line or line.startswith("#"):
                    continue
                include = True
                if line.startswith("!"):
                    line = line[1:]
                    include = False
                anchored = line.startswith("/")
                if anchored:
                    line = line[1:]
                is_dir = line.endswith("/")
                if is_dir:
                    line = line.rstrip("/")

                glob_pattern = line
                if anchored:
                    glob_pattern = str(Path(root_dir) / glob_pattern)
                else:
                    glob_pattern = "**/" + glob_pattern

                patterns.append((glob_pattern, include, is_dir))
    except Exception as e:
        print(f"[zipper] Warning: Failed to parse .gitignore: {e}")
    return patterns


def should_include_git(rel_path, pattern_rules):
    path_str = normalize_path(rel_path)
    result = True
    for pat, include, is_dir in pattern_rules:
        if fnmatch.fnmatch(path_str, pat):
            if is_dir and not str(rel_path).endswith("/"):
                continue
            result = include
    return result


def find_default_ignore_file(src_dir):
    for fname in [".zipignore.yaml", ".zipignore", ".gitignore"]:
        candidate = Path(src_dir) / fname
        if candidate.exists():
            return str(candidate)
    return None

    for fname in [".zipignore.yaml", ".zipignore"]:
        candidate = Path(src_dir) / fname
        if candidate.exists():
            return str(candidate)
    return None


def zip_project(
    src_dir,
    out_dir,
    include="",
    exclude="",
    preview=False,
    ignore_file=None,
    checkpoint=False,
    checkpoint_keep=None,
    checkpoint_dir=".history",
    include_only="",
    load_context_yaml="",
):
    src_dir = Path(src_dir).resolve()
    out_dir = Path(out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_name = f"{src_dir.name}_{timestamp}.zip"
    zip_path = out_dir / zip_name

    # Load includes from context YAML if specified
    if load_context_yaml:
        try:
            with open(load_context_yaml, "r") as f:
                context_data = yaml.safe_load(f)
                context_includes = context_data.get("include_only", [])
                if isinstance(context_includes, list):
                    include_only = context_includes
                else:
                    include_only = []
        except Exception as e:
            print(
                f"[zipper] Warning: Failed to load context YAML {load_context_yaml}: {e}"
            )
            include_only = []
    else:
        include_only = [i.strip() for i in include_only.split(",") if i.strip()]

    # Load patterns
    if ignore_file:
        include_patterns, exclude_patterns = load_ignore_patterns(ignore_file)
    else:
        default_ignore = find_default_ignore_file(src_dir)
        if default_ignore:
            include_patterns, exclude_patterns = (
                load_ignore_patterns(default_ignore)
                if default_ignore.endswith(".yaml")
                or default_ignore.endswith(".zipignore")
                else ([], parse_gitignore(default_ignore, src_dir))
            )
        else:
            include_patterns = [i.strip() for i in include.split(",") if i.strip()]
            exclude_patterns = [
                normalize_pattern(e.strip()) for e in exclude.split(",") if e.strip()
            ]

    if include_only:
        # Only gather files under explicitly included paths
        filtered_list = []
        for path in include_only:
            abs_path = (src_dir / path).resolve()
            if abs_path.is_file():
                filtered_list.append(Path(path))
            elif abs_path.is_dir():
                for root, _, files in os.walk(abs_path, followlinks=False):
                    rel_root = Path(root).relative_to(src_dir)
                    for file in files:
                        rel_file = rel_root / file
                        if (
                            should_include_git(rel_file, exclude_patterns)
                            if isinstance(exclude_patterns, list)
                            and all(isinstance(p, tuple) for p in exclude_patterns)
                            else should_include(
                                rel_file, include_patterns, exclude_patterns
                            )
                        ):
                            filtered_list.append(rel_file)
        file_list = filtered_list
    else:
        file_list = gather_files(src_dir, include_patterns, exclude_patterns)

    if preview:
        print_tree(file_list)
        total_bytes = sum(
            (src_dir / f).stat().st_size for f in file_list if (src_dir / f).is_file()
        )
        print(f"\n{len(file_list)} files will be zipped.")
        print(f"Total size: {total_bytes / (1024 * 1024):.2f} MB")
        return

    print(f"[zipper] Archiving from: {src_dir}")
    print(f"[zipper] Output: {zip_path}")
    print(
        f"[zipper] INCLUDE patterns: {include_patterns if include_patterns else '[ALL]'}"
    )
    print(f"[zipper] EXCLUDE patterns: {exclude_patterns}")
    print(f"[zipper] {len(file_list)} files will be zipped.")

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for rel_file in file_list:
            abs_file = src_dir / rel_file
            if abs_file.is_file():
                zipf.write(abs_file, rel_file)
    print(f"[zipper] Done. {len(file_list)} files added to archive.")
    # Handle checkpointing
    if checkpoint:
        history_dir = out_dir / checkpoint_dir
        history_dir.mkdir(parents=True, exist_ok=True)
        checkpoint_name = f"{zip_name.replace('.zip', f'_{timestamp}.zip')}"
        checkpoint_path = history_dir / checkpoint_name
        shutil.copy(zip_path, checkpoint_path)
        print(f"[zipper] Checkpoint saved: {checkpoint_path}")

        # Check size of .history
        total_bytes = sum(f.stat().st_size for f in history_dir.glob("*.zip"))
        total_mb = total_bytes / (1024 * 1024)
        if total_mb > 100:
            print(
                f"[zipper] ⚠️ .history exceeds 100MB ({total_mb:.2f} MB). Run with --checkpoint_keep N to prune."
            )

        # Optionally prune old checkpoints
        if checkpoint_keep is not None:
            all_checkpoints = sorted(
                history_dir.glob("*.zip"), key=lambda f: f.stat().st_mtime, reverse=True
            )
            to_delete = all_checkpoints[checkpoint_keep:]
            for f in to_delete:
                f.unlink()
            print(
                f"[zipper] Pruned {len(to_delete)} old checkpoints. Kept {checkpoint_keep}."
            )


if __name__ == "__main__":
    args = parse_args()
    zip_project(
        args.src_dir,
        args.out_dir,
        args.include,
        args.exclude,
        args.preview,
        args.ignore_file,
        args.checkpoint,
        args.checkpoint_keep,
        args.checkpoint_dir,
        args.include_only,
        args.load_context_yaml,
    )
