# environments/gridworld.py
import random
from collections import deque


class RLWorld:
    """
    RLWorld: Represents the grid-based environment for agent navigation.
    Handles obstacle placement, action validation, and state transitions.
    """

    def __init__(
        self, width, height, start_state=(0, 0), goal_state=None, num_obstacles=3
    ):
        """
        Initializes the environment.

        Parameters:
        - width (int): Width of the grid.
        - height (int): Height of the grid.
        - start_state (tuple): Starting coordinate (default is (0, 0)).
        - goal_state (tuple): Goal coordinate (default is bottom-right corner).
        - num_obstacles (int): Number of obstacles to place in the grid.
        """
        self.width = width
        self.height = height
        self.start_state = start_state
        self.goal_state = goal_state if goal_state else (width - 1, height - 1)
        self.current_state = start_state
        self.num_obstacles = num_obstacles

        # ✅ Initialize actions properly
        self.actions = {"UP": (-1, 0), "DOWN": (1, 0), "LEFT": (0, -1), "RIGHT": (0, 1)}

        # ✅ Initialize the obstacles list
        self.obstacles = set()

        # Generate the first set of obstacles
        self.reset()

    def reset(self):
        """
        Resets the environment for a new episode, generates random obstacles,
        and guarantees there is a valid path to the goal.
        """
        self.current_state = self.start_state
        max_attempts = 10
        attempts = 0

        # ✅ Try to generate obstacles and validate the path
        while attempts < max_attempts:
            self.obstacles.clear()
            while len(self.obstacles) < self.num_obstacles:
                new_obstacle = (
                    random.randint(0, self.height - 1),
                    random.randint(0, self.width - 1),
                )
                if new_obstacle != self.goal_state and new_obstacle != self.start_state:
                    self.obstacles.add(new_obstacle)

            if self.is_path_available():
                print(f"🪨 Obstacles set at: {self.obstacles}")
                return self.current_state

            attempts += 1
            print(f"🔄 Path not found. Regenerating obstacles... Attempt {attempts}")

        # If it fails after max attempts, clear obstacles to avoid a deadlock
        print(
            f"❌ Could not find a valid path after {max_attempts} attempts. No obstacles placed."
        )
        self.obstacles.clear()
        return self.current_state

    def validate_action(self, action):
        """
        Checks if the specified action is valid.

        Parameters:
        - action (str): Action to validate ('UP', 'DOWN', 'LEFT', 'RIGHT').

        Returns:
        - bool: True if the action is valid, False otherwise.
        """
        if action not in self.actions:
            print(f"❌ Action {action} is not valid.")
            return False

        move = self.actions[action]
        new_state = (self.current_state[0] + move[0], self.current_state[1] + move[1])

        # Check boundaries
        if (0 <= new_state[0] < self.height) and (0 <= new_state[1] < self.width):
            # Check for obstacles
            if new_state not in self.obstacles:
                print(f"✅ Action {action} is valid to {new_state}.")
                return True

        print(f"❌ Action {action} would hit an obstacle or boundary.")
        return False

    def step(self, action):
        """
        Executes the action in the environment if it is valid.

        Parameters:
        - action (str): Action to execute ('UP', 'DOWN', 'LEFT', 'RIGHT')

        Returns:
        - tuple: (new_state, reward, done)
        """
        if not self.validate_action(action):
            print(f"❌ Step failed: Invalid action {action}")
            return self.current_state, -5, False, False

        move = self.actions[action]
        new_state = (self.current_state[0] + move[0], self.current_state[1] + move[1])

        # ✅ Detect if the new state is an obstacle
        if new_state in self.obstacles:
            print(f"💥 Collision detected at {new_state}")
            return (
                self.current_state,
                -10,
                False,
                True,
            )  # Stronger penalty for collision

        # Agent moves successfully
        self.current_state = new_state

        # Check if we reached the goal
        if self.current_state == self.goal_state:
            return self.current_state, 1, True, False
        else:
            return self.current_state, -0.1, False, False

    def is_path_available(self):
        """
        Performs BFS to check if a path exists from start to goal.

        Returns:
        - bool: True if a path exists, False otherwise.
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        queue = deque([self.start_state])

        while queue:
            current = queue.popleft()

            if current == self.goal_state:
                return True

            for d in directions:
                neighbor = (current[0] + d[0], current[1] + d[1])

                if (
                    0 <= neighbor[0] < self.height
                    and 0 <= neighbor[1] < self.width
                    and neighbor not in self.obstacles
                    and neighbor not in visited
                ):
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False
