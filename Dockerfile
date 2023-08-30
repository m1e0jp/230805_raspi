#!docker image build

FROM ubuntu:23.04

ENV LANG=ja_JP.UTF-8
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y language-pack-ja-base language-pack-ja
#RUN apt-get install -y pip
RUN apt-get install -y build-essential gcc-arm-linux-gnueabihf
RUN apt-get install -y python3-venv && python3 -m venv venv
RUN apt-get install -y python3.11-dev

RUN apt-get install -y sudo alsa-utils pulseaudio fcitx5-mozc fonts-ipafont python3-pil.imagetk
RUN apt-get install -y open-jtalk open-jtalk-mecab-naist-jdic hts-voice-nitech-jp-atr503-m001 zlib1g-dev libsdl2-dev libasound2-dev libpulse-dev libgtk-3-dev libgtk-4-dev libadwaita-1-dev
RUN apt-get autoremove -y 
RUN apt-get clean all

RUN . /venv/bin/activate && pip install chromadb==0.3.29 customtkinter langchain openai bs4 tiktoken  azure-identity msgraph-sdk pygobject pycairo

RUN rm -rf /var/cache/* /usr/local/src/* ~/.cache/pip

COPY setup/ setup/
RUN . setup/first.sh

#230815
RUN apt-get install -y dbus-x11
RUN im-config -n fcitx
ENV GTK_IM_MODULE=dbus \
    QT_IM_MODULE=fcitx \
    XMODIFIERS=@im=fcitx \
    DefalutIMModule=fcitx
RUN locale-gen ja_JP.UTF-8
RUN echo 'LC_CTYPE=ja_JP.UTF-8' >> /etc/locale.conf
ENV LANG=ja_JP.UTF-8 \
    LC_ALL=ja_JP.UTF-8
