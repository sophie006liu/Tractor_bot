FROM pytorch/pytorch:2.3.1-cuda11.8-cudnn8-devel

RUN apt update
RUN apt install -y git vim

RUN pip3 install mypy==1.10.0
RUN pip3 install gymnasium==0.29.1
RUN pip3 install pettingzoo==1.24.3

# Allow Python import paths to originate from the /workspace dir.
ENV PYTHONPATH=/workspace
