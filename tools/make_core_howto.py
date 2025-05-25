#!/usr/bin/env python3
"""
make_core_howto.py  –  deterministic & testable replacement for the Bash helper
Run:  python tools/make_core_howto.py
"""
import json, re, sys, pathlib, argparse, textwrap

KEEP = re.compile(
    r"(Install-Guide|Running-a-Simulation|Input-File|"
    r"Building-a-Simulation|Simulation-Definition-File)_"
)


def build(chunks_dir: pathlib.Path, out: pathlib.Path):
    added = 0
    with (chunks_dir / "chunks.jsonl").open() as jf, out.open(
        "w", encoding="utf-8"
    ) as of:
        for line in jf:
            rec = json.loads(line)
            if not KEEP.search(rec["chunk_id"]):
                continue
            md_path = chunks_dir / rec["type"] / f"{rec['chunk_id']}.md"
            try:
                of.write(md_path.read_text())
            except FileNotFoundError:
                sys.exit(f"✖ missing file {md_path}")
            of.write("\n\\pagebreak\n")
            added += 1
            if added % 25 == 0:
                print(f"…{added}", end="\r", file=sys.stderr)
    if added == 0:
        sys.exit("✖ keep-regex matched zero chunks.")
    size = out.stat().st_size / 1024
    print(f"\n✔ wrote {added} chunks  ({size:.0f} KB) → {out}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--chunks", default="chunks", type=pathlib.Path)
    p.add_argument("--out", default="chunks/core_howto.md", type=pathlib.Path)
    args = p.parse_args()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    build(args.chunks, args.out)
