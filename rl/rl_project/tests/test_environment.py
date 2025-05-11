# tests/test_environment.py
import unittest
from environments.gridworld import RLWorld


class TestRLWorld(unittest.TestCase):

    def setUp(self):
        """Set up a 5x5 grid for testing."""
        self.env = RLWorld(width=5, height=5)

    def test_initial_state(self):
        """Agent should start at (0, 0) initially."""
        self.assertEqual(self.env.current_state, (0, 0))

    def test_goal_state(self):
        """Default goal state should be bottom-right corner."""
        self.assertEqual(self.env.goal_state, (4, 4))

    def test_step_valid_move(self):
        """A valid move should change the agent's state."""
        self.env.step("RIGHT")
        self.assertEqual(self.env.current_state, (0, 1))

    def test_step_invalid_move(self):
        """An invalid move should not change the state."""
        self.env.step("UP")
        self.assertEqual(self.env.current_state, (0, 0))

    def test_step_reward_boundary(self):
        """Going out of bounds should yield a reward of -1."""
        _, reward, _ = self.env.step("UP")
        self.assertEqual(reward, -1)

    def test_step_reward_goal(self):
        """Reaching the goal should yield a reward of +1."""
        for _ in range(4):
            self.env.step("DOWN")
        for _ in range(3):
            self.env.step("RIGHT")
        _, reward, done = self.env.step("RIGHT")
        self.assertEqual(reward, 1)
        self.assertTrue(done)

    def test_reset(self):
        """Reset should bring the agent back to (0, 0)."""
        self.env.step("RIGHT")
        self.env.reset()
        self.assertEqual(self.env.current_state, (0, 0))


if __name__ == "__main__":
    unittest.main()
