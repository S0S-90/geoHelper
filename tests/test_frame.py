#!/usr/bin/python
# -*- coding: utf-8 -*-

"""provide general features for running tests, e.g. change the path to the sources folder"""

import unittest
from io import StringIO
import os
import sys

sys.path.append('../src')  # for importing modules
os.chdir('../src')  # switching path for using modules

saved_stdout = sys.stdout  # save standard output


def run(v, testsuite_creating_function, filename):
    """runs the testsuite that is created from testsuite_creating_function with verbosity v
    filename is the name of the file that is currently tested

    return: list [number of testruns, number of failed tests, number of errors in tests]"""

    sys.stdout = saved_stdout  # print output to display
    print("\nTesting {}".format(filename))
    out = StringIO()
    sys.stdout = out
    testsuite = testsuite_creating_function()
    x = unittest.TextTestRunner(verbosity=v).run(testsuite)
    return x.testsRun, len(x.failures), len(x.errors)


def changepath(newpath):
    """adds newpath to path"""
    os.chdir(newpath)
