# rl/rl_project/environments/board_game_env.py

import gymnasium as gym
import numpy as np
import random
import pygame
import os
from typing import Optional, Dict, Any, Tuple, Type, List
from collections import OrderedDict

# --- Tile Definitions (No Changes) ---

class Tile:
    def __init__(self, **kwargs):
        pass
    def get_reward(self, multiplier: int) -> Dict[str, float]:
        return {}

class FlatTile(Tile):
    def __init__(self, points: float = 0, gems: float = 0, turns: float = 0, gold: float = 0, **kwargs):
        super().__init__(**kwargs)
        self.points = points
        self.gems = gems
        self.turns = turns
        self.gold = gold
    def get_reward(self, multiplier: int) -> Dict[str, float]:
        return {"points": self.points * multiplier, "gems": self.gems * multiplier, "free_turns": self.turns * multiplier, "gold": self.gold * multiplier}

class GrandPrizeTile(Tile):
    def __init__(self, points_reward: float = 10000, **kwargs):
        super().__init__(**kwargs)
        self.points_reward = points_reward

    def get_reward(self, multiplier: int) -> Dict[str, float]:
        rewards = {}
        for _ in range(multiplier):
            spin = random.randint(1, 10000)
            if spin <= 666: rewards["chroma"] = rewards.get("chroma", 0) + 2
            elif spin <= 3333: rewards["obsidian"] = rewards.get("obsidian", 0) + 1
            elif spin <= 6000: rewards["gems"] = rewards.get("gems", 0) + 100
            elif spin <= 6666: rewards["chroma"] = rewards.get("chroma", 0) + 1
            elif spin <= 7333: rewards["free_turns"] = rewards.get("free_turns", 0) + 2
            else: rewards["free_turns"] = rewards.get("free_turns", 0) + 1
            
            if spin > 5000:
                rewards["points"] = rewards.get("points", 0) + self.points_reward
        return rewards

class PointWheelTile(Tile):
    def get_reward(self, multiplier: int) -> Dict[str, float]:
        total_points = 0
        for _ in range(multiplier):
            spin = random.randint(1, 10000)
            points = 100
            if spin <= 3478: points = 200
            elif spin <= 3478 + 2608: points = 500
            elif spin <= 3478 + 2608 + 434: points = 1000
            spin2 = random.randint(1, 10000)
            spin_multiplier = 1
            if spin2 <= 3076: spin_multiplier = 3
            elif spin2 <= 3076 + 769: spin_multiplier = 5
            total_points += points * spin_multiplier
        return {"points": total_points}

class FateWheelTile(Tile):
    def __init__(self, outcomes: List[Dict[str, Any]], **kwargs):
        super().__init__(**kwargs)
        total_chance = sum(o.get('chance', 0) for o in outcomes)
        if total_chance != 10000:
            raise ValueError(f"Sum of chances for FateWheelTile must be 10000, but got {total_chance}")
        self.outcomes = outcomes

    def get_reward(self, multiplier: int) -> Dict[str, float]:
        rewards = {}
        for _ in range(multiplier):
            spin = random.randint(1, 10000)
            cumulative_chance = 0
            for outcome in self.outcomes:
                cumulative_chance += outcome['chance']
                if spin <= cumulative_chance:
                    for resource, amount in outcome['reward'].items():
                        rewards[resource] = rewards.get(resource, 0) + amount
                    break
        return rewards

TILE_TYPE_MAP: Dict[str, Type[Tile]] = {"FlatTile": FlatTile, "GrandPrizeTile": GrandPrizeTile, "PointWheelTile": PointWheelTile, "FateWheelTile": FateWheelTile}


