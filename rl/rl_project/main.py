# main.py
"""
Main execution script for training the Q-learning agent in the GridWorld environment.

Steps:
1. Environment and agent initialization.
2. Training using the AdvancedTrainer class.
3. Visualization:
   - Pathfinding heatmap.
   - Q-value state mapping.
   - Reward trajectory over episodes.
   - Animated GIF of agent's pathfinding process.
"""

# === Imports ===
from environments.gridworld import RLWorld
from agents.q_learning_agent import Agent
from trainers.advanced_trainer import AdvancedTrainer
from visualization.plot_agent_path import plot_agent_path
from visualization.plot_q_values import plot_q_values
from visualization.path_animator import PathAnimator

# === Step 1: Initialize Environment and Agent ===
"""
We create a 5x5 GridWorld environment with 5 randomly placed obstacles.
The agent is initialized with four possible actions: UP, DOWN, LEFT, RIGHT.
"""
env = RLWorld(width=5, height=5, num_obstacles=5)
agent = Agent(actions=["UP", "DOWN", "LEFT", "RIGHT"])

# === Step 2: Initialize the Trainer ===
"""
The AdvancedTrainer class handles:
1. Interaction between agent and environment.
2. Training loop over multiple episodes.
3. Reward optimization and loop detection.
"""
trainer = AdvancedTrainer(agent=agent, environment=env, episodes=50, max_steps=50)

# === Step 3: Run the Training Loop ===
"""
The agent is trained over 50 episodes, with each episode capped at 50 steps.
- Obstacles are re-randomized on each reset.
- The agent receives penalties for:
    - Hitting obstacles (-5).
    - Revisiting states (-0.5).
    - Moving without progress (-0.1).
- Reaching the goal is rewarded with +1.
"""
trainer.train()

# === Step 4: Static Visualizations ===
"""
We generate three static visualizations:
1. The final agent path taken in the last episode.
2. A heatmap of Q-values representing the agent's learned state-action values.
3. A plot of the reward trajectory to understand learning efficiency.
"""
# ➡️ Plot the path
plot_agent_path((5, 5), trainer.path_history, trainer.environment.goal_state)

# ➡️ Plot the heatmap of Q-values
plot_q_values(agent, (5, 5))

# ➡️ Plot the reward trajectory over time
trainer.plot_rewards()

# === Step 5: Animated Visualization ===
"""
We create an animated GIF of the agent's path:
- Shows step-by-step navigation.
- Includes obstacles (black squares) and the goal (green square).
- Saved to 'output/agent_animation.gif'.
"""
animator = PathAnimator(
    grid_size=(5, 5),
    path=trainer.path_history,
    obstacles=trainer.environment.obstacles,
    goal=trainer.environment.goal_state,
)
animator.animate()

"""
All generated files are saved to the 'output/' directory:
- agent_path.png: The final path taken.
- q_values_heatmap.png: Heatmap of learned Q-values.
- reward_trajectory.png: Plot of reward progression.
- agent_animation.gif: Animated GIF of the agent's navigation.
"""
