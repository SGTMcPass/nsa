# sb3_app/trainers/sb3_runner.py

from typing import Any, Type, Dict
import os

from stable_baselines3.common.base_class import BaseAlgorithm
from stable_baselines3 import PPO, A2C, SAC, TD3
# --- Import the callback ---
from rl_project.utils.callback import RenderCallback

from rl_project.interfaces.irunner import IRunner
from rl_project.interfaces.ienvironment_factory import IEnvironmentFactory
from rl_project.interfaces.ilogger import ILogger
from rl_project.config import Config


class StableBaselines3_Runner(IRunner):
    """
    A concrete implementation of the IRunner interface using stable-baselines3.
    """

    def __init__(self, config: Config, logger: ILogger, env_factory: IEnvironmentFactory, tensorboard_log_path: str):
        # ... (init logic is unchanged) ...
        self.config = config
        self.logger = logger
        self.env_factory = env_factory
        self.tensorboard_log_path = tensorboard_log_path

        self.env = self.env_factory.create_env(self.config.environment)
        
        
        self.logger.log("StableBaselines3_Runner initialized.")
        
        self._algorithm_map: Dict[str, Type[BaseAlgorithm]] = {
            "PPO": PPO, "A2C": A2C, "SAC": SAC, "TD3": TD3
        }

        self.model: BaseAlgorithm = self._create_model()


    def _create_model(self) -> BaseAlgorithm:
        """Helper method to instantiate the SB3 model."""
        algo_name = self.config.runner.hyperparams.get("algorithm", "PPO")
        
        if algo_name not in self._algorithm_map:
            raise ValueError(f"Algorithm '{algo_name}' not supported by StableBaselines3_Runner.")
        
        algo_class = self._algorithm_map[algo_name]
        
        self.logger.log(f"Creating new SB3 model using {algo_name}.")

        # --- SAFER PARAMETER HANDLING ---
        
        # 1. Define the set of known, valid hyperparameters for SB3 models.
        #    (This can be expanded as needed)
        VALID_HYPERPARAMS = {
            "learning_rate", "n_steps", "batch_size", "n_epochs",
            "gamma", "gae_lambda", "clip_range", "ent_coef", "vf_coef",
            "max_grad_norm", "device"
        }

        # 2. Get the parameters from the config.
        config_params = self.config.runner.hyperparams.get("params", {})
        
        # 3. Build a clean dictionary of validated parameters.
        model_kwargs = {}
        for key, value in config_params.items():
            if key in VALID_HYPERPARAMS:
                model_kwargs[key] = value
            else:
                # Warn the user about a potential typo or unsupported parameter.
                self.logger.log(f"Warning: Ignoring unknown hyperparameter '{key}' from config.")
        
        # 4. Pass the validated keyword arguments to the constructor.
        return algo_class(
            policy=self.config.runner.policy,
            env=self.env,
            verbose=1 if self.config.runner.show_metrics_table else 0,
            tensorboard_log=self.tensorboard_log_path, # From our previous fix
            **model_kwargs  # Unpack the clean, validated dictionary
        )

    def train(self) -> None:
        """Executes the main training loop and saves the model upon completion."""
        self.logger.log(f"Starting training for {self.config.runner.total_timesteps} timesteps.")

        # --- MODIFIED: Conditionally create and use the RenderCallback ---
        active_callbacks = []
        # Check the config to see if rendering is enabled
        if self.config.environment.params.get("render_mode") == "human":
            # We import here to avoid a pygame dependency if rendering is not used
            # NOTE: You have an import for RenderCallback at the top of the file,
            # which is fine, but stable_baselines3's CallbackList should be imported here.
            from stable_baselines3.common.callbacks import CallbackList
            from rl_project.utils.callback import RenderCallback
            active_callbacks.append(RenderCallback())

        try:
            self.model.learn(
                total_timesteps=self.config.runner.total_timesteps,
                # Pass the list of callbacks (or None if empty)
                callback=CallbackList(active_callbacks) if active_callbacks else None,
                progress_bar=self.config.runner.show_progress_bar
            )
            self.logger.log("Training completed successfully.")

            # --- FIX: ADD THIS SECTION TO SAVE THE MODEL ---
            self.logger.log("Saving final model...")
            # We construct a path inside the unique TensorBoard log directory
            model_save_path = os.path.join(self.tensorboard_log_path, "final_model")
            self.save(model_save_path)
            # -----------------------------------------------

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

        # Ensure directory exists
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
            self.model = algo_class.load(file_path, env=self.env)
            self.logger.log(f"Model successfully loaded from {file_path}")
        except Exception as e:
            self.logger.log(f"Failed to load model from {file_path}: {e}")
            raise
