# rl_project/config.py

from pydantic import BaseModel, Field
from typing import Dict, Any, Literal

class EnvironmentConfig(BaseModel):
    """Configuration for the environment to be created."""
    factory_class: str  # The full import path to the factory class, e.g., 'my_project.factories.BoardGameFactory'
    params: Dict[str, Any] = Field(default_factory=dict)

class RunnerConfig(BaseModel):
    """Configuration for the training runner."""
    backend: Literal['sb3', 'rllib']
    policy: str = 'MlpPolicy'
    total_timesteps: int = 1_000_000
    hyperparams: Dict[str, Any] = Field(default_factory=dict)

class Config(BaseModel):
    """The main configuration model for the entire project."""
    project_name: str
    environment: EnvironmentConfig
    runner: RunnerConfig