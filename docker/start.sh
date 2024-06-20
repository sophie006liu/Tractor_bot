DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
echo $DIR

docker rm unified_docker
docker build -f $DIR/Dockerfile $DIR/.. --tag unified_docker
docker run --name unified_docker -it unified_docker bash
