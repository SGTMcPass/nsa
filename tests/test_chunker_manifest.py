import os
import tempfile
import pytest
from chunker_lib.manifest import load_manifest, save_manifest, ChunkerManifestError


def test_save_and_load_manifest(tmp_path):
    data = [{"id": 1, "text": "foo"}, {"id": 2, "text": "bar"}]
    path = tmp_path / "manifest.jsonl"
    save_manifest(str(path), data)
    loaded = load_manifest(str(path))
    assert loaded == data


def test_load_manifest_bad_json(tmp_path):
    path = tmp_path / "bad.jsonl"
    path.write_text('{"id": 1}\nnot json\n')
    with pytest.raises(ChunkerManifestError):
        load_manifest(str(path))


def test_save_manifest_not_list(tmp_path):
    path = tmp_path / "manifest.jsonl"
    with pytest.warns(UserWarning):
        with pytest.raises(ChunkerManifestError):
            save_manifest(str(path), {"id": 1})


def test_save_manifest_item_not_dict(tmp_path):
    path = tmp_path / "manifest.jsonl"
    with pytest.raises(ChunkerManifestError):
        save_manifest(str(path), [{"id": 1}, "not a dict"])
