import unittest
import sys
sys.path.append('../src/') # path to source file (ownfunctions.py)

import ownfunctions  
    
class TestZeichenErsetzen(unittest.TestCase):

    def test_find_cp1252(self):
        x = ownfunctions.find_cp1252()
        expected_result = ['NULL', 'START OF HEADING', 'START OF TEXT', 'END OF TEXT', 'END OF TRANSMISSION', 'ENQUIRY', 'ACKNOWLEDGE', 'BELL', 'BACKSPACE', 'HORIZONTAL TABULATION', 'LINE FEED', 'VERTICAL TABULATION', 'FORM FEED', 'CARRIAGE RETURN', 'SHIFT OUT', 'SHIFT IN', 'DATA LINK ESCAPE', 'DEVICE CONTROL ONE', 'DEVICE CONTROL TWO', 'DEVICE CONTROL THREE', 'DEVICE CONTROL FOUR', 'NEGATIVE ACKNOWLEDGE', 'SYNCHRONOUS IDLE', 'END OF TRANSMISSION BLOCK', 'CANCEL', 'END OF MEDIUM', 'SUBSTITUTE', 'ESCAPE', 'FILE SEPARATOR', 'GROUP SEPARATOR', 'RECORD SEPARATOR', 'UNIT SEPARATOR', 'SPACE', 'EXCLAMATION MARK', 'QUOTATION MARK', 'NUMBER SIGN', 'DOLLAR SIGN', 'PERCENT SIGN', 'AMPERSAND', 'APOSTROPHE', 'LEFT PARENTHESIS', 'RIGHT PARENTHESIS', 'ASTERISK', 'PLUS SIGN', 'COMMA', 'HYPHEN-MINUS', 'FULL STOP', 'SOLIDUS', 'DIGIT ZERO', 'DIGIT ONE', 'DIGIT TWO', 'DIGIT THREE', 'DIGIT FOUR', 'DIGIT FIVE', 'DIGIT SIX', 'DIGIT SEVEN', 'DIGIT EIGHT', 'DIGIT NINE', 'COLON', 'SEMICOLON', 'LESS-THAN SIGN', 'EQUALS SIGN', 'GREATER-THAN SIGN', 'QUESTION MARK', 'COMMERCIAL AT', 'LATIN CAPITAL LETTER A', 'LATIN CAPITAL LETTER B', 'LATIN CAPITAL LETTER C', 'LATIN CAPITAL LETTER D', 'LATIN CAPITAL LETTER E', 'LATIN CAPITAL LETTER F', 'LATIN CAPITAL LETTER G', 'LATIN CAPITAL LETTER H', 'LATIN CAPITAL LETTER I', 'LATIN CAPITAL LETTER J', 'LATIN CAPITAL LETTER K', 'LATIN CAPITAL LETTER L', 'LATIN CAPITAL LETTER M', 'LATIN CAPITAL LETTER N', 'LATIN CAPITAL LETTER O', 'LATIN CAPITAL LETTER P', 'LATIN CAPITAL LETTER Q', 'LATIN CAPITAL LETTER R', 'LATIN CAPITAL LETTER S', 'LATIN CAPITAL LETTER T', 'LATIN CAPITAL LETTER U', 'LATIN CAPITAL LETTER V', 'LATIN CAPITAL LETTER W', 'LATIN CAPITAL LETTER X', 'LATIN CAPITAL LETTER Y', 'LATIN CAPITAL LETTER Z', 'LEFT SQUARE BRACKET', 'REVERSE SOLIDUS', 'RIGHT SQUARE BRACKET', 'CIRCUMFLEX ACCENT', 'LOW LINE', 'GRAVE ACCENT', 'LATIN SMALL LETTER A', 'LATIN SMALL LETTER B', 'LATIN SMALL LETTER C', 'LATIN SMALL LETTER D', 'LATIN SMALL LETTER E', 'LATIN SMALL LETTER F', 'LATIN SMALL LETTER G', 'LATIN SMALL LETTER H', 'LATIN SMALL LETTER I', 'LATIN SMALL LETTER J', 'LATIN SMALL LETTER K', 'LATIN SMALL LETTER L', 'LATIN SMALL LETTER M', 'LATIN SMALL LETTER N', 'LATIN SMALL LETTER O', 'LATIN SMALL LETTER P', 'LATIN SMALL LETTER Q', 'LATIN SMALL LETTER R', 'LATIN SMALL LETTER S', 'LATIN SMALL LETTER T', 'LATIN SMALL LETTER U', 'LATIN SMALL LETTER V', 'LATIN SMALL LETTER W', 'LATIN SMALL LETTER X', 'LATIN SMALL LETTER Y', 'LATIN SMALL LETTER Z', 'LEFT CURLY BRACKET', 'VERTICAL LINE', 'RIGHT CURLY BRACKET', 'TILDE', 'DELETE', 'EURO SIGN', 'SINGLE LOW-9 QUOTATION MARK', 'LATIN SMALL LETTER F WITH HOOK', 'DOUBLE LOW-9 QUOTATION MARK', 'HORIZONTAL ELLIPSIS', 'DAGGER', 'DOUBLE DAGGER', 'MODIFIER LETTER CIRCUMFLEX ACCENT', 'PER MILLE SIGN', 'LATIN CAPITAL LETTER S WITH CARON', 'SINGLE LEFT-POINTING ANGLE QUOTATION MARK', 'LATIN CAPITAL LIGATURE OE', 'LATIN CAPITAL LETTER Z WITH CARON', 'LEFT SINGLE QUOTATION MARK', 'RIGHT SINGLE QUOTATION MARK', 'LEFT DOUBLE QUOTATION MARK', 'RIGHT DOUBLE QUOTATION MARK', 'BULLET', 'EN DASH', 'EM DASH', 'SMALL TILDE', 'TRADE MARK SIGN', 'LATIN SMALL LETTER S WITH CARON', 'SINGLE RIGHT-POINTING ANGLE QUOTATION MARK', 'LATIN SMALL LIGATURE OE', 'LATIN SMALL LETTER Z WITH CARON', 'LATIN CAPITAL LETTER Y WITH DIAERESIS', 'NO-BREAK SPACE', 'INVERTED EXCLAMATION MARK', 'CENT SIGN', 'POUND SIGN', 'CURRENCY SIGN', 'YEN SIGN', 'BROKEN BAR', 'SECTION SIGN', 'DIAERESIS', 'COPYRIGHT SIGN', 'FEMININE ORDINAL INDICATOR', 'LEFT-POINTING DOUBLE ANGLE QUOTATION MARK', 'NOT SIGN', 'SOFT HYPHEN', 'REGISTERED SIGN', 'MACRON', 'DEGREE SIGN', 'PLUS-MINUS SIGN', 'SUPERSCRIPT TWO', 'SUPERSCRIPT THREE', 'ACUTE ACCENT', 'MICRO SIGN', 'PILCROW SIGN', 'MIDDLE DOT', 'CEDILLA', 'SUPERSCRIPT ONE', 'MASCULINE ORDINAL INDICATOR', 'RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK', 'VULGAR FRACTION ONE QUARTER', 'VULGAR FRACTION ONE HALF', 'VULGAR FRACTION THREE QUARTERS', 'INVERTED QUESTION MARK', 'LATIN CAPITAL LETTER A WITH GRAVE', 'LATIN CAPITAL LETTER A WITH ACUTE', 'LATIN CAPITAL LETTER A WITH CIRCUMFLEX', 'LATIN CAPITAL LETTER A WITH TILDE', 'LATIN CAPITAL LETTER A WITH DIAERESIS', 'LATIN CAPITAL LETTER A WITH RING ABOVE', 'LATIN CAPITAL LETTER AE', 'LATIN CAPITAL LETTER C WITH CEDILLA', 'LATIN CAPITAL LETTER E WITH GRAVE', 'LATIN CAPITAL LETTER E WITH ACUTE', 'LATIN CAPITAL LETTER E WITH CIRCUMFLEX', 'LATIN CAPITAL LETTER E WITH DIAERESIS', 'LATIN CAPITAL LETTER I WITH GRAVE', 'LATIN CAPITAL LETTER I WITH ACUTE', 'LATIN CAPITAL LETTER I WITH CIRCUMFLEX', 'LATIN CAPITAL LETTER I WITH DIAERESIS', 'LATIN CAPITAL LETTER ETH', 'LATIN CAPITAL LETTER N WITH TILDE', 'LATIN CAPITAL LETTER O WITH GRAVE', 'LATIN CAPITAL LETTER O WITH ACUTE', 'LATIN CAPITAL LETTER O WITH CIRCUMFLEX', 'LATIN CAPITAL LETTER O WITH TILDE', 'LATIN CAPITAL LETTER O WITH DIAERESIS', 'MULTIPLICATION SIGN', 'LATIN CAPITAL LETTER O WITH STROKE', 'LATIN CAPITAL LETTER U WITH GRAVE', 'LATIN CAPITAL LETTER U WITH ACUTE', 'LATIN CAPITAL LETTER U WITH CIRCUMFLEX', 'LATIN CAPITAL LETTER U WITH DIAERESIS', 'LATIN CAPITAL LETTER Y WITH ACUTE', 'LATIN CAPITAL LETTER THORN', 'LATIN SMALL LETTER SHARP S', 'LATIN SMALL LETTER A WITH GRAVE', 'LATIN SMALL LETTER A WITH ACUTE', 'LATIN SMALL LETTER A WITH CIRCUMFLEX', 'LATIN SMALL LETTER A WITH TILDE', 'LATIN SMALL LETTER A WITH DIAERESIS', 'LATIN SMALL LETTER A WITH RING ABOVE', 'LATIN SMALL LETTER AE', 'LATIN SMALL LETTER C WITH CEDILLA', 'LATIN SMALL LETTER E WITH GRAVE', 'LATIN SMALL LETTER E WITH ACUTE', 'LATIN SMALL LETTER E WITH CIRCUMFLEX', 'LATIN SMALL LETTER E WITH DIAERESIS', 'LATIN SMALL LETTER I WITH GRAVE', 'LATIN SMALL LETTER I WITH ACUTE', 'LATIN SMALL LETTER I WITH CIRCUMFLEX', 'LATIN SMALL LETTER I WITH DIAERESIS', 'LATIN SMALL LETTER ETH', 'LATIN SMALL LETTER N WITH TILDE', 'LATIN SMALL LETTER O WITH GRAVE', 'LATIN SMALL LETTER O WITH ACUTE', 'LATIN SMALL LETTER O WITH CIRCUMFLEX', 'LATIN SMALL LETTER O WITH TILDE', 'LATIN SMALL LETTER O WITH DIAERESIS', 'DIVISION SIGN', 'LATIN SMALL LETTER O WITH STROKE', 'LATIN SMALL LETTER U WITH GRAVE', 'LATIN SMALL LETTER U WITH ACUTE', 'LATIN SMALL LETTER U WITH CIRCUMFLEX', 'LATIN SMALL LETTER U WITH DIAERESIS', 'LATIN SMALL LETTER Y WITH ACUTE', 'LATIN SMALL LETTER THORN', 'LATIN SMALL LETTER Y WITH DIAERESIS']
        self.assertEqual(x,expected_result)

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
        x = ownfunctions.koordinaten_dezimalgrad_to_minuten([-52.520817,-13.40945])
        self.assertEqual(x, u"S 52°31.249, W 013°24.567")
        
    def test_equator(self):
        x = ownfunctions.koordinaten_dezimalgrad_to_minuten([0,13.40945])
        self.assertEqual(x, u"N 00°00.000, E 013°24.567")
        
    def test_zero_meridian(self):
        x = ownfunctions.koordinaten_dezimalgrad_to_minuten([52.520817,0])
        self.assertEqual(x, u"N 52°31.249, E 000°00.000")
        
    def test_north_bigger_than_90(self):
        self.assertRaises(ValueError, ownfunctions.koordinaten_dezimalgrad_to_minuten, [92.520817,13.40945])
        
    def test_east_bigger_than_180(self):
        self.assertRaises(ValueError, ownfunctions.koordinaten_dezimalgrad_to_minuten, [52.520817,200.40945])
        
    def test_north_smaller_than_minus90(self):
        self.assertRaises(ValueError, ownfunctions.koordinaten_dezimalgrad_to_minuten, [-92.520817,13.40945])
        
    def test_east_smaller_than_minus180(self):
        self.assertRaises(ValueError, ownfunctions.koordinaten_dezimalgrad_to_minuten, [52.520817,-200.40945])
        
    def test_one_coord_is_shit(self):
        self.assertRaises(TypeError, ownfunctions.koordinaten_dezimalgrad_to_minuten, [52.520817,"bla"])
        
    def test_string_instead_of_list(self):
        self.assertRaises(TypeError, ownfunctions.koordinaten_dezimalgrad_to_minuten, "12")
        
    def test_list_of_wrong_length(self):
        self.assertRaises(TypeError, ownfunctions.koordinaten_dezimalgrad_to_minuten, [52.520817,13.40945, 42.42])
        
