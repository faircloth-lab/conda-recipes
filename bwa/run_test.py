#!/usr/bin/env python
# encoding: utf-8
"""
File: run_test.py
Author: Brant Faircloth

Created by Brant Faircloth on 23 December 2013 19:08 PST (-0800)
Copyright (c) 2013 Brant C. Faircloth. All rights reserved.

"""

import os
import re
import unittest
import subprocess


class TestAlignments(unittest.TestCase):
    def test_samtools(self):
        cmd = [os.path.join(os.path.join(os.environ["PREFIX"], "bin", "bwa"))]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.stdout, self.stderr = proc.communicate()
        assert self.stderr == "\nProgram: bwa (alignment via Burrows-Wheeler " + \
        "transformation)\nVersion: 0.7.5a-r405\nContact: Heng Li " + \
        "<lh3@sanger.ac.uk>\n\nUsage:   bwa <command> [options]\n\nCommand: " + \
        "index         index sequences in the FASTA format\n         mem    " + \
        "       BWA-MEM algorithm\n         fastmap       identify " + \
        "super-maximal exact matches\n         pemerge       merge overlapping " + \
        "paired ends (EXPERIMENTAL)\n         aln           gapped/ungapped " + \
        "alignment\n         samse         generate alignment (single ended)\n" + \
        "         sampe         generate alignment (paired ended)\n         " + \
        "bwasw         BWA-SW for long queries\n\n         fa2pac        " + \
        "convert FASTA to PAC format\n         pac2bwt       generate BWT " + \
        "from PAC\n         pac2bwtgen    alternative algorithm for generating " + \
        "BWT\n         bwtupdate     update .bwt to the new format\n         " + \
        "bwt2sa        generate SA from BWT and Occ\n\nNote: To use BWA, you " + \
        "need to first index the genome with `bwa index'. There are\n      " + \
        "three alignment algorithms in BWA: `mem', `bwasw' and " + \
        "`aln/samse/sampe'. If\n      you are not sure which to use, try " + \
        "`bwa mem' first. Please `man ./bwa.1' for\n      for the manual.\n\n"

if __name__ == '__main__':
    unittest.main()
