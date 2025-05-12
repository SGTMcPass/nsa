# main.py
"""
Main execution script for training the Q-learning agent in the GridWorld environment.

- Loads the Q-table if available.
- Runs training.
- Saves the Q-table checkpoint on completion.
- Logs all activities to 'output/training_log.log'
"""

# === Imports ===
from environments.gridworld import RLWorld
from agents.q_learning_agent import Agent
from trainers.advanced_trainer import AdvancedTrainer
from trainers.checkpoint_manager import CheckpointManager
from visualization.plot_agent_path import plot_agent_path
from visualization.plot_q_values import plot_q_values
from visualization.path_animator import PathAnimator
from utils.logger import RLLogger

# === Initialize the Logger ===
logger = RLLogger()

# === Step 1: Initialize Environment and Agent ===
env = RLWorld(width=5, height=5, num_obstacles=5)
agent = Agent(actions=["UP", "DOWN", "LEFT", "RIGHT"])

# === Step 2: Initialize the Checkpoint Manager ===
checkpoint_manager = CheckpointManager()
loaded_q_table = checkpoint_manager.load()
if loaded_q_table:
    agent.q_table = loaded_q_table

# === Step 3: Initialize the Trainer and Train ===
# ✅ Increased Episodes and Adjusted Decay
trainer = AdvancedTrainer(
    agent=agent,
    environment=env,
    episodes=200,  # 🚀 Increased to 200 episodes
    max_steps=50,
    epsilon_decay=0.995,  # 🚀 Slower decay rate
)
trainer.train()

# === Step 4: Save the Q-Table Checkpoint ===
checkpoint_manager.save(agent.q_table)

# === Step 5: Static Visualizations ===
plot_agent_path((5, 5), trainer.path_history, trainer.environment.goal_state)
plot_q_values(agent, (5, 5))

# === Step 6: Learning Curve Visualization ===
trainer.plot_learning_curves()

# === Step 7: Animated Visualization ===
animator = PathAnimator(
    grid_size=(5, 5),
    path=trainer.path_history,
    obstacles=trainer.environment.obstacles,
    goal=trainer.environment.goal_state,
)
animator.animate()

# === Step 8: Logging Output ===
logger.info("Training and visualization complete. Check output directory for results.")
