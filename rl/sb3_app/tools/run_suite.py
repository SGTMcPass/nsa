# sb3_app/run_suite.py

import argparse
import subprocess
import sys
from pathlib import Path

def run_suite(config_path: Path):
    """
    Finds and runs all .yaml configurations in a specified path.
    If the path is a file, it runs that single config.
    If the path is a directory, it runs all configs in that directory.
    """
    if not config_path.exists():
        print(f"❌ Error: Path does not exist: {config_path.resolve()}")
        sys.exit(1)

    if config_path.is_file() and config_path.suffix in ['.yaml', '.yml']:
        config_files = [config_path]
    elif config_path.is_dir():
        config_files = list(config_path.glob("*.yaml"))
        config_files.extend(list(config_path.glob("*.yml")))
    else:
        print(f"❌ Error: Path is not a valid YAML file or directory: {config_path.resolve()}")
        sys.exit(1)

    if not config_files:
        print(f"Info: No .yaml or .yml configuration files found in '{config_path}'.")
        return

    print(f"--- Found {len(config_files)} configuration(s) to run in '{config_path.name}' ---")
    print("-" * 30)

    failed_runs = []
    successful_runs = 0

    for config_file_path in config_files:
        print(f"▶️ Running experiment for: {config_file_path.name}")

        # --- CORRECTED COMMAND ---
        # This now matches the argument parser of your run_sb3.py script,
        # which expects a single '--config' argument.
        command = [
            "python",
            "-m",
            "sb3_app.trainers.run_sb3",
            "--config",
            str(config_file_path),  # Pass the full path to the config file
        ]

        try:
            subprocess.run(command, check=True, text=True)
            print(f"✅ Successfully completed experiment: {config_file_path.name}")
            successful_runs += 1
        except subprocess.CalledProcessError as e:
            print(f"❌ ERROR: Experiment '{config_file_path.name}' failed with exit code {e.returncode}.")
            failed_runs.append(config_file_path.name)
        
        print("-" * 30)

    print(f"--- Suite Finished for '{config_path.name}' ---")
    print(f"Total Successful Runs: {successful_runs}")
    if failed_runs:
        print(f"Total Failed Runs: {len(failed_runs)}")
        print("Failed configurations:")
        for run_name in failed_runs:
            print(f"  - {run_name}")
    else:
        print("All experiments completed successfully!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run a suite of RL experiments from a directory of config files."
    )
    parser.add_argument(
        "config_path",
        type=Path,
        help="Path to a single .yaml config file or a directory containing .yaml files."
    )
    args = parser.parse_args()
    
    run_suite(args.config_path)
