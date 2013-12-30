#!/bin/bash

BINARY=scythe
BINARY_HOME=$PREFIX/bin
POST_LINK=$BINARY_HOME/$BINARY

# go to scythe checkout
cd $SRC_DIR

# checkout appropriate commit for current version 0.992
git checkout 9b965ee399a18caf1f96e433f78d405620e3a1df -b 9b965ee399

# build source
make all

# copy source to bin
mkdir $BINARY_HOME
cp $SRC_DIR/$BINARY $POST_LINK
chmod +x $POST_LINK
