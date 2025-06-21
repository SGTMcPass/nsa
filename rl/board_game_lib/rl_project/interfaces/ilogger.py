# rl_project/interfaces/ilogger.py

from abc import ABC, abstractmethod

class ILogger(ABC):
    """Abstract interface for a logger."""

    @abstractmethod
    def log(self, message: str) -> None:
        """Logs a message."""
        pass

    @abstractmethod
    def log_dict(self, data: dict, step: int) -> None:
        """Logs a dictionary of key-value pairs at a given step, useful for metrics."""
        pass