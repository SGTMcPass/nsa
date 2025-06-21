# rl_project/trainers/rllib_runner.py

import ray
from ray.rllib.algorithms.algorithm import Algorithm
from ray.rllib.algorithms.algorithm_config import AlgorithmConfig
from typing import Any, Dict, Type

# --- Import the SPECIFIC CONFIG classes, not the algorithms ---
from ray.rllib.algorithms.ppo import PPOConfig
from ray.rllib.algorithms.sac import SACConfig

from rl_project.interfaces.irunner import IRunner
from rl_project.interfaces.ienvironment_factory import IEnvironmentFactory
from rl_project.interfaces.ilogger import ILogger
from rl_project.config import Config

class RLlib_Runner(IRunner):
    """
    A concrete implementation of the IRunner interface using Ray RLlib.
    """

    def __init__(self, config: Config, logger: ILogger, env_factory: IEnvironmentFactory):
        self.config = config
        self.logger = logger
        self.env_factory = env_factory
        
        # --- This map now points to the CONFIG classes ---
        self._algorithm_config_map: Dict[str, Type[AlgorithmConfig]] = {
            "PPO": PPOConfig,
            "SAC": SACConfig,
        }
        
        if not ray.is_initialized():
            ray.init(logging_level="ERROR")
            self.logger.log("Ray cluster initialized.")
        
        self.logger.log("RLlib_Runner initialized.")
        self.algo: Algorithm = self._create_algorithm()

    # --- REWRITTEN with the correct, documented API pattern ---
    # In RLlib_Runner class

    # In RLlib_Runner class

    # In RLlib_Runner class

    def _create_algorithm(self) -> Algorithm:
        """Helper method to build the RLlib AlgorithmConfig and instantiate the algorithm."""
        
        env_class_path = self.config.environment.factory_class.replace("Factory", "Env")
        algo_name = self.config.runner.hyperparams.get("algorithm", "PPO")
        
        if algo_name not in self._algorithm_config_map:
            raise ValueError(f"Algorithm '{algo_name}' not supported by RLlib_Runner.")
        
        # Get the specific Config class, e.g., PPOConfig
        config_class = self._algorithm_config_map[algo_name]
        
        # Extract training parameters and handle special cases
        training_params = self.config.runner.hyperparams.get("params", {}).copy()
        render_env_flag = training_params.pop("render_env", False)
        rollout_fragment_length_val = training_params.pop("rollout_fragment_length", "auto")
        
        # This is the canonical, correct builder pattern
        config_obj = (
            config_class()
            .environment(
                env=env_class_path, 
                env_config=self.config.environment.params,
                render_env=render_env_flag
            )
            .framework("torch")
            .rollouts(
                num_rollout_workers=self.config.runner.hyperparams.get("num_rollout_workers", 1),
                rollout_fragment_length=rollout_fragment_length_val
            )
            .resources(
                num_gpus=1 if training_params.get("device") == "cuda" else 0
            )
            .training(**training_params)
        )

        self.logger.log(f"Building RLlib algorithm '{algo_name}' with config: {config_obj.to_dict()}")
        
        # The .build() method takes no arguments because the PPOConfig object
        # already knows it is supposed to build a PPO algorithm.
        return config_obj.build()

    # ... (The rest of the file: train, predict, save, load, remains unchanged) ...
    def train(self) -> None:
        """Executes the main training loop by iteratively calling algo.train()."""
        self.logger.log(f"Starting RLlib training for {self.config.runner.total_timesteps} total timesteps.")
        
        total_steps = 0
        while total_steps < self.config.runner.total_timesteps:
            try:
                result = self.algo.train()
                total_steps = result["timesteps_total"]
                
                log_data = {
                    "episode_reward_mean": result.get("episode_reward_mean", 0),
                    "episodes_total": result["episodes_total"],
                    "timesteps_total": total_steps
                }
                self.logger.log_dict(log_data, step=total_steps)
                
            except Exception as e:
                self.logger.log(f"An error occurred during RLlib training: {e}")
                raise
        
        self.logger.log("RLlib training completed successfully.")


    def predict(self, observation: Any, deterministic: bool = True) -> Any:
        if self.algo is None:
            self.logger.log("Error: RLlib algorithm has not been initialized.")
            return None
        return self.algo.compute_single_action(observation)

    def save(self, file_path: str) -> None:
        if self.algo is None:
            self.logger.log("No algorithm to save.")
            return
        checkpoint_dir = self.algo.save(checkpoint_dir=file_path)
        self.logger.log(f"Algorithm checkpoint saved to {checkpoint_dir}")

    def load(self, file_path: str) -> None:
        try:
            # For loading, we still use the base Algorithm class method
            self.algo = Algorithm.from_checkpoint(file_path)
            self.logger.log(f"Algorithm successfully restored from checkpoint {file_path}")
        except Exception as e:
            self.logger.log(f"Failed to load algorithm from checkpoint {file_path}: {e}")
            raise