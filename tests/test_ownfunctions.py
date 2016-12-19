import unittest
import datetime
import sys
sys.path.append('../src/') # path to source file (ownfunctions.py)
from StringIO import StringIO

import ownfunctions  

out = StringIO()
sys.stdout = out   # don't print output
    
class TestZeichenErsetzen(unittest.TestCase):

    def test_find_cp1252(self):
        x = ownfunctions.find_cp1252()
        expected_result = ['NULL', 'START OF HEADING', 'START OF TEXT', 'END OF TEXT', 'END OF TRANSMISSION', 'ENQUIRY', 'ACKNOWLEDGE', 'BELL', 'BACKSPACE', 'HORIZONTAL TABULATION', 'LINE FEED', 'VERTICAL TABULATION', 'FORM FEED', 'CARRIAGE RETURN', 'SHIFT OUT', 'SHIFT IN', 'DATA LINK ESCAPE', 'DEVICE CONTROL ONE', 'DEVICE CONTROL TWO', 'DEVICE CONTROL THREE', 'DEVICE CONTROL FOUR', 'NEGATIVE ACKNOWLEDGE', 'SYNCHRONOUS IDLE', 'END OF TRANSMISSION BLOCK', 'CANCEL', 'END OF MEDIUM', 'SUBSTITUTE', 'ESCAPE', 'FILE SEPARATOR', 'GROUP SEPARATOR', 'RECORD SEPARATOR', 'UNIT SEPARATOR', 'SPACE', 'EXCLAMATION MARK', 'QUOTATION MARK', 'NUMBER SIGN', 'DOLLAR SIGN', 'PERCENT SIGN', 'AMPERSAND', 'APOSTROPHE', 'LEFT PARENTHESIS', 'RIGHT PARENTHESIS', 'ASTERISK', 'PLUS SIGN', 'COMMA', 'HYPHEN-MINUS', 'FULL STOP', 'SOLIDUS', 'DIGIT ZERO', 'DIGIT ONE', 'DIGIT TWO', 'DIGIT THREE', 'DIGIT FOUR', 'DIGIT FIVE', 'DIGIT SIX', 'DIGIT SEVEN', 'DIGIT EIGHT', 'DIGIT NINE', 'COLON', 'SEMICOLON', 'LESS-THAN SIGN', 'EQUALS SIGN', 'GREATER-THAN SIGN', 'QUESTION MARK', 'COMMERCIAL AT', 'LATIN CAPITAL LETTER A', 'LATIN CAPITAL LETTER B', 'LATIN CAPITAL LETTER C', 'LATIN CAPITAL LETTER D', 'LATIN CAPITAL LETTER E', 'LATIN CAPITAL LETTER F', 'LATIN CAPITAL LETTER G', 'LATIN CAPITAL LETTER H', 'LATIN CAPITAL LETTER I', 'LATIN CAPITAL LETTER J', 'LATIN CAPITAL LETTER K', 'LATIN CAPITAL LETTER L', 'LATIN CAPITAL LETTER M', 'LATIN CAPITAL LETTER N', 'LATIN CAPITAL LETTER O', 'LATIN CAPITAL LETTER P', 'LATIN CAPITAL LETTER Q', 'LATIN CAPITAL LETTER R', 'LATIN CAPITAL LETTER S', 'LATIN CAPITAL LETTER T', 'LATIN CAPITAL LETTER U', 'LATIN CAPITAL LETTER V', 'LATIN CAPITAL LETTER W', 'LATIN CAPITAL LETTER X', 'LATIN CAPITAL LETTER Y', 'LATIN CAPITAL LETTER Z', 'LEFT SQUARE BRACKET', 'REVERSE SOLIDUS', 'RIGHT SQUARE BRACKET', 'CIRCUMFLEX ACCENT', 'LOW LINE', 'GRAVE ACCENT', 'LATIN SMALL LETTER A', 'LATIN SMALL LETTER B', 'LATIN SMALL LETTER C', 'LATIN SMALL LETTER D', 'LATIN SMALL LETTER E', 'LATIN SMALL LETTER F', 'LATIN SMALL LETTER G', 'LATIN SMALL LETTER H', 'LATIN SMALL LETTER I', 'LATIN SMALL LETTER J', 'LATIN SMALL LETTER K', 'LATIN SMALL LETTER L', 'LATIN SMALL LETTER M', 'LATIN SMALL LETTER N', 'LATIN SMALL LETTER O', 'LATIN SMALL LETTER P', 'LATIN SMALL LETTER Q', 'LATIN SMALL LETTER R', 'LATIN SMALL LETTER S', 'LATIN SMALL LETTER T', 'LATIN SMALL LETTER U', 'LATIN SMALL LETTER V', 'LATIN SMALL LETTER W', 'LATIN SMALL LETTER X', 'LATIN SMALL LETTER Y', 'LATIN SMALL LETTER Z', 'LEFT CURLY BRACKET', 'VERTICAL LINE', 'RIGHT CURLY BRACKET', 'TILDE', 'DELETE', 'EURO SIGN', 'SINGLE LOW-9 QUOTATION MARK', 'LATIN SMALL LETTER F WITH HOOK', 'DOUBLE LOW-9 QUOTATION MARK', 'HORIZONTAL ELLIPSIS', 'DAGGER', 'DOUBLE DAGGER', 'MODIFIER LETTER CIRCUMFLEX ACCENT', 'PER MILLE SIGN', 'LATIN CAPITAL LETTER S WITH CARON', 'SINGLE LEFT-POINTING ANGLE QUOTATION MARK', 'LATIN CAPITAL LIGATURE OE', 'LATIN CAPITAL LETTER Z WITH CARON', 'LEFT SINGLE QUOTATION MARK', 'RIGHT SINGLE QUOTATION MARK', 'LEFT DOUBLE QUOTATION MARK', 'RIGHT DOUBLE QUOTATION MARK', 'BULLET', 'EN DASH', 'EM DASH', 'SMALL TILDE', 'TRADE MARK SIGN', 'LATIN SMALL LETTER S WITH CARON', 'SINGLE RIGHT-POINTING ANGLE QUOTATION MARK', 'LATIN SMALL LIGATURE OE', 'LATIN SMALL LETTER Z WITH CARON', 'LATIN CAPITAL LETTER Y WITH DIAERESIS', 'NO-BREAK SPACE', 'INVERTED EXCLAMATION MARK', 'CENT SIGN', 'POUND SIGN', 'CURRENCY SIGN', 'YEN SIGN', 'BROKEN BAR', 'SECTION SIGN', 'DIAERESIS', 'COPYRIGHT SIGN', 'FEMININE ORDINAL INDICATOR', 'LEFT-POINTING DOUBLE ANGLE QUOTATION MARK', 'NOT SIGN', 'SOFT HYPHEN', 'REGISTERED SIGN', 'MACRON', 'DEGREE SIGN', 'PLUS-MINUS SIGN', 'SUPERSCRIPT TWO', 'SUPERSCRIPT THREE', 'ACUTE ACCENT', 'MICRO SIGN', 'PILCROW SIGN', 'MIDDLE DOT', 'CEDILLA', 'SUPERSCRIPT ONE', 'MASCULINE ORDINAL INDICATOR', 'RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK', 'VULGAR FRACTION ONE QUARTER', 'VULGAR FRACTION ONE HALF', 'VULGAR FRACTION THREE QUARTERS', 'INVERTED QUESTION MARK', 'LATIN CAPITAL LETTER A WITH GRAVE', 'LATIN CAPITAL LETTER A WITH ACUTE', 'LATIN CAPITAL LETTER A WITH CIRCUMFLEX', 'LATIN CAPITAL LETTER A WITH TILDE', 'LATIN CAPITAL LETTER A WITH DIAERESIS', 'LATIN CAPITAL LETTER A WITH RING ABOVE', 'LATIN CAPITAL LETTER AE', 'LATIN CAPITAL LETTER C WITH CEDILLA', 'LATIN CAPITAL LETTER E WITH GRAVE', 'LATIN CAPITAL LETTER E WITH ACUTE', 'LATIN CAPITAL LETTER E WITH CIRCUMFLEX', 'LATIN CAPITAL LETTER E WITH DIAERESIS', 'LATIN CAPITAL LETTER I WITH GRAVE', 'LATIN CAPITAL LETTER I WITH ACUTE', 'LATIN CAPITAL LETTER I WITH CIRCUMFLEX', 'LATIN CAPITAL LETTER I WITH DIAERESIS', 'LATIN CAPITAL LETTER ETH', 'LATIN CAPITAL LETTER N WITH TILDE', 'LATIN CAPITAL LETTER O WITH GRAVE', 'LATIN CAPITAL LETTER O WITH ACUTE', 'LATIN CAPITAL LETTER O WITH CIRCUMFLEX', 'LATIN CAPITAL LETTER O WITH TILDE', 'LATIN CAPITAL LETTER O WITH DIAERESIS', 'MULTIPLICATION SIGN', 'LATIN CAPITAL LETTER O WITH STROKE', 'LATIN CAPITAL LETTER U WITH GRAVE', 'LATIN CAPITAL LETTER U WITH ACUTE', 'LATIN CAPITAL LETTER U WITH CIRCUMFLEX', 'LATIN CAPITAL LETTER U WITH DIAERESIS', 'LATIN CAPITAL LETTER Y WITH ACUTE', 'LATIN CAPITAL LETTER THORN', 'LATIN SMALL LETTER SHARP S', 'LATIN SMALL LETTER A WITH GRAVE', 'LATIN SMALL LETTER A WITH ACUTE', 'LATIN SMALL LETTER A WITH CIRCUMFLEX', 'LATIN SMALL LETTER A WITH TILDE', 'LATIN SMALL LETTER A WITH DIAERESIS', 'LATIN SMALL LETTER A WITH RING ABOVE', 'LATIN SMALL LETTER AE', 'LATIN SMALL LETTER C WITH CEDILLA', 'LATIN SMALL LETTER E WITH GRAVE', 'LATIN SMALL LETTER E WITH ACUTE', 'LATIN SMALL LETTER E WITH CIRCUMFLEX', 'LATIN SMALL LETTER E WITH DIAERESIS', 'LATIN SMALL LETTER I WITH GRAVE', 'LATIN SMALL LETTER I WITH ACUTE', 'LATIN SMALL LETTER I WITH CIRCUMFLEX', 'LATIN SMALL LETTER I WITH DIAERESIS', 'LATIN SMALL LETTER ETH', 'LATIN SMALL LETTER N WITH TILDE', 'LATIN SMALL LETTER O WITH GRAVE', 'LATIN SMALL LETTER O WITH ACUTE', 'LATIN SMALL LETTER O WITH CIRCUMFLEX', 'LATIN SMALL LETTER O WITH TILDE', 'LATIN SMALL LETTER O WITH DIAERESIS', 'DIVISION SIGN', 'LATIN SMALL LETTER O WITH STROKE', 'LATIN SMALL LETTER U WITH GRAVE', 'LATIN SMALL LETTER U WITH ACUTE', 'LATIN SMALL LETTER U WITH CIRCUMFLEX', 'LATIN SMALL LETTER U WITH DIAERESIS', 'LATIN SMALL LETTER Y WITH ACUTE', 'LATIN SMALL LETTER THORN', 'LATIN SMALL LETTER Y WITH DIAERESIS']
        self.assertEqual(x,expected_result)

    def test_hallo(self):
        x = ownfunctions.zeichen_ersetzen("hallo")
        self.assertEqual(x,"hallo")
        
    def test_maerchen(self):
        x = ownfunctions.zeichen_ersetzen(u"m{}rchen".format(u"\u00E4"))
        self.assertEqual(x, u"m{}rchen".format(u"\u00E4"))
        
    def test_smiley_u263a(self):
        x = ownfunctions.zeichen_ersetzen(u"hallo {}".format(u"\u263a"))
        self.assertEqual(x, u"hallo :-)")
    
    def test_sum_u2211(self):
        x = ownfunctions.zeichen_ersetzen(u"{}(1,2,3,4)".format(u"\u2211"))
        self.assertEqual(x, u"sum(1,2,3,4)")
        
    def test_squareroot_u221a(self):
        x = ownfunctions.zeichen_ersetzen(u"{}(4) = 2".format(u"\u221a"))
        self.assertEqual(x, u"sqrt(4) = 2")
        
    def test_newline(self):
        x = ownfunctions.zeichen_ersetzen(u"hallo\nWelt")
        self.assertEqual(x, u"hallo\nWelt")
        
    def test_tab(self):
        x = ownfunctions.zeichen_ersetzen(u"hallo\tWelt\v")
        self.assertEqual(x, u"hallo\tWelt\v")
    
    def test_unknown_sign(self):
        x = ownfunctions.zeichen_ersetzen(u"tuerkische Flagge: {}".format(u"\u262a"))
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
        self.assertEqual(ownfunctions.koordinaten_minuten_to_dezimalgrad(u"N 90°31.249, E 013°24.567"), None)
        
    def test_east_bigger_than_180(self):
        self.assertEqual(ownfunctions.koordinaten_minuten_to_dezimalgrad(u"N 52°31.249, E 213°24.567"), None)
        
    def test_north_bigger_than_90_south(self):
        self.assertEqual(ownfunctions.koordinaten_minuten_to_dezimalgrad(u"S 92°31.249, E 013°24.567"), None)
        
    def test_east_bigger_than_180_west(self):
        self.assertEqual(ownfunctions.koordinaten_minuten_to_dezimalgrad(u"N 52°31.249, W 213°24.567"), None)
        
    def test_small_mistake_in_unicode(self):
        self.assertRaises(ValueError, ownfunctions.koordinaten_minuten_to_dezimalgrad, u"N 92°310249, E 013°24.567")
        
    def test_list_instead_of_unicode(self):
        self.assertRaises(TypeError, ownfunctions.koordinaten_minuten_to_dezimalgrad, [u"N 52°31.249, E 013°24.567"])
        
