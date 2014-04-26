#!/bin/bash

BINARY_HOME=$PREFIX
./configure --prefix=$PREFIX
make
make install
# rename so it does not conflict w/ local make installs
# make is only needed for abyss...
mv $PREFIX/bin/make $PREFIX/bin/condaflmake
mv $PREFIX/share/info/make.info $PREFIX/share/info/condaflmake.info
mv $PREFIX/share/info/make.info-1 $PREFIX/share/info/condaflmake.info-1
mv $PREFIX/share/info/make.info-2 $PREFIX/share/info/condaflmake.info-2
mv $PREFIX/share/man/man1/make.1 $PREFIX/share/man/man1/condaflmake.1
