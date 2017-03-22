import sys

import test_ownfunctions
import test_geocache
import test_user_io
import test_main

saved_stdout = sys.stdout # save standard output

verbosity = input("Verbosity (1 oder 2): ")

a = test_ownfunctions.main(verbosity)
b = test_geocache.main(verbosity)
c = test_user_io.main(verbosity)
d = test_main.main(verbosity)

def passed(test_list):
    """find number of passed tests from a list [testsRuns, testFailures, testErrors]"""
    return test_list[0] - (test_list[1] + test_list[2])

sys.stdout = saved_stdout # print output to display
print "\nTesten beendet. Zusammenfassung:"
print "{} Tests in ownfunctions.py, davon {} erfolgreich, {} fehlgeschlagen und {} abgebrochen".format(a[0], passed(a), a[1], a[2])
print "{} Tests in geocache.py, davon {} erfolgreich, {} fehlgeschlagen und {} abgebrochen".format(b[0], passed(b), b[1], b[2])
print "{} Tests in user_io.py, davon {} erfolgreich, {} fehlgeschlagen und {} abgebrochen".format(c[0], passed(c), c[1], c[2])
print "{} Tests in geohelper.py, davon {} erfolgreich, {} fehlgeschlagen und {} abgebrochen".format(d[0], passed(d), d[1], d[2])
print "Gesamt: {} Tests, davon {} erfolgreich, {} fehlgeschlagen und {} abgebrochen".format(a[0]+b[0]+c[0]+d[0], passed(a)+passed(b)+passed(c)+passed(d), a[1]+b[1]+c[1]+d[1], a[2]+b[2]+c[2]+d[2])