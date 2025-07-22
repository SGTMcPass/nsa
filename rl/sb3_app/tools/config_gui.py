# sb3_app/config_gui.py

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path
from ruamel.yaml import YAML
import copy

# --- Configuration ---
CONFIG_DIR = Path("./configs/education")
DEFAULT_BASELINE_FILE = CONFIG_DIR / "sb3_updated_baseline.yaml"
MAX_LAYERS = 4 

class ConfigEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RL Config Editor")
        self.root.geometry("450x650")

        self.yaml = YAML()
        self.yaml.preserve_quotes = True
        self.file_path = None
        self.data = None

        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.file_label = ttk.Label(self.main_frame, text="No file loaded.")
        self.file_label.pack(pady=5)
        self.load_button = ttk.Button(self.main_frame, text="Load Baseline Config", command=self.load_file)
        self.load_button.pack(pady=5)
        
        ttk.Separator(self.main_frame, orient='horizontal').pack(fill='x', pady=10)

        self.editors_frame = ttk.Frame(self.main_frame)
        self.editors_frame.pack(fill=tk.X)

        self.entries = {}
        self.create_section_label("Algorithm Hyperparameters")
        self.create_editor("Learning Rate", "runner.hyperparams.params.learning_rate")
        self.create_editor("Gamma", "runner.hyperparams.params.gamma")
        
        self.create_section_label("Environment Goal")
        self.create_editor("Goal Points", "environment.params.goal_points")
        self.create_editor("Initial Turns", "environment.params.initial_resources.initial_turns")
        self.create_editor("Total Timesteps", "runner.total_timesteps")

        self.create_section_label("Reward Weights")
        self.create_editor("Points Weight", "environment.params.reward_weights.points")
        self.create_editor("Turn Penalty", "environment.params.reward_weights.turn_penalty")
        self.create_editor("Goal Miss Penalty", "environment.params.reward_weights.goal_miss_penalty")
        
        self.create_section_label("Neural Network Architecture")
        self.net_arch_entries = {'pi': [], 'vf': []}
        self.create_net_arch_editors("Policy (pi)", 'pi')
        self.create_net_arch_editors("Value (vf)", 'vf')

        ttk.Separator(self.main_frame, orient='horizontal').pack(fill='x', pady=10)
        self.save_button = ttk.Button(self.main_frame, text="Save Current File", command=self.save_file, state=tk.DISABLED)
        self.save_button.pack(pady=5)
        
        self.bulk_update_button = ttk.Button(
            self.main_frame, 
            text="Apply to All Education Configs", 
            command=self.bulk_update_hook, 
            state=tk.DISABLED
        )
        self.bulk_update_button.pack(pady=5)

    def create_section_label(self, text):
        label = ttk.Label(self.editors_frame, text=text, font=('TkDefaultFont', 10, 'bold'))
        label.pack(fill=tk.X, pady=(10, 2))

    def create_editor(self, label_text, param_path):
        frame = ttk.Frame(self.editors_frame)
        frame.pack(fill=tk.X, pady=2)
        label = ttk.Label(frame, text=f"{label_text}:", width=18)
        label.pack(side=tk.LEFT, padx=5)
        entry = ttk.Entry(frame)
        entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.entries[param_path] = entry

    def create_net_arch_editors(self, section_label, net_type):
        section_frame = ttk.Frame(self.editors_frame)
        section_frame.pack(fill=tk.X, pady=2)
        label = ttk.Label(section_frame, text=f"{section_label}:", width=18)
        label.pack(side=tk.LEFT, padx=5)
        
        for i in range(MAX_LAYERS):
            entry = ttk.Entry(section_frame, width=6)
            entry.pack(side=tk.LEFT, padx=2)
            self.net_arch_entries[net_type].append(entry)

    def load_file(self):
        self.file_path = DEFAULT_BASELINE_FILE
        if not self.file_path.exists():
            messagebox.showerror("Error", f"Baseline file not found at:\n{self.file_path.resolve()}")
            return

        try:
            with open(self.file_path, 'r') as f:
                self.data = self.yaml.load(f)
            
            self.file_label.config(text=f"Loaded: {self.file_path.name}")
            
            for path, entry in self.entries.items():
                entry.delete(0, tk.END)
                try:
                    value = self.get_nested_value(path)
                    entry.insert(0, str(value))
                except KeyError:
                    entry.insert(0, "Not Found")
            
            self.load_net_arch()
            
            self.save_button.config(state=tk.NORMAL)
            self.bulk_update_button.config(state=tk.NORMAL)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load or parse YAML file.\nError: {e}")

    def load_net_arch(self):
        try:
            net_arch_data = self.get_nested_value("runner.hyperparams.policy_kwargs.net_arch")
            for net_type in ['pi', 'vf']:
                for entry in self.net_arch_entries[net_type]:
                    entry.delete(0, tk.END)
                if net_type in net_arch_data:
                    for i, layer_size in enumerate(net_arch_data[net_type]):
                        if i < MAX_LAYERS:
                            self.net_arch_entries[net_type][i].insert(0, str(layer_size))
        except KeyError:
            pass

    def save_file(self, show_success_msg=True):
        if not self.data or not self.file_path:
            if show_success_msg:
                messagebox.showerror("Error", "No file loaded to save.")
            return False

        try:
            for path, entry in self.entries.items():
                new_value_str = entry.get()
                self.set_nested_value(path, new_value_str)
            
            self.save_net_arch()
            
            with open(self.file_path, 'w') as f:
                self.yaml.dump(self.data, f)
            
            if show_success_msg:
                messagebox.showinfo("Success", f"File '{self.file_path.name}' saved successfully.")
            return True
        except Exception as e:
            if show_success_msg:
                messagebox.showerror("Error", f"Failed to save file.\nError: {e}")
            return False
            
    def save_net_arch(self):
        new_net_arch = self.get_net_arch_from_ui()
        self.set_nested_value("runner.hyperparams.policy_kwargs.net_arch", new_net_arch, is_structured=True)

    def get_net_arch_from_ui(self):
        """Constructs a net_arch dictionary from the current UI fields."""
        net_arch = {}
        for net_type in ['pi', 'vf']:
            layer_sizes = []
            for entry in self.net_arch_entries[net_type]:
                value_str = entry.get()
                if value_str.strip():
                    try:
                        layer_sizes.append(int(value_str))
                    except ValueError:
                        messagebox.showerror("Input Error", f"Invalid number for layer size: '{value_str}'")
                        raise
            net_arch[net_type] = layer_sizes
        return net_arch

    def bulk_update_hook(self):
        # First, ensure the baseline file is saved with the current UI values
        if not self.save_file(show_success_msg=False):
            messagebox.showerror("Error", "Could not save baseline file before applying changes. Aborting.")
            return

        # --- Get New Baseline Values from UI ---
        baseline_lr = float(self.entries["runner.hyperparams.params.learning_rate"].get())
        baseline_net_arch = self.get_net_arch_from_ui()
        
        if not messagebox.askyesno("Confirm Bulk Update", "This will apply the current baseline settings to all other education configs according to the defined logic. Proceed?"):
            messagebox.showinfo("Cancelled", "Bulk update cancelled.")
            return
        
        all_configs = [p for p in CONFIG_DIR.glob("*.yaml") if p.resolve() != self.file_path.resolve()]
        updated_count, failed_count = 0, 0

        for config_file in all_configs:
            try:
                with open(config_file, 'r') as f:
                    data = self.yaml.load(f)
                
                # --- Apply Foundational Parameters ---
                self.set_nested_value("environment.params.goal_points", self.entries["environment.params.goal_points"].get(), data_source=data)
                self.set_nested_value("environment.params.initial_resources.initial_turns", self.entries["environment.params.initial_resources.initial_turns"].get(), data_source=data)
                self.set_nested_value("runner.total_timesteps", self.entries["runner.total_timesteps"].get(), data_source=data)
                self.set_nested_value("runner.hyperparams.policy_kwargs.net_arch", baseline_net_arch, is_structured=True, data_source=data)
                
                # --- Apply Test-Case Specific Logic ---
                filename = config_file.name
                if filename == "aggressive.yaml":
                    self.set_nested_value("runner.hyperparams.params.learning_rate", baseline_lr * 3.33, data_source=data)
                elif filename == "cautious.yaml":
                    self.set_nested_value("runner.hyperparams.params.learning_rate", baseline_lr * 0.1, data_source=data)
                elif filename == "farsighted.yaml":
                    self.set_nested_value("runner.hyperparams.params.gamma", 0.999, data_source=data)
                elif filename == "short-sighted.yaml":
                    self.set_nested_value("runner.hyperparams.params.gamma", 0.9, data_source=data)
                elif filename == "uninspired.yaml":
                    self.set_nested_value("runner.hyperparams.params.ent_coef", 0.0, data_source=data)
                elif filename == "frequent_stops.yaml":
                    self.set_nested_value("runner.hyperparams.params.n_steps", 256, data_source=data)
                elif filename == "infrequent_stops.yaml":
                    self.set_nested_value("runner.hyperparams.params.n_steps", 8192, data_source=data)
                elif filename == "high_intensity.yaml":
                    self.set_nested_value("runner.hyperparams.params.n_epochs", 20, data_source=data)
                    self.set_nested_value("runner.hyperparams.params.batch_size", 64, data_source=data)
                elif filename == "low_intensity.yaml":
                    self.set_nested_value("runner.hyperparams.params.n_epochs", 3, data_source=data)
                    self.set_nested_value("runner.hyperparams.params.batch_size", 512, data_source=data)
                elif filename in ["point_hoarder.yaml", "speed_runner.yaml", "no_fear.yaml"]:
                    # These have unique reward structures that are preserved
                    pass 
                elif filename == "genius.yaml":
                    genius_arch = copy.deepcopy(baseline_net_arch)
                    for net in ['pi', 'vf']:
                        genius_arch[net] = [layer * 2 for layer in genius_arch[net]]
                        if genius_arch[net]:
                            genius_arch[net].append(genius_arch[net][-1] // 2)
                    self.set_nested_value("runner.hyperparams.policy_kwargs.net_arch", genius_arch, is_structured=True, data_source=data)
                elif filename == "einstein.yaml":
                    genius_arch = copy.deepcopy(baseline_net_arch)
                    for net in ['pi', 'vf']:
                        genius_arch[net] = [layer * 2 for layer in genius_arch[net]]
                        if genius_arch[net]:
                            genius_arch[net].append(genius_arch[net][-1] // 2)
                    einstein_arch = copy.deepcopy(genius_arch)
                    for net in ['pi', 'vf']:
                        einstein_arch[net] = [layer * 2 for layer in einstein_arch[net]]
                    self.set_nested_value("runner.hyperparams.policy_kwargs.net_arch", einstein_arch, is_structured=True, data_source=data)


                # Save the modified file
                with open(config_file, 'w') as f:
                    self.yaml.dump(data, f)
                updated_count += 1

            except Exception as e:
                print(f"Failed to update {config_file.name}: {e}")
                failed_count += 1

        messagebox.showinfo("Complete", f"Bulk update finished.\n\nSuccessfully updated: {updated_count} files.\nFailed: {failed_count} files.")


    def get_nested_value(self, param_path, data_source=None):
        if data_source is None:
            data_source = self.data
        keys = param_path.split('.')
        value = data_source
        for key in keys:
            value = value[key]
        return value

    def set_nested_value(self, param_path, new_value, is_structured=False, data_source=None):
        if data_source is None:
            data_source = self.data
        keys = param_path.split('.')
        current_level = data_source
        for key in keys[:-1]:
            current_level = current_level[key]
        
        if is_structured:
            processed_value = new_value
        else:
            try:
                processed_value = float(new_value)
                if processed_value.is_integer():
                    processed_value = int(processed_value)
            except ValueError:
                processed_value = new_value
        
        current_level[keys[-1]] = processed_value


if __name__ == "__main__":
    root = tk.Tk()
    app = ConfigEditorApp(root)
    root.mainloop()
