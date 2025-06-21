# test_board_game_features.py

import pytest
import numpy as np # <-- Import numpy for np.inf
from unittest.mock import patch
from rl_project.environments.board_game_env import BoardGameEnv, FlatTile

# ===== Test Fixtures =====

@pytest.fixture
def feature_test_config():
    """Provides a standard configuration for feature tests."""
    return {
        "board_layout": [
            {"type": "FlatTile", "params": {"points": 200}},
            {"type": "FlatTile", "params": {"gems": 10}},
        ],
        "initial_resources": {"initial_turns": 50, "points": 0, "gems": 0},
        "observed_resources": ["points", "gems"],
        "reward_weights": {"points": 1.0, "gems": 0.5, "free_turns": 0.1},
        "goal_points": 500,
        "max_turns": 20,
        "points_breakpoints": [100, 300, 600],
        "turn_task_breakpoints": [5, 10, 15],
        "turn_task_reward": [1, 2, 3]
    }

@pytest.fixture
def env(feature_test_config):
    """Creates a BoardGameEnv instance for feature testing."""
    return BoardGameEnv(**feature_test_config)


# ===== Feature Test Class =====

class TestBoardGameFeatures:
    """Tests for complex, multi-step features of the environment."""

    def test_termination_by_reaching_goal(self, env):
        """Tests that the episode terminates correctly when goal_points is reached."""
        env.reset()
        env.master_resources["points"] = 400
        
        with patch('random.randint', return_value=0):
            _obs, _reward, terminated, truncated, _info = env.step(0)

        assert env.master_resources["points"] >= env.goal_points
        assert terminated is True
        assert truncated is False

    def test_truncation_by_max_turns(self, env):
        """
        Tests that the episode truncates correctly when max_turns is exceeded.
        
        FIX NOTE: Set goal_points to infinity for this test to ensure
        that the episode cannot terminate, isolating the truncation logic.
        """
        env.max_turns = 5
        env.goal_points = np.inf # <-- THE FIX
        env.reset()
        truncated = False
        
        # Loop up to the step *before* truncation
        for i in range(env.max_turns - 1):
            _obs, _reward, terminated, truncated, _info = env.step(0)
            assert terminated is False, "Should not terminate when goal is unreachable"
            assert truncated is False, f"Should not be truncated at step {i+1}"
            
        # This final step will make turns_done == max_turns, triggering truncation
        _obs, _reward, _terminated, truncated, _info = env.step(0)

        assert env.turns_done == env.max_turns
        assert truncated is True, "Episode should be truncated on the final step."

    def test_point_breakpoint_crossing(self, env):
        """Tests that crossing a points_breakpoint correctly awards bonus turns."""
        env.reset()
        env.master_resources["points"] = 50 
        initial_turns = env.turns_remaining

        with patch('random.randint', return_value=0):
             env.step(0) 

        expected_turns = initial_turns - 1 + 2 
        assert env.turns_remaining == expected_turns
        assert env.points_bp_met == 0

    def test_turn_breakpoint_crossing(self, env):
        """Tests that crossing a turn_task_breakpoint correctly awards bonus turns."""
        env._board = [FlatTile(points=0)]
        env.reset()
        env.turns_done = 4
        initial_turns = env.turns_remaining

        env.step(0)

        expected_turns = initial_turns - 1 + 1
        assert env.turns_remaining == expected_turns
        assert env.turn_bp_met == 0