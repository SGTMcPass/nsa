import matplotlib.pyplot as plt


def plot_agent_path(grid_size, path, goal_state, save_path="output/agent_path.png"):
    """
    Plots the agent's path on a grid and saves it to a PNG.
    """
    width, height = grid_size

    # Create the grid
    fig, ax = plt.subplots()
    ax.set_xticks(range(width))
    ax.set_yticks(range(height))
    ax.grid(True)
    ax.invert_yaxis()

    # Plot the path
    x_vals = [pos[1] for pos in path]
    y_vals = [pos[0] for pos in path]
    ax.plot(x_vals, y_vals, marker="o", color="blue", label="Path")

    # Plot the start and goal
    ax.plot(x_vals[0], y_vals[0], marker="s", color="green", label="Start")
    ax.plot(goal_state[1], goal_state[0], marker="*", color="red", label="Goal")

    # Add labels
    ax.legend()
    plt.title("Agent Path Visualization")
    plt.savefig(save_path)
    plt.close()
