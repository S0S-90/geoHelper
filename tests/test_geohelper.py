import unittest
import datetime
import sys
sys.path.append('../src/') # path to source file (geohelper.py)
from StringIO import StringIO

import geohelper

saved_stdout = sys.stdout # save standard output

class TestInit(unittest.TestCase):

    def test_no_logfile_geocaches(self):
        x = geohelper.GPS_content(r"examples\no_logfile")
        number_of_geocaches = len(x.geocaches)
        self.assertEqual(number_of_geocaches,6)

def create_testsuite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestInit))
    return suite

def main(v):
    sys.stdout = saved_stdout  # print output to display
    print "\nTesting geohelper.py"
    out = StringIO()
    sys.stdout = out   # don't print output
    testsuite = create_testsuite()
    unittest.TextTestRunner(verbosity=v).run(testsuite)  

if __name__ == '__main__':
    main(2)
