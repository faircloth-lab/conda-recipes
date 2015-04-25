#!/bin/bash

# go to source location
cd $SRC_DIR

./configure --prefix=$PREFIX
make
make install