class BoardGameEnv(gym.Env):
    metadata = {"render_modes": ["human"], "render_fps": 4}

    def __init__(self,
                 board_layout: List[Dict[str, Any]],
                 initial_resources: Dict[str, float],
                 observed_resources: list[str],
                 reward_weights: Dict[str, float],
                 goal_points: int = 100_000,
                 max_turns: int = 1000,
                 points_breakpoints: Optional[List[int]] = None,
                 turn_task_breakpoints: Optional[List[int]] = None,
                 turn_task_reward: Optional[List[int]] = None,
                 gem_purchase_settings: Optional[Dict[str, int]] = None,
                 test_mode: bool = False,
                 render_mode: Optional[str] = None):
        super().__init__()
        
        self.goal_points = goal_points
        self.initial_resources = initial_resources
        self.observed_keys = observed_resources
        self.reward_weights = reward_weights
        self.max_turns = max_turns
        self._board = self._create_board(board_layout)
                
        self.points_breakpoints = points_breakpoints or []
        self.turn_task_breakpoints = turn_task_breakpoints or []
        self.turn_task_reward = turn_task_reward or []
        
        if gem_purchase_settings is None:
            self.gem_purchase_cost = 750
            self.gem_purchase_reward_turns = 5
            self.gem_purchase_limit = 7
        else:
            self.gem_purchase_cost = gem_purchase_settings.get("cost", 750)
            self.gem_purchase_reward_turns = gem_purchase_settings.get("reward_turns", 5)
            self.gem_purchase_limit = gem_purchase_settings.get("limit", 7)
            
        self.action_space = gym.spaces.Discrete(6)
        self._multipliers = [1, 2, 3, 5, 10]
        self._test_mode = test_mode
        
        num_observed_resources = len(self.observed_keys)
        observation_size = 3 + num_observed_resources
        
        self.observation_space = gym.spaces.Dict({
            "obs": gym.spaces.Box(
                low=np.zeros(observation_size, dtype=np.float32),
                high=np.full(observation_size, np.inf, dtype=np.float32),
                dtype=np.float32
            ),
            "action_mask": gym.spaces.Box(
                low=0, high=1, shape=(self.action_space.n,), dtype=np.int8
            ),
        })
        self.render_mode = render_mode
        self.screen = None
        self.clock = None

        if self.render_mode == "human":
            pygame.init()
            pygame.display.set_caption("Board Game RL")
            self.screen = pygame.display.set_mode((800, 600))
            self.clock = pygame.time.Clock()
            self.font = pygame.font.Font(None, 24)

    def _create_board(self, layout_config: List[Dict[str, Any]]) -> List[Tile]:
        board = []
        for tile_config in layout_config:
            tile_type_str = tile_config.get("type")
            tile_class = TILE_TYPE_MAP.get(tile_type_str)
            if not tile_class: raise ValueError(f"Unknown tile type in config: {tile_type_str}")
            board.append(tile_class(**tile_config.get("params", {})))
        return board

    def _get_action_mask(self) -> np.ndarray:
        mask = np.ones(self.action_space.n, dtype=np.int8)
        for i, multiplier in enumerate(self._multipliers):
            if self.turns_remaining < multiplier:
                mask[i] = 0
        can_afford = self.master_resources.get("gems", 0) >= self.gem_purchase_cost
        under_limit = self.master_resources.get("gem_purchases_done", 0) < self.gem_purchase_limit
        if not (can_afford and under_limit):
            mask[5] = 0
        return mask
        
    def render(self):
        if self.render_mode != "human": return
        self.screen.fill((20, 20, 40))
        board_radius = 200
        center_x, center_y = 300, 300
        num_tiles = len(self._board)
        for i in range(num_tiles):
            angle = (i / num_tiles) * 2 * np.pi
            x = center_x + int(board_radius * np.cos(angle))
            y = center_y + int(board_radius * np.sin(angle))
            color = (200, 200, 200) if i == self.position else (100, 100, 120)
            pygame.draw.circle(self.screen, color, (x, y), 20)
            text = self.font.render(str(i), True, (0,0,0))
            self.screen.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))
        y_offset = 50
        for i, (resource, value) in enumerate(self.master_resources.items()):
            text = self.font.render(f"{resource.title()}: {value:,.0f}", True, (255, 255, 255))
            self.screen.blit(text, (620, y_offset + i * 30))
        pygame.display.flip()
        self.clock.tick(self.metadata["render_fps"])

    def close(self):
        if self.screen is not None:
            pygame.display.quit()
            pygame.quit()

    def reset(self, *, seed: Optional[int] = None, options: Optional[Dict] = None) -> Tuple[np.ndarray, Dict]:
        super().reset(seed=seed)
        self.master_resources = self.initial_resources.copy()
        self.position, self.turns_done = 0, 0
        self.turns_remaining = self.master_resources.get("initial_turns", 50)
        self.points_bp_met, self.turn_bp_met = -1, -1
        return self._get_observation(), self._get_info()

    def step(self, action: int) -> Tuple[np.ndarray, float, bool, bool, Dict]:
        if self._get_action_mask()[action] == 0:
            penalty = -1.0
            return self._get_observation(), penalty, False, False, self._get_info()

        resources_before = self.master_resources.copy()
        tile_rewards = {}
        turns_spent_this_step = 0

        if action < len(self._multipliers):
            multiplier = self._multipliers[action]
            turns_spent_this_step = multiplier
            self.turns_remaining -= multiplier
            self.turns_done += multiplier
            roll = random.randint(1, 6) + random.randint(1, 6)
            self.position = (self.position + roll) % len(self._board)
            tile = self._board[self.position]
            tile_rewards = tile.get_reward(multiplier)
        elif action == 5:
            self.master_resources["gems"] -= self.gem_purchase_cost
            self.master_resources["gem_purchases_done"] = self.master_resources.get("gem_purchases_done", 0) + 1
            tile_rewards["free_turns"] = self.gem_purchase_reward_turns
        
        for key, value in tile_rewards.items():
            self.master_resources[key] = self.master_resources.get(key, 0) + value

        bonus_turns_from_bp = 0
        while (self.points_bp_met + 1 < len(self.points_breakpoints) and 
               self.master_resources["points"] >= self.points_breakpoints[self.points_bp_met + 1]):
            self.points_bp_met += 1
            bonus_turns_from_bp += 2
        while (self.turn_bp_met + 1 < len(self.turn_task_breakpoints) and 
               self.turns_done >= self.turn_task_breakpoints[self.turn_bp_met + 1]):
            self.turn_bp_met += 1
            bonus_turns_from_bp += self.turn_task_reward[self.turn_bp_met]

        if bonus_turns_from_bp > 0:
            self.turns_remaining += bonus_turns_from_bp
            self.master_resources["free_turns"] = self.master_resources.get("free_turns", 0) + bonus_turns_from_bp
        
        resource_deltas = {k: self.master_resources.get(k, 0) - resources_before.get(k, 0) 
                          for k in set(resources_before) | set(self.master_resources)}
        
        points_gained = resource_deltas.get("points", 0)
        final_reward = points_gained * self.reward_weights.get("points", 1.0)
        
        turn_penalty = turns_spent_this_step * self.reward_weights.get("turn_penalty", 0.0)
        final_reward -= turn_penalty
        
        free_turns_gained = resource_deltas.get("free_turns", 0)
        if free_turns_gained > 0:
            final_reward += free_turns_gained * self.reward_weights.get("free_turns", 0.0)

        terminated = self.master_resources.get("points", 0) >= self.goal_points
        truncated = (self.turns_remaining <= 0) or (self.turns_done >= self.max_turns)
        
        if terminated:
            truncated = False
        
        return self._get_observation(), final_reward, terminated, truncated, self._get_info()
        
    def _get_observation(self) -> Dict[str, np.ndarray]:
        obs_values = [self.position, self.turns_remaining, self.turns_done]
        obs_values.extend(self.master_resources.get(key, 0) for key in self.observed_keys)
        obs = np.array(obs_values, dtype=np.float32)
        mask = self._get_action_mask()
        return OrderedDict([("obs", obs), ("action_mask", mask)])

    def _get_info(self) -> Dict:
        """Gets the info dictionary, including the action mask."""
        info = self.master_resources.copy()
        info["action_mask"] = self._get_action_mask()
        info["turns_remaining"] = self.turns_remaining
        # --- CORRECTED: Assign self.turns_done to info["turns_done"] ---
        info["turns_done"] = self.turns_done
        return info

