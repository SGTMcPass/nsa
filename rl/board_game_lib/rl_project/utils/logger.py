# rl/rl_project/utils/logger.py

import datetime
from rl_project.interfaces.ilogger import ILogger

class ConsoleLogger(ILogger):
    """A simple concrete logger that prints to the console."""

    def log(self, message: str) -> None:
        """Logs a message to the console with a timestamp."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] {message}")

    def log_dict(self, data: dict, step: int) -> None:
        """Logs key-value pairs from a dictionary."""
        self.log(f"Step: {step} | Metrics: {data}")