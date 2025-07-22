""
"""
Custom callbacks for the RL project.
"""
import numpy as np
from stable_baselines3.common.callbacks import BaseCallback
from PIL import Image, ImageDraw, ImageFont
import os
import io
import tensorflow as tf
from stable_baselines3.common.vec_env import VecNormalize

class RenderCallback(BaseCallback):
    def _on_step(self) -> bool:
        if self.training_env.get_attr("render_mode")[0] == "human":
            self.training_env.render()
        return True

class AnnealingCallback(BaseCallback):
    def __init__(self, initial_value: float, verbose: int = 0):
        super().__init__(verbose)
        self.initial_value = initial_value

    def _on_step(self) -> bool:
        progress = self.model._current_progress_remaining
        self.model.ent_coef = progress * self.initial_value
        return True

class CustomMetricsCallback(BaseCallback):
    def __init__(self, log_freq: int = 1000, verbose: int = 0):
        super().__init__(verbose)
        self.log_freq = log_freq
        self.action_counts = np.zeros(6, dtype=int)
        self.overlay_output_dir = "./logs/strategy_overlays"
        os.makedirs(self.overlay_output_dir, exist_ok=True)
        self.tb_writer = None
        self.ep_points_history = []
        self.ep_points_per_action_history = []
        self.ep_turns_history = []
        self.ep_points_per_turn_history = []

    def _on_training_start(self):
        self.tb_writer = self.logger.writer if hasattr(self.logger, 'writer') else None

    def _on_step(self) -> bool:
        dones = self.locals['dones']
        actions = self.locals['actions']
        for action in actions:
            self.action_counts[action] += 1

        if self.n_calls % self.log_freq == 0:
            for i in range(len(self.action_counts)):
                self.logger.record(f"policy/action_distribution/action_{i}", self.action_counts[i])

            if hasattr(self.model, 'logger'):
                if hasattr(self.model, 'entropy'):
                    self.logger.record("policy/entropy", self.model.entropy)
                if hasattr(self.model, 'value_loss'):
                    self.logger.record("training/loss/value", self.model.value_loss)
                if hasattr(self.model, 'advantage_mean'):
                    self.logger.record("policy/advantage_mean", self.model.advantage_mean)

        if any(dones):
            for i, info in enumerate(self.locals['infos']):
                if dones[i]:
                    if 'net_turns_spent' in info:
                        self.logger.record('rollout/turns/net_turns_spent_mean', info['net_turns_spent'])
                        self.ep_turns_history.append(info['net_turns_spent'])
                    if 'points' in info:
                        self.logger.record('rollout/score/ep_points_mean', info['points'])
                        self.ep_points_history.append(info['points'])
                    if 'net_turns_spent' in info and info['net_turns_spent'] > 0:
                        points_per_turn = info['points'] / info['net_turns_spent']
                        self.logger.record('rollout/score/ep_points_per_turn', points_per_turn)
                        self.ep_points_per_turn_history.append(points_per_turn)
                    if 'actions_taken' in info and info['actions_taken'] > 0:
                        points_per_action = info['points'] / info['actions_taken']
                        self.logger.record('rollout/score/ep_points_per_action', points_per_action)
                        self.ep_points_per_action_history.append(points_per_action)
                    if 'ev_alignment_rate' in info:
                        self.logger.record('policy/ev/alignment_rate', info['ev_alignment_rate'])
                        if info['ev_alignment_rate'] >= 0.8:
                            self.logger.record('highlights/ev_performance/Excellent_EV_Alignment', info['ev_alignment_rate'])
                        elif info['ev_alignment_rate'] >= 0.5:
                            self.logger.record('highlights/ev_performance/Moderate_EV_Alignment', info['ev_alignment_rate'])
                        else:
                            self.logger.record('highlights/ev_performance/Poor_EV_Alignment', info['ev_alignment_rate'])
                    if 'ev_action_mean' in info:
                        self.logger.record('policy/ev/action_mean', info['ev_action_mean'])
                    if 'ev_delta_mean' in info:
                        self.logger.record('policy/ev/delta_mean', info['ev_delta_mean'])
                    if 'most_common_action' in info:
                        self.logger.record('policy/ev/most_common_action', info['most_common_action'])
                        if info['most_common_action'] == 4:
                            self.logger.record('highlights/action_strategy/Favoring_10x', 1)
                        elif info['most_common_action'] == 0:
                            self.logger.record('highlights/action_strategy/Favoring_1x', 1)
                        else:
                            self.logger.record('highlights/action_strategy/Mixed_Multipliers', 1)
                    if 'tile_stats' in info:
                        self._generate_overlay_image(info['tile_stats'], self.num_timesteps)

        def ema(data, alpha=0.1):
            if not data: return 0
            avg = data[0]
            for val in data[1:]:
                avg = alpha * val + (1 - alpha) * avg
            return avg

        def sma(data):
            return np.mean(data) if data else 0

        max_window = 100
        self.ep_points_history = self.ep_points_history[-max_window:]
        self.ep_points_per_action_history = self.ep_points_per_action_history[-max_window:]
        self.ep_turns_history = self.ep_turns_history[-max_window:]
        self.ep_points_per_turn_history = self.ep_points_per_turn_history[-max_window:]

        self.logger.record('rollout/score/ema_ep_points', ema(self.ep_points_history))
        self.logger.record('rollout/score/sma_ep_points', sma(self.ep_points_history))
        self.logger.record('rollout/score/ema_points_per_action', ema(self.ep_points_per_action_history))
        self.logger.record('rollout/score/sma_points_per_action', sma(self.ep_points_per_action_history))
        self.logger.record('rollout/score/ema_points_per_turn', ema(self.ep_points_per_turn_history))
        self.logger.record('rollout/score/sma_points_per_turn', sma(self.ep_points_per_turn_history))
        self.logger.record('rollout/turns/ema_net_turns', ema(self.ep_turns_history))
        self.logger.record('rollout/turns/sma_net_turns', sma(self.ep_turns_history))

        return True

    def _generate_overlay_image(self, tile_stats: dict, step_count: int):
        base_path = "./board_overlay_base.png"
        if not os.path.exists(base_path):
            return

        image = Image.open(base_path).convert("RGBA")
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default()

        tile_centers = {
            0: (630, 870), 1: (550, 870), 2: (470, 870), 3: (390, 870), 4: (310, 870), 5: (230, 870),
            6: (150, 800), 7: (150, 720), 8: (150, 640), 9: (230, 570), 10: (310, 570),
            11: (150, 480), 12: (230, 410), 13: (310, 340), 14: (390, 340), 15: (470, 340),
            16: (550, 340), 17: (630, 410), 18: (710, 480), 19: (710, 570), 20: (630, 640),
            21: (550, 710), 22: (630, 790), 23: (710, 870)
        }

        for tile_id, stats in tile_stats.items():
            if tile_id not in tile_centers:
                continue
            cx, cy = tile_centers[tile_id]
            visits = stats.get("visits", 0)
            ev = stats.get("ev", 0)
            reward = stats.get("reward", 0)
            overlay = f"V:{visits}\nEV:{int(ev)}\nR:{int(reward)}"
            draw.text((cx - 20, cy - 30), overlay, fill="black", font=font)

        output_path = os.path.join(self.overlay_output_dir, f"strategy_overlay_{step_count}.png")
        image.save(output_path)

        if self.tb_writer:
            with io.BytesIO() as output:
                image.save(output, format="PNG")
                image_bytes = output.getvalue()
                tf_image = tf.image.decode_png(image_bytes, channels=4)
                tf_image = tf.expand_dims(tf_image, 0)
                tf.summary.image("strategy_overlay", tf_image, step=step_count)
                self.tb_writer.flush()

