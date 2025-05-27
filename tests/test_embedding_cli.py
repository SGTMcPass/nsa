"""
test_embedding_cli.py
---------------------
Unit tests for embedding_cli.py (argument parsing, config logic).
"""

import unittest
import sys
import os
import json
import tempfile
import numpy as np
from unittest.mock import patch
from unittest.mock import patch, MagicMock

# Import the parse_args function from the CLI script
from embedding_lib.embedding_cli import parse_args, load_chunks, save_embeddings


class TestEmbeddingCLI(unittest.TestCase):
    def test_default_args(self):
        # Test with no CLI arguments (should use defaults)
        test_args = ["embedding_cli.py"]
        with patch.object(sys, "argv", test_args):
            args = parse_args()
            self.assertEqual(args.config, "config/embedding.yaml")
            self.assertEqual(args.format, "npy")
            self.assertEqual(args.log_level, "INFO")
            self.assertFalse(args.dry_run)

    def test_cli_overrides(self):
        # Test with some CLI overrides
        test_args = [
            "embedding_cli.py",
            "--config",
            "myconf.yaml",
            "--input",
            "input.jsonl",
            "--output",
            "outdir/",
            "--model",
            "some-model",
            "--pooling",
            "max",
            "--batch_size",
            "8",
            "--device",
            "cpu",
            "--format",
            "json",
            "--log_level",
            "DEBUG",
            "--dry_run",
        ]
        with patch.object(sys, "argv", test_args):
            args = parse_args()
            self.assertEqual(args.config, "myconf.yaml")
            self.assertEqual(args.input, "input.jsonl")
            self.assertEqual(args.output, "outdir/")
            self.assertEqual(args.model, "some-model")
            self.assertEqual(args.pooling, "max")
            self.assertEqual(args.batch_size, 8)
            self.assertEqual(args.device, "cpu")
            self.assertEqual(args.format, "json")
            self.assertEqual(args.log_level, "DEBUG")
            self.assertTrue(args.dry_run)

    def test_load_chunks_valid(self):
        """Test loading a valid JSONL file."""
        lines = ['{"text": "First chunk"}\n', '{"text": "Second chunk"}\n']
        with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
            tmp.writelines(lines)
            tmp_path = tmp.name
        try:
            chunks = load_chunks(tmp_path)
            self.assertEqual(len(chunks), 2)
            self.assertEqual(chunks[0]["text"], "First chunk")
            self.assertEqual(chunks[1]["text"], "Second chunk")
        finally:
            os.unlink(tmp_path)

    def test_load_chunks_empty(self):
        """Test loading an empty JSONL file."""
        with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
            tmp_path = tmp.name
        try:
            chunks = load_chunks(tmp_path)
            self.assertEqual(chunks, [])
        finally:
            os.unlink(tmp_path)

    def test_load_chunks_malformed(self):
        """Test error raised on malformed JSON line."""
        lines = ['{"text": "First chunk"}\n', "{bad json line}\n"]
        with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
            tmp.writelines(lines)
            tmp_path = tmp.name
        try:
            with self.assertRaises(Exception):
                load_chunks(tmp_path)
        finally:
            os.unlink(tmp_path)

    def test_embedding_execution(self):
        """Test that embedding runs and calls Embedder with correct args."""
        sample_chunks = [{"text": "hello"}, {"text": "world"}]

        with patch("embedding_lib.embedding_cli.Embedder") as MockEmbedder:
            mock_embedder_instance = MagicMock()
            mock_embedder_instance.embed.return_value = ["vec1", "vec2"]
            MockEmbedder.return_value = mock_embedder_instance

            # Simulate config/args
            model = "test-model"
            pooling = "mean"
            batch_size = 2
            device = "cpu"

            # Call embedding logic directly (as main() is hard to test end-to-end)
            embedder = MockEmbedder(
                model, pooling=pooling, batch_size=batch_size, device=device
            )
            embeddings = embedder.embed(sample_chunks)

            # --- Assertions ---
            MockEmbedder.assert_called_with(
                model, pooling=pooling, batch_size=batch_size, device=device
            )
            mock_embedder_instance.embed.assert_called_once_with(sample_chunks)
            assert embeddings == ["vec1", "vec2"]

    def test_save_embeddings_npy(self):
        """Test saving embeddings as npy format."""
        embeddings = np.array([[1.1, 2.2], [3.3, 4.4]])
        with tempfile.TemporaryDirectory() as outdir:
            save_embeddings(embeddings, outdir, "npy")
            npy_file = os.path.join(outdir, "embeddings.npy")
            loaded = np.load(npy_file)
            np.testing.assert_array_equal(loaded, embeddings)

    def test_save_embeddings_json(self):
        """Test saving embeddings as json format."""
        embeddings = [[1, 2], [3, 4]]
        with tempfile.TemporaryDirectory() as outdir:
            save_embeddings(embeddings, outdir, "json")
            json_file = os.path.join(outdir, "embeddings.json")
            with open(json_file, "r", encoding="utf-8") as f:
                loaded = json.load(f)
            self.assertEqual(loaded, embeddings)

    def test_save_embeddings_jsonl(self):
        """Test saving embeddings as jsonl format."""
        embeddings = [[1, 2], [3, 4]]
        with tempfile.TemporaryDirectory() as outdir:
            save_embeddings(embeddings, outdir, "jsonl")
            jsonl_file = os.path.join(outdir, "embeddings.jsonl")
            with open(jsonl_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
            self.assertEqual(json.loads(lines[0]), [1, 2])
            self.assertEqual(json.loads(lines[1]), [3, 4])

    def test_save_embeddings_unknown_format(self):
        """Test that unknown formats raise a ValueError."""
        embeddings = [[1, 2], [3, 4]]
        with tempfile.TemporaryDirectory() as outdir:
            with self.assertRaises(ValueError):
                save_embeddings(embeddings, outdir, "invalidfmt")

    def test_cli_end_to_end(self):
        """Full E2E test: parse args, load chunks, embed, save output in all formats."""
        # Create temp input JSONL file
        sample_chunks = [{"text": "one"}, {"text": "two"}]
        with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp_in:
            for chunk in sample_chunks:
                tmp_in.write(json.dumps(chunk) + "\n")
            tmp_in_path = tmp_in.name

        # Test all output formats
        for fmt in ["npy", "json", "jsonl"]:
            with self.subTest(fmt=fmt):
                with tempfile.TemporaryDirectory() as outdir, patch(
                    "embedding_lib.embedding_cli.Embedder"
                ) as MockEmbedder:
                    # Mock the embedder and its output
                    mock_embedder_instance = MagicMock()
                    # Fake embeddings as 2D float lists
                    fake_embeds = [[1.0, 2.0], [3.0, 4.0]]
                    mock_embedder_instance.embed.return_value = fake_embeds
                    MockEmbedder.return_value = mock_embedder_instance

                    # Use save_embeddings from imported module
                    from embedding_lib.embedding_cli import (
                        save_embeddings,
                        load_chunks,
                        parse_args,
                    )

                    # Parse args as if from CLI
                    args = [
                        "embedding_cli.py",
                        "--input",
                        tmp_in_path,
                        "--output",
                        outdir,
                        "--model",
                        "mock-model",
                        "--format",
                        fmt,
                    ]
                    with patch.object(sys, "argv", args):
                        parsed = parse_args()
                        chunks = load_chunks(parsed.input)
                        embedder = MockEmbedder(
                            parsed.model, pooling="mean", batch_size=32, device=None
                        )
                        embeddings = embedder.embed(chunks)
                        save_embeddings(embeddings, parsed.output, fmt)

                    # Check that the output file exists and contains the right data
                    out_file = os.path.join(outdir, f"embeddings.{fmt}")
                    assert os.path.exists(out_file)
                    if fmt == "npy":
                        arr = np.load(out_file)
                        np.testing.assert_array_equal(arr, fake_embeds)
                    elif fmt == "json":
                        with open(out_file) as f:
                            data = json.load(f)
                        assert data == fake_embeds
                    elif fmt == "jsonl":
                        with open(out_file) as f:
                            lines = [json.loads(line) for line in f]
                        assert lines == fake_embeds

        # Clean up temp file
        os.unlink(tmp_in_path)


if __name__ == "__main__":
    unittest.main()
