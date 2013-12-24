#!/bin/bash

BINARY1=samtools
BINARY_HOME=$PREFIX/bin

# go to build
cd $SRC_DIR

# build source
make

# copy source to bin
mkdir -p $BINARY_HOME
cp $SRC_DIR/$BINARY1 $BINARY_HOME/
chmod +x $BINARY_HOME/$BINARY1
