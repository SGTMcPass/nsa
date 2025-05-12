# tests/test_trainer.py
import unittest
from environments.gridworld import RLWorld
from agents.q_learning_agent import Agent
from trainers.advanced_trainer import AdvancedTrainer


class TestAdvancedTrainer(unittest.TestCase):

    def setUp(self):
        """Initialize the environment and agent for testing."""
        self.env = RLWorld(width=5, height=5, num_obstacles=0)
        self.env.obstacles.add((1, 1))  # 🚀 Place a known obstacle
        self.agent = Agent(actions=["UP", "DOWN", "LEFT", "RIGHT"])
        self.trainer = AdvancedTrainer(
            agent=self.agent, environment=self.env, episodes=2, max_steps=5
        )

    def test_collision_tracking(self):
        """Ensure collisions are tracked correctly."""
        self.env.current_state = (0, 1)
        _, reward, done, collision = self.env.step("DOWN")
        self.assertTrue(collision)
        self.assertEqual(reward, -10)

    def test_path_history_tracking(self):
        """Test that the path history is correctly tracked."""
        self.trainer.train()
        self.assertTrue(len(self.trainer.path_history) > 0)

    def test_learning_loop(self):
        """Test that learning updates the Q-table."""
        initial_q_values = self.agent.q_table[(0, 0)]
        self.trainer.train()
        updated_q_values = self.agent.q_table[(0, 0)]
        self.assertNotEqual(initial_q_values, updated_q_values)


if __name__ == "__main__":
    unittest.main()
