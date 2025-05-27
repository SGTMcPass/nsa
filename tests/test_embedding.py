# tests/test_embedding.py

import pytest
from embedding_lib.embedder import Embedder
import torch


def is_cuda_really_usable():
    if not torch.cuda.is_available():
        return False
    try:
        # Actually try to allocate a small tensor on GPU to verify working CUBLAS/context
        torch.zeros(1).cuda()
        return True
    except RuntimeError:
        return False


@pytest.fixture
def dummy_chunks():
    return [
        'S_define { #include "foo.sm" ... }',
        "The main engine burn occurred at T+6:32.",
        "Python SWIG input: sim_object = TrickSimObject()",
    ]


def test_embedder_cpu(dummy_chunks):
    # Test Embedder instantiation and CPU fallback
    embedder = Embedder(model_name="intfloat/e5-base-v2", device="cpu")
    embeddings = embedder.encode_chunks(dummy_chunks)
    assert embeddings.shape[0] == len(dummy_chunks)
    assert embeddings.shape[1] == 768


def test_embedder_cuda_if_available(dummy_chunks):
    # Only run this if CUDA is available; skip otherwise
    if not is_cuda_really_usable():
        pytest.skip("CUDA not available on this system.")
    embedder = Embedder(model_name="intfloat/e5-base-v2", device="cuda")
    embeddings = embedder.encode_chunks(dummy_chunks)
    assert embeddings.shape[0] == len(dummy_chunks)
    assert embeddings.shape[1] == 768


def test_embedder_auto_device(dummy_chunks):
    # Test auto device selection logic
    embedder = Embedder(model_name="intfloat/e5-base-v2", device="auto")
    embeddings = embedder.encode_chunks(dummy_chunks)
    assert embeddings.shape[0] == len(dummy_chunks)
    assert embeddings.shape[1] == 768


def test_embedder_with_prefix(dummy_chunks):
    # Test that prefix is correctly prepended
    embedder = Embedder(model_name="intfloat/e5-base-v2", device="cpu")
    out = embedder.encode_chunks(dummy_chunks, prefix="passage:")
    assert out.shape[0] == len(dummy_chunks)


def test_embedder_without_prefix(dummy_chunks):
    # Test that omitting prefix still works
    embedder = Embedder(model_name="intfloat/e5-base-v2", device="cpu")
    out = embedder.encode_chunks(dummy_chunks, prefix=None)
    assert out.shape[0] == len(dummy_chunks)


def test_invalid_model_name():
    # Should raise OSError or similar if model doesn't exist
    with pytest.raises(Exception):
        Embedder(model_name="not-a-real-model", device="cpu")
