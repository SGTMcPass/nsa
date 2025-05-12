# trainers/advanced_trainer.py
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os


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
        """
        self.agent = agent
        self.environment = environment
        self.episodes = episodes
        self.max_steps = max_steps
        self.epsilon_decay = epsilon_decay
        self.min_epsilon = min_epsilon
        self.training_rewards = []
        self.path_history = []

    def train(self):
        for episode in range(self.episodes):
            state = self.environment.reset()
            total_reward = 0
            episode_path = [state]
            visited_states = set()

            for step in range(self.max_steps):
                if state in visited_states:
                    # Penalize revisiting the same state
                    total_reward -= 0.5
                    print(f"🔁 Loop detected at {state}! Penalty applied.")
                visited_states.add(state)

                action = self.agent.select_action(state)
                next_state, reward, done = self.environment.step(action)
                self.agent.learn(state, action, reward, next_state)
                state = next_state
                total_reward += reward
                episode_path.append(state)

                if done:
                    break

            self.path_history = episode_path
            self.agent.exploration_rate = max(
                self.min_epsilon, self.agent.exploration_rate * self.epsilon_decay
            )
            self.training_rewards.append(total_reward)

            print(
                f"Episode {episode + 1}: Total Reward = {total_reward}, Exploration Rate = {self.agent.exploration_rate}"
            )

        print("Training completed.")

    def plot_rewards(self, save_path="output/agent_path.png"):
        """
        Plots the reward accumulation over episodes and saves it as a PNG.
        """
        print(
            f"📝 Checking if path exists: {os.path.exists('/app/output')}"
        )  # Debugging line
        plt.figure(figsize=(6, 4))
        plt.plot(self.training_rewards, label="Total Reward")
        plt.title("Training Rewards Over Time")
        plt.xlabel("Episode")
        plt.ylabel("Total Reward")
        plt.grid()
        plt.legend()
        plt.savefig(save_path)
        print(f"✅ Plot saved to {save_path}")
        plt.close()