class TestKoordinatenMinutenToSekunden(unittest.TestCase):

    def test_north_east_coords(self):
        x = ownfunctions.koordinaten_minuten_to_sekunden(u"N 52°31.249, E 013°24.567")
        self.assertEqual(x, u"52°31'14.9\"N+13°24'34.0\"E")
        
    def test_south_west(self):
        x = ownfunctions.koordinaten_minuten_to_sekunden(u"S 52°31.249, W 013°24.567")
        self.assertEqual(x, u"52°31'14.9\"S+13°24'34.0\"W")
        
    def test_equator(self):
        x = ownfunctions.koordinaten_minuten_to_sekunden(u"N 00°00.000, E 013°24.567")
        self.assertEqual(x, u"0°0'0.0\"N+13°24'34.0\"E")
        
    def test_zero_meridian(self):
        x = ownfunctions.koordinaten_minuten_to_sekunden(u"N 52°31.249, E 000°00.000")
        self.assertEqual(x, u"52°31'14.9\"N+0°0'0.0\"E")

    def test_north_bigger_than_90(self):
        self.assertEqual(ownfunctions.koordinaten_minuten_to_sekunden(u"N 90°31.249, E 013°24.567"), None)
        
    def test_east_bigger_than_180(self):
        self.assertEqual(ownfunctions.koordinaten_minuten_to_sekunden(u"N 52°31.249, E 213°24.567"), None)
        
    def test_north_bigger_than_90_south(self):
        self.assertEqual(ownfunctions.koordinaten_minuten_to_sekunden(u"S 92°31.249, E 013°24.567"), None)
        
    def test_east_bigger_than_180_west(self):
        self.assertEqual(ownfunctions.koordinaten_minuten_to_sekunden(u"N 52°31.249, W 213°24.567"), None)
        
    def test_small_mistake_in_unicode(self):
        self.assertEqual(ownfunctions.koordinaten_minuten_to_sekunden(u"N 92°310249, E 013°24.567"), None)
        
    def test_list_instead_of_unicode(self):
        self.assertRaises(TypeError, ownfunctions.koordinaten_minuten_to_sekunden, [u"N 52°31.249, E 013°24.567"])
        
