# rl_project/interfaces/irunner.py

from abc import ABC, abstractmethod
from typing import Any
from rl_project.utils.config import Config
from rl_project.interfaces.ienvironment_factory import IEnvironmentFactory
from rl_project.interfaces.ilogger import ILogger


class IRunner(ABC):
    """Abstract interface for a reinforcement learning training runner."""

    @abstractmethod
    def __init__(self, config: Config, logger: ILogger, env_factory: IEnvironmentFactory):
        """
        Initializes the runner with the main configuration, a logger, and an environment factory.
        """
        pass

    @abstractmethod
    def train(self) -> None:
        """
        Executes the main training loop.
        """
        pass

    @abstractmethod
    def predict(self, observation: Any, deterministic: bool = True) -> Any:
        """
        Performs inference using the trained model on a single observation.

        Returns:
            The action determined by the policy.
        """
        pass

    @abstractmethod
    def save(self, file_path: str) -> None:
        """
        Saves the state of the trained agent to a file.
        
        Args:
            file_path: The path (directory or file) to save the model to.
        """
        pass

    @abstractmethod
    def load(self, file_path: str) -> None:
        """
        Loads the state of a trained agent from a file.

        Args:
            file_path: The path (directory or file) to load the model from.
        """
        pass