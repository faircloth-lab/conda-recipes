#!/usr/bin/env python
# encoding: utf-8
"""
File: run_test.py
Author: Brant Faircloth

Created by Brant Faircloth on 22 December 2013 08:12 PST (-0800)
Copyright (c) 2013 Brant C. Faircloth. All rights reserved.

"""

import os
import pdb
import difflib
import tempfile
import subprocess
import unittest

class TestAlignments(unittest.TestCase):
    def setUp(self):
        self.TEST_DIR = os.path.join(os.environ["PREFIX"], "test", "mafft")
        self.TEST_DATA = os.path.join(self.TEST_DIR, "sample")
        self.BINARY = os.path.join(os.environ["PREFIX"], "bin", "mafft")
        self.expected_results = {}
        alignments = [
                "sample.fftns2",
                "sample.fftnsi",
                "sample.gins1",
                "sample.ginsi",
                "sample.lins1",
                "sample.linsi"
            ]
        for expected in alignments:
            self.expected_results[expected.replace("sample.", "")] = os.path.join(self.TEST_DIR, expected)

    def compare(self, typ, tmp):
        a = open(tmp, 'rU').readlines()
        b = open(self.expected_results[typ], 'rU').readlines()
        delta = ''.join(difflib.unified_diff(a, b))
        assert delta == ''
        os.remove(tmp)

    def test_fftns2(self):
        """Testing fftns2"""
        tmp = tempfile.mkstemp(suffix=".mafft")
        cmd = [
            self.BINARY,
            self.TEST_DATA
        ]
        proc1 = subprocess.Popen(cmd, stdout=tmp[0], stderr=subprocess.PIPE)
        proc1.communicate()
        os.close(tmp[0])
        self.compare("fftns2", tmp[1])

    def test_fftnsi(self):
        """Testing fftnsi"""
        tmp = tempfile.mkstemp(suffix=".mafft")
        cmd = [
            self.BINARY,
            "--maxiterate",
            "100",
            self.TEST_DATA
        ]
        proc1 = subprocess.Popen(cmd, stdout=tmp[0], stderr=subprocess.PIPE)
        proc1.communicate()
        os.close(tmp[0])
        self.compare("fftnsi", tmp[1])

    def test_gins1(self):
        """Testing gins1"""
        tmp = tempfile.mkstemp(suffix=".mafft")
        cmd = [
            self.BINARY,
            "--globalpair",
            self.TEST_DATA
        ]
        proc1 = subprocess.Popen(cmd, stdout=tmp[0], stderr=subprocess.PIPE)
        proc1.communicate()
        os.close(tmp[0])
        self.compare("gins1", tmp[1])

    def test_ginsi(self):
        """Testing ginsi"""
        tmp = tempfile.mkstemp(suffix=".mafft")
        cmd = [
            self.BINARY,
            "--globalpair",
            "--maxiterate",
            "100",
            self.TEST_DATA
        ]
        proc1 = subprocess.Popen(cmd, stdout=tmp[0], stderr=subprocess.PIPE)
        proc1.communicate()
        os.close(tmp[0])
        self.compare("ginsi", tmp[1])

    def test_lins1(self):
        """Testing lins1"""
        tmp = tempfile.mkstemp(suffix=".mafft")
        cmd = [
            self.BINARY,
            "--localpair",
            self.TEST_DATA
        ]
        proc1 = subprocess.Popen(cmd, stdout=tmp[0], stderr=subprocess.PIPE)
        proc1.communicate()
        os.close(tmp[0])
        self.compare("lins1", tmp[1])

    def test_lins1(self):
        """Testing linsi"""
        tmp = tempfile.mkstemp(suffix=".mafft")
        cmd = [
            self.BINARY,
            "--localpair",
            "--maxiterate",
            "100",
            self.TEST_DATA
        ]
        proc1 = subprocess.Popen(cmd, stdout=tmp[0], stderr=subprocess.PIPE)
        proc1.communicate()
        os.close(tmp[0])
        self.compare("linsi", tmp[1])

if __name__ == '__main__':
    unittest.main()
