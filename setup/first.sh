#!env bash

apt-get update

#apt full-upgrade
apt install -y pip

pip install chromadb==0.3.29
#pip install chromadb==0.3.29 setuptools wheel customtkinter langchain openai tiktoken streamlit bs4 openai-whisper

#apt install -y libopenblas-dev libblas-dev m4 cmake python3-dev python3-yaml python3-setuptools git python3-pip python3-pil.imagetk python3-opencv fcitx-mozc fonts-ipafont

#pip install --upgrade pip setuptools wheel
#pip install setuptools wheel
#pip install customtkinter langchain openai tiktoken streamlit bs4


#apt-get install -y --no-install-recommends sudo build-essential gcc-arm-linux-gnueabihf pip alsa-utils pulseaudio fcitx-mozc fonts-ipafont
 apt-get install -y                         sudo build-essential gcc-arm-linux-gnueabihf     alsa-utils pulseaudio fcitx-mozc fonts-ipafont python3-pil.imagetk


apt-get autoremove -y 
apt-get clean all
pip install customtkinter langchain openai bs4 tiktoken
rm -rf /var/cache/* /usr/local/src/* ~/.cache/pip


# Julius
(
    cpu="$(uname -m)"
    if [ "$cpu" = 'aarch64' ]; then
        option="--build=arm --host=arm-linux-gnueabihf --with-mictype=pulseaudio"
    elif [ "$cpu" = 'x86_64' ]; then
        option=""
    else
        echo 'Error: 対応していない種類のCPUです'
        exit 1
    fi

    cd my/julius
    CFLAG='-O3' ./configure $option
    make
    sudo make install
)

:
