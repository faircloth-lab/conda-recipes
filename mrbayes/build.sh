#!/bin/bash

BINARY1=mb
BINARY2=mb-mpi
BINARY_HOME=$PREFIX/bin

# go to source location
MB_SRC=$SRC_DIR/src
cd $MB_SRC

autoconf
./configure --with-beagle=no
make
# copy source to bin
mkdir -p $BINARY_HOME
cp $MB_SRC/$BINARY1 $BINARY_HOME/$BINARY1
chmod +x $BINARY_HOME/$BINARY1

# now build MPI version
if [[ "$OSTYPE" == 'darwin'* ]]; then\
    export MACOSX_DEPLOYMENT_TARGET="10.7"
fi
# clean old src
make distclean
autoconf
./configure --enable-mpi=yes --with-beagle=no
make
# copy that to the binary dir with a diff name
cp $MB_SRC/$BINARY1 $BINARY_HOME/$BINARY2
chmod +x $BINARY_HOME/$BINARY2