class TestKoordinatenMinutenToDezimalgrad(unittest.TestCase):

    def test_north_east_coords(self):
        x = ownfunctions.koordinaten_minuten_to_dezimalgrad(u"N 52°31.249, E 013°24.567")
        n = round(x[0],6)
        e = round(x[1],5)
        self.assertEqual([n,e], [52.520817,13.40945])
        
    def test_south_west(self):
        x = ownfunctions.koordinaten_minuten_to_dezimalgrad(u"S 52°31.249, W 013°24.567")
        n = round(x[0],6)
        e = round(x[1],5)
        self.assertEqual([n,e], [-52.520817,-13.40945])
        
    def test_equator(self):
        x = ownfunctions.koordinaten_minuten_to_dezimalgrad(u"N 00°00.000, E 013°24.567")
        n = round(x[0],6)
        e = round(x[1],5)
        self.assertEqual([n,e], [0,13.40945])
        
    def test_zero_meridian(self):
        x = ownfunctions.koordinaten_minuten_to_dezimalgrad(u"N 52°31.249, E 000°00.000")
        n = round(x[0],6)
        e = round(x[1],5)
        self.assertEqual([n,e], [52.520817,0])
        
    def test_north_bigger_than_90(self):
        self.assertRaises(ValueError, ownfunctions.koordinaten_minuten_to_dezimalgrad, u"N 92°31.249, E 013°24.567")
        
    def test_east_bigger_than_180(self):
        self.assertRaises(ValueError, ownfunctions.koordinaten_minuten_to_dezimalgrad, u"N 52°31.249, E 213°24.567")
        
    def test_north_bigger_than_90_south(self):
        self.assertRaises(ValueError, ownfunctions.koordinaten_minuten_to_dezimalgrad, u"S 92°31.249, E 013°24.567")
        
    def test_east_bigger_than_180_west(self):
        self.assertRaises(ValueError, ownfunctions.koordinaten_minuten_to_dezimalgrad, u"N 52°31.249, W 213°24.567")
        
    def test_small_mistake_in_unicode(self):
        self.assertRaises(ValueError, ownfunctions.koordinaten_minuten_to_dezimalgrad, u"N 92°310249, E 013°24.567")
        
    def test_string_instead_of_unicode(self):
        self.assertRaises(TypeError, ownfunctions.koordinaten_minuten_to_dezimalgrad, "N 92.310249, E 013.24.567")
        
class TestKoordinatenMinutenToSekunden(unittest.TestCase):

    pass
        

def create_testsuite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestZeichenErsetzen))
    suite.addTest(unittest.makeSuite(TestKoordinatenDezimalgradToMinuten))
    suite.addTest(unittest.makeSuite(TestKoordinatenMinutenToDezimalgrad))
    suite.addTest(unittest.makeSuite(TestKoordinatenMinutenToSekunden))
    return suite

if __name__ == '__main__':
    testsuite = create_testsuite()
    unittest.TextTestRunner(verbosity=2).run(testsuite)
