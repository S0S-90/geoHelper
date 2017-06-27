#!/usr/bin/python
# -*- coding: utf-8 -*-

"""import the path to the source files"""

import unittest
# noinspection PyCompatibility
from StringIO import StringIO  # module not existent in python 3
import sys
sys.path.append('../src/')

saved_stdout = sys.stdout  # save standard output


def run(v, testsuite_creating_function, filename):
    """runs the testsuite that is created from testsuite_creating_function with verbosity v
    filename is the name of the file that is currently tested

    return: list [number of testruns, number of failed tests, number of errors in tests"""
    sys.stdout = saved_stdout  # print output to display
    print("\nTesting {}".format(filename))
    out = StringIO()
    sys.stdout = out
    testsuite = testsuite_creating_function()
    x = unittest.TextTestRunner(verbosity=v).run(testsuite)
    return x.testsRun, len(x.failures), len(x.errors)
