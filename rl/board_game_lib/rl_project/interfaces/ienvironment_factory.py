# rl_project/interfaces/ienvironment_factory.py

from abc import ABC, abstractmethod
import gymnasium as gym
from rl_project.utils.config import EnvironmentConfig

class IEnvironmentFactory(ABC):
    """Abstract interface for an environment factory."""

    @abstractmethod
    def create_env(self, config: EnvironmentConfig) -> gym.Env:
        """Creates and returns a Gymnasium environment based on the provided configuration."""
        pass