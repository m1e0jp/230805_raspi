#:  ユーザ指定変数
SHELL:=env bash
ifndef VERBOSE
  MAKEFLAGS += --no-print-directory
endif
ifndef HOST_PWD
  HOST_PWD:=$(shell pwd)
endif

.PHONY: //%

%: //always-true
	: $@

//build:
	podman image build --tag localhost/230805_raspi:1 .

//go:
	podman run -it --rm \
	  --mount type=bind,source="sample",destination="/sample" \
	  --mount type=bind,source="/mnt/wslg",destination="/mnt/wslg" \
	  --mount type=bind,source="/tmp/.X11-unix",destination="/tmp/.X11-unix" \
	  -e=DISPLAY \
	  -e=PULSE_SERVER \
	  -e=WAYLAND_DISPLAY \
	  -e=XDG_RUNTIME_DIR \
	  -e OPENAI_API_KEY="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" \
	  --net=host \
	  localhost/230805_raspi:1

//setup:
	@julius -version >/dev/null 2>&1 || $(MAKE) //julius
	[ -f dictation-kit-v4.3.1/main.jconf ] || $(MAKE) //dictation-kit

//julius:
	@julius -version >/dev/null 2>&1 && exit 1 || :
	$(MAKE) julius-v4.6.tgz && tar zxf julius-v4.6.tgz
	cd julius-v4.6
	CFLAG='-O3' ./configure --build=arm --host=arm-linux-gnueabihf --with-mictype=pulseaudio
	make
	sudo install

//dictation-kit:
	[ -f julius-v4.6.tgz ] || wget -O julius-v4.6.tgz https://github.com/julius-speech/julius/archive/refs/tags/v4.6.tar.gz
	tar zxf julius-v4.6.tgz

julius-v4.6.tgz:

grammar-kit-v4.3.1.tgz:
	wget -O grammar-kit-v4.3.1.tgz https://github.com/julius-speech/grammar-kit/archive/refs/tags/v4.3.1.tar.gz

dictation-kit-v4.3.1.tgz:
	wget -O dictation-kit-v4.3.1.tgz https://github.com/julius-speech/dictation-kit/archive/refs/tags/dictation-kit-v4.3.1.tar.gz

//always-true:
#:          //always-true
#:              必ず実行したいターゲットに依存指定する用の仮想ターゲット
	@true

//?:
#::         //?:
#::             makefile中のコメント（この文章）を表示する。
	@cat $(firstword $(MAKEFILE_LIST)) | sed -n -E 's/^#:1 ?(.*)$$/\1/p'
	@cat $(firstword $(MAKEFILE_LIST)) | sed -n -E 's/^#:: (.*)$$/\1/p'
	@cat $(firstword $(MAKEFILE_LIST)) | sed -n -E 's/^#:2 ?(.*)$$/\1/p' | sed 's|$${TAG_ORIGIN}|${TAG_ORIGIN}|g'
	@cat $(firstword $(MAKEFILE_LIST)) | sed -n -E 's/^#:3 ?(.*)$$/\1/p'

.DEFAULT_GOAL:=//?
