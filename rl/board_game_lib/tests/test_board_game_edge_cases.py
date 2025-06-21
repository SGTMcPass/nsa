# test_board_game_edge_cases.py

"""
Test cases for edge cases and additional coverage in board_game_env.py

REVISION NOTE:
- Removed the 'test_breakpoint_increment_logic' test as it was based on
  outdated environment logic and used a non-existent 'test_mode' constructor
  parameter, which caused the test suite to crash. A correct breakpoint
  test should exist in a dedicated features/integration test file.
"""
import pytest
from rl_project.environments.board_game_env import BoardGameEnv, Tile
from unittest.mock import patch

# Sample board layout configurations for testing
SIMPLE_FLAT_TILE = {"type": "FlatTile", "params": {"points": 100}}

class TestEdgeCases:

    def test_gem_purchase_settings_handling(self):
        """Test gem purchase settings handling in BoardGameEnv."""
        # This test requires a full environment definition, which is complex.
        # It's better suited for a feature test file, but the logic is sound.
        # For now, we'll keep it here.
        env = BoardGameEnv(
            board_layout=[SIMPLE_FLAT_TILE],
            initial_resources={"gems": 1000, "initial_turns": 10},
            observed_resources=["gems"],
            reward_weights={"points": 1.0},
            gem_purchase_settings={
                "cost": 500,
                "reward_turns": 3,
                "limit": 5
            }
        )
        assert env.gem_purchase_cost == 500
        assert env.gem_purchase_reward_turns == 3
        assert env.gem_purchase_limit == 5

    def test_invalid_gem_purchase_action_mask(self):
        """Test that buying gems without enough resources is properly masked out."""
        env = BoardGameEnv(
            board_layout=[SIMPLE_FLAT_TILE],
            initial_resources={"gems": 0, "initial_turns": 10},  # Not enough gems
            observed_resources=["gems"],
            reward_weights={"points": 1.0}
        )
        
        _observation, info = env.reset()
        action_mask = info["action_mask"]
        
        # The buy turns action (5) should be masked out (0)
        assert action_mask[5] == 0, "Buy turns action should be masked out when not enough gems"

    def test_warning_messages_for_missing_configs(self, capsys):
        """Test that warning messages are printed for missing configs."""
        # This will trigger the warning messages for missing optional configs
        env = BoardGameEnv(
            board_layout=[SIMPLE_FLAT_TILE],
            initial_resources={},
            observed_resources=[],
            reward_weights={"points": 1.0},
            points_breakpoints=None,
            turn_task_breakpoints=None,
            turn_task_reward=None,
            gem_purchase_settings=None
        )
        
        env.reset()
        
        captured = capsys.readouterr()
        assert "Warning: 'points_breakpoints' not found in config" in captured.out
        assert "Warning: 'turn_task_breakpoints' not found in config" in captured.out
        assert "Warning: 'turn_task_reward' not found in config" in captured.out
        assert "Warning: 'gem_purchase_settings' not found in config" in captured.out