"""
test_embedding_cli.py
------------------
Unit tests for embedding_cli.py (argument parsing, config logic).
"""

import unittest
import sys
import os
import tempfile
from unittest.mock import patch

# Import the main function from the CLI script
from embedding_lib.embedding_cli import main as embedding_cli_main

class TestEmbeddingCLI(unittest.TestCase):
    @patch('embedding_lib.embedding_cli.embed_documents')
    def test_main_success(self, mock_embed_documents):
        # Setup mock
        mock_embed_documents.return_value = {
            'total_embeddings': 10,
            'skipped_chunks': 0
        }
        
        # Create a temporary directory for testing
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a dummy config file
            config_path = os.path.join(tmpdir, 'test_config.yaml')
            with open(config_path, 'w', encoding='utf-8') as f:
                f.write('test: config')
            
            # Set up command line arguments
            test_args = [
                'embedding_cli.py',
                '--config', config_path,
                '--output_dir', tmpdir,
                '--overwrite'
            ]
            
            with patch('sys.argv', test_args):
                with patch('builtins.print') as mock_print:
                    embedding_cli_main()
                    
                    # Verify the function was called with the right keyword arguments
                    mock_embed_documents.assert_called_once()
                    args, kwargs = mock_embed_documents.call_args
                    self.assertEqual(kwargs['config_path'], config_path)
                    self.assertEqual(kwargs['output_dir'], tmpdir)
                    self.assertTrue(kwargs['overwrite'])
                    
                    # Verify the output
                    mock_print.assert_any_call("Embedded chunks: 10")
                    mock_print.assert_any_call("Skipped files: 0")

    @patch('embedding_lib.embedding_cli.embed_documents')
    def test_missing_required_args(self, mock_embed_documents):
        # Test with missing required arguments
        test_args = ['embedding_cli.py']
        
        with patch('sys.argv', test_args):
            with self.assertRaises(SystemExit) as cm:
                embedding_cli_main()
            self.assertEqual(cm.exception.code, 2)  # ArgumentError exit code
            mock_embed_documents.assert_not_called()
            
    @patch('embedding_lib.embedding_cli.embed_documents')
    def test_embedding_failure(self, mock_embed_documents):
        # Test handling of embedding failure
        mock_embed_documents.side_effect = Exception("Embedding failed")
        
        # Create a temporary directory for testing
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a dummy config file
            config_path = os.path.join(tmpdir, 'test_config.yaml')
            with open(config_path, 'w', encoding='utf-8') as f:
                f.write('test: config')
                
            # Set up command line arguments
            test_args = [
                'embedding_cli.py',
                '--config', config_path,
                '--output_dir', tmpdir
            ]
            
            with patch('sys.argv', test_args):
                with self.assertRaises(Exception) as cm:
                    embedding_cli_main()
                self.assertEqual(str(cm.exception), "Embedding failed")

if __name__ == "__main__":
    unittest.main()
