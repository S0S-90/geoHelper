import unittest
import datetime
import mock
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
        __builtins__.raw_input = lambda _: 'hello'   # mock raw_input 
        self.assertEqual(user_io.general_input(">> "), 'hello')
        
    def test_textwithcapitalsandnumbers(self):
        __builtins__.raw_input = lambda _: 'hAllo2'   # mock raw_input 
        self.assertEqual(user_io.general_input(">> "), 'hAllo2')
        
    def test_replacable_signs(self):
        __builtins__.raw_input = lambda _: u"hallo {}".format(u"\u263a")   # mock raw_input 
        self.assertEqual(user_io.general_input(">> "), u"hallo {}".format(u"\u263a"))
        
    def test_umlaute(self):
        __builtins__.raw_input = lambda _: u"m{}rchen".format(u"\u00E4")   # mock raw_input 
        self.assertEqual(user_io.general_input(">> "), u"m{}rchen".format(u"\u00E4"))
        
    def test_unknown_signs(self):
        __builtins__.raw_input = lambda _: u"tuerkische Flagge: {}".format(u"\u262a")   # mock raw_input 
        self.assertEqual(user_io.general_input(">> "), u"tuerkische Flagge: {}".format(u"\u262a"))
        
    def test_number(self):
        __builtins__.raw_input = lambda _: "42"   # mock raw_input 
        self.assertEqual(user_io.general_input(">> "), "42")
        
class TestInputDecode(unittest.TestCase):   

    def test_normaltext(self):
        __builtins__.raw_input = lambda _: 'hello'   # mock raw_input 
        self.assertEqual(user_io.input_decode(">> "), 'hello')
        
    def test_textwithcapitalsandnumbers(self):
        __builtins__.raw_input = lambda _: 'hAllo2'   # mock raw_input 
        self.assertEqual(user_io.input_decode(">> "), 'hAllo2')
        
    def test_replacable_signs(self):
        __builtins__.raw_input = lambda _: "hallo {}".format(u"\u263a")   # mock raw_input 
        self.assertRaises(UnicodeEncodeError, user_io.input_decode, ">> ")
        
    def test_umlaute(self):
        __builtins__.raw_input = lambda _: 'M\xe4rchen'   # mock raw_input 
        self.assertEqual(user_io.input_decode(">> "), u"Märchen")
        
    def test_unknown_signs(self):
        __builtins__.raw_input = lambda _: u"tuerkische Flagge: {}".format(u"\u262a")   # mock raw_input 
        self.assertRaises(UnicodeEncodeError, user_io.input_decode, ">> ")
        
    def test_number(self):
        __builtins__.raw_input = lambda _: "42"   # mock raw_input 
        self.assertEqual(user_io.input_decode(">> "), "42")
        
class TestHauptmenueAnzeigen(unittest.TestCase):
    
    def test_nofoundexists(self):
        out = StringIO()
        sys.stdout = out                  # capture print output in out
        user_io.hauptmenue_anzeigen(False)   # fill out 
        output = out.getvalue().strip()   # save value of out in output
        expected_output = "Was moechtest du als naechstes tun?\n"
        expected_output = expected_output + "1: Geocaches aktualisieren\n"
        expected_output = expected_output + "2: Alle auf dem Geraet gespeicherten Geocaches sortieren und anzeigen\n"
        expected_output = expected_output + "3: Beschreibung fuer einen bestimmten Cache anzeigen (GC-Code erforderlich)\n"
        expected_output = expected_output + "4: Geocaches durchsuchen\n" 
        expected_output = expected_output + "5: https://www.geocaching.com/map aufrufen\n"
        expected_output = expected_output + "6: https://www.google.de/maps aufrufen\n"
        expected_output = expected_output + "7: Programm verlassen"
        self.assertEqual(output, expected_output)
        
    def test_foundexists(self):
        out = StringIO()
        sys.stdout = out                  # capture print output in out
        user_io.hauptmenue_anzeigen(True)   # fill out 
        output = out.getvalue().strip()   # save value of out in output
        expected_output = "Was moechtest du als naechstes tun?\n"
        expected_output = expected_output + "1: Geocaches aktualisieren\n"
        expected_output = expected_output + "2: Alle auf dem Geraet gespeicherten Geocaches sortieren und anzeigen\n"
        expected_output = expected_output + "3: Beschreibung fuer einen bestimmten Cache anzeigen (GC-Code erforderlich)\n"
        expected_output = expected_output + "4: Geocaches durchsuchen\n" 
        expected_output = expected_output + "5: Alle gefundenen Caches anzeigen\n"
        expected_output = expected_output + "6: https://www.geocaching.com/map aufrufen\n"
        expected_output = expected_output + "7: https://www.google.de/maps aufrufen\n"
        expected_output = expected_output + "8: Programm verlassen"
        self.assertEqual(output, expected_output)
        
