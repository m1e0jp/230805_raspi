#:  ユーザ指定変数
SHELL:=env bash
ifndef VERBOSE
  MAKEFLAGS += --no-print-directory
endif
ifndef HOST_PWD
  HOST_PWD:=$(shell pwd)
endif

//build:
	podman image build --tag localhost/230805_raspi:1 .

//run
	podman run -it --rm --mount type=bind,source="sample",destination="/sample" -e=DISPLAY --net=host localhost/230805_raspi:1 .

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
