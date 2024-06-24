DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
echo $DIR

# Kill existing container if it's running.
docker stop unified_docker
docker rm unified_docker

docker build -f $DIR/Dockerfile $DIR/.. --tag unified_docker

# Start the container and mount the project repo to /workspace.
docker run -itd --name unified_docker \
  -v $DIR/..:/workspace \
  -v ~/.ssh:/root/.ssh \
  -v ~/.gitconfig:/root/.gitconfig \
  unified_docker bash

# Add a step to source the provide
docker exec -it unified_docker bash -c "echo '[[ -f /workspace/docker/.bashrc ]] && source /workspace/docker/.bashrc' >> ~/.bashrc"
