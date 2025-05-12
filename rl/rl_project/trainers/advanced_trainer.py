# trainers/advanced_trainer.py
import matplotlib.pyplot as plt
import os


class AdvancedTrainer:
    """
    Advanced Trainer for RL Agent with dynamic exploration and reward shaping.

    This class handles:
    - Training over multiple episodes.
    - Decaying the exploration rate.
    - Tracking cumulative rewards, steps taken, and path history.
    - Plotting learning efficiency over time.
    """

    def __init__(
        self,
        agent,
        environment,
        episodes=200,
        max_steps=50,
        epsilon_decay=0.995,
        min_epsilon=0.01,
    ):
        """
        Initializes the AdvancedTrainer with the agent and environment.

        Parameters:
        - agent (Agent): The learning agent.
        - environment (RLWorld): The environment for the agent to interact with.
        - episodes (int): Number of training episodes.
        - max_steps (int): Maximum steps per episode.
        - epsilon_decay (float): Decay rate for exploration.
        - min_epsilon (float): Minimum exploration rate.
        """
        self.agent = agent
        self.environment = environment
        self.episodes = episodes
        self.max_steps = max_steps
        self.epsilon_decay = epsilon_decay
        self.min_epsilon = min_epsilon
        self.training_rewards = []
        self.steps_per_episode = []
        self.path_history = []  # ✅ Added this to track the agent's path
        self.collision_history = []  # ✅ Tracks collisions
        self.loop_history = []  # ✅ Tracks loops

    def train(self):
        """
        Train the agent over multiple episodes with decay-based exploration.
        """
        for episode in range(self.episodes):
            # ✅ Start a new episode
            state = self.environment.reset()
            total_reward = 0
            step_count = 0
            episode_path = [state]  # ✅ Track the path for this episode
            collisions = 0
            loops = 0

            seen_states = set()
            seen_states.add(state)

            for step in range(self.max_steps):
                # ✅ Select an action and interact with the environment
                action = self.agent.select_action(state)
                next_state, reward, done, collided = self.environment.step(action)

                # ✅ Learn from the experience
                self.agent.learn(state, action, reward, next_state)

                # ✅ Detect looping (revisiting the same state)
                if next_state == state:
                    reward -= 0.5  # 🚀 Penalty for revisiting a state

                # ✅ Update state and track reward
                episode_path.append(state)
                total_reward += reward
                step_count += 1

                # ✅ Track collision detection
                if collided:
                    collisions += 1

                state = next_state

                # ✅ Detect looping (revisiting the same state)
                if next_state in seen_states:
                    loops += 1
                else:
                    seen_states.add(next_state)

                # ✅ If the goal is reached, end the episode early
                if done:
                    break

            # ✅ Decay the exploration rate and clip it to a minimum value
            self.agent.exploration_rate = max(
                self.min_epsilon, self.agent.exploration_rate * self.epsilon_decay
            )

            # ✅ Log rewards, steps, collisions, and loops
            self.training_rewards.append(total_reward)
            self.steps_per_episode.append(step_count)
            self.path_history = episode_path
            self.collision_history.append(collisions)
            self.loop_history.append(loops)

            # ✅ Logging information for each episode
            print(
                f"Episode {episode + 1}: Total Reward = {total_reward}, Steps = {step_count}, Collisions = {collisions}, Loops = {loops}"
            )

        print("🎓 Training completed.")

    def plot_learning_curves(self, save_path="output/learning_curve.png"):
        """
        Plots the learning efficiency over episodes and saves it as an image.

        Parameters:
        - save_path (str): Path to save the plot.
        """
        if not os.path.exists("output"):
            os.makedirs("output", exist_ok=True)

        plt.figure(figsize=(18, 5))

        # ✅ Plot Cumulative Rewards
        plt.subplot(1, 3, 1)
        plt.plot(self.training_rewards)
        plt.title("Cumulative Reward Over Time")
        plt.xlabel("Episode")
        plt.ylabel("Total Reward")
        plt.grid()

        # ✅ Plot Steps Taken
        plt.subplot(1, 3, 2)
        plt.plot(self.steps_per_episode)
        plt.title("Steps Taken Over Time")
        plt.xlabel("Episode")
        plt.ylabel("Steps Taken")
        plt.grid()

        # ✅ Plot Collisions and Loops
        plt.subplot(1, 3, 3)
        plt.plot(self.collision_history, label="Collisions")
        plt.plot(self.loop_history, label="Loops")
        plt.title("Collisions & Loops Over Time")
        plt.xlabel("Episode")
        plt.ylabel("Count")
        plt.legend()
        plt.grid()

        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
        print(f"📊 Learning curves saved to {save_path}")
