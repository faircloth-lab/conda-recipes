#!/bin/bash

BINARY=sickle
BINARY_HOME=$PREFIX/bin
POST_LINK=$BINARY_HOME/$BINARY

# go to scythe checkout
cd $SRC_DIR

# checkout appropriate commit for current version 1.3a
# (incorporates usage change to 1.2 tagged release)
git checkout bab15f7d14b06400be37d50df7c092b1ec6fe0c5 -b bab15f7d14

# build source
make

# copy source to bin
mkdir $BINARY_HOME
cp $SRC_DIR/$BINARY $POST_LINK
chmod +x $POST_LINK
