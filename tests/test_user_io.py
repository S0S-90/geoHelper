import unittest
import datetime
import sys
sys.path.append('../src/') # path to source file (user_io.py)
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

    def test_normaltext(self):
        original_raw_input = __builtins__.raw_input  # save original raw_input function
        __builtins__.raw_input = lambda _: 'hello'   # mock raw_input 
        self.assertEqual(user_io.general_input(">> "), 'hello')
        __builtins__.raw_input = original_raw_input  # activate original raw_input function again
        
    def test_textwithcapitalsandnumbers(self):
        original_raw_input = __builtins__.raw_input  # save original raw_input function
        __builtins__.raw_input = lambda _: 'hAllo2'   # mock raw_input 
        self.assertEqual(user_io.general_input(">> "), 'hAllo2')
        __builtins__.raw_input = original_raw_input  # activate original raw_input function again
        
    def test_replacable_signs(self):
        original_raw_input = __builtins__.raw_input  # save original raw_input function
        __builtins__.raw_input = lambda _: u"hallo {}".format(u"\u263a")   # mock raw_input 
        self.assertEqual(user_io.general_input(">> "), u"hallo {}".format(u"\u263a"))
        __builtins__.raw_input = original_raw_input  # activate original raw_input function again
        
    def test_umlaute(self):
        original_raw_input = __builtins__.raw_input  # save original raw_input function
        __builtins__.raw_input = lambda _: u"m{}rchen".format(u"\u00E4")   # mock raw_input 
        self.assertEqual(user_io.general_input(">> "), u"m{}rchen".format(u"\u00E4"))
        __builtins__.raw_input = original_raw_input  # activate original raw_input function again
        
    def test_unknown_signs(self):
        original_raw_input = __builtins__.raw_input  # save original raw_input function
        __builtins__.raw_input = lambda _: u"tuerkische Flagge: {}".format(u"\u262a")   # mock raw_input 
        self.assertEqual(user_io.general_input(">> "), u"tuerkische Flagge: {}".format(u"\u262a"))
        __builtins__.raw_input = original_raw_input  # activate original raw_input function again
        
    def test_number(self):
        original_raw_input = __builtins__.raw_input  # save original raw_input function
        __builtins__.raw_input = lambda _: "42"   # mock raw_input 
        self.assertEqual(user_io.general_input(">> "), "42")
        __builtins__.raw_input = original_raw_input  # activate original raw_input function again
        
class TestInputDecode(unittest.TestCase):   

    def test_normaltext(self):
        original_raw_input = __builtins__.raw_input  # save original raw_input function
        __builtins__.raw_input = lambda _: 'hello'   # mock raw_input 
        self.assertEqual(user_io.input_decode(">> "), 'hello')
        __builtins__.raw_input = original_raw_input  # activate original raw_input function again
        
    def test_textwithcapitalsandnumbers(self):
        original_raw_input = __builtins__.raw_input  # save original raw_input function
        __builtins__.raw_input = lambda _: 'hAllo2'   # mock raw_input 
        self.assertEqual(user_io.input_decode(">> "), 'hAllo2')
        __builtins__.raw_input = original_raw_input  # activate original raw_input function again
        
    def test_replacable_signs(self):
        original_raw_input = __builtins__.raw_input  # save original raw_input function
        __builtins__.raw_input = lambda _: "hallo {}".format(u"\u263a")   # mock raw_input 
        self.assertRaises(UnicodeEncodeError, user_io.input_decode, ">> ")
        __builtins__.raw_input = original_raw_input  # activate original raw_input function again
        
    def test_umlaute(self):
        original_raw_input = __builtins__.raw_input  # save original raw_input function
        __builtins__.raw_input = lambda _: 'M\xe4rchen'   # mock raw_input 
        self.assertEqual(user_io.input_decode(">> "), u"Märchen")
        __builtins__.raw_input = original_raw_input  # activate original raw_input function again
        
    def test_unknown_signs(self):
        original_raw_input = __builtins__.raw_input  # save original raw_input function
        __builtins__.raw_input = lambda _: u"tuerkische Flagge: {}".format(u"\u262a")   # mock raw_input 
        self.assertRaises(UnicodeEncodeError, user_io.input_decode, ">> ")
        __builtins__.raw_input = original_raw_input  # activate original raw_input function again
        
    def test_number(self):
        original_raw_input = __builtins__.raw_input  # save original raw_input function
        __builtins__.raw_input = lambda _: "42"   # mock raw_input 
        self.assertEqual(user_io.input_decode(">> "), "42")
        __builtins__.raw_input = original_raw_input  # activate original raw_input function again
        
class TestHauptmenue(unittest.TestCase):
    pass
        
def create_testsuite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGeneralOutput))
    suite.addTest(unittest.makeSuite(TestGeneralInput))
    suite.addTest(unittest.makeSuite(TestInputDecode))
    suite.addTest(unittest.makeSuite(TestHauptmenue))
    return suite

if __name__ == '__main__':
    testsuite = create_testsuite()
    unittest.TextTestRunner(verbosity=2).run(testsuite)   # set verbosity to 2 if you want to see the name and result of every test and to 1 if you don't
