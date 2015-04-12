#!/bin/bash

BINARY=gblocks
BINARY_HOME=$PREFIX/bin
GBLOCKS_HOME=$BINARY_HOME/$BINARY-$PKG_VERSION
GBLOCKS_EXE=$TRINITY_HOME/Gblocks

# go to build
cd $SRC_DIR

# detect os and copy correct files for platform
platform='unknown'
unamestr=`uname`
if [[ "$unamestr" == 'Linux' ]]; then
    mkdir -p $GBLOCKS_HOME
    cp -R $SRC_DIR/Gblocks_0.91b-linux64/* $GBLOCKS_HOME/
elif [[ "$unamestr" == 'Darwin' ]]; then
    mkdir -p $GBLOCKS_HOME
    cp -R $SRC_DIR/Gblocks_0.91b-osx/* $GBLOCKS_HOME/
fi

cd $GBLOCKS_HOME/ && chmod +x Gblocks
cd $BINARY_HOME && ln -s gblocks-$PKG_VERSION/Gblocks $BINARY
