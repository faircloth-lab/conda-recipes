#!/bin/bash

BINARY1=raxmlHPC-PTHREADS-SSE3
BINARY2=raxmlHPC-SSE3
BINARY_HOME=$PREFIX/bin

# go to source location
cd $SRC_DIR

# check for OSX, then compile:
if [[ "$OSTYPE" == 'darwin'* ]]; then
    make -f Makefile.SSE3.PTHREADS.mac
    rm *.o
    make -f Makefile.SSE3.mac
    rm *.o
else
    make -f Makefile.SSE3.PTHREADS.gcc
    rm *.o
    make -f Makefile.SSE3.gcc
    rm *.o
fi

# copy source to bin
mkdir -p $BINARY_HOME
cp $SRC_DIR/$BINARY1 $BINARY_HOME/
cp $SRC_DIR/$BINARY2 $BINARY_HOME/
chmod +x $BINARY_HOME/$BINARY1
chmod +x $BINARY_HOME/$BINARY2
