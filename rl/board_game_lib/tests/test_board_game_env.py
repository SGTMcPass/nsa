# test_board_game_env.py

"""
Unit tests for the BoardGameEnv class and its component Tiles.

REVISION NOTE:
- This file has been refactored to focus strictly on unit tests.
- It uses a fixture-based approach for clarity and maintainability.
- Complex integration/feature tests (e.g., for breakpoints, termination) have
  been removed and should be placed in 'test_board_game_features.py'.
- Incorrect assertions have been fixed.
"""

import pytest
import numpy as np
from unittest.mock import patch
from rl_project.environments.board_game_env import (
    BoardGameEnv,
    FlatTile,
    GrandPrizeTile,
    PointWheelTile,
    FateWheelTile,
)

# ===== Test Fixtures =====

@pytest.fixture
def sample_config():
    """Provides a complete, sample configuration dictionary for the environment."""
    return {
        "board_layout": [
            {"type": "FlatTile", "params": {"points": 100, "gems": 5}},
            {"type": "GrandPrizeTile", "params": {"points_reward": 10000}},
            {
                "type": "FateWheelTile",
                "params": {
                    "outcomes": [
                        {"chance": 5000, "reward": {"points": 500}},
                        {"chance": 5000, "reward": {"gems": 50}},
                    ]
                }
            }
        ],
        "initial_resources": {"initial_turns": 10, "gems": 0},
        "observed_resources": ["points", "gems"],
        "reward_weights": {"points": 1.0, "gems": 0.5, "free_turns": 0.1},
        "goal_points": 1000,
        "max_turns": 100,
        "gem_purchase_settings": {"cost": 750, "reward_turns": 5, "limit": 7}
    }

@pytest.fixture
def env(sample_config):
    """Creates a BoardGameEnv instance using the sample configuration."""
    return BoardGameEnv(**sample_config)


# ===== Tile Unit Tests =====

class TestTileClasses:
    """Unit tests for individual Tile classes, testing them in isolation."""

    def test_flat_tile_reward(self):
        """Tests that FlatTile returns correctly multiplied rewards."""
        tile = FlatTile(points=100, gems=5)
        assert tile.get_reward(1) == {"points": 100, "gems": 5, "free_turns": 0, "gold": 0}
        assert tile.get_reward(3) == {"points": 300, "gems": 15, "free_turns": 0, "gold": 0}

    @patch('random.randint')
    def test_grand_prize_tile_reward(self, mock_randint):
        """Tests GrandPrizeTile outcomes by mocking the random spin."""
        tile = GrandPrizeTile(points_reward=10000)
        # Test a specific outcome (e.g., gems reward)
        mock_randint.return_value = 4000  # This falls in the gem reward range
        reward = tile.get_reward(1)
        assert reward.get("gems") == 100
        # Test the bonus points outcome
        mock_randint.return_value = 6000  # > 5000, but not in a specific prize range
        reward = tile.get_reward(1)
        assert reward.get("points") == 10000

    def test_fate_wheel_tile_parsing(self):
        """Tests that FateWheelTile correctly parses outcomes and handles validation."""
        # Test valid outcomes
        outcomes = [{"chance": 10000, "reward": {"points": 100}}]
        tile = FateWheelTile(outcomes=outcomes)
        assert tile.outcomes == outcomes

        # Test that incorrect chance sum raises an error
        with pytest.raises(ValueError):
            FateWheelTile(outcomes=[{"chance": 5000, "reward": {}}])

    @patch('random.randint')
    def test_fate_wheel_reward(self, mock_randint):
        """Tests data-driven FateWheelTile reward logic."""
        outcomes = [
            {"chance": 5000, "reward": {"points": 500}},
            {"chance": 5000, "reward": {"gems": 50}},
        ]
        tile = FateWheelTile(outcomes=outcomes)
        # Test first outcome
        mock_randint.return_value = 1
        assert tile.get_reward(1) == {"points": 500}
        # Test second outcome
        mock_randint.return_value = 6000
        assert tile.get_reward(2) == {"gems": 100} # 50 gems * 2x multiplier


# ===== Environment Unit Tests =====

class TestBoardGameEnvUnit:
    """Unit tests for individual methods of the BoardGameEnv class."""

    def test_initialization(self, env):
        """Tests that the environment initializes its state correctly."""
        assert len(env._board) == 3
        assert env.goal_points == 1000
        assert env.max_turns == 100
        assert env.gem_purchase_cost == 750

    def test_reset(self, env):
        """Tests that reset() correctly initializes the environment state."""
        obs, info = env.reset()
        assert env.position == 0
        assert env.turns_remaining == 10
        assert env.turns_done == 0
        assert env.points_bp_met == -1
        assert isinstance(obs, dict)
        assert "observation" in obs
        assert "action_mask" in info

    @pytest.mark.parametrize("turns_left, gems, expected_mask", [
        (10, 0,   [1, 1, 1, 1, 1, 0]), # Can afford all multipliers, but not gems
        (4,  750, [1, 1, 1, 0, 0, 1]), # Can't afford 5x or 10x multiplier
        (0,  750, [0, 0, 0, 0, 0, 1]), # Can't afford any multiplier
        (10, 749, [1, 1, 1, 1, 1, 0]), # Can't afford gems
    ])
    def test_get_action_mask(self, env, turns_left, gems, expected_mask):
        """Tests the _get_action_mask method under different resource conditions."""
        env.reset()
        env.turns_remaining = turns_left
        env.master_resources["gems"] = gems
        
        mask = env._get_action_mask()
        np.testing.assert_array_equal(mask, np.array(expected_mask, dtype=np.int8))

    def test_step_invalid_action_penalty(self, env):
        """Tests that taking a masked (invalid) action results in a penalty."""
        env.reset()
        env.master_resources["gems"] = 0 # Cannot afford to buy turns
        
        # Action 5 (buy turns) should be invalid
        assert env._get_action_mask()[5] == 0

        # The step method asserts that the action is valid, so attempting
        # to step with an invalid action will raise an AssertionError.
        # This confirms the protection is working.
        with pytest.raises(AssertionError):
            env.step(5)