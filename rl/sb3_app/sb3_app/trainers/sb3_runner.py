# sb3_app/trainers/sb3_runner.py

from typing import Any, Type, Dict, Callable
import os
from functools import partial

from stable_baselines3.common.base_class import BaseAlgorithm
from stable_baselines3 import PPO, A2C, SAC, TD3
from stable_baselines3.common.vec_env import SubprocVecEnv
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.callbacks import CallbackList

# --- Import all necessary callbacks ---
from rl_project.utils.callback import RenderCallback, AnnealingCallback, CustomMetricsCallback

from rl_project.interfaces.irunner import IRunner
# --- CORRECTED IMPORT PATH ---
from rl_project.interfaces.ienvironment_factory import IEnvironmentFactory
from rl_project.interfaces.ilogger import ILogger
from rl_project.config import Config


class StableBaselines3_Runner(IRunner):
    """
    A concrete implementation of the IRunner interface using stable-baselines3.
    """

    def __init__(self, config: Config, logger: ILogger, env_factory: IEnvironmentFactory):
        self.config = config
        self.logger = logger
        self.env_factory = env_factory
        
        self.tensorboard_log_path = os.path.join(
            self.config.runner.tensorboard_log, self.config.project_name
        )

        num_envs = self.config.runner.num_envs
        env_creator = partial(self.env_factory.create_env, config=self.config.environment)

        if num_envs > 1:
            self.logger.log(f"Creating {num_envs} parallel environments.")
            self.env = make_vec_env(env_creator, n_envs=num_envs, vec_env_cls=SubprocVecEnv)
        else:
            self.logger.log("Creating a single environment.")
            self.env = env_creator()
        
        self.logger.log("StableBaselines3_Runner initialized.")
        
        self._algorithm_map: Dict[str, Type[BaseAlgorithm]] = {
            "PPO": PPO, "A2C": A2C, "SAC": SAC, "TD3": TD3
        }

        self.model: BaseAlgorithm = self._create_model()


    def _create_model(self) -> BaseAlgorithm:
        """Helper method to instantiate the SB3 model."""
        
        def linear_schedule(initial_value: float) -> Callable[[float], float]:
            def func(progress_remaining: float) -> float:
                return progress_remaining * initial_value
            return func

        algo_name = self.config.runner.hyperparams.get("algorithm", "PPO")
        
        if algo_name not in self._algorithm_map:
            raise ValueError(f"Algorithm '{algo_name}' not supported by StableBaselines3_Runner.")
        
        algo_class = self._algorithm_map[algo_name]
        
        self.logger.log(f"Creating new SB3 model using {algo_name}.")

        VALID_HYPERPARAMS = {
            "learning_rate", "n_steps", "batch_size", "n_epochs",
            "gamma", "gae_lambda", "clip_range", "ent_coef", "vf_coef",
            "max_grad_norm", "device"
        }

        config_params = self.config.runner.hyperparams.get("params", {})
        
        model_kwargs = {}
        for key, value in config_params.items():
            if key in VALID_HYPERPARAMS:
                model_kwargs[key] = value
            else:
                self.logger.log(f"Warning: Ignoring unknown hyperparameter '{key}' from config.")
        
        policy_kwargs = self.config.runner.hyperparams.get("policy_kwargs", {})
        if policy_kwargs:
            self.logger.log(f"Applying custom policy_kwargs: {policy_kwargs}")

        if self.config.runner.anneal_lr:
            if "learning_rate" in model_kwargs:
                initial_lr = model_kwargs["learning_rate"]
                self.logger.log(f"Applying linear learning rate annealing from {initial_lr} to 0.")
                model_kwargs["learning_rate"] = linear_schedule(initial_lr)
        
        return algo_class(
            policy=self.config.runner.policy,
            env=self.env,
            verbose=1 if self.config.runner.show_metrics_table else 0,
            tensorboard_log=self.tensorboard_log_path,
            policy_kwargs=policy_kwargs,
            **model_kwargs
        )

    def train(self) -> None:
        """Executes the main training loop and saves the model upon completion."""
        self.logger.log(f"Starting training for {self.config.runner.total_timesteps} timesteps.")

        active_callbacks = []
        if self.config.environment.params.get("render_mode") == "human":
            active_callbacks.append(RenderCallback())

        if self.config.runner.anneal_entropy:
            if hasattr(self.model, "ent_coef") and self.model.ent_coef is not None:
                 initial_ent = self.model.ent_coef
                 self.logger.log(f"Activating entropy annealing callback, starting from {initial_ent}.")
                 active_callbacks.append(AnnealingCallback(initial_value=initial_ent))

        self.logger.log("Activating custom metrics logger.")
        active_callbacks.append(CustomMetricsCallback(log_freq=1000))

        try:
            self.model.learn(
                total_timesteps=self.config.runner.total_timesteps,
                callback=CallbackList(active_callbacks) if active_callbacks else None,
                progress_bar=self.config.runner.show_progress_bar
            )
            self.logger.log("Training completed successfully.")

            self.logger.log("Saving final model...")
            model_save_path = os.path.join(self.tensorboard_log_path, "final_model.zip")
            self.save(model_save_path)

        except Exception as e:
            self.logger.log(f"An error occurred during training: {e}")
            raise

    def predict(self, observation: Any, deterministic: bool = True) -> Any:
        """Performs inference using the trained SB3 model."""
        if self.model is None:
            self.logger.log("Error: Model has not been initialized or loaded.")
            return None
            
        action, _states = self.model.predict(observation, deterministic=deterministic)
        return action

    def save(self, file_path: str) -> None:
        """Saves the trained SB3 model."""
        if self.model is None:
            self.logger.log("No model to save.")
            return

        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        self.model.save(file_path)
        self.logger.log(f"Model saved to {file_path}")

    def load(self, file_path: str) -> None:
        """Loads a pre-trained SB3 model."""
        algo_name = self.config.runner.hyperparams.get("algorithm", "PPO")
        if algo_name not in self._algorithm_map:
            raise ValueError(f"Cannot load model: Algorithm '{algo_name}' not supported.")

        algo_class = self._algorithm_map[algo_name]
        
        try:
            if self.config.runner.pretrained_model_path:
                self.logger.log(f"Loading pre-trained model from: {self.config.runner.pretrained_model_path}")
                self.model = algo_class.load(self.config.runner.pretrained_model_path, env=self.env)
            else:
                 self.model = algo_class.load(file_path, env=self.env)
            self.logger.log(f"Model successfully loaded from {file_path}")
        except Exception as e:
            self.logger.log(f"Failed to load model from {file_path}: {e}")
            raise

