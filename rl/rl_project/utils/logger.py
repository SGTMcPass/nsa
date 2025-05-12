# utils/logger.py
import logging
import os


class RLLogger:
    """
    RLLogger handles logging of important events, suppresses non-critical
    output from the terminal, and saves logs to a file for detailed inspection.
    """

    def __init__(self, log_file="output/training_log.log", level=logging.INFO):
        """
        Initializes the RLLogger.

        Parameters:
        - log_file (str): Path to the log file.
        - level (int): Logging level, default is INFO.
        """
        self.logger = logging.getLogger("RLLogger")
        self.logger.setLevel(level)

        # ✅ Ensure the output directory exists
        directory = os.path.dirname(log_file)
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        # ✅ Create a file handler to write logs to a file
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(level)

        # ✅ Create a console handler for warnings and errors
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.WARNING)

        # ✅ Define the format for logs
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # ✅ Add handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)
