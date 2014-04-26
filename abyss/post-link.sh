echo $PREFIX
sed -i '' 's|#!\/usr\/bin\/make -rRf|#!'$PREFIX'\/bin\/condaflmake -rRf|' $PREFIX/bin/abyss-pe
