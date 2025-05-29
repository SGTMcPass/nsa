from fastapi import FastAPI, Query
from pydantic import BaseModel
from embedding_lib.embedder import Embedder
from embedding_lib.faiss_vector_store import FaissVectorStore
import numpy as np

# ----- Setup (singleton/global objects for MVP) -----
DIM = 768
MODEL_NAME = "intfloat/e5-base-v2"

# Load model and vector store
embedder = Embedder(model_name=MODEL_NAME, device="cpu")  # or "cuda" if available
store = FaissVectorStore(dim=DIM)
store.load("your_index_path")  # <-- Point to your real FAISS index files

# ----- FastAPI App -----
app = FastAPI(title="NASA Simulation Vector Search API", version="0.1.0")


class SearchRequest(BaseModel):
    query: str
    k: int = 5


class SearchResult(BaseModel):
    ids: list[str]
    scores: list[float] = []


@app.post("/search", response_model=SearchResult)
def search_chunks(request: SearchRequest):
    # Embed the input query (using "query:" prefix for e5)
    query_emb = embedder.encode_chunks([request.query], prefix="query:")
    # Run vector search
    ids = store.search(query_emb, k=request.k)[0]
    # (Optional: return similarity scores if you extend the interface)
    return SearchResult(ids=ids)
