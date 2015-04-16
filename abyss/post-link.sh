platform='unknown'
unamestr=$(uname)
if [[ "$unamestr" == 'Linux' ]]; then
    sed -i'' 's|#!/usr/bin/make -rRf|#!'$PREFIX'/bin/condaflmake -rRf|' $PREFIX/bin/abyss-pe
elif [[ "$unamestr" == 'Darwin' ]]; then
    sed -i '' 's|#!/usr/bin/make -rRf|#!'$PREFIX'/bin/condaflmake -rRf|' $PREFIX/bin/abyss-pe
fi
