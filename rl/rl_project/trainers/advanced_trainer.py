# trainers/advanced_trainer.py
import matplotlib.pyplot as plt


class AdvancedTrainer:
    def __init__(
        self,
        agent,
        environment,
        episodes=100,
        max_steps=50,
        epsilon_decay=0.99,
        min_epsilon=0.01,
    ):
        """
        Advanced Trainer for RL Agent with dynamic exploration and reward shaping.

        Parameters:
        - agent: The Q-learning agent.
        - environment: The environment (GridWorld).
        - episodes: Number of training episodes.
        - max_steps: Maximum steps per episode.
        - epsilon_decay: Rate at which exploration reduces.
        - min_epsilon: The lowest possible exploration rate.
        """
        self.agent = agent
        self.environment = environment
        self.episodes = episodes
        self.max_steps = max_steps
        self.epsilon_decay = epsilon_decay
        self.min_epsilon = min_epsilon
        self.training_rewards = []
        self.path_history = []  # ✅ Added this to track the path

    def train(self):
        """
        Train the agent over multiple episodes with decay-based exploration.
        """
        for episode in range(self.episodes):
            state = self.environment.reset()
            total_reward = 0
            episode_path = [state]  # Start tracking the path

            for step in range(self.max_steps):
                action = self.agent.select_action(state)
                next_state, reward, done = self.environment.step(action)
                self.agent.learn(state, action, reward, next_state)
                state = next_state
                total_reward += reward
                episode_path.append(state)  # Add each state to the path

                if done:
                    break

            # Store the final path of the episode
            self.path_history = episode_path

            # Decay the exploration rate and clip it to a minimum value
            self.agent.exploration_rate = max(
                self.min_epsilon, self.agent.exploration_rate * self.epsilon_decay
            )
            self.training_rewards.append(total_reward)

            print(
                f"Episode {episode + 1}: Total Reward = {total_reward}, Exploration Rate = {self.agent.exploration_rate}"
            )

        print("Training completed.")

    def plot_rewards(self, save_path="output/reward_trajectory.png"):
        """
        Plots the reward accumulation over episodes and saves it as a PNG.
        """
        plt.figure(figsize=(6, 4))
        plt.plot(self.training_rewards, label="Total Reward")
        plt.title("Training Rewards Over Time")
        plt.xlabel("Episode")
        plt.ylabel("Total Reward")
        plt.grid()
        plt.legend()
        plt.savefig(save_path)
        plt.close()
