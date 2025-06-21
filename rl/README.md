# Board Game RL Environment

A customizable board game environment designed for reinforcement learning research and experimentation. This environment simulates a board game where an agent moves around a circular board, collecting rewards and managing resources.

## Table of Contents
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Environment Details](#environment-details)
  - [Tiles](#tiles)
  - [Resources](#resources)
  - [Actions](#actions)
  - [Observations](#observations)
  - [Rewards](#rewards)
- [Configuration](#configuration)
- [Training Agents](#training-agents)
- [Visualization](#visualization)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This environment is designed to help researchers and developers train reinforcement learning agents in a controlled, customizable board game setting. The game mechanics are simple enough for beginners to understand but complex enough to be interesting for advanced research.

## Key Concepts

### For Non-Technical Users

Imagine a board game where:
- You're a player moving around a circular path
- Each space on the board gives you different rewards when you land on it
- You can choose how many dice to roll each turn (1, 2, 3, 5, or 10)
- More dice mean bigger rewards but cost more turns
- You can also spend gems to buy extra turns
- The goal is to get as many points as possible before running out of turns

### For Technical Users

- **State Space**: Current position, turns remaining, and various resources
- **Action Space**: 6 discrete actions (5 multipliers + buy turns)
- **Reward**: Configurable weighted sum of collected resources
- **Termination**: When goal points are reached or max turns exceeded

## Installation

1. Clone this repository
2. Navigate to the RL directory:
   ```bash
   cd rl/rl
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Quick Start

```python
import gymnasium as gym
import numpy as np
from rl_project.environments.board_game_env import BoardGameEnv

# Create a simple board
board_config = [
    {"type": "FlatTile", "params": {"points": 100, "gems": 1}},
    {"type": "GrandPrizeTile", "params": {"points_reward": 10000}},
    {"type": "PointWheelTile", "params": {}},
    {"type": "FateWheelTile", "params": {}}
]

# Initialize the environment
env = BoardGameEnv(
    board_layout=board_config,
    initial_resources={"points": 0, "gems": 0, "gold": 0},
    observed_resources=["points", "gems", "gold"],
    reward_weights={"points": 1.0, "gems": 0.1, "gold": 0.05},
    goal_points=100000,
    max_turns=1000
)

# Run a simple random agent
observation, _ = env.reset()
done = False
total_reward = 0

while not done:
    action = env.action_space.sample()  # Random action
    observation, reward, terminated, truncated, info = env.step(action)
    total_reward += reward
    done = terminated or truncated

print(f"Total reward: {total_reward}")
```

## Environment Details

### Tiles

1. **FlatTile**: Provides fixed rewards
   - Example: `{"type": "FlatTile", "params": {"points": 100, "gems": 1}}`

2. **GrandPrizeTile**: Spin-to-win with special rewards
   - Example: `{"type": "GrandPrizeTile", "params": {"points_reward": 10000}}`

3. **PointWheelTile**: Two-stage wheel spin for points
   - Example: `{"type": "PointWheelTile"}`

4. **FateWheelTile**: Special wheel with various rewards
   - Example: `{"type": "FateWheelTile"}`

### Resources

- **points**: Main scoring resource
- **gems**: Used to buy additional turns
- **gold**: General purpose currency
- **free_turns**: Extra turns granted by certain tiles
- **chroma/obsidian**: Special resources from GrandPrizeTile

### Actions

| Action | Description |
|--------|-------------|
| 0 | 1x multiplier (roll 1 die) |
| 1 | 2x multiplier (roll 2 dice) |
| 2 | 3x multiplier (roll 3 dice) |
| 3 | 5x multiplier (roll 5 dice) |
| 4 | 10x multiplier (roll 10 dice) |
| 5 | Buy turns (750 gems for 5 turns, max 7 purchases) |

### Observations

The observation space includes:
1. Current position (0 to board_size-1)
2. Turns remaining
3. Turns taken
4. Additional resources as specified in `observed_resources`

### Rewards

Rewards are calculated as a weighted sum of collected resources:
```
total_reward = sum(resource_value * weight for resource, weight in reward_weights.items())
```

## Configuration

### BoardGameEnv Parameters

| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| board_layout | List[Dict] | List of tile configurations | Required |
| initial_resources | Dict[str, float] | Starting resources | Required |
| observed_resources | List[str] | Resources to include in observations | Required |
| reward_weights | Dict[str, float] | Weights for reward calculation | Required |
| goal_points | int | Points needed to win | 100,000 |
| max_turns | int | Maximum turns before game ends | 1,000 |

## Training Agents

### Example with Stable Baselines3

```python
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env

# Create vectorized environment
env = make_vec_env(
    lambda: BoardGameEnv(
        board_layout=board_config,
        initial_resources={"points": 0, "gems": 0},
        observed_resources=["points", "gems"],
        reward_weights={"points": 1.0, "gems": 0.1}
    ),
    n_envs=4
)

# Initialize and train agent
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=100000)
```

## Visualization

The environment supports basic rendering in human mode:

```python
env = BoardGameEnv(...)
observation, _ = env.reset()
done = False

while not done:
    action = env.action_space.sample()
    observation, _, terminated, truncated, _ = env.step(action)
    env.render()  # Render the current state
    done = terminated or truncated
```

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
