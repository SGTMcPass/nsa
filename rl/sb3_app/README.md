# Reinforcement Learning for Custom Board Game

This project uses the Stable Baselines3 library to train a reinforcement learning agent to play a custom, resource-management-based board game. The goal is to develop an agent that can learn optimal strategies to maximize its score under various constraints.

## Project Structure

- `rl/`: Root directory for the reinforcement learning projects.
- `board_game_lib/`: A shared library containing the core game logic, including the custom `BoardGameEnv`.
- `sb3_app/`: The main application for training agents using Stable Baselines3.
- `configs/`: Contains YAML configuration files for experiments.
- `trainers/`: Contains the Python scripts for running the training (`run_sb3.py`) and the `StableBaselines3_Runner` implementation.
- `tools/`: Contains analysis scripts like `live_plotter.py` and `visualize_policy.py`.

## How to Run a Training Session

> All commands should be run from the `rl/sb3_app/` directory.

### Install Dependencies

```bash
poetry install
```

### Install GUI Backend (for live plotting)

#### For Fedora/CentOS/Rocky

```bash
sudo dnf install python3.11-tkinter python3.12-tkinter
```

#### For Debian/Ubuntu

```bash
# sudo apt-get install python3-tk
```

### Run Training

Execute the main training script, pointing it to a configuration file.

```bash
poetry run python sb3_app/trainers/run_sb3.py --config configs/sb3_board_game_config.yaml
```

## Understanding the Configuration (`sb3_board_game_config.yaml`)

The YAML configuration file is the primary way to control an experiment. Here is a breakdown of the key parameters:

### `runner` Section

This section controls the high-level execution of the training.

- `num_envs`: The number of parallel environments to run for data collection. A good starting point is the number of physical CPU cores on your machine.
- `total_timesteps`: The total number of environment steps the agent will be trained for.
- `tensorboard_log`: The base directory where TensorBoard logs will be saved.
- `anneal_lr`: (boolean) If true, the `learning_rate` will linearly decay to zero over the course of training.
- `anneal_entropy`: (boolean) If true, the `ent_coef` will linearly decay to zero over the course of training.
- `pretrained_model_path`: (Optional) Path to a `.zip` model file to use as a starting point for training (transfer learning).

### `hyperparams` Section

This section contains all parameters for the PPO algorithm.

#### `policy_kwargs`

- `net_arch`: Defines the neural network architecture.
  - `pi`: A list defining the hidden layer sizes for the policy network (the "Actor"). Example: `[512, 512]` is two layers with 512 neurons each.
  - `vf`: A list defining the hidden layer sizes for the value function network (the "Critic").

#### `params`

- `device`: The hardware to use for training (`cuda` or `cpu`).
- `n_steps`: The number of steps collected from each parallel environment before a training update. A larger value reduces the variance of the training data. Total batch size is `n_steps * num_envs`.
- `batch_size`: The size of the mini-batch used for each gradient descent update.
- `n_epochs`: How many times the agent iterates over the collected data buffer during each update. This is the primary lever to control the CPU/GPU workload balance.
- `gamma`: The discount factor for future rewards. A value closer to 1 (e.g., `0.999`) makes the agent more "far-sighted."
- `ent_coef`: The initial entropy coefficient. A higher value encourages more exploration.
- `learning_rate`: The initial step size for the optimizer.

### `environment` Section

This section configures the game rules and reward structure.

#### `params.reward_weights`

- `points`: The weight for each point scored (e.g., `1.0`).
- `turn_penalty`: The penalty subtracted from the reward for each turn spent. This teaches the agent to be efficient.
- `goal_miss_penalty`: A large penalty applied at the end of an episode if the agent ran out of turns without reaching the `goal_points`.
- `reward_scaling_factor`: A divisor used to scale down all rewards and penalties to a smaller, more numerically stable range.

## Analysis and Visualization

### Live Training Dashboard

To monitor training in real time, run the live plotter script in a separate terminal. It will automatically find the latest run and display key metrics.

```bash
poetry run python tools/live_plotter.py --log-dir ./logs/sb3_tensorboard/Your_Project_Name
```

### Understanding the Learning Outputs

The live plotter will show three key graphs:

- **`rollout/ep_rew_mean` (Mean Episode Reward)**: This is the most important graph. It shows the average final reward (Points - Penalties) per episode. An upward trend indicates the agent is successfully learning to optimize its strategy.
- **`rollout/ep_points_mean` (Mean Episode Points)**: This shows the average raw points scored per episode, ignoring any penalties. This is useful for understanding the agent's raw performance.
- **`rollout/ep_net_turns_spent_mean` (Mean Net Turns Spent)**: This shows the average number of turns the agent actually spent from its initial budget (`initial_turns - turns_remaining`). This is the key metric for judging efficiency. A downward trend means the agent is learning to achieve its goals faster.

## Visualizing the Agent's Strategy

After a model is trained and saved, you can use the `visualize_policy.py` script to see what decisions it has learned to make.

```bash
poetry run python tools/visualize_policy.py   --model ./logs/sb3_tensorboard/Your_Project_Name_1/final_model.zip   --config ./configs/sb3_board_game_config.yaml
```

This script runs a Monte Carlo analysis for each tile on the board, querying the agent's policy across many randomized game states to produce a "policy map" showing its most likely action in any given situation.
