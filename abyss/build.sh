#!/bin/bash

# go to source location
cd $SRC_DIR

./configure --prefix=$PREFIX --with-boost=$PREFIX/include
make AM_CXXFLAGS=-Wall
make install