class TestKoordinatenUrlToDezimalgrad(unittest.TestCase):
     
    def test_gc_north_east(self):
        x = ownfunctions.koordinaten_url_to_dezimalgrad("https://www.geocaching.com/map/#?ll=49.7821,9.87731&z=14S")
        self.assertEqual(x, [49.7821, 9.87731])

    def test_gc_south_west(self):
        x = ownfunctions.koordinaten_url_to_dezimalgrad("https://www.geocaching.com/map/#?ll=-32.54681,-23.20312&z=2")
        self.assertEqual(x, [-32.54681, -23.20312])

    def test_gc_from_special_location(self):
        x = ownfunctions.koordinaten_url_to_dezimalgrad("https://www.geocaching.com/map/default.aspx?lat=49.81&lng=9.936667#?ll=49.77877,9.9131&z=14")
        self.assertEqual(x, [49.77877, 9.9131])

    def test_gc_equator(self):
        x = ownfunctions.koordinaten_url_to_dezimalgrad("https://www.geocaching.com/map/#?ll=0,-68.49309&z=18")
        self.assertEqual(x, [0.0, -68.49309])
        
    def test_googlemaps_north_east(self):
        x = ownfunctions.koordinaten_url_to_dezimalgrad("https://www.google.de/maps/@49.780988,9.9699965,14z")
        self.assertEqual(x, [49.780988, 9.9699965])

    def test_googlemaps_south_west(self):
        x = ownfunctions.koordinaten_url_to_dezimalgrad("https://www.google.de/maps/place/Rio+de+Janeiro,+Brasilien/@-22.9108558,-43.5884197,11z/data=!3m1!4b1!4m5!3m4!1s0x9bde559108a05b:0x50dc426c672fd24e!8m2!3d-22.9068467!4d-43.1728965")
        self.assertEqual(x, [-22.9108558, -43.5884197])

    def test_googlemaps_equator(self):
        x = ownfunctions.koordinaten_url_to_dezimalgrad("https://www.google.de/maps/place/0%C2%B000'00.0%22N+34%C2%B027'07.3%22E/@0,34.4497481,17z/data=!4m4!3m3!1s0x0:0x0!8m1!4d34.4520333")
        self.assertEqual(x, [0.0, 34.4497481])
        
    def test_different_website(self):
        self.assertEqual(ownfunctions.koordinaten_minuten_to_sekunden("https://www.google.de/"), None)
        
    def test_different_input_type(self):
        self.assertRaises(TypeError, ownfunctions.koordinaten_minuten_to_sekunden, 42)

