#!/bin/bash

BINARY_HOME=$PREFIX/bin

# go to source location
cd $SRC_DIR

# make
make

# copy source to bin
mkdir -p $BINARY_HOME
for i in bowtie bowtie-align-l bowtie-align-s bowtie-build bowtie-build-l bowtie-build-s bowtie-inspect bowtie-inspect-l bowtie-inspect-s;
do
    cp $i $BINARY_HOME;
    chmod +x $i;
done
