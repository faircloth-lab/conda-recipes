#!/bin/bash

BINARY=Trinity
BINARY_HOME=$PREFIX/bin
TRINITY_HOME=$PREFIX/bin/trinity-$PKG_VERSION
TRINITY_EXE=$TRINITY_HOME/Trinity

# go to trinity
cd $SRC_DIR

# remove the sample data
rm -rf $SRC_DIR/sample_data

# build source
make

# copy source to bin
mkdir -p $TRINITY_HOME
cp -R $SRC_DIR/* $TRINITY_HOME/
cd $TRINITY_HOME && chmod +x Trinity
cd $BINARY_HOME && ln -s trinity-$PKG_VERSION/Trinity $BINARY