class TestKoordinatenStringToDezimalgrad(unittest.TestCase):

    def test_manual_coords(self):
        x = ownfunctions.koordinaten_string_to_dezimalgrad(u"N 52°31.249, E 013°24.567") 
        n = round(x[0],6)
        e = round(x[1],5)
        self.assertEqual([n,e], [52.520817,13.40945])     

    def test_geocachingcom_coords(self): 
        x = ownfunctions.koordinaten_string_to_dezimalgrad("https://www.geocaching.com/map/#?ll=49.7821,9.87731&z=14S")
        self.assertEqual(x, [49.7821, 9.87731])
        
    def test_googlemaps_coords(self):
        x = ownfunctions.koordinaten_string_to_dezimalgrad("https://www.google.de/maps/place/Rio+de+Janeiro,+Brasilien/@-22.9108558,-43.5884197,11z/data=!3m1!4b1!4m5!3m4!1s0x9bde559108a05b:0x50dc426c672fd24e!8m2!3d-22.9068467!4d-43.1728965")
        self.assertEqual(x, [-22.9108558, -43.5884197])
        
    def test_bullshitstring_givesNone(self):
        x = ownfunctions.koordinaten_string_to_dezimalgrad("grwttqq")
        self.assertEqual(x, None)
        
    def test_nostring_givesError(self):
        self.assertRaises(TypeError, ownfunctions.koordinaten_string_to_dezimalgrad, 42)
        
