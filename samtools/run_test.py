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
    def test_samtools(self):
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

    def test_bcftools(self):
        cmd = [os.path.join(os.path.join(os.environ["PREFIX"], "bin", "bcftools"))]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.stdout, self.stderr = proc.communicate()
        assert self.stderr == "\nProgram: bcftools (Tools for data in the " + \
            "VCF/BCF formats)\nVersion: 0.1.19-44428cd\n\nUsage:   bcftools" + \
            " <command> <arguments>\n\nCommand: view      print, extract, " + \
            "convert and call SNPs from BCF\n         index     index BCF\n" + \
            "         cat       concatenate BCFs\n         ld        compute " + \
            "all-pair r^2\n         ldpair    compute r^2 between requested " + \
            "pairs\n\n"

    def test_vcfutils(self):
        cmd = [os.path.join(os.path.join(os.environ["PREFIX"], "bin", "vcfutils.pl"))]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.stdout, self.stderr = proc.communicate()
        assert self.stderr == "\nUsage:   vcfutils.pl <command> [<arguments>]" + \
        "\n\nCommand: subsam       get a subset of samples\n         listsam" + \
        "      list the samples\n         fillac       fill the allele count " + \
        "field\n         qstats       SNP stats stratified by QUAL\n\n         " + \
        "hapmap2vcf   convert the hapmap format to VCF\n         ucscsnp2vcf  " + \
        "convert UCSC SNP SQL dump to VCF\n\n         varFilter    filtering " + \
        "short variants (*)\n         vcf2fq       VCF->fastq (**)\n\nNotes: " + \
        "Commands with description endting with (*) may need bcftools\n       " + \
        "specific annotations.\n\n"

    def test_wgsim(self):
        cmd = [os.path.join(os.path.join(os.environ["PREFIX"], "bin", "wgsim"))]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.stdout, self.stderr = proc.communicate()
        assert self.stderr == "\nProgram: wgsim (short read simulator)\n" + \
        "Version: 0.3.0\nContact: Heng Li <lh3@sanger.ac.uk>\n\nUsage:   wgsim" + \
        " [options] <in.ref.fa> <out.read1.fq> <out.read2.fq>\n\nOptions: " + \
        "-e FLOAT      base error rate [0.020]\n         -d INT        outer " + \
        "distance between the two ends [500]\n         -s INT        standard " + \
        "deviation [50]\n         -N INT        number of read pairs [1000000]" + \
        "\n         -1 INT        length of the first read [70]\n         -2 " + \
        "INT        length of the second read [70]\n         -r FLOAT      " + \
        "rate of mutations [0.0010]\n         -R FLOAT      fraction of " + \
        "indels [0.15]\n         -X FLOAT      probability an indel is " + \
        "extended [0.30]\n         -S INT        seed for random generator " + \
        "[-1]\n         -h            haplotype mode\n\n"


if __name__ == '__main__':
    unittest.main()
