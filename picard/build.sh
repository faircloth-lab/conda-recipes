#!/bin/bash

JAR=$PREFIX/jar

# make a $JAR directory
mkdir -p $JAR

cd $SRC_DIR/picard-tools-*
# move useful files to $JAR, exclude build files
find . -maxdepth 1 -mindepth 1 \
-not -name apache-ant-1.8.2-bzip2.jar \
-not -name commons-jexl-2.1.1.jar \
-not -name commons-logging-1.1.1.jar \
-not -name libIntelDeflater.so \
-not -name picard-1.106.jar \
-not -name sam-1.106.jar \
-not -name snappy-java-1.0.3-rc3.jar \
-not -name tribble-1.106.jar \
-not -name variant-1.106.jar \
-not -name libIntelDeflater.so \
-exec mv '{}' $JAR \;
