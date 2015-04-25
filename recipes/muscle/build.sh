#!/bin/bash

BINARY1=muscle
BINARY_HOME=$PREFIX/bin

# go to source location
MUSCLE_SRC=$SRC_DIR/src
cd $MUSCLE_SRC

make

# copy source to bin
mkdir -p $BINARY_HOME
cp $MUSCLE_SRC/$BINARY1 $BINARY_HOME/
chmod +x $BINARY_HOME/$BINARY1
