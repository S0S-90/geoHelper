import unittest
import datetime
import sys
sys.path.append('../src/') # path to source file (ownfunctions.py)
from StringIO import StringIO

import user_io  
    
class TestGeneralOutput(unittest.TestCase):

    def test_normaltext(self):
        out = StringIO()
        sys.stdout = out                  # capture print output in out
        user_io.general_output("hallo")   # fill out 
        output = out.getvalue().strip()   # save value of out in output
        self.assertEqual(output, "hallo")
        
    def test_textwithcapitalsandnumbers(self):
        out = StringIO()
        sys.stdout = out                  # capture print output in out
        user_io.general_output("hAllo2")  # fill out 
        output = out.getvalue().strip()   # save value of out in output
        self.assertEqual(output, "hAllo2")
        
    def test_umlaute(self):
        out = StringIO()
        sys.stdout = out                                       # capture print output in out
        user_io.general_output(u"m{}rchen".format(u"\u00E4"))  # fill out 
        output = out.getvalue().strip()                        # save value of out in output
        self.assertEqual(output, u"m{}rchen".format(u"\u00E4"))
        
    def test_replacable_signs(self):
        out = StringIO()
        sys.stdout = out                                        # capture print output in out
        user_io.general_output(u"hallo {}".format(u"\u263a"))   # fill out 
        output = out.getvalue().strip()                         # save value of out in output
        self.assertEqual(output, "hallo :-)")
        
    def test_unknown_signs(self):
        out = StringIO()
        sys.stdout = out                                                    # capture print output in out
        user_io.general_output(u"tuerkische Flagge: {}".format(u"\u262a"))  # fill out 
        output = out.getvalue().strip()                                     # save value of out in output
        self.assertEqual(output, u"tuerkische Flagge: {}".format(u"\u001a"))

class TestGeneralInput(unittest.TestCase):   

    def test_foo(self):
        self.assertEqual(True, True) 
        
def create_testsuite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGeneralOutput))
    suite.addTest(unittest.makeSuite(TestGeneralInput))
    return suite

if __name__ == '__main__':
    testsuite = create_testsuite()
    unittest.TextTestRunner(verbosity=2).run(testsuite)   # set verbosity to 2 if you want to see the name and result of every test
