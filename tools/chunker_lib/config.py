"""
chunker_lib.config
YAML config loader for chunking tools.
Warns on type mismatch, robust error handling, reusable.
"""

import warnings
from typing import Any, Dict, Optional, Union
from pathlib import Path
import yaml


class ChunkerConfigError(Exception):
    """Custom exception for configuration load failures."""


def load_config(path: Optional[Union[str, Path]]) -> Dict[str, Any]:
    """
    Load chunker configuration from a YAML file.
    Returns an empty dict if path is None or empty.
    Warns if the path is not a str or Path.
    Raises ChunkerConfigError on I/O or parse errors.
    """
    if not path:
        return {}
    if not isinstance(path, (str, Path)):
        warnings.warn(
            f"[chunker_lib.config] 'path' is type {type(path)}, expected str, Path, or None. "
            "Proceeding, but future versions may enforce stricter types.",
            stacklevel=2,
        )
    try:
        path_obj = Path(path)
        with path_obj.open("r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        return config if config else {}
    except Exception as e:
        raise ChunkerConfigError(f"Failed to load config from {path}: {e}")
