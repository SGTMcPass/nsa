"""Configuration models for the RL project."""

from pydantic import BaseModel, Field, validator
from typing import Dict, Any, Optional, List, Union

class EnvironmentConfig(BaseModel):
    """Configuration for the environment."""
    factory_class: str = Field(
        ...,
        description="Fully qualified class name of the environment factory"
    )
    params: Dict[str, Any] = Field(
        default_factory=dict,
        description="Parameters to pass to the environment factory"
    )

class RunnerConfig(BaseModel):
    """Configuration for the RL runner."""
    backend: str = Field(
        ...,
        description="Backend to use (e.g., 'sb3' or 'rllib')",
        pattern="^(sb3|rllib)$"
    )
    policy: str = Field(
        "MlpPolicy",
        description="Policy network architecture to use"
    )
    total_timesteps: int = Field(
        1_000_000,
        description="Total number of timesteps to train for",
        gt=0
    )
    show_progress_bar: Optional[bool] = Field(True, description="Show TQDM progress bar during training.")
    show_metrics_table: Optional[bool] = Field(True, description="Show table of metrics in console.")
    hyperparams: Dict[str, Any] = Field(
        default_factory=dict,
        description="Hyperparameters specific to the backend"
    )

class Config(BaseModel):
    """Top-level configuration model."""
    project_name: str = Field(
        ...,
        description="Name of the project (used for saving models and logs)"
    )
    environment: EnvironmentConfig = Field(
        ...,
        description="Configuration for the environment"
    )
    runner: RunnerConfig = Field(
        ...,
        description="Configuration for the RL runner"
    )
    
    class Config:
        """Pydantic config."""
        extra = "forbid"  # Don't allow extra fields
        validate_all = True
        validate_assignment = True

# For backward compatibility with existing code
EnvironmentConfig = EnvironmentConfig
RunnerConfig = RunnerConfig
Config = Config
