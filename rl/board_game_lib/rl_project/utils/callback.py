from stable_baselines3.common.callbacks import BaseCallback

class RenderCallback(BaseCallback):
    """
    A custom callback that calls env.render() at each step.
    """
    def __init__(self, verbose=0):
        super(RenderCallback, self).__init__(verbose)

    def _on_step(self) -> bool:
        self.training_env.render()
        return True