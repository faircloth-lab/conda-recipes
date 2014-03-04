#!/usr/bin/env python
# encoding: utf-8
"""
File: run_test.py
Author: Brant Faircloth

Created by Brant Faircloth on 23 December 2013 19:08 PST (-0800)
Copyright (c) 2013 Brant C. Faircloth. All rights reserved.

"""

import os
import unittest
import subprocess


class TestAlignments(unittest.TestCase):
    def test_samtools(self):
        cmd = [os.path.join(os.path.join(os.environ["PREFIX"], "bin", "bwa"))]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.stdout, self.stderr = proc.communicate()
        stderr = self.stderr.split("\n")
        assert stderr[1] == "Program: bwa (alignment via Burrows-Wheeler transformation)"
        assert stderr[2] == "Version: 0.7.7-r441"

if __name__ == '__main__':
    unittest.main()
