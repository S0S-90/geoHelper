#!/usr/bin/python
# -*- coding: utf-8 -*-

"""main file for testing"""

from __future__ import print_function
import sys
import time

import test_ownfunctions
import test_geocache
import test_user_io
import test_gpscontent

saved_stdout = sys.stdout  # save standard output

if len(sys.argv) > 1:      # if script is run with argument
    verbosity = int(sys.argv[1])
else:                      # if no argument -> verbosity 1
    verbosity = 1

start_time = time.clock()

a = test_ownfunctions.main(verbosity)   # perform tests
b = test_geocache.main(verbosity)
c = test_user_io.main(verbosity)
d = test_gpscontent.main(verbosity)

end_time = time.clock()
time_needed = end_time - start_time


def passed(test_list):
    """find number of passed tests from a list [testsRuns, testFailures, testErrors]"""
    return test_list[0] - (test_list[1] + test_list[2])

sys.stdout = saved_stdout  # print output to display

print("\nFinished testing. Summary:")
print ("-----------------------------")
print ("{} tests in ownfunctions.py, {} OK, {} failed and {} errors".format(a[0], passed(a), a[1], a[2]))
print ("{} tests in geocache.py, {} OK, {} failed and {} errors".format(b[0], passed(b), b[1], b[2]))
print ("{} tests in user_io.py, {} OK, {} failed and {} errors".format(c[0], passed(c), c[1], c[2]))
print ("{} tests in gpscontent.py, {} OK, {} failed and {} errors".format(d[0], passed(d), d[1], d[2]))
print ("---------------------------------------------------------------")
print ("Total: {} tests, {} OK, {} failed and {} errors".format(a[0]+b[0]+c[0]+d[0], passed(a)+passed(b)+passed(c)
                                                                + passed(d), a[1]+b[1]+c[1]+d[1], a[2]+b[2]+c[2]+d[2]))
print ("Time needed: {:0.2f} seconds".format(time_needed))
