import os
import tempfile
import json
import pytest
from chunker_lib.utils import (
    read_file,
    write_file,
    find_markdown_files,
    load_json,
    save_json,
    ChunkerUtilsError,
)


def test_write_and_read_file():
    with tempfile.NamedTemporaryFile(delete=False, mode="w+", encoding="utf-8") as tf:
        path = tf.name
    try:
        write_file(path, "hello world")
        assert read_file(path) == "hello world"
    finally:
        os.remove(path)


def test_find_markdown_files(tmp_path):
    # Setup: create fake dir tree
    md1 = tmp_path / "a.md"
    md2 = tmp_path / "subdir" / "b.md"
    os.makedirs(md2.parent, exist_ok=True)
    md1.write_text("hi")
    md2.write_text("there")
    found = find_markdown_files(str(tmp_path))
    assert md1.as_posix() in found
    assert md2.as_posix() in found


def test_save_and_load_json(tmp_path):
    path = tmp_path / "data.json"
    obj = {"x": 42}
    save_json(str(path), obj)
    loaded = load_json(str(path))
    assert loaded == obj


def test_read_file_error():
    with pytest.raises(ChunkerUtilsError):
        read_file("/unlikely/to/exist/foobar.txt")


def test_load_json_error(tmp_path):
    bad_json = tmp_path / "bad.json"
    bad_json.write_text("{not:valid}")
    with pytest.raises(ChunkerUtilsError):
        load_json(str(bad_json))
