# rl/rl_project/environments/board_game_factory.py

import gymnasium as gym
from rl_project.interfaces.ienvironment_factory import IEnvironmentFactory
from rl_project.config import EnvironmentConfig
from rl_project.environments.board_game_env import BoardGameEnv

class BoardGameFactory(IEnvironmentFactory):
    """Factory for creating the BoardGameEnv."""

    def create_env(self, config: EnvironmentConfig) -> gym.Env:
        """
        Creates and returns a BoardGameEnv instance.
        
        The 'params' in the config can be used to pass arguments
        like 'goal_points' or 'initial_turns'.
        """
        env_params = config.params.copy()
        render_mode = env_params.pop("render_mode", None)
        return BoardGameEnv(**config.params)
