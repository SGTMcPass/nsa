# run.py

import argparse
import yaml
import importlib
from pathlib import Path
from datetime import datetime
from typing import Any

from rl_project.config import Config
from rl_project.utils.logger import ConsoleLogger
from rl_project.interfaces.irunner import IRunner
from rl_project.interfaces.ienvironment_factory import IEnvironmentFactory

def dynamic_import(path: str) -> Any:
    """
    Dynamically imports a class from a string path.
    e.g., 'rl_project.utils.logger.ConsoleLogger' -> ConsoleLogger class
    """
    try:
        module_path, class_name = path.rsplit('.', 1)
        module = importlib.import_module(module_path)
        return getattr(module, class_name)
    except (ImportError, AttributeError) as e:
        raise ImportError(f"Could not import {path}: {e}")

def main():
    """
    Main execution function to run the RL training pipeline.
    """
    # 1. --- Argument Parsing ---
    parser = argparse.ArgumentParser(description="Run a reinforcement learning experiment.")
    parser.add_argument('--config', type=str, required=True, help="Path to the YAML configuration file.")
    args = parser.parse_args()

    config_path = Path(args.config)
    if not config_path.is_file():
        raise FileNotFoundError(f"Configuration file not found at: {config_path}")

    # 2. --- Configuration Loading ---
    with open(config_path, 'r') as f:
        config_dict = yaml.safe_load(f)
    
    config = Config(**config_dict)

    # 3. --- Component Initialization ---
    logger = ConsoleLogger()
    logger.log(f"Project: {config.project_name}")
    logger.log(f"Using backend: {config.runner.backend}")

    env_factory_class = dynamic_import(config.environment.factory_class)
    env_factory: IEnvironmentFactory = env_factory_class()
    
    # --- MODIFIED: Corrected runner instantiation logic ---
    if config.runner.backend == 'sb3':
        runner_class = dynamic_import("sb3_app.trainers.sb3_runner.StableBaselines3_Runner")
        # Note: The tensorboard_log_path is specific to our SB3 runner for now
        runner: IRunner = runner_class(
            config, 
            logger, 
            env_factory, 
            tensorboard_log_path=f"results/{config.project_name}_{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        )
    elif config.runner.backend == 'rllib':
        runner_class = dynamic_import("rl_project.trainers.rllib_runner.RLlib_Runner")
        runner: IRunner = runner_class(config, logger, env_factory)
    else:
        raise ValueError(f"Unsupported backend: {config.runner.backend}")


    # 4. --- Directory Setup ---
    # Moved directory creation into the SB3 runner logic since RLlib handles it internally
    logger.log(f"Results will be saved in the 'results' directory.")

    # 5. --- Execution ---
    try:
        logger.log("Starting training...")
        runner.train()
        logger.log("Training complete.")

        # Save logic can be handled inside the runner or called here
        # For now, let's assume the runner handles its own saving path internally
        # runner.save(str(model_save_path)) 
        # logger.log("Model saved successfully.")

    except Exception as e:
        logger.log(f"An error occurred during the run: {e}")
        raise

if __name__ == "__main__":
    main()