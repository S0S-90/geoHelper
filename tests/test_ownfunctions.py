import unittest
import sys
sys.path.append('../src/') # path to source file (ownfunctions.py)

import ownfunctions  

class TestZeichenErsetzen(unittest.TestCase):

    def test_hallo(self):
        x = ownfunctions.zeichen_ersetzen("hallo")
        self.assertEqual(x,"hallo")
        
    def test_maerchen(self):
        x = ownfunctions.zeichen_ersetzen(u"m{}rchen".format(u"\u00E4"))
        self.assertEqual(x, u"m{}rchen".format(u"\u00E4"))
        
    def test_hyphen_u2013(self):
        x = ownfunctions.zeichen_ersetzen(u"hey {} was geht?".format(u"\u2013"))
        self.assertEqual(x, u"hey - was geht?")
        
    def test_smiley_u263a(self):
        x = ownfunctions.zeichen_ersetzen(u"hallo {}".format(u"\u263a"))
        self.assertEqual(x, u"hallo :-)")
    
    def test_sum_u2211(self):
        x = ownfunctions.zeichen_ersetzen(u"{}(1,2,3,4)".format(u"\u2211"))
        self.assertEqual(x, u"sum(1,2,3,4)")
        
    def test_squareroot_u221a(self):
        x = ownfunctions.zeichen_ersetzen(u"{}(4) = 2".format(u"\u221a"))
        self.assertEqual(x, u"sqrt(4) = 2")
        

class TestBla(unittest.TestCase):  # to be removed
    def test_bla(self):
        self.assertEqual(1,1)
        

def create_testsuite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestZeichenErsetzen))
    suite.addTest(unittest.makeSuite(TestBla))
    return suite

if __name__ == '__main__':
    testsuite = create_testsuite()
    unittest.TextTestRunner(verbosity=2).run(testsuite)
