import gymnasium as gym
from ray.rllib.algorithms.dqn.dqn_torch_model import DQNTorchModel
from ray.rllib.utils.typing import ModelConfigDict
from ray.rllib.models.torch.fcnet import FullyConnectedNetwork

class TorchMaskedActions(DQNTorchModel):
    def __init__(self, obs_space: gym.spaces.Space, action_space: gym.spaces.Space, num_outputs: int, model_config: ModelConfigDict, name, **kw):
        DQNTorchModel.__init__(self, obs_space, action_space, num_outputs, model_config, name, **kw)

        # The observation space includes the action mask. To consider the observation itself, we
        # must remove the action mask portion.
        obs_len = obs_space.shape[0]-action_space.n
        orig_obs_space = Box(shape=(obs_len,), low=obs_space.low[:obs_len], high=obs_space.high[:obs_len])

        # This is the actual model, but the architecture of the model is passed in.
        self.action_embed_model = FullyConnectedNetwork(orig_obs_space, action_space, action_space.n, model_config, name + "_action_embed")

    def forward(self, input_dict, state, seq_lens):
        # Extract the available actions tensor from the observation.
        action_mask = input_dict["obs"]["action_mask"]

        # Compute the predicted action embedding
        action_logits, _ = self.action_embed_model({
            "obs": input_dict["obs"]["observation"]
        })

        # turns probit action mask into logit action mask
        inf_mask = torch.clamp(torch.log(action_mask), -1e10, FLOAT_MAX)
        return action_logits + inf_mask, state

    def value_function(self):
        return self.action_embed_model.value_function()
