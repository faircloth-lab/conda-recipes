#!/bin/bash

BINARY_HOME=$PREFIX
./configure --prefix=$PREFIX
make
make install
