# agents/q_learning_agent.py
import random
from collections import defaultdict


class Agent:
    def __init__(
        self, actions, learning_rate=0.1, discount_factor=0.9, exploration_rate=1.0
    ):
        self.actions = actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate

        # Initialize the Q-Table
        self.q_table = defaultdict(lambda: {action: 0.0 for action in self.actions})

    def select_action(self, state):
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
        current_q = self.q_table[state][action]
        next_max_q = max(self.q_table[next_state].values())
        new_q = current_q + self.learning_rate * (
            reward + self.discount_factor * next_max_q - current_q
        )
        self.q_table[state][action] = new_q