class TestCalculateDistance(unittest.TestCase):

    def test_both_north_east(self):
        x = ownfunctions.calculate_distance([49.7781628,9.8729888],[50.3342402,10.1413188])
        x = round(x,1)
        self.assertEqual(x, 64.7) 
        
    def test_both_south_west(self):
        x = ownfunctions.calculate_distance([-49.7781628,-9.8729888],[-50.3342402,-10.1413188])
        x = round(x,1)
        self.assertEqual(x, 64.7) 
        
    def test_both_identical(self):
        x = ownfunctions.calculate_distance([49.7781628,9.8729888],[49.7781628,9.8729888])
        self.assertEqual(x, 0) 
        
    def test_one_north_one_south(self):
        x = ownfunctions.calculate_distance([0.1245831,29.2351313],[-0.0968813,29.2067241])
        x = round(x,1)
        self.assertEqual(x, 24.8)
        
    def test_one_east_one_west(self):
        x = ownfunctions.calculate_distance([51.4819611,-0.0030331],[51.476207,0.0216696])
        x = round(x,1)
        self.assertEqual(x, 1.8)
        
    def test_both_sides_of_dateline(self):
        x = ownfunctions.calculate_distance([-16.9008043,179.9575312],[-16.826478,-179.9430943])
        x = round(x,1)
        self.assertEqual(x, 13.4)
        
    def test_north_bigger_than_90(self):
        self.assertRaises(ValueError, ownfunctions.calculate_distance, [92.520817,13.40945], [49.7781628,9.8729888])
        
    def test_east_bigger_than_180(self):
        self.assertRaises(ValueError, ownfunctions.calculate_distance, [52.520817,200.40945], [49.7781628,9.8729888])
        
    def test_north_smaller_than_minus90(self):
        self.assertRaises(ValueError, ownfunctions.calculate_distance, [49.7781628,9.8729888], [-92.520817,13.40945])
        
    def test_east_smaller_than_minus180(self):
        self.assertRaises(ValueError, ownfunctions.calculate_distance, [49.7781628,9.8729888], [52.520817,-200.40945])
        
    def test_one_coord_is_shit(self):
        self.assertRaises(TypeError, ownfunctions.calculate_distance, [52.520817,"bla"], [49.7781628,9.8729888])
        
    def test_string_instead_of_list(self):
        self.assertRaises(TypeError, ownfunctions.calculate_distance, [49.7781628,9.8729888], "12")
        
    def test_list_of_wrong_length(self):
        self.assertRaises(TypeError, ownfunctions.calculate_distance, [52.520817,13.40945, 42.42], [49.7781628,9.8729888])
        
