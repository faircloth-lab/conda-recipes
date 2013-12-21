#!/bin/bash

HEADERS=boost
INCLUDE_HOME=$PREFIX/include/$HEADERS

# go to boost src
cd $SRC_DIR

mkdir -p $INCLUDE_HOME
mv boost/* $INCLUDE_HOME/
