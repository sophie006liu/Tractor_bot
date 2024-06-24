import numpy as np
import typing
import gymnasium as gym
from gymnasium import spaces
from pettingzoo import AECEnv
from pettingzoo.utils import agent_selector

class TractorEnv(AECEnv):
    """
    Defines the observation space, action space, initialization, and gameplay mechanics for a
    4-player game of Tractor.
    """

    metadata = {"render_modes": ["human"], "name": "tractor"}

    def __init__(self, render_mode=None):
        self.possible_agents = ["player_" + str(r) for r in range(4)]
        self.render_mode = render_mode

    def observation_space(self, agent: str) -> spaces.Space:
        # TODO: define observation space. What information will be in an "observation", and how
        # will it be structured? See https://www.gymlibrary.dev/content/environment_creation/#declaration-and-initialization.
        return spaces.Discrete(1)

    def action_space(self, agent: str) -> spaces.Space:
        # TODO: define action space. What information will be in an action, and how will it be
        # structured? See above link for example.
        return spaces.Discrete(1)

    def render(self) -> None | np.ndarray | str | list:
        if self.render_mode is None:
            gym.logger.warn("Render called but render_mode is None.")
            return None

        # TODO: print the game state in a human-readable fashion.
        return None

    def reset(self, seed: int | None = None, options: dict[str, typing.Any] | None = None) -> None:
        """
        This should initialize the game state randomly using the provided seed, and do all
        preparations necessary for `step` to be called.

        Reset needs to initialize the following attributes as per the contract of the AECEnv API.
        - agents
        - rewards
        - _cumulative_rewards
        - terminations
        - truncations
        - infos
        - agent_selection
        It must also set up the environment so that render(), step(), and observe() can be called
        without issues.

        See https://pettingzoo.farama.org/content/environment_creation/ for details.
        """
        super().reset(seed=seed)

        self.agents = self.possible_agents[:]
        self.rewards = {agent: 0 for agent in self.agents}
        self._cumulative_rewards = {agent: 0 for agent in self.agents}
        self.terminations = {agent: False for agent in self.agents}
        self.truncations = {agent: False for agent in self.agents}
        self.infos: dict[str, typing.Any] = {agent: {} for agent in self.agents}

        self._agent_selector = agent_selector(self.agents)
        self.agent_selection = self._agent_selector.next()

        # TODO: initialize any other needed game state (e.g. hands, trump card and suite, anything
        # else needed to calculate observations and rewards, etc.).

    def observe(self, agent: str) -> gym.core.ObsType | None:
        """Return the observation of the specified agent on the current came state."""
        # TODO: implement observation by any agent on the game state.
        pass

    def step(self, action: gym.core.ActType) -> None:
        """
        Accepts an action and updates the game state. Specifically, it must update:
        - rewards
        - _cumulative_rewards (accumulating the rewards)
        - terminations
        - truncations
        - infos
        - agent_selection (to the next agent)
        And any internal state used by observe() or render().
        """
        # TODO: implement `step` to update the game state, compute reward, determine if the game is
        # done, and return any needed extra info.
        pass

    def close(self) -> None:
        """
        Tears down any game state that needs to be cleaned up.
        """
        pass
