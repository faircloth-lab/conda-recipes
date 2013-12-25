# conda-recipes

A selection of recipes for the [conda][1] build system (from the [anaconda][2]
[Python][3] distro) that we use in our [lab].  Most of these packages build 
binaries for external programs or install libraries for external programs, 
rather than specifically building [Python][3] packages.  This is why [conda][1]
is excellent for this task - to help install programs with very long 
dependency chains.  As such, it's largely equal to a cross-platform
[homebrew][4] rather than just a [Python][3] package manger.

## Installing packages

[conda][1] is a binary package manger.  As such, we have built binary versions 
of most/all of the packages in this repository for the following platforms:

* OS X (x86_64)
* Linux (x86_64)

We do not (at present) support Windows.

### Package repository

All packages builds within are available from: 
https://binstar.org/faircloth-lab

To install packages from this repository using [conda][1], edit your `.condarc`
file to look like:

    # channel locations. These override conda defaults, i.e., conda will
    # search *only* the channels listed here, in the order given. Use "default"
    # to automatically include all default channels.

    channels:
      - defaults
      - http://conda.binstar.org/faircloth-lab

Then install a given package using:

    conda install <package name>

## Build requirements

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
