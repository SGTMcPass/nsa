"""
Custom callbacks for the RL project.
"""
import numpy as np
import psutil
from stable_baselines3.common.callbacks import BaseCallback

class RenderCallback(BaseCallback):
    """
    A custom callback to render the environment during training.
    """
    def _on_step(self) -> bool:
        # get_attr() is used for vectorized environments
        if self.training_env.get_attr("render_mode")[0] == "human":
            self.training_env.render()
        return True

class AnnealingCallback(BaseCallback):
    """
    A custom callback to anneal a hyperparameter, such as the entropy coefficient.
    """
    def __init__(self, initial_value: float, verbose: int = 0):
        super().__init__(verbose)
        self.initial_value = initial_value

    def _on_step(self) -> bool:
        # self.model._current_progress_remaining goes from 1.0 to 0.0 over training
        progress = self.model._current_progress_remaining
        self.model.ent_coef = progress * self.initial_value
        return True

class CustomMetricsCallback(BaseCallback):
    """
    A custom callback to log system metrics and episodic info to TensorBoard.
    """
    def __init__(self, log_freq: int = 1000, verbose: int = 0):
        super().__init__(verbose)
        self.log_freq = log_freq
        # Initialize psutil to start measuring CPU usage
        psutil.cpu_percent(interval=None, percpu=True)

    def _on_step(self) -> bool:
        # Log system metrics every 'log_freq' steps
        if self.n_calls % self.log_freq == 0:
            cpu_percents = psutil.cpu_percent(interval=None, percpu=True)
            for i, cpu_percent in enumerate(cpu_percents):
                self.logger.record(f'sys/cpu_{i+1}_percent', cpu_percent)

        # Check if any environments finished an episode on this step
        # self.locals['dones'] is a numpy array of booleans for each parallel env
        dones = self.locals['dones']
        if any(dones):
            # Iterate through the infos from each environment
            for i, info in enumerate(self.locals['infos']):
                # Check if this specific environment is done
                if dones[i]:
                    # If an episode is done, log the final values from its info dict
                    
                    # --- MODIFIED: Log the correct net_turns_spent value ---
                    if 'net_turns_spent' in info:
                        self.logger.record('rollout/ep_net_turns_spent_mean', info['net_turns_spent'])
                    # --------------------------------------------------------

                    if 'points' in info:
                        self.logger.record('rollout/ep_points_mean', info['points'])
        return True

