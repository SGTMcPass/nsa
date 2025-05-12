# environments/gridworld.py
from collections import defaultdict
import random


class RLWorld:
    def __init__(
        self, width, height, start_state=(0, 0), goal_state=None, num_obstacles=3
    ):
        self.width = width
        self.height = height
        self.start_state = start_state
        self.goal_state = goal_state if goal_state else (height - 1, width - 1)
        self.current_state = start_state
        self.num_obstacles = num_obstacles

        # Action space
        self.actions = {"UP": (-1, 0), "DOWN": (1, 0), "LEFT": (0, -1), "RIGHT": (0, 1)}

        # Set up the grid and obstacles
        self.obstacles = set()
        self.reset()

    def step(self, action):
        """
        Executes the action in the environment.
        """
        if action not in self.actions:
            raise ValueError(f"Invalid action: {action}")

        move = self.actions[action]
        new_state = (self.current_state[0] + move[0], self.current_state[1] + move[1])

        # Check boundaries
        if (0 <= new_state[0] < self.height) and (0 <= new_state[1] < self.width):
            # Check for obstacles
            if new_state in self.obstacles:
                print(f"💥 Hit an obstacle at {new_state}! Penalty applied.")
                return self.current_state, -5, False
            else:
                self.current_state = new_state

        # Check if we reached the goal
        if self.current_state == self.goal_state:
            return self.current_state, 1, True
        else:
            return self.current_state, -0.1, False

    def reset(self):
        """
        Resets the environment for a new episode and generates random obstacles.
        """
        self.current_state = self.start_state
        self.obstacles = set()

        while len(self.obstacles) < self.num_obstacles:
            new_obstacle = (
                random.randint(0, self.height - 1),
                random.randint(0, self.width - 1),
            )
            if new_obstacle != self.goal_state and new_obstacle != self.start_state:
                self.obstacles.add(new_obstacle)

        print(f"🪨 Obstacles set at: {self.obstacles}")
        return self.current_state

    def validate_action(self, state):
        x, y = state
        return 0 <= x < self.height and 0 <= y < self.width

    def render(self):
        grid = [["." for _ in range(self.width)] for _ in range(self.height)]

        sx, sy = self.start_state
        gx, gy = self.goal_state
        cx, cy = self.current_state

        grid[sx][sy] = "S"
        grid[gx][gy] = "G"

        if (cx, cy) != (sx, sy) and (cx, cy) != (gx, gy):
            grid[cx][cy] = "A"

        for row in grid:
            print(" ".join(row))
        print("\n")
