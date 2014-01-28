#!/bin/bash

JAR=$PREFIX/jar

# make a $JAR directory
mkdir -p $JAR

# copy to location
cp $SRC_DIR/GenomeAnalysisTKLite.jar $JAR/
