# config.py
import yaml
from pathlib import Path
import os


def load_config(path: str | Path) -> dict:
    """
    Load configuration from YAML file.

    Expands environment variables in 'docs_root' and returns the config dict.
    """
    path = Path(path)
    with path.open("r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    # Expand environment variables in docs_root
    if "docs_root" in cfg:
        cfg["docs_root"] = os.path.expandvars(cfg["docs_root"])
    return cfg
