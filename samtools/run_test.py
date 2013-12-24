#!/usr/bin/env python
# encoding: utf-8
"""
File: run_test.py
Author: Brant Faircloth

Created by Brant Faircloth on 23 December 2013 16:22 PST (-0800)
Copyright (c) 2013 Brant C. Faircloth. All rights reserved.

"""

import os
import re
import unittest
import subprocess


class TestAlignments(unittest.TestCase):
    def test_trimmomatic(self):
        cmd = [os.path.join(os.path.join(os.environ["PREFIX"], "bin", "samtools"))]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.stdout, self.stderr = proc.communicate()
        assert self.stderr == "\nProgram: samtools (Tools for alignments in the " + \
        "SAM format)\nVersion: 0.1.19-44428cd\n\nUsage:   samtools <command> " + \
        "[options]\n\nCommand: view        SAM<->BAM conversion\n         sort" + \
        "        sort alignment file\n         mpileup     multi-way pileup\n" + \
        "         depth       compute the depth\n         faidx       " + \
        "index/extract FASTA\n         tview       text alignment viewer\n" + \
        "         index       index alignment\n         idxstats    BAM index " + \
        "stats (r595 or later)\n         fixmate     fix mate information\n" + \
        "         flagstat    simple stats\n         calmd       recalculate " + \
        "MD/NM tags and '=' bases\n         merge       merge sorted " + \
        "alignments\n         rmdup       remove PCR duplicates\n         " + \
        "reheader    replace BAM header\n         cat         concatenate " + \
        "BAMs\n         bedcov      read depth per BED region\n         " + \
        "targetcut   cut fosmid regions (for fosmid pool only)\n         " + \
        "phase       phase heterozygotes\n         bamshuf     shuffle and" + \
        " group alignments by name\n\n"

if __name__ == '__main__':
    unittest.main()
