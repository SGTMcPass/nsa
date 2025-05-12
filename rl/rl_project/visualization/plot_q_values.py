import matplotlib.pyplot as plt
import numpy as np


def plot_q_values(agent, grid_size, save_path="output/q_values_heatmap.png"):
    """
    Plots a heatmap of the maximum Q-values for each state in the grid and saves it.
    """
    width, height = grid_size

    # Initialize a 2D array for Q-values
    q_values_grid = np.zeros((height, width))

    # Populate the grid with maximum Q-values
    for state, actions in agent.q_table.items():
        max_q = max(actions.values())  # Get the best action's Q-value
        if 0 <= state[0] < height and 0 <= state[1] < width:
            q_values_grid[state[0], state[1]] = max_q

    # Plot the heatmap
    plt.figure(figsize=(5, 5))
    plt.imshow(q_values_grid, cmap="hot", interpolation="nearest")
    plt.colorbar(label="Q-Value Intensity")
    plt.title("Q-Value Heatmap of Agent Learning")
    plt.savefig(save_path)
    plt.close()
