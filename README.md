# conda-recipes

A selection of recipes for the [conda][1] build system (from the [anaconda][2]
[Python][3] distro) that we use in our [lab].  Most of these packages build 
binaries for external programs or install libraries for external programs, 
rather than specifically building [Python][3] packages.  This is why [conda][1]
is excellent for this task - to help install programs with very long 
dependency chains.  As such, it's largely equal to a cross-platform
[homebrew][4] rather than just a [Python][3] package manger.

## Installing [conda][1]

To install [conda][1], see 
https://store.continuum.io/static/img/Anaconda-Quickstart.pdf. You can install [miniconda][6] if you want a smaller distribution.


## Installing packages

[conda][1] is a binary package manger.  As such, we have built binary versions 
of most/all of the packages in this repository for the following platforms:

* OS X (x86_64) [tested on 10.9]
* Linux (x86_64) [tested on CentOS 6.5 and Ubuntu 14.04]

We do not (at present) support Windows.

### Package repository

Packages build from these recipes are available from the binstar repository: 
https://binstar.org/faircloth-lab. To install packages from this repository 
using [conda][1], edit your `.condarc` file to look like:

    # channel locations. These override conda defaults, i.e., conda will
    # search *only* the channels listed here, in the order given. Use "default"
    # to automatically include all default channels.

    channels:
      - defaults
      - http://conda.binstar.org/faircloth-lab

Then install a given package using:

    conda install <package name>

You can search for specific packages using:

    conda search <package name>

## Package structure

Within your [conda][1] environment, the directory structure should look like:

    Examples/
    Launcher.app
    bin/
    conda-meta/
    docs/
    include/
    jar/ # contains all java *.jar files
    lib/
    libexec/
    python.app/
    share/ # contains additional support files
    test/ # contains text code for certain programs (e.g. mafft)

## Build requirements

Ordinarily, you do not need to build packages from this repo.  We have done
this for you and the binary versions are available from 
https://binstar.org/faircloth-lab (see above).  However, if you are interested
in how we build each package or want to clone/contribute to these build files,
build instructions are below.

### OSX

* anaconda
* OSX Command Line Tools
* cmake
* JAVA (1.7)

### Linux

* anaconda
* Developer tools (`yum groupinstall "Development Tools"`)
* cmake
* JAVA (1.7)

## Building

To build an individual package, use:

    conda build <package name>

## More info

See http://docs.continuum.io/conda/build.html for information on how to make a 
recipe, or just look at the at the [main conda-recipes repo][2], particularly the [sample recipe](https://github.com/ContinuumIO/conda-recipes/tree/master/sample).

[1]: https://github.com/continuumio/conda
[2]: https://github.com/continuumio/anaconda
[3]: http://www.python.org
[4]: http://faircloth-lab.org
[5]: https://github.com/ContinuumIO/conda-recipes
[6]: http://repo.continuum.io/miniconda/
