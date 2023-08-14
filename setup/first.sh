#!env bash



# Julius
(
    cpu="$(uname -m)"
    if [ "$cpu" = 'aarch64' ]; then
        option="--build=aarch64 --with-mictype=pulseaudio"
    elif [ "$cpu" = 'x86_64' ]; then
        option=""
    else
        echo 'Error: 対応していない種類のCPUです'
        exit 1
    fi

    cd setup
    tar zxf julius-v4.6.tar.gz
    cd julius-4.6
    CFLAGS='-O6' ./configure $option
    make -j2
    sudo make install
)
:
