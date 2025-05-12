# trainers/checkpoint_manager.py
import os
import pickle


class CheckpointManager:
    """
    CheckpointManager handles saving and loading of Q-tables to and from disk.
    """

    def __init__(self, save_path="output/q_table_checkpoint.pkl"):
        """
        Initializes the CheckpointManager with a specified save path.

        Parameters:
        - save_path (str): Path to save or load the Q-table.
        """
        self.save_path = save_path

        # ✅ Create the output directory if it doesn't exist
        directory = os.path.dirname(save_path)
        if not os.path.exists(directory):
            print(f"🛠️ Creating directory: {directory}")
            os.makedirs(directory, exist_ok=True)

    def save(self, q_table):
        """
        Saves the Q-table to disk using pickle.

        Parameters:
        - q_table (dict): The agent's Q-table to be saved.
        """
        try:
            with open(self.save_path, "wb") as f:
                pickle.dump(q_table, f)
            print(f"✅ Q-table successfully saved to {self.save_path}")
        except Exception as e:
            print(f"❌ Failed to save Q-table: {e}")

    def load(self):
        """
        Loads the Q-table from disk if it exists.

        Returns:
        - dict: The loaded Q-table, or an empty dictionary if not found.
        """
        if os.path.exists(self.save_path):
            try:
                with open(self.save_path, "rb") as f:
                    q_table = pickle.load(f)
                print(f"✅ Q-table successfully loaded from {self.save_path}")
                return q_table
            except Exception as e:
                print(f"❌ Failed to load Q-table: {e}")
                return {}
        else:
            print("⚠️ No checkpoint found. Starting with an empty Q-table.")
            return {}
