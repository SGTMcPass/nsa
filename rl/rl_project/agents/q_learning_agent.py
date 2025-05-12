# agents/q_learning_agent.py
import random
from collections import defaultdict


class Agent:
    def __init__(
        self, actions, learning_rate=0.1, discount_factor=0.9, exploration_rate=1.0
    ):
        """
        Q-Learning Agent that interacts with the environment and updates its Q-Table.

        Parameters:
        - actions (list): List of possible actions.
        - learning_rate (float): Learning rate for Q-value updates.
        - discount_factor (float): Future reward discount factor.
        - exploration_rate (float): Exploration rate for action selection.
        """
        self.actions = actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate

        # ✅ Initialize the Q-Table using a static method instead of a lambda
        self.q_table = defaultdict(self.default_q_values)

    @staticmethod
    def default_q_values():
        """
        Initializes the default Q-values for any unseen state.

        Returns:
        - dict: All actions mapped to 0.0 Q-values.
        """
        return {action: 0.0 for action in ["UP", "DOWN", "LEFT", "RIGHT"]}

    def select_action(self, state):
        """
        Selects the next action for the agent based on the exploration/exploitation strategy.

        Parameters:
        - state (tuple): Current state of the agent.

        Returns:
        - str: Chosen action.
        """
        if random.random() < self.exploration_rate:
            return random.choice(self.actions)
        else:
            state_actions = self.q_table[state]
            max_value = max(state_actions.values())
            best_actions = [
                action for action, value in state_actions.items() if value == max_value
            ]
            return random.choice(best_actions)

    def learn(self, state, action, reward, next_state):
        """
        Updates the Q-table based on agent experience.

        Parameters:
        - state (tuple): Current state of the agent.
        - action (str): Action taken.
        - reward (float): Reward received after the action.
        - next_state (tuple): Resulting state after the action.
        """
        current_q = self.q_table[state][action]
        next_max_q = max(self.q_table[next_state].values())
        new_q = current_q + self.learning_rate * (
            reward + self.discount_factor * next_max_q - current_q
        )
        self.q_table[state][action] = new_q
