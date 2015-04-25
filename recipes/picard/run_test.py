#!/usr/bin/env python
# encoding: utf-8
"""
File: run_test.py
Author: Brant Faircloth

Created by Brant Faircloth on 22 December 2013 11:12 PST (-0800)
Copyright (c) 2013 Brant C. Faircloth. All rights reserved.

"""

import os
import re
import unittest
import subprocess


class TestAlignments(unittest.TestCase):
    def setUp(self):
        cmd = ["java", "-version"]
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        self.stdout, self.stderr = proc.communicate()
        self.result_split = self.stderr.strip().split("\n")

    def get_version(self, s):
        result = re.search('java version "(.*)"', s)
        return result.groups()[0].split(".")

    def test_install(self):
        assert self.result_split[0].startswith("java version"), "Java does not appear to be installed"

    def test_version(self):
        version = self.get_version(self.result_split[0])
        assert (version[:2] == ["1", "6"] or version[:2] == ["1", "7"]), "Java does not appear to be 1.6 or 1.7"

    def test_trimmomatic(self):
        cmd = [
            "java",
            "-jar",
            os.path.join(os.path.join(
                os.environ["PREFIX"], "jar", "CleanSam.jar", "--version")
            ),
            "--help"
        ]
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        self.stdout, self.stderr = proc.communicate()
        assert self.stderr == "1.106(1655)\n"
