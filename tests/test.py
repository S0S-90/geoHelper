import sys

import test_ownfunctions
import test_geocache
import test_user_io
import test_gpscontent

saved_stdout = sys.stdout # save standard output

verbosity = input("Verbosity (1 oder 2): ")

a = test_ownfunctions.main(verbosity)
b = test_geocache.main(verbosity)
c = test_user_io.main(verbosity)
d = test_gpscontent.main(verbosity)


def passed(test_list):
    """find number of passed tests from a list [testsRuns, testFailures, testErrors]"""
    return test_list[0] - (test_list[1] + test_list[2])

sys.stdout = saved_stdout # print output to display
print "\nFinished testing. Summary:"
print "{} tests in ownfunctions.py, {} OK, {} failed and {} errors".format(a[0], passed(a), a[1], a[2])
print "{} tests in geocache.py, {} OK, {} failed and {} errors".format(b[0], passed(b), b[1], b[2])
print "{} tests in user_io.py, {} OK, {} failed and {} errors".format(c[0], passed(c), c[1], c[2])
print "{} tests in gpscontent.py, {} OK, {} failed and {} errors".format(d[0], passed(d), d[1], d[2])
print "Total: {} tests, {} OK, {} failed and {} errors".format(a[0]+b[0]+c[0]+d[0], passed(a)+passed(b)+passed(c)+passed(d), a[1]+b[1]+c[1]+d[1], a[2]+b[2]+c[2]+d[2])