#!/bin/bash

# go to source location
cd $SRC_DIR/core

# make a libexec directory
mkdir -p $PREFIX/libexec

# export prefix in to temp variable so makefile
# will pick it up
export PRFX=$PREFIX
make all
make install
