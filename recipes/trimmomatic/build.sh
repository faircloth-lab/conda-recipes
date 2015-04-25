#!/bin/bash

JAR=$PREFIX/jar
SHARE_DIR=$PREFIX/share

# make a libexec directory
mkdir -p $JAR

# copy to location
cp $SRC_DIR/trimmomatic* $JAR/trimmomatic.jar
# put supporting adapter sequences in "share"
cp -R $SRC_DIR/adapters $SHARE_DIR
