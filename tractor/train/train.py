import os
import ray
from ray import tune
from ray.rllib.algorithms.dqn import DQNConfig
from ray.rllib.env import PettingZooEnv
from ray.rllib.models import ModelCatalog
from ray.tune.registry import register_env
from tractor.agents import dqn
from tractor.env import tractor_env

def main():
    print("Initializing Ray...")
    ray.init(num_cpus=2, local_mode=True, logging_level="DEBUG")

    # Register model and environment.
    print("Registering model and environment...")
    # TODO put model and model name in a model file
    model_name = "model"
    ModelCatalog.register_custom_model(model_name, dqn.TorchMaskedActions)
    register_env(tractor_env.ENV_NAME, lambda config: PettingZooEnv(tractor_env.TractorEnv()))

    # Get the observation and action spaces by creating a dummy environment.
    print("Computing observation and action spaces...")
    dummy_env = PettingZooEnv(tractor_env.TractorEnv())
    obs_space = dummy_env.observation_space
    act_space = dummy_env.action_space

    print("Creating config...")
    config = (
        DQNConfig()
        .environment(env=tractor_env.ENV_NAME)
        .rollouts(num_rollout_workers=1, rollout_fragment_length=30)
        .training(
            train_batch_size=200,
            hiddens=[],
            dueling=False,
            model={"custom_model": model_name},
        )
        .multi_agent(
            policies={
                "player_0": (None, obs_space, act_space, {}),
                "player_1": (None, obs_space, act_space, {}),
                "player_2": (None, obs_space, act_space, {}),
                "player_3": (None, obs_space, act_space, {}),
            },
            policy_mapping_fn=(lambda agent_id, *args, **kwargs: agent_id),
        )
        .resources(num_cpus_for_main_process=1, num_gpus=int(os.environ.get("RLLIB_NUM_GPUS", "0")))
        .debugging(
            log_level="DEBUG"
        )
        .framework(framework="torch")
        .exploration(
            exploration_config={
                # The Exploration class to use.
                "type": "EpsilonGreedy",
                # Config for the Exploration class' constructor:
                "initial_epsilon": 0.1,
                "final_epsilon": 0.0,
                "epsilon_timesteps": 100000,  # Timesteps over which to anneal epsilon.
            }
        )
    )

    print("Training...")
    tune.run(
        "DQN",
        name="DQN",
        stop={"timesteps_total": 50000}, # TODO this should be way higher
        checkpoint_freq=10,
        config=config.to_dict(),
    )

if __name__ == "__main__":
    main()