"""
A script for post-training policy analysis and visualization.

This script loads a trained agent and its corresponding environment config.
It then iterates through each tile on the board, constructs a standardized
observation for that tile, and queries the agent's deterministic policy
to determine the "ideal" action. Finally, it prints a map of the board
showing the agent's preferred action for each tile.
"""
import argparse
import yaml
from pathlib import Path
import numpy as np
from stable_baselines3 import PPO
from collections import OrderedDict

# We need to import the environment directly to inspect its properties
from rl_project.environments.board_game_env import BoardGameEnv, TILE_TYPE_MAP
from rl_project.config import Config

def analyze_policy(model_path: str, config_path: str):
    """
    Loads a model and generates a strategic map of its preferred actions.

    Args:
        model_path: Path to the saved agent model (.zip file).
        config_path: Path to the corresponding YAML configuration file.
    """
    print(f"Loading model from: {model_path}")
    print(f"Loading config from: {config_path}")

    # 1. --- Load Configuration and Model ---
    with open(config_path, 'r') as f:
        config_dict = yaml.safe_load(f)
    config = Config(**config_dict)

    # Load the trained PPO model
    model = PPO.load(model_path)

    # 2. --- Recreate Board Information ---
    # We instantiate the environment once to get the board layout details
    temp_env = BoardGameEnv(**config.environment.params.dict())
    num_tiles = len(temp_env._board)
    tile_types = [tile.__class__.__name__ for tile in temp_env._board]
    multipliers = temp_env._multipliers
    del temp_env # We don't need the instance anymore

    print("\n--- Generating Strategic Map ---")
    print("Querying agent for the ideal action at each tile, assuming all multipliers are available.")

    # 3. --- Define a Standardized State for Querying the Agent ---
    # We create a hypothetical "average" game state to see what the agent
    # would do under normal conditions.
    standard_state = {
        "turns_remaining": 100,  # A high number to ensure all multipliers are valid
        "turns_done": 50,
    }
    # Add observed resources with a default value of 0 if not in standard_state
    for res in config.environment.params.observed_resources:
        if res not in standard_state:
            standard_state[res] = 0

    policy_map = []
    for i in range(num_tiles):
        # 4. --- Construct the Observation for the Current Tile ---
        
        # Build the core observation vector based on the standard state
        obs_values = [
            i, # The current tile position
            standard_state["turns_remaining"],
            standard_state["turns_done"],
        ]
        obs_values.extend(standard_state.get(key, 0) for key in config.environment.params.observed_resources)
        
        obs_vec = np.array(obs_values, dtype=np.float32)

        # Create a full action mask where all actions are unlocked
        action_mask = np.ones(6, dtype=np.int8)

        # Combine into the dictionary format the model expects
        observation = OrderedDict([
            ("obs", obs_vec),
            ("action_mask", action_mask),
        ])

        # 5. --- Query the Model for the Best Action ---
        # `deterministic=True` asks for the single best action, not a random sample.
        action, _ = model.predict(observation, deterministic=True)
        
        # Map the action index to a human-readable string
        if action < len(multipliers):
            action_str = f"x{multipliers[action]} Multiplier"
        else:
            action_str = "Buy Turns"
            
        policy_map.append((i, tile_types[i], action_str))

    # 6. --- Display the Results ---
    print("\n--- Board Policy Map ---")
    print("=====================================================")
    print(f"{'Tile #':<8} | {'Tile Type':<18} | {'Ideal Action'}")
    print("-----------------------------------------------------")
    for tile_num, tile_type, action_str in policy_map:
        print(f"{tile_num:<8} | {tile_type:<18} | {action_str}")
    print("=====================================================")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze and display the learned policy of an RL agent.")
    parser.add_argument(
        "--model",
        type=str,
        required=True,
        help="Path to the trained agent model (.zip file)."
    )
    parser.add_argument(
        "--config",
        type=str,
        required=True,
        help="Path to the corresponding YAML environment config file."
    )
    args = parser.parse_args()
    
    analyze_policy(args.model, args.config)

