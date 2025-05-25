#!/usr/bin/env bash
# make_core_howto.sh  –  build chunks/core_howto.md  (no realpath)
set -euo pipefail

CHUNKS_DIR="chunks"                 # relative
JSONL="$CHUNKS_DIR/chunks.jsonl"
OUT="$CHUNKS_DIR/core_howto.md"

KEEP_RE='(Install-Guide|Running-a-Simulation|Input-File|Building-a-Simulation|Simulation-Definition-File)_'

[[ -s $JSONL ]] || { echo "❌  $JSONL not found or empty"; exit 1; }

echo "🛠  Building $OUT ..."
: > "$OUT"
added=0

# Use jq for reliable field order (install once: sudo dnf install jq)
jq -r '. | "\(.chunk_id)\t\(.type)"' "$JSONL" |
grep -E "$KEEP_RE" |
while IFS=$'\t' read -r cid typ; do
  FILE="$CHUNKS_DIR/$typ/$cid.md"
  [[ -f $FILE ]] || { echo "⛔  Missing $FILE"; exit 1; }
  cat "$FILE" >> "$OUT"
  echo -e '\n\\pagebreak\n' >> "$OUT"
  ((added++))
  (( added % 25 == 0 )) && printf '.'
done
echo

(( added > 0 )) || { echo "⚠️  No matching chunks copied – adjust KEEP_RE."; exit 1; }

printf "✅  Added %s chunks. Size: %s\n" "$added" "$(du -h "$OUT" | cut -f1)"
