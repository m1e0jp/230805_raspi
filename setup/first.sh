#!env bash



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

    cd setup
    tar zxf julius-v4.6.tar.gz
    cd julius-4.6
    ls -l
    pwd
    CFLAGS='-O3' ./configure $option
    make
    sudo make install
)
:
