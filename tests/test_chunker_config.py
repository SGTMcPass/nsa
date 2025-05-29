import os
import tempfile
import pytest
from chunker_lib.config import load_config, ChunkerConfigError


def test_load_config_valid_yaml(tmp_path):
    yaml_path = tmp_path / "test.yaml"
    yaml_path.write_text("foo: 123\nbar: true")
    cfg = load_config(str(yaml_path))
    assert cfg == {"foo": 123, "bar": True}


def test_load_config_empty_path():
    assert load_config(None) == {}


def test_load_config_bad_yaml(tmp_path):
    yaml_path = tmp_path / "bad.yaml"
    yaml_path.write_text(":\nnot valid yaml")
    with pytest.raises(ChunkerConfigError):
        load_config(str(yaml_path))


def test_load_config_missing_file(tmp_path):
    missing = tmp_path / "nope.yaml"
    with pytest.raises(ChunkerConfigError):
        load_config(str(missing))
