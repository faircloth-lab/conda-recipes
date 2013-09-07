#!/bin/bash

BINARY=scythe
BINARY_HOME=$PREFIX/bin
POST_LINK=$BINARY_HOME/$BINARY

# go to scythe checkout
cd $SRC_DIR

# checkout appropriate commit for current version 0.991
git checkout fb3114743e59c6255b2f2a3bacced9816aef46fe -b fb3114743e

# build source
make all

# copy source to bin
mkdir $BINARY_HOME
cp $SRC_DIR/$BINARY $POST_LINK
chmod +x $POST_LINK
