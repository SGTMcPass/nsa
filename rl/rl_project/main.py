# main.py
from environments.gridworld import RLWorld
from agents.q_learning_agent import Agent

# Initialize the environment and the agent
env = RLWorld(width=5, height=5)
agent = Agent(actions=["UP", "DOWN", "LEFT", "RIGHT"])

# Training parameters
episodes = 10
max_steps = 50

# Training loop
for episode in range(episodes):
    print(f"Episode {episode + 1} Start")
    state = env.reset()
    for step in range(max_steps):
        action = agent.select_action(state)
        next_state, reward, done = env.step(action)
        agent.learn(state, action, reward, next_state)
        state = next_state
        env.render()
        print(
            f"Step: {step + 1}, Action: {action}, State: {state}, Reward: {reward}, Done: {done}"
        )
        print("-" * 20)
        if done:
            print("🏁 Goal reached! Episode complete.")
            break
    print(f"Episode {episode + 1} End\n")
    print("=" * 40)
