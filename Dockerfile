#!docker image build

FROM ubuntu:22.04

ENV LANG=ja_JP.UTF-8
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y language-pack-ja-base language-pack-ja
RUN apt-get install -y pip
RUN pip install chromadb==0.3.29


RUN apt-get install -y sudo build-essential gcc-arm-linux-gnueabihf     alsa-utils pulseaudio fcitx-mozc fonts-ipafont python3-pil.imagetk
RUN pip install customtkinter langchain openai bs4 tiktoken

RUN apt-get install -y open-jtalk open-jtalk-mecab-naist-jdic hts-voice-nitech-jp-atr503-m001
RUN apt-get install -y alsa-utils
RUN apt-get install -y pulseaudio
RUN apt-get install -y zlib1g-dev libsdl2-dev libasound2-dev libpulse-dev
RUN apt-get autoremove -y 
RUN apt-get clean all
RUN rm -rf /var/cache/* /usr/local/src/* ~/.cache/pip

COPY setup/ setup/
RUN . setup/first.sh

#230815
RUN im-config -n fcitx
ENV GTK_IM_MODULE=xim \
    QT_IM_MODULE=fcitx \
    XMODIFIERS=@im=fcitx \
    DefalutIMModule=fcitx
RUN locale-gen ja_JP.UTF-8  
ENV LANG=ja_JP.UTF-8 \
    LC_ALL=ja_JP.UTF-8
