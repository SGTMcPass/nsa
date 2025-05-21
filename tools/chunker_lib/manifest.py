# manifest.py
import json
from pathlib import Path
from typing import List, Dict


def write_manifest(metadata: List[Dict], output_dir: Path) -> None:
    """
    Write:
      - `chunks.jsonl`: JSON Lines metadata index
      - `chunks_manifest.md`: Markdown table of metadata
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    # JSONL
    with (output_dir / 'chunks.jsonl').open('w', encoding='utf-8') as jf:
        for m in metadata:
            jf.write(json.dumps(m, ensure_ascii=False) + '\n')
    # Markdown manifest
    with (output_dir / 'chunks_manifest.md').open('w', encoding='utf-8') as mf:
        mf.write('| chunk_id | type | path | heading | preview |\n')
        mf.write('|---|---|---|---|---|\n')
        for m in metadata:
            p = m.get('preview', '').replace('|', '&#124;')
            mf.write(f"| {m['chunk_id']} | {m['type']} | {m['path']} | {m['heading']} | {p} |\n")
