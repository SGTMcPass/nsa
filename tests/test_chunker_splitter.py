import pytest
from chunker_lib.splitter import split_markdown, ChunkerSplitterError


def test_split_word_basic():
    text = " ".join(str(i) for i in range(100))
    chunks = split_markdown(
        text, mode="word", category="reference", chunk_rules={"reference": 20}
    )
    assert len(chunks) == 5
    assert all(c["mode"].startswith("word") for c in chunks)


def test_split_paragraph_basic():
    text = "First para.\n\nSecond para.\n\nThird para."
    chunks = split_markdown(
        text, mode="paragraph", category="howto", chunk_rules={"howto": 4}
    )
    assert len(chunks) == 2
    assert "First para." in chunks[0]["content"]
    assert "Second para." in chunks[0]["content"]
    assert "Third para." in chunks[1]["content"]


def test_split_heading_basic():
    text = "# H1\nText one.\n\n## H2\nText two."
    chunks = split_markdown(
        text, mode="heading", category="reference", chunk_rules={"reference": 10}
    )
    assert len(chunks) == 2
    assert chunks[0]["content"].startswith("H1")
    assert all(c["mode"].startswith("heading") for c in chunks)


def test_split_word_overlap():
    text = "a " * 100
    rules = {"reference": 50}
    overlap = 0.2
    chunks = split_markdown(
        text, mode="word", category="reference", chunk_rules=rules, overlap_pc=overlap
    )
    assert len(chunks) > 1
    assert chunks[1]["start_word"] == 30  # As per implementation math


def test_split_paragraph_superchunking():
    text = "word " * 30 + "\n\n" + "word " * 25 + "\n\n" + "word " * 50
    rules = {"concept": 70}
    chunks = split_markdown(
        text, mode="paragraph", category="concept", chunk_rules=rules
    )
    assert len(chunks) == 2  # First two paras merge, third is one chunk


def test_split_heading_with_large_section():
    # Large section triggers fallback to word chunking
    text = "# Heading\n" + ("word " * 200)
    rules = {"reference": 100}
    chunks = split_markdown(
        text, mode="heading", category="reference", chunk_rules=rules
    )
    assert len(chunks) >= 2
    assert all(c["mode"] == "heading+word" for c in chunks)


def test_split_type_error():
    with pytest.warns(UserWarning):
        with pytest.raises(ChunkerSplitterError):
            split_markdown(1234, mode="word")


def test_split_unknown_mode():
    with pytest.raises(ChunkerSplitterError):
        split_markdown("text", mode="banana")
