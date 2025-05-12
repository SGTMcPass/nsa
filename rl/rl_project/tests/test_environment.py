# tests/test_environment.py
import unittest
from environments.gridworld import RLWorld


class TestRLWorld(unittest.TestCase):

    def setUp(self):
        """Initialize the GridWorld for testing."""
        self.env = RLWorld(width=5, height=5, num_obstacles=0)
        self.env.goal_state = (4, 4)  # Ensure goal is known
        self.env.current_state = (0, 0)  # Starting point

    def test_valid_movement(self):
        """Test valid agent movements."""
        _, reward, done, _ = self.env.step("RIGHT")
        self.assertEqual(self.env.current_state, (0, 1))
        self.assertAlmostEqual(reward, -0.1)
        self.assertFalse(done)

        _, reward, done, _ = self.env.step("DOWN")
        self.assertEqual(self.env.current_state, (1, 1))
        self.assertAlmostEqual(reward, -0.1)
        self.assertFalse(done)

    def test_obstacle_collision(self):
        """Test collision detection with an obstacle."""
        self.env.obstacles.add((0, 1))
        _, reward, done, collision = self.env.step("RIGHT")
        self.assertEqual(self.env.current_state, (0, 0))  # Position unchanged
        self.assertEqual(reward, -10)
        self.assertFalse(done)
        self.assertTrue(collision)

    def test_out_of_bounds(self):
        """Test out-of-bounds movement."""
        _, reward, done, _ = self.env.step("UP")
        self.assertEqual(self.env.current_state, (0, 0))
        self.assertEqual(reward, -5)
        self.assertFalse(done)

    def test_goal_reached(self):
        """Test reaching the goal state."""
        self.env.current_state = (3, 4)
        _, reward, done, _ = self.env.step("DOWN")
        self.assertEqual(self.env.current_state, (4, 4))
        self.assertEqual(reward, 1)
        self.assertTrue(done)


if __name__ == "__main__":
    unittest.main()
