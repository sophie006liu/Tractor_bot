import torch
import torch.nn as nn
import torch.optim as optim
import typing
import gymnasium as gym
from gymnasium import spaces

class TractorEnv(gym.Env):
    """
    Defines the observation space, action space, initialization, and gameplay mechanics for a
    4-player game of Tractor.
    """

    def __init__(self):
        # TODO: define observation space. What information will be in an "observation", and how
        # will it be structured? See https://www.gymlibrary.dev/content/environment_creation/#declaration-and-initialization.
        self.observation_space = spaces.Discrete(1)

        # TODO: define action space. What information will be in an action, and how will it be
        # structured? See above link for example.
        self.action_space = spaces.Discrete(1)

    def reset(self, *, seed: int | None = None, options: dict[str, typing.Any] | None = None) -> tuple[gym.core.ObsType, dict[str, typing.Any]]:
        """
        This should initialize the game state randomly using the provided seed, and do all
        preparations necessary for `step` to be called.
        """
        super().reset(seed=seed)

        # TODO: implement initialization of game state here. Return the initial observation object,
        # and a dict of extra information if needed.
        return self.observation_space.sample(), {}

    def step(self, action: gym.core.ActType) -> tuple[gym.core.ObsType, gym.core.SupportsFloat, bool, bool, dict[str, typing.Any]]:
        """
        Accepts an action, updates the game state, and outputs a tuple of (observation, reward, done, truncated, info).
        """
        # TODO: implement `step` to update the game state, compute reward, determine if the game is
        # done, and return any needed extra info.
        return self.observation_space.sample(), 0, True, False, {}

    def close(self) -> None:
        """
        Tears down any game state that needs to be cleaned up.
        """
        return
