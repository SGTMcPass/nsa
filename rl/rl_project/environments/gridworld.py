# environments/gridworld.py
from collections import defaultdict


class RLWorld:
    def __init__(self, width, height, start_state=(0, 0), goal_state=None):
        self.width = width
        self.height = height
        self.start_state = start_state
        self.goal_state = goal_state if goal_state else (height - 1, width - 1)
        self.current_state = start_state

        # Action space
        self.ACTIONS = {"UP": (-1, 0), "DOWN": (1, 0), "LEFT": (0, -1), "RIGHT": (0, 1)}

    def step(self, action):
        if action not in self.ACTIONS:
            raise ValueError(f"Invalid action: {action}")

        move = self.ACTIONS[action]
        new_state = (self.current_state[0] + move[0], self.current_state[1] + move[1])

        if not self.validate_action(new_state):
            reward = -1
            done = False
            new_state = self.current_state
        else:
            self.current_state = new_state
            if new_state == self.goal_state:
                reward = 1
                done = True
            else:
                reward = 0
                done = False

        return new_state, reward, done

    def reset(self):
        self.current_state = self.start_state
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
