# main.py
from environments.gridworld import RLWorld
from agents.q_learning_agent import Agent
from trainers.advanced_trainer import AdvancedTrainer
from visualization.plot_agent_path import plot_agent_path
from visualization.plot_q_values import plot_q_values

# Initialize environment and agent
env = RLWorld(width=5, height=5)
agent = Agent(actions=["UP", "DOWN", "LEFT", "RIGHT"])

# Initialize the trainer
trainer = AdvancedTrainer(agent=agent, environment=env, episodes=100, max_steps=50)

# Run training
trainer.train()

# Plot the agent path using the tracked path history
plot_agent_path((5, 5), trainer.path_history, trainer.environment.goal_state)

# Plot the Q-Value Heatmap
plot_q_values(agent, (5, 5))

# Plot the reward trajectory
trainer.plot_rewards()
