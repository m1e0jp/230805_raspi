#!docker image build

FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
COPY setup/ setup/
RUN . ./setup/first.sh
