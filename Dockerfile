#!docker image build

FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update
RUN apt install -y pip
RUN pip install chromadb==0.3.29
RUN : \
    && apt install -y libopenblas-dev libblas-dev m4 cmake python3-dev python3-yaml python3-setuptools git python3-pip python3-pil.imagetk python3-opencv \
    && pip install --upgrade pip setuptools wheel \
    && pip install \
        customtkinter langchain openai tiktoken \
    && apt clean all \
    && rm -rf /var/cache \
    && :
RUN : \
    && pip install streamlit \
    && :
RUN : \
    && apt update \
    && apt install -y language-pack-ja-base language-pack-ja locales \
    && locale-gen ja_JP.UTF-8 \
    && echo "export LANG=ja_JP.UTF-8" >> ~/.bashrc \ 
    && source ~/.bashrc \
    && apt clean all \
    && rm -rf /var/cache \
    && :
