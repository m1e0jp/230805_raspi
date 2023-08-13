#!docker image build

FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
COPY setup/ setup/
RUN . ./setup/first.sh
RUN apt-get install -y open-jtalk open-jtalk-mecab-naist-jdic hts-voice-nitech-jp-atr503-m001
RUN apt-get install -y alsa-utils
RUN apt-get install -y pulseaudio