class TestGetMonth(unittest.TestCase):

    def test_january(self):
        x = ownfunctions.get_month("Jan")
        self.assertEqual(x, 1)
        
    def test_february(self):
        x = ownfunctions.get_month("Feb")
        self.assertEqual(x, 2)
    
    def test_march(self):
        x = ownfunctions.get_month("Mar")
        self.assertEqual(x, 3)
        
    def test_april(self):
        x = ownfunctions.get_month("Apr")
        self.assertEqual(x, 4)
        
    def test_may(self):
        x = ownfunctions.get_month("May")
        self.assertEqual(x, 5)
        
    def test_june(self):
        x = ownfunctions.get_month("Jun")
        self.assertEqual(x, 6)
        
    def test_july(self):
        x = ownfunctions.get_month("Jul")
        self.assertEqual(x, 7)
        
    def test_august(self):
        x = ownfunctions.get_month("Aug")
        self.assertEqual(x, 8)
        
    def test_september(self):
        x = ownfunctions.get_month("Sep")
        self.assertEqual(x, 9)
        
    def test_october(self):
        x = ownfunctions.get_month("Oct")
        self.assertEqual(x, 10)
        
    def test_november(self):
        x = ownfunctions.get_month("Nov")
        self.assertEqual(x, 11)
        
    def test_december(self):
        x = ownfunctions.get_month("Dec")
        self.assertEqual(x, 12)
        
    def test_other_string_givesNone(self):
        x = ownfunctions.get_month("bla")
        self.assertEqual(x, None)
        
    def test_other_type_givesNone(self):
        x = ownfunctions.get_month(42)
        self.assertEqual(x, None)
        
