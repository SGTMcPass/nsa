# tests/test_agent.py
import unittest
from agents.q_learning_agent import Agent


class TestAgent(unittest.TestCase):

    def setUp(self):
        """Set up the agent with standard actions."""
        self.agent = Agent(actions=["UP", "DOWN", "LEFT", "RIGHT"])

    def test_initial_q_values(self):
        """Q-values for new states should be 0.0."""
        self.assertEqual(self.agent.q_table[(0, 0)]["UP"], 0.0)
        self.assertEqual(self.agent.q_table[(0, 0)]["DOWN"], 0.0)

    def test_select_action_exploration(self):
        """Agent should explore if epsilon is high."""
        self.agent.exploration_rate = 1.0
        action = self.agent.select_action((0, 0))
        self.assertIn(action, ["UP", "DOWN", "LEFT", "RIGHT"])

    def test_select_action_exploitation(self):
        """Agent should exploit best-known action."""
        self.agent.q_table[(0, 0)]["RIGHT"] = 5.0
        self.agent.q_table[(0, 0)]["LEFT"] = 2.0
        self.agent.exploration_rate = 0.0
        action = self.agent.select_action((0, 0))
        self.assertEqual(action, "RIGHT")

    def test_learn_updates_q_value(self):
        """Agent should update Q-value after learning."""
        self.agent.learn((0, 0), "RIGHT", 1, (0, 1))
        updated_q = self.agent.q_table[(0, 0)]["RIGHT"]
        self.assertGreater(updated_q, 0.0)


if __name__ == "__main__":
    unittest.main()
