# visualization/path_animator.py
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
import os


class PathAnimator:
    """
    PathAnimator: A class to animate the agent's path in the environment.

    This class takes the agent's path, obstacle locations, and the goal state,
    and generates an animated GIF to visualize the agent's decision-making process.
    """

    def __init__(
        self, grid_size, path, obstacles, goal, save_path="output/agent_animation.gif"
    ):
        """
        Initializes the PathAnimator object.

        Parameters:
        - grid_size (tuple): The (width, height) of the grid environment.
        - path (list): A list of (x, y) tuples representing the agent's path.
        - obstacles (set): A set of (x, y) tuples representing obstacle positions.
        - goal (tuple): The (x, y) coordinates of the goal state.
        - save_path (str): The file path to save the animated GIF.
        """
        self.grid_size = grid_size
        self.path = path
        self.obstacles = obstacles
        self.goal = goal
        self.save_path = save_path

        # ✅ Create the output directory if it doesn't exist
        directory = os.path.dirname(save_path)
        if not os.path.exists(directory):
            print(f"🛠️ Creating directory: {directory}")
            os.makedirs(directory, exist_ok=True)

    def animate(self):
        """
        Generates an animated GIF of the agent's pathfinding process.
        """
        # 🚀 Check if path is valid
        if not self.path or len(self.path) == 0:
            print("❌ Path is empty. Cannot generate animation.")
            return

        print(f"🛠️ Path length: {len(self.path)}")
        print(f"🛠️ Path data: {self.path}")

        # 🔄 Initialize the plot
        fig, ax = plt.subplots()
        ax.set_xlim(-0.5, self.grid_size[1] - 0.5)
        ax.set_ylim(-0.5, self.grid_size[0] - 0.5)
        ax.invert_yaxis()  # 🔄 Flip the grid to match (0, 0) at the top-left
        ax.set_xticks(range(self.grid_size[1]))
        ax.set_yticks(range(self.grid_size[0]))
        ax.grid(True)  # ✅ Show grid lines for better visibility

        # 🚧 Draw Obstacles
        for obs in self.obstacles:
            ax.add_patch(
                patches.Rectangle((obs[1] - 0.5, obs[0] - 0.5), 1, 1, color="black")
            )

        # 🎯 Draw Goal
        ax.add_patch(
            patches.Rectangle(
                (self.goal[1] - 0.5, self.goal[0] - 0.5), 1, 1, color="green"
            )
        )

        # 🏷️ Initialize the agent marker (a red dot)
        (agent_marker,) = ax.plot([], [], "ro")

        # 🎥 Animation Update Function
        def update(frame):
            """
            This function updates the agent's position at each frame.

            Parameters:
            - frame (int): The index of the path to render.

            Returns:
            - agent_marker (matplotlib object): Updated agent marker for animation.
            """
            # 🚀 Debugging info
            print(f"📝 Frame {frame} | Path Data: {self.path[frame]}")

            # ✅ Safety check before setting data
            if isinstance(self.path[frame], tuple) and len(self.path[frame]) == 2:
                # Wrap the coordinates in a list to make them sequences
                agent_marker.set_data([self.path[frame][1]], [self.path[frame][0]])
            else:
                print(f"❌ Invalid path data at frame {frame}: {self.path[frame]}")
                agent_marker.set_data([], [])  # Empty it if invalid

            return (agent_marker,)

        # 🎞️ Generate the animation
        print(f"🛠️ Generating animation...")
        try:
            anim = animation.FuncAnimation(
                fig, update, frames=len(self.path), interval=300, blit=True
            )
            anim.save(self.save_path, writer="pillow")
            print(f"✅ Animation saved to {self.save_path}")
        except Exception as e:
            print(f"❌ Animation generation failed: {e}")

        # 🔄 Close the plot to avoid display
        plt.close()
