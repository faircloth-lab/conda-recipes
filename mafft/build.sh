#!/bin/bash

#LIBEXEC=$PREFIX/libexec
TEST_DIR=$PREFIX/test/mafft

# make a libexec directory
#mkdir -p $LIBEXEC
mkdir -p $TEST_DIR

# copy test data to location
cp $SRC_DIR/test/* $TEST_DIR/

# go to source location for build
cd $SRC_DIR/core

# export prefix to temp variable so makefile
# will pick it up
export PRFX=$PREFIX
make all
make install
