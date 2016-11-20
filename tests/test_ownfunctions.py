import unittest
import sys
sys.path.append('../src/') # path to source file (ownfunctions.py)

import ownfunctions  

class TestZeichenErsetzen(unittest.TestCase):

    def test_hallo(self):
        x = ownfunctions.zeichen_ersetzen("hallo", ownfunctions.ALLOWED_SIGNS)
        self.assertEqual(x,"hallo")
        
    def test_maerchen(self):
        x = ownfunctions.zeichen_ersetzen(u"m{}rchen".format(u"\u00E4"), ownfunctions.ALLOWED_SIGNS)
        self.assertEqual(x, u"m{}rchen".format(u"\u00E4"))
        
    def test_smiley_u263a(self):
        x = ownfunctions.zeichen_ersetzen(u"hallo {}".format(u"\u263a"), ownfunctions.ALLOWED_SIGNS)
        self.assertEqual(x, u"hallo :-)")
    
    def test_sum_u2211(self):
        x = ownfunctions.zeichen_ersetzen(u"{}(1,2,3,4)".format(u"\u2211"), ownfunctions.ALLOWED_SIGNS)
        self.assertEqual(x, u"sum(1,2,3,4)")
        
    def test_squareroot_u221a(self):
        x = ownfunctions.zeichen_ersetzen(u"{}(4) = 2".format(u"\u221a"), ownfunctions.ALLOWED_SIGNS)
        self.assertEqual(x, u"sqrt(4) = 2")
        
    def test_newline(self):
        x = ownfunctions.zeichen_ersetzen(u"hallo\nWelt", ownfunctions.ALLOWED_SIGNS)
        self.assertEqual(x, u"hallo\nWelt")
        
    def test_tab(self):
        x = ownfunctions.zeichen_ersetzen(u"hallo\tWelt\v", ownfunctions.ALLOWED_SIGNS)
        self.assertEqual(x, u"hallo\tWelt\v")
    
    def test_unknown_sign(self):
        x = ownfunctions.zeichen_ersetzen(u"tuerkische Flagge: {}".format(u"\u262a"), ownfunctions.ALLOWED_SIGNS)
        self.assertEqual(x, u"tuerkische Flagge: {}".format(u"\u001a"))

class TestKoordinatenDezimalgradToMinuten(unittest.TestCase):  
    
    def test_north_east_coords(self):
        x = ownfunctions.koordinaten_dezimalgrad_to_minuten([52.520817,13.40945])
        self.assertEqual(x, u"N 52°31.249, E 013°24.567")
        
    def test_south_west(self):
        pass
        
    def test_equator(self):
        pass
        
    def test_zero_meridian(self):
        pass
        
    def test_north_bigger_than_90(self):
        pass
        
    def test_east_bigger_than_180(self):
        pass
        

def create_testsuite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestZeichenErsetzen))
    suite.addTest(unittest.makeSuite(TestKoordinatenDezimalgradToMinuten))
    return suite

if __name__ == '__main__':
    testsuite = create_testsuite()
    unittest.TextTestRunner(verbosity=2).run(testsuite)