class TestHauptmenue(unittest.TestCase):

    def test_1_nofoundexists(self):
        __builtins__.raw_input = lambda _: '1'   # mock raw_input 
        self.assertEqual(user_io.hauptmenue(False), 'aktualisieren')
        
    def test_2_nofoundexists(self):
        __builtins__.raw_input = lambda _: '2'   # mock raw_input 
        self.assertEqual(user_io.hauptmenue(False), 'alle_anzeigen')
        
    def test_3_nofoundexists(self):
        __builtins__.raw_input = lambda _: '3'   # mock raw_input 
        self.assertEqual(user_io.hauptmenue(False), 'einen_anzeigen')
        
    def test_4_nofoundexists(self):
        __builtins__.raw_input = lambda _: '4'   # mock raw_input 
        self.assertEqual(user_io.hauptmenue(False), 'suchen')
        
    def test_5_nofoundexists(self):
        __builtins__.raw_input = lambda _: '5'   # mock raw_input 
        self.assertEqual(user_io.hauptmenue(False), 'gc-maps')
        
    def test_6_nofoundexists(self):
        __builtins__.raw_input = lambda _: '6'   # mock raw_input 
        self.assertEqual(user_io.hauptmenue(False), 'google-maps')
        
    def test_7_nofoundexists(self):
        __builtins__.raw_input = lambda _: '7'   # mock raw_input 
        self.assertEqual(user_io.hauptmenue(False), 'exit')
        
    def test_8_nofoundexists(self):
        __builtins__.raw_input = lambda _: '8'   # mock raw_input 
        self.assertEqual(user_io.hauptmenue(False), None)
        
    def test_1_foundexists(self):
        __builtins__.raw_input = lambda _: '1'   # mock raw_input 
        self.assertEqual(user_io.hauptmenue(True), 'aktualisieren')
        
    def test_2_foundexists(self):
        __builtins__.raw_input = lambda _: '2'   # mock raw_input 
        self.assertEqual(user_io.hauptmenue(True), 'alle_anzeigen')
        
    def test_3_foundexists(self):
        __builtins__.raw_input = lambda _: '3'   # mock raw_input 
        self.assertEqual(user_io.hauptmenue(True), 'einen_anzeigen')
        
    def test_4_foundexists(self):
        __builtins__.raw_input = lambda _: '4'   # mock raw_input 
        self.assertEqual(user_io.hauptmenue(True), 'suchen')
        
    def test_5_foundexists(self):
        __builtins__.raw_input = lambda _: '5'   # mock raw_input 
        self.assertEqual(user_io.hauptmenue(True), 'gefundene_anzeigen')
        
    def test_6_foundexists(self):
        __builtins__.raw_input = lambda _: '6'   # mock raw_input 
        self.assertEqual(user_io.hauptmenue(True), 'gc-maps')
        
    def test_7_foundexists(self):
        __builtins__.raw_input = lambda _: '7'   # mock raw_input 
        self.assertEqual(user_io.hauptmenue(True), 'google-maps')
        
    def test_8_foundexists(self):
        __builtins__.raw_input = lambda _: '8'   # mock raw_input 
        self.assertEqual(user_io.hauptmenue(True), 'exit')
        
class TestSortieren(unittest.TestCase):

    def test_gccode(self):
        with mock.patch('__builtin__.raw_input', side_effect=['1', '1']):   # mock raw_input
            self.assertEqual(user_io.sortieren(), ["gccode", False])
        
    def test_name(self):
        with mock.patch('__builtin__.raw_input', side_effect=['2', '1']):   # mock raw_input 
            self.assertEqual(user_io.sortieren(), ["name", False])
            
    # TODO: alle Standardinput-Mocks durch Mock-Modul
        
    # def test_type(self):
        # __builtins__.raw_input = lambda _: '3\n1'   # mock raw_input 
        # self.assertEqual(user_io.sortieren(), ["type", False])
        
    # def test_difficulty(self):
        # __builtins__.raw_input = lambda _: '4\n1'   # mock raw_input 
        # self.assertEqual(user_io.sortieren(), ["difficulty", False])
        
    # def test_terrain(self):
        # __builtins__.raw_input = lambda _: '5\n1'   # mock raw_input 
        # self.assertEqual(user_io.sortieren(), ["terrain", False])
        
    # def test_size(self):
        # __builtins__.raw_input = lambda _: '6\n1'   # mock raw_input 
        # self.assertEqual(user_io.sortieren(), ["size", False])
        
    # def test_downloaddate(self):
        # __builtins__.raw_input = lambda _: '7\n1'   # mock raw_input 
        # self.assertEqual(user_io.sortieren(), ["downloaddate", False])
        
    # def test_available(self):
        # __builtins__.raw_input = lambda _: '8\n1'   # mock raw_input 
        # self.assertEqual(user_io.sortieren(), ["available", False])
        
    # def test_distance(self):
        # __builtins__.raw_input = lambda _: '9\n1'   # mock raw_input 
        # self.assertEqual(user_io.sortieren(), ["distance", False])
        
def create_testsuite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGeneralOutput))
    suite.addTest(unittest.makeSuite(TestGeneralInput))
    suite.addTest(unittest.makeSuite(TestInputDecode))
    suite.addTest(unittest.makeSuite(TestHauptmenueAnzeigen))
    suite.addTest(unittest.makeSuite(TestHauptmenue))
    suite.addTest(unittest.makeSuite(TestSortieren))
    return suite

if __name__ == '__main__':
    testsuite = create_testsuite()
    unittest.TextTestRunner(verbosity=2).run(testsuite)   # set verbosity to 2 if you want to see the name and result of every test and to 1 if you don't
