#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
(c) 2015 Brant Faircloth || http://faircloth-lab.org/
All rights reserved.

This code is distributed under a 3-clause BSD license. Please see
LICENSE.txt for more information.

Created on 17 April 2015 08:46 CDT (-0500)
"""


from phyluce.pth import get_user_path, get_user_param

binary_entries = [
    ["abyss", "abyss", "ABYSS"],
    ["abyss", "abyss", "abyss-pe"],
    ["bowtie", "bowtie", "bowtie",],
    ["bwa", "bwa", "bwa"],
    ["gblocks", "gblocks", "gblocks"],
    ["lastz", "lastz", "lastz"],
    ["mafft", "mafft", "mafft"],
    ["muscle", "muscle", "muscle"],
    ["ngm", "ngm", "ngm"],
    ["raxml", "raxmlHPC-SSE3", "raxmlHPC-SSE3"],
    ["raxml", "raxmlHPC-SSE3","raxmlHPC-PTHREADS-SSE3"],
    ["samtools", "samtools", "samtools"],
    ["trinity", "trinity", "trinity"],
    ["velvet", "velvet", "velvetg"],
    ["velvet", "velvet", "velveth"],
]

param_entries = [
    ["trinity", "max_memory", "24G"],
    ["java", "executable", "java"],
    ["java", "mem", "-Xmx8g"],
    ["java", "jar", "$HOME/anaconda/jar"],
    ["java", "gatk", "GenomeAnalysisTKLite.jar"],
    ["trinity", "max_memory", "8G"],
    ["headers", "trinity", "comp\d+_c\d+_seq\d+|c\d+_g\d+_i\d+|TR\d+\|c\d+_g\d+_i\d+"],
    ["headers", "velvet", "node_\d+"],
]

for binary in binary_entries:
    assert get_user_path[binary[0],binary[1]] == "$HOME/anaconda/bin/{0}".format(binary[2])

for param in param_entries:
    assert get_user_param[param[0],param[1]] == "$HOME/anaconda/bin/{0}".format(param[2])
