#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
(c) 2013 Brant Faircloth || http://faircloth-lab.org/
All rights reserved.

This code is distributed under a 3-clause BSD license. Please see
LICENSE.txt for more information.

Created on 30 December 2013 16:33 PST (-0800)
"""

import unittest
import subprocess


class TestMb(unittest.TestCase):
    def test_mb(self):
        cmd = ["mb", "-h"]
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        self.stdout, self.stderr = proc.communicate()
        text = [v.strip() for k, v in enumerate(self.stdout.split("\n"))
                if k in range(0, 6, 2)]
        assert text == [
            '',
            'MrBayes v3.2.2 x64',
            '(Bayesian Analysis of Phylogeny)'
        ]


class TestMbMpi(unittest.TestCase):
    def test_mb(self):
        cmd = ["mb-mpi", "-h"]
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        self.stdout, self.stderr = proc.communicate()
        text = [v.strip() for k, v in enumerate(self.stdout.split("\n"))
                if k in range(0, 6, 2)]
        assert text == [
            'MrBayes v3.2.2 x64',
            '(Bayesian Analysis of Phylogeny)',
            '(Parallel version)'
        ]

if __name__ == '__main__':
    unittest.main()
