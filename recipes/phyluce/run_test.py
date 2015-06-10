#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
(c) 2015 Brant Faircloth || http://faircloth-lab.org/
All rights reserved.

This code is distributed under a 3-clause BSD license. Please see
LICENSE.txt for more information.

Created on 17 April 2015 08:46 CDT (-0500)
"""

import os
import sys
import unittest
from phyluce.pth import get_user_path, get_user_param

class TestBinaries(unittest.TestCase):
    def setUp(self):
        self.binaries = [
            ["abyss", "abyss", "ABYSS"],
            ["abyss", "abyss-pe", "abyss-pe"],
            ["bowtie", "bowtie", "bowtie",],
            ["bwa", "bwa", "bwa"],
            ["gblocks", "gblocks", "gblocks"],
            ["lastz", "lastz", "lastz"],
            ["mafft", "mafft", "mafft"],
            ["muscle", "muscle", "muscle"],
            ["raxml", "raxmlHPC-SSE3", "raxmlHPC-SSE3"],
            ["raxml", "raxmlHPC-PTHREADS-SSE3","raxmlHPC-PTHREADS-SSE3"],
            ["samtools", "samtools", "samtools"],
            ["trinity", "trinity", "Trinity"],
            ["velvet", "velvetg", "velvetg"],
            ["velvet", "velveth", "velveth"],
        ]
        self.parameters = [
            ["trinity", "max_memory", "8G"],
            ["java", "executable", "java"],
            ["java", "mem", "-Xmx8g"],
            ["java", "gatk", "GenomeAnalysisTKLite.jar"],
            ["trinity", "max_memory", "8G"],
            ["headers", "trinity", "comp\d+_c\d+_seq\d+|c\d+_g\d+_i\d+|TR\d+\|c\d+_g\d+_i\d+"],
            ["headers", "velvet", "node_\d+"],
        ]
        self.directories = [
            ["java", "jar"],
        ]

    def test_config_binaries(self):
        """Test that config is properly located"""
        for program in self.binaries:
            binary = get_user_path(program[0], program[1], package_only=True)
            expected = os.path.join(sys.prefix, "bin", program[2])
            self.assertEqual(
                binary,
                expected,
                "Config entry {} != {} (expected)".format(binary, expected)
            )

    def test_config_parameters(self):
        """Test that config parameters exist"""
        for parameter in self.parameters:
            param = get_user_param(parameter[0], parameter[1])
            expected = parameter[2]
            self.assertEqual(
                param,
                expected,
                "Config entry {} != {} (expected)".format(param, expected)
            )

    def test_config_directories(self):
        for directory in self.directories:
            param = get_user_path(directory[0], directory[1], package_only=True)
            expected = os.path.join(sys.prefix, directory[1])
            self.assertEqual(
                param,
                expected,
                "Directory {} is missing".format(directory[1])
            )

    def test_config_directories_exist(self):
        for directory in self.directories:
            param = get_user_path(directory[0], directory[1], package_only=True)
            self.assertTrue(
                os.path.isdir(param),
                "Directory {} is missing".format(param)
            )

    def test_binaries_exist(self):
        """Test that binaries in config are properly located"""
        for program in self.binaries:
            binary = get_user_path(program[0], program[1], package_only=True)
            self.assertTrue(os.path.isfile(binary) and os.access(binary, os.X_OK),
                "Binary {} is missing".format(binary)
            )


if __name__ == '__main__':
    unittest.main()
