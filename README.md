# Tractor_bot

https://spinningup.openai.com/en/latest/user/algorithms.html
https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html?highlight=concatenate
https://github.com/werner-duvaud/muzero-general

## Development

### Setup
1. Prerequisites: VSCode, VSCode Dev Containers Extension, Docker
2. Optionally, you can create `docker/.bashrc` if you want certain Bash configurations inside the container.
3. Run `docker/start.sh`. This will build the Docker container for this project, run, and exec into it. The build will take a long time if it it is your first time running this, as the CUDA base image is very large. Now you can `docker/into.sh` to exec into a Bash shell inside the container.

4. Attach VSCode to the container (named `unified_docker`). You can do this with `Cmd + Shift + P` and searching the action: `Dev Containers: Attach to Running Container...`.

### Running Tests
Simply run any `*_test.py` file.
```
unified_docker$ python3 env/tractor_env_test.py
```

### Running Typing
Simply run `mypy` on any Python file.
```
unified_docker$ mypy env/tractor_env.py
```

## Game Plan

- [x] Docker environment setup
- [ ] Setup Gym and Tractor environment
- [ ] Define neural network model
- [ ] Define RL algorithm (e.g. DQN, PPO, etc.)
- [ ] Train :))
