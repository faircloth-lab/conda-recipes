#!/bin/bash

BINARY1=samtools
BINARY_HOME=$PREFIX/bin

# go to build
cd $SRC_DIR

# build source
make

# copy source to bin
mkdir -p $BINARY_HOME
cp $SRC_DIR/$BINARY1 $BINARY_HOME/
chmod +x $BINARY_HOME/$BINARY1

for PROG in bcftools vcfutils.pl
do
    cp $SRC_DIR/bcftools/$PROG $BINARY_HOME/
    chmod +x $BINARY_HOME/$PROG
done

for PROG in bamcheck wgsim
do
    cp $SRC_DIR/misc/$PROG $BINARY_HOME/
    chmod +x $BINARY_HOME/$PROG
done

