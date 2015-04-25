FROM centos:6
MAINTAINER "Brant Faircloth" <brant _at_ faircloth-lab _dot_ org>
ENV container docker

# update yum
RUN yum -y update; yum clean all
# install devtools
RUN yum -y groupinstall "Development tools"
# install wget
RUN yum -y install wget
RUN yum -y install tar
RUN yum -y install gzip
# add build user
RUN useradd -ms /bin/bash build

# switch to build user
USER build
ENV HOME /home/build
WORKDIR /home/build/

# download conda
RUN ["/bin/bash", "-c", "wget http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh -O $HOME/miniconda.sh"]
RUN chmod 0755 $HOME/miniconda.sh
RUN ["/bin/bash", "-c", "$HOME/miniconda.sh -b -p $HOME/conda"]
ENV PATH="$HOME/conda/bin:$PATH"
RUN rm $HOME/miniconda.sh

# update conda
RUN conda update conda
RUN conda install conda-build
RUN conda install binstar

# get conda recipes
RUN mkdir git; cd git
RUN git clone https://github.com/faircloth-lab/conda-recipes.git
