#!/bin/bash

BINARY=lastz
BINARY_HOME=$PREFIX/bin
POST_LINK=$BINARY_HOME/$BINARY

# go to lastz
cd $SRC_DIR

# build source
make
make test

# copy source to bin
mkdir $BINARY_HOME
cp $SRC_DIR/src/$BINARY $POST_LINK
chmod +x $POST_LINK
