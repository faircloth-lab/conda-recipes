#!/bin/bash

BINARY1=velveth
BINARY2=velvetg
BINARY_HOME=$PREFIX/bin

# go to build
cd $SRC_DIR

# build source
make
make test

# copy source to bin
mkdir $BINARY_HOME
cp $SRC_DIR/$BINARY1 $BINARY_HOME
cp $SRC_DIR/$BINARY2 $BINARY_HOME
chmod +x $BINARY_HOME/$BINARY1
chmod +x $BINARY_HOME/$BINARY2
