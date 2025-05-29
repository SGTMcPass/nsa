import os
import logging
from pathlib import Path
from embedding_lib.embedder import Embedder
from embedding_lib.faiss_vector_store import FaissVectorStore
from chunker_lib.core import chunk_documents, load_config  # Update if needed

# --- Config: Use TRICK_HOME ---
TRICK_HOME = os.environ.get("TRICK_HOME")
if not TRICK_HOME:
    raise EnvironmentError("TRICK_HOME environment variable not set!")
INDEX_MD_PATH = Path(TRICK_HOME) / "docs" / "index.md"
INPUT_DOCS_DIR = os.path.join(TRICK_HOME, "docs")
OUTPUT_DOCS_DIR = Path("data/chunks_out")
CFG_PATH = "config/chunker_config.yaml"
OUTPUT_CHUNKS_FILE = "data/chunks.txt"
INDEX_PATH = "data/trick_embeddings"
MODEL_NAME = "intfloat/e5-base-v2"
DEVICE = "cpu"  # or "cuda"

logging.basicConfig(level=logging.INFO)


def main():
    logging.info(f"Reading Trick docs from: {INPUT_DOCS_DIR}")
    cfg = load_config(CFG_PATH)
    OUTPUT_DOCS_DIR.mkdir(parents=True, exist_ok=True)
    num_files = chunk_documents(cfg, INDEX_MD_PATH, OUTPUT_DOCS_DIR)

    # Save chunk output for audit/debug
    with open(OUTPUT_CHUNKS_FILE, "w") as f:
        for cid, chunk in zip(id, chunks):
            f.write(f"{cid}\t{chunk}\n")

    # Embedding
    logging.info("Generating embeddings...")
    embedder = Embedder(model_name=MODEL_NAME, device=DEVICE)
    embeddings = embedder.encode_chunks(chunks, prefix="passage:")
    assert embeddings.shape[0] == len(ids), "Embedding/chunk count mismatch"
    assert embeddings.shape[1] == 768, "Expected 768-dim for e5-base-v2"

    # FAISS index
    logging.info("Building FAISS index...")
    store = FaissVectorStore(dim=embeddings.shape[1])
    store.add(embeddings, ids)
    store.save(INDEX_PATH)
    logging.info(f"Saved FAISS index and IDs to: {INDEX_PATH}.index/.ids")

    logging.info("Pipeline complete! Ready for API/retrieval.")


if __name__ == "__main__":
    main()