class TestStringToDate(unittest.TestCase):

    def test_normal_date(self):
        x = ownfunctions.string_to_date("04.07.1990")
        expected_result = datetime.date(1990,7,4)
        self.assertEqual(x,expected_result)
        
    def test_day_is_zero(self):
        self.assertRaises(ValueError, ownfunctions.string_to_date, "00.07.1990")
        
    def test_month_is_zero(self):
        self.assertRaises(ValueError, ownfunctions.string_to_date, "04.00.1990")
        
    def test_year_is_zero_givesError(self):
        self.assertRaises(ValueError, ownfunctions.string_to_date, "04.07.0000")
        
    def test_29th_feb(self):
        self.assertRaises(ValueError, ownfunctions.string_to_date, "29.02.2005")
        
    def test_29th_feb_leapyear(self):
        x = ownfunctions.string_to_date("29.02.2004")
        expected_result = datetime.date(2004,2,29)
        self.assertEqual(x,expected_result)
        
    def test_wrong_type(self):
        self.assertRaises(TypeError, ownfunctions.string_to_date, 42)
        
    def test_small_mistake_in_string(self):
        self.assertRaises(ValueError, ownfunctions.string_to_date, "29.x2.2005")
        
class TestRemoveSpaces(unittest.TestCase):

    def test_text(self):
        x = ownfunctions.remove_spaces("   abc   def   ")
        self.assertEqual(x,"abc def")
        
    def test_wrong_type(self):
        self.assertRaises(TypeError, ownfunctions.remove_spaces, 42)
        
def create_testsuite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestZeichenErsetzen))
    suite.addTest(unittest.makeSuite(TestKoordinatenDezimalgradToMinuten))
    suite.addTest(unittest.makeSuite(TestKoordinatenMinutenToDezimalgrad))
    suite.addTest(unittest.makeSuite(TestKoordinatenMinutenToSekunden))
    suite.addTest(unittest.makeSuite(TestKoordinatenUrlToDezimalgrad))
    suite.addTest(unittest.makeSuite(TestKoordinatenStringToDezimalgrad))
    suite.addTest(unittest.makeSuite(TestCalculateDistance))
    suite.addTest(unittest.makeSuite(TestGetMonth))
    suite.addTest(unittest.makeSuite(TestStringToDate))
    suite.addTest(unittest.makeSuite(TestRemoveSpaces))
    return suite

if __name__ == '__main__':
    testsuite = create_testsuite()
    unittest.TextTestRunner(verbosity=1).run(testsuite)   # set verbosity to 2 if you want to see the name and result of every test and to 1 if you don't
