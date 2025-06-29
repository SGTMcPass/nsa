"""
A script for LIVE post-training analysis.

This script runs in a loop, periodically reading data from TensorBoard event files
and redrawing a plot to provide a live, custom visualization of training progress.
"""
import matplotlib
matplotlib.use('TkAgg')
import argparse
import os
import time
import pandas as pd
import matplotlib.pyplot as plt
from tensorboard.backend.event_processing import event_accumulator

def find_latest_run_dir(parent_dir: str) -> str:
    """Finds the most recently modified subdirectory in a parent log directory."""
    if not os.path.isdir(parent_dir):
        return parent_dir
    subdirs = [os.path.join(parent_dir, d) for d in os.listdir(parent_dir) if os.path.isdir(os.path.join(parent_dir, d))]
    if not subdirs:
        return parent_dir
    return max(subdirs, key=os.path.getmtime)

def plot_single_metric(ax, ea: event_accumulator.EventAccumulator, tag: str, smoothing_weights: list[float]):
    """Helper function to plot data for a single metric on a given axis."""
    if tag not in ea.Tags()['scalars']:
        ax.text(0.5, 0.5, f"Tag '{tag}' not found", ha='center', va='center')
        ax.set_title(f"Analysis of '{tag}'")
        ax.grid(True, which='both', linestyle='--', linewidth=0.5)
        return

    scalar_events = ea.Scalars(tag)
    df = pd.DataFrame([{'Step': ev.step, 'Value': ev.value} for ev in scalar_events])

    if df.empty:
        ax.text(0.5, 0.5, "No data points yet", ha='center', va='center')
        ax.set_title(f"Analysis of '{tag}'")
        ax.grid(True, which='both', linestyle='--', linewidth=0.5)
        return

    ax.plot(df['Step'], df['Value'], color='grey', alpha=0.3, label='Raw Data')
    for weight in smoothing_weights:
        alpha = 1 - weight
        smoothed_values = df['Value'].ewm(alpha=alpha).mean()
        ax.plot(df['Step'], smoothed_values, label=f'Smoothed ({weight})')

    ax.set_title(f"Analysis of '{tag}'")
    ax.set_xlabel('Training Timesteps')
    ax.set_ylabel(tag.split('/')[-1].replace('_', ' ').title())
    ax.legend()
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)

def live_plot_tensorboard(log_dir: str, tags: list[str], smoothing_weights: list[float], refresh_rate: int):
    """Continuously reads a TensorBoard log and updates plots for multiple metrics."""
    print("--- Live Plotter Initialized ---")
    print(f"Watching log directory: {log_dir}")
    print(f"Metrics to plot: {tags}")
    print(f"Refresh rate: {refresh_rate} seconds")
    print("Close the plot window to exit the script.")
    print("--------------------------------")

    plt.ion()
    fig, axes = plt.subplots(len(tags), 1, figsize=(15, 6 * len(tags)), sharex=True)
    if len(tags) == 1:
        axes = [axes]
    
    while True:
        try:
            ea = event_accumulator.EventAccumulator(log_dir)
            ea.Reload()
            
            for ax, tag in zip(axes, tags):
                ax.clear()
                plot_single_metric(ax, ea, tag, smoothing_weights)

            fig.suptitle(f"Live Analysis (last updated: {time.strftime('%H:%M:%S')})", fontsize=16)
            plt.tight_layout(rect=[0, 0.03, 1, 0.95])
            
            plt.pause(refresh_rate)
            
            if not plt.fignum_exists(fig.number):
                print("\nPlot window closed. Exiting script.")
                break

        except Exception as e:
            print(f"\nAn error occurred: {e}. Retrying in {refresh_rate} seconds...")
            time.sleep(refresh_rate)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Live plot metrics from a TensorBoard log file.")
    parser.add_argument("--log-dir", type=str, required=True, help="Path to the parent TensorBoard log directory.")
    parser.add_argument("--refresh-rate", type=int, default=30, help="How many seconds between plot updates.")
    args = parser.parse_args()
    
    latest_run_dir = find_latest_run_dir(args.log_dir)
    print(f"Found latest run directory: {latest_run_dir}")
    
    # --- MODIFIED: Changed the tag to plot the new metric ---
    tags_to_plot = ["rollout/ep_rew_mean", "rollout/ep_net_turns_spent_mean", "rollout/ep_points_mean"]
    smoothing_levels = [0.5, 0.8, 0.99]
    
    live_plot_tensorboard(latest_run_dir, tags_to_plot, smoothing_levels, args.refresh_rate)

