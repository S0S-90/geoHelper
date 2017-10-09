#!/usr/bin/python
# -*- coding: utf-8 -*-

"""tests for ownfunctions.py"""

import unittest
import datetime
import sys
from io import StringIO
import xml.etree.ElementTree as ElementTree

import test_frame
import ownfunctions


class TestReplaceSigns(unittest.TestCase):

    def test_find_cp1252(self):
        test_frame.changepath("../src")
        x = ownfunctions.find_cp1252()
        expected_result = ['NULL', 'START OF HEADING', 'START OF TEXT', 'END OF TEXT', 'END OF TRANSMISSION', 'ENQUIRY',
                           'ACKNOWLEDGE', 'BELL', 'BACKSPACE', 'HORIZONTAL TABULATION', 'LINE FEED',
                           'VERTICAL TABULATION', 'FORM FEED', 'CARRIAGE RETURN', 'SHIFT OUT', 'SHIFT IN',
                           'DATA LINK ESCAPE', 'DEVICE CONTROL ONE', 'DEVICE CONTROL TWO', 'DEVICE CONTROL THREE',
                           'DEVICE CONTROL FOUR', 'NEGATIVE ACKNOWLEDGE', 'SYNCHRONOUS IDLE',
                           'END OF TRANSMISSION BLOCK', 'CANCEL', 'END OF MEDIUM', 'SUBSTITUTE', 'ESCAPE',
                           'FILE SEPARATOR', 'GROUP SEPARATOR', 'RECORD SEPARATOR', 'UNIT SEPARATOR', 'SPACE',
                           'EXCLAMATION MARK', 'QUOTATION MARK', 'NUMBER SIGN', 'DOLLAR SIGN', 'PERCENT SIGN',
                           'AMPERSAND', 'APOSTROPHE', 'LEFT PARENTHESIS', 'RIGHT PARENTHESIS', 'ASTERISK', 'PLUS SIGN',
                           'COMMA', 'HYPHEN-MINUS', 'FULL STOP', 'SOLIDUS', 'DIGIT ZERO', 'DIGIT ONE', 'DIGIT TWO',
                           'DIGIT THREE', 'DIGIT FOUR', 'DIGIT FIVE', 'DIGIT SIX', 'DIGIT SEVEN', 'DIGIT EIGHT',
                           'DIGIT NINE', 'COLON', 'SEMICOLON', 'LESS-THAN SIGN', 'EQUALS SIGN', 'GREATER-THAN SIGN',
                           'QUESTION MARK', 'COMMERCIAL AT', 'LATIN CAPITAL LETTER A', 'LATIN CAPITAL LETTER B',
                           'LATIN CAPITAL LETTER C', 'LATIN CAPITAL LETTER D', 'LATIN CAPITAL LETTER E',
                           'LATIN CAPITAL LETTER F', 'LATIN CAPITAL LETTER G', 'LATIN CAPITAL LETTER H',
                           'LATIN CAPITAL LETTER I', 'LATIN CAPITAL LETTER J', 'LATIN CAPITAL LETTER K',
                           'LATIN CAPITAL LETTER L', 'LATIN CAPITAL LETTER M', 'LATIN CAPITAL LETTER N',
                           'LATIN CAPITAL LETTER O', 'LATIN CAPITAL LETTER P', 'LATIN CAPITAL LETTER Q',
                           'LATIN CAPITAL LETTER R', 'LATIN CAPITAL LETTER S', 'LATIN CAPITAL LETTER T',
                           'LATIN CAPITAL LETTER U', 'LATIN CAPITAL LETTER V', 'LATIN CAPITAL LETTER W',
                           'LATIN CAPITAL LETTER X', 'LATIN CAPITAL LETTER Y', 'LATIN CAPITAL LETTER Z',
                           'LEFT SQUARE BRACKET', 'REVERSE SOLIDUS', 'RIGHT SQUARE BRACKET', 'CIRCUMFLEX ACCENT',
                           'LOW LINE', 'GRAVE ACCENT', 'LATIN SMALL LETTER A', 'LATIN SMALL LETTER B',
                           'LATIN SMALL LETTER C', 'LATIN SMALL LETTER D', 'LATIN SMALL LETTER E',
                           'LATIN SMALL LETTER F', 'LATIN SMALL LETTER G', 'LATIN SMALL LETTER H',
                           'LATIN SMALL LETTER I', 'LATIN SMALL LETTER J', 'LATIN SMALL LETTER K',
                           'LATIN SMALL LETTER L', 'LATIN SMALL LETTER M', 'LATIN SMALL LETTER N',
                           'LATIN SMALL LETTER O', 'LATIN SMALL LETTER P', 'LATIN SMALL LETTER Q',
                           'LATIN SMALL LETTER R', 'LATIN SMALL LETTER S', 'LATIN SMALL LETTER T',
                           'LATIN SMALL LETTER U', 'LATIN SMALL LETTER V', 'LATIN SMALL LETTER W',
                           'LATIN SMALL LETTER X', 'LATIN SMALL LETTER Y', 'LATIN SMALL LETTER Z',
                           'LEFT CURLY BRACKET', 'VERTICAL LINE', 'RIGHT CURLY BRACKET', 'TILDE', 'DELETE',
                           'EURO SIGN', 'SINGLE LOW-9 QUOTATION MARK', 'LATIN SMALL LETTER F WITH HOOK',
                           'DOUBLE LOW-9 QUOTATION MARK', 'HORIZONTAL ELLIPSIS', 'DAGGER', 'DOUBLE DAGGER',
                           'MODIFIER LETTER CIRCUMFLEX ACCENT', 'PER MILLE SIGN', 'LATIN CAPITAL LETTER S WITH CARON',
                           'SINGLE LEFT-POINTING ANGLE QUOTATION MARK', 'LATIN CAPITAL LIGATURE OE',
                           'LATIN CAPITAL LETTER Z WITH CARON', 'LEFT SINGLE QUOTATION MARK',
                           'RIGHT SINGLE QUOTATION MARK', 'LEFT DOUBLE QUOTATION MARK', 'RIGHT DOUBLE QUOTATION MARK',
                           'BULLET', 'EN DASH', 'EM DASH', 'SMALL TILDE', 'TRADE MARK SIGN',
                           'LATIN SMALL LETTER S WITH CARON', 'SINGLE RIGHT-POINTING ANGLE QUOTATION MARK',
                           'LATIN SMALL LIGATURE OE', 'LATIN SMALL LETTER Z WITH CARON',
                           'LATIN CAPITAL LETTER Y WITH DIAERESIS', 'NO-BREAK SPACE', 'INVERTED EXCLAMATION MARK',
                           'CENT SIGN', 'POUND SIGN', 'CURRENCY SIGN', 'YEN SIGN', 'BROKEN BAR', 'SECTION SIGN',
                           'DIAERESIS', 'COPYRIGHT SIGN', 'FEMININE ORDINAL INDICATOR',
                           'LEFT-POINTING DOUBLE ANGLE QUOTATION MARK', 'NOT SIGN', 'SOFT HYPHEN', 'REGISTERED SIGN',
                           'MACRON', 'DEGREE SIGN', 'PLUS-MINUS SIGN', 'SUPERSCRIPT TWO', 'SUPERSCRIPT THREE',
                           'ACUTE ACCENT', 'MICRO SIGN', 'PILCROW SIGN', 'MIDDLE DOT', 'CEDILLA', 'SUPERSCRIPT ONE',
                           'MASCULINE ORDINAL INDICATOR', 'RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK',
                           'VULGAR FRACTION ONE QUARTER', 'VULGAR FRACTION ONE HALF', 'VULGAR FRACTION THREE QUARTERS',
                           'INVERTED QUESTION MARK', 'LATIN CAPITAL LETTER A WITH GRAVE',
                           'LATIN CAPITAL LETTER A WITH ACUTE', 'LATIN CAPITAL LETTER A WITH CIRCUMFLEX',
                           'LATIN CAPITAL LETTER A WITH TILDE', 'LATIN CAPITAL LETTER A WITH DIAERESIS',
                           'LATIN CAPITAL LETTER A WITH RING ABOVE', 'LATIN CAPITAL LETTER AE',
                           'LATIN CAPITAL LETTER C WITH CEDILLA', 'LATIN CAPITAL LETTER E WITH GRAVE',
                           'LATIN CAPITAL LETTER E WITH ACUTE', 'LATIN CAPITAL LETTER E WITH CIRCUMFLEX',
                           'LATIN CAPITAL LETTER E WITH DIAERESIS', 'LATIN CAPITAL LETTER I WITH GRAVE',
                           'LATIN CAPITAL LETTER I WITH ACUTE', 'LATIN CAPITAL LETTER I WITH CIRCUMFLEX',
                           'LATIN CAPITAL LETTER I WITH DIAERESIS', 'LATIN CAPITAL LETTER ETH',
                           'LATIN CAPITAL LETTER N WITH TILDE', 'LATIN CAPITAL LETTER O WITH GRAVE',
                           'LATIN CAPITAL LETTER O WITH ACUTE', 'LATIN CAPITAL LETTER O WITH CIRCUMFLEX',
                           'LATIN CAPITAL LETTER O WITH TILDE', 'LATIN CAPITAL LETTER O WITH DIAERESIS',
                           'MULTIPLICATION SIGN', 'LATIN CAPITAL LETTER O WITH STROKE',
                           'LATIN CAPITAL LETTER U WITH GRAVE', 'LATIN CAPITAL LETTER U WITH ACUTE',
                           'LATIN CAPITAL LETTER U WITH CIRCUMFLEX', 'LATIN CAPITAL LETTER U WITH DIAERESIS',
                           'LATIN CAPITAL LETTER Y WITH ACUTE', 'LATIN CAPITAL LETTER THORN',
                           'LATIN SMALL LETTER SHARP S', 'LATIN SMALL LETTER A WITH GRAVE',
                           'LATIN SMALL LETTER A WITH ACUTE', 'LATIN SMALL LETTER A WITH CIRCUMFLEX',
                           'LATIN SMALL LETTER A WITH TILDE', 'LATIN SMALL LETTER A WITH DIAERESIS',
                           'LATIN SMALL LETTER A WITH RING ABOVE', 'LATIN SMALL LETTER AE',
                           'LATIN SMALL LETTER C WITH CEDILLA', 'LATIN SMALL LETTER E WITH GRAVE',
                           'LATIN SMALL LETTER E WITH ACUTE', 'LATIN SMALL LETTER E WITH CIRCUMFLEX',
                           'LATIN SMALL LETTER E WITH DIAERESIS', 'LATIN SMALL LETTER I WITH GRAVE',
                           'LATIN SMALL LETTER I WITH ACUTE', 'LATIN SMALL LETTER I WITH CIRCUMFLEX',
                           'LATIN SMALL LETTER I WITH DIAERESIS', 'LATIN SMALL LETTER ETH',
                           'LATIN SMALL LETTER N WITH TILDE', 'LATIN SMALL LETTER O WITH GRAVE',
                           'LATIN SMALL LETTER O WITH ACUTE', 'LATIN SMALL LETTER O WITH CIRCUMFLEX',
                           'LATIN SMALL LETTER O WITH TILDE', 'LATIN SMALL LETTER O WITH DIAERESIS', 'DIVISION SIGN',
                           'LATIN SMALL LETTER O WITH STROKE', 'LATIN SMALL LETTER U WITH GRAVE',
                           'LATIN SMALL LETTER U WITH ACUTE', 'LATIN SMALL LETTER U WITH CIRCUMFLEX',
                           'LATIN SMALL LETTER U WITH DIAERESIS', 'LATIN SMALL LETTER Y WITH ACUTE',
                           'LATIN SMALL LETTER THORN', 'LATIN SMALL LETTER Y WITH DIAERESIS']
        self.assertEqual(x, expected_result)

    def test_hello(self):
        x = ownfunctions.replace_signs("hello")
        self.assertEqual(x, "hello")

    def test_maerchen(self):
        x = ownfunctions.replace_signs("m{}rchen".format("\u00E4"))
        self.assertEqual(x, "m{}rchen".format("\u00E4"))

    def test_smiley_u263a(self):
        x = ownfunctions.replace_signs("hallo {}".format("\u263a"))
        self.assertEqual(x, "hallo :-)")

    def test_sum_u2211(self):
        x = ownfunctions.replace_signs("{}(1,2,3,4)".format("\u2211"))
        self.assertEqual(x, "sum(1,2,3,4)")

    def test_squareroot_u221a(self):
        x = ownfunctions.replace_signs("{}(4) = 2".format("\u221a"))
        self.assertEqual(x, "sqrt(4) = 2")

    def test_newline(self):
        x = ownfunctions.replace_signs("hello\nWorld")
        self.assertEqual(x, "hello\nWorld")

    def test_tab(self):
        x = ownfunctions.replace_signs("hello\tWorld\v")
        self.assertEqual(x, "hello\tWorld\v")

    def test_unknown_sign(self):
        x = ownfunctions.replace_signs("Flag Turkey: {}".format("\u262a"))
        self.assertEqual(x, "Flag Turkey: {}".format("\u001a"))


class TestShowXML(unittest.TestCase):

    def test(self):
        self.maxDiff = None
        tree = ElementTree.parse(r"..\tests\examples\xml_test.gpx")
        out = StringIO()
        sys.stdout = out
        ownfunctions.show_xml(tree)
        output = out.getvalue()
        expected_output = "{http://www.topografix.com/GPX/1/1}gpx {'creator': 'eTrex 10', 'version': '1.1', '{http://www" \
                          ".w3.org/2001/XMLSchema-instance}schemaLocation': 'http://www.topografix.com/GPX/1/1 " \
                          "http://www.topografix.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3" \
                          " http://www8.garmin.com/xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/Way" \
                          "pointExtension/v1 http://www8.garmin.com/xmlschemas/WaypointExtensionv1.xsd http://www.garmin" \
                          ".com/xmlschemas/TrackPointExtension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1" \
                          ".xsd'} \n"
        expected_output += "{http://www.topografix.com/GPX/1/1}metadata {} \n"
        expected_output += "{http://www.topografix.com/GPX/1/1}link {'href': 'http://www.garmin.com'} \n"
        expected_output += "{http://www.topografix.com/GPX/1/1}text {} Garmin International\n"
        expected_output += "{http://www.topografix.com/GPX/1/1}time {} 2016-09-10T13:36:17Z\n"
        expected_output += "{http://www.topografix.com/GPX/1/1}wpt {'lat': '49.794845', 'lon': '9.944192'} \n"
        expected_output += "{http://www.topografix.com/GPX/1/1}ele {} 187.175018\n"
        expected_output += "{http://www.topografix.com/GPX/1/1}time {} 2016-09-10T13:36:17Z\n"
        expected_output += "{http://www.topografix.com/GPX/1/1}name {} ELEFANT\n"
        expected_output += "{http://www.topografix.com/GPX/1/1}sym {} Flag, Blue\n"
        expected_output += "{http://www.topografix.com/GPX/1/1}wpt {'lat': '49.793617', 'lon': '9.943833'} \n"
        expected_output += "{http://www.topografix.com/GPX/1/1}ele {} 187.503296\n"
        expected_output += "{http://www.topografix.com/GPX/1/1}time {} 2016-09-10T14:24:16Z\n"
        expected_output += "{http://www.topografix.com/GPX/1/1}name {} ELEFANT FINAL\n"
        expected_output += "{http://www.topografix.com/GPX/1/1}sym {} Flag, Blue\n"
        self.assertEqual(output, expected_output)


class TestValidateCoordinates(unittest.TestCase):

    def test_north_east(self):
        ownfunctions.validate_coordinates([52.520817, 13.40945])

    def test_south_west(self):
        ownfunctions.validate_coordinates([-52.520817, -13.40945])

    def test_equator(self):
        ownfunctions.validate_coordinates([0, 13.40945])

    def test_zero_meridian(self):
        ownfunctions.validate_coordinates([52.520817, 0])

    def test_north_bigger_than_90(self):
        self.assertRaises(ValueError, ownfunctions.validate_coordinates, [92.520817, 13.40945])

    def test_east_bigger_than_180(self):
        self.assertRaises(ValueError, ownfunctions.validate_coordinates, [52.520817, 200.40945])

    def test_north_smaller_than_minus90(self):
        self.assertRaises(ValueError, ownfunctions.validate_coordinates, [-92.520817, 13.40945])

    def test_east_smaller_than_minus180(self):
        self.assertRaises(ValueError, ownfunctions.validate_coordinates, [52.520817, -200.40945])

    def test_one_coord_is_shit(self):
        self.assertRaises(TypeError, ownfunctions.validate_coordinates, [52.520817, "bla"])

    def test_other_coord_is_shit(self):
        self.assertRaises(TypeError, ownfunctions.validate_coordinates, ["bla", 13.40945])

    def test_string_instead_of_list(self):
        self.assertRaises(TypeError, ownfunctions.validate_coordinates, "12")

    def test_list_of_wrong_length(self):
        self.assertRaises(TypeError, ownfunctions.validate_coordinates, [52.520817, 13.40945, 42.42])


class TestCoordsDecimalToMinutes(unittest.TestCase):
    def test_north_east(self):
        x = ownfunctions.coords_decimal_to_minutes([52.520817, 13.40945])
        self.assertEqual(x, "N 52°31.249, E 013°24.567")

    def test_south_west(self):
        x = ownfunctions.coords_decimal_to_minutes([-52.520817, -13.40945])
        self.assertEqual(x, "S 52°31.249, W 013°24.567")

    def test_equator(self):
        x = ownfunctions.coords_decimal_to_minutes([0, 13.40945])
        self.assertEqual(x, "N 00°00.000, E 013°24.567")

    def test_zero_meridian(self):
        x = ownfunctions.coords_decimal_to_minutes([52.520817, 0])
        self.assertEqual(x, "N 52°31.249, E 000°00.000")

    def test_north_bigger_than_90(self):
        self.assertRaises(ValueError, ownfunctions.coords_decimal_to_minutes, [92.520817, 13.40945])

    def test_east_bigger_than_180(self):
        self.assertRaises(ValueError, ownfunctions.coords_decimal_to_minutes, [52.520817, 200.40945])

    def test_north_smaller_than_minus90(self):
        self.assertRaises(ValueError, ownfunctions.coords_decimal_to_minutes, [-92.520817, 13.40945])

    def test_east_smaller_than_minus180(self):
        self.assertRaises(ValueError, ownfunctions.coords_decimal_to_minutes, [52.520817, -200.40945])

    def test_one_coord_is_shit(self):
        self.assertRaises(TypeError, ownfunctions.coords_decimal_to_minutes, [52.520817, "bla"])

    def test_string_instead_of_list(self):
        self.assertRaises(TypeError, ownfunctions.coords_decimal_to_minutes, "12")

    def test_list_of_wrong_length(self):
        self.assertRaises(TypeError, ownfunctions.coords_decimal_to_minutes, [52.520817, 13.40945, 42.42])


class TestCoordsMinutesToDecimal(unittest.TestCase):
    def test_north_east(self):
        x = ownfunctions.coords_minutes_to_decimal("N 52°31.249, E 013°24.567")
        n = round(x[0], 6)
        e = round(x[1], 5)
        self.assertEqual([n, e], [52.520817, 13.40945])

    def test_south_west(self):
        x = ownfunctions.coords_minutes_to_decimal("S 52°31.249, W 013°24.567")
        n = round(x[0], 6)
        e = round(x[1], 5)
        self.assertEqual([n, e], [-52.520817, -13.40945])

    def test_equator(self):
        x = ownfunctions.coords_minutes_to_decimal("N 00°00.000, E 013°24.567")
        n = round(x[0], 6)
        e = round(x[1], 5)
        self.assertEqual([n, e], [0, 13.40945])

    def test_zero_meridian(self):
        x = ownfunctions.coords_minutes_to_decimal("N 52°31.249, E 000°00.000")
        n = round(x[0], 6)
        e = round(x[1], 5)
        self.assertEqual([n, e], [52.520817, 0])

    def test_north_bigger_than_90(self):
        self.assertEqual(ownfunctions.coords_minutes_to_decimal("N 90°31.249, E 013°24.567"), None)

    def test_east_bigger_than_180(self):
        self.assertEqual(ownfunctions.coords_minutes_to_decimal("N 52°31.249, E 213°24.567"), None)

    def test_north_bigger_than_90_south(self):
        self.assertEqual(ownfunctions.coords_minutes_to_decimal("S 92°31.249, E 013°24.567"), None)

    def test_east_bigger_than_180_west(self):
        self.assertEqual(ownfunctions.coords_minutes_to_decimal("N 52°31.249, W 213°24.567"), None)

    def test_small_mistake_in_unicode(self):
        self.assertRaises(ValueError, ownfunctions.coords_minutes_to_decimal, "N 92°310249, E 013°24.567")

    def test_list_instead_of_unicode(self):
        self.assertRaises(TypeError, ownfunctions.coords_minutes_to_decimal, ["N 52°31.249, E 013°24.567"])


class TestCoordsMinutesToSeconds(unittest.TestCase):
    def test_north_east(self):
        x = ownfunctions.coords_minutes_to_seconds("N 52°31.249, E 013°24.567")
        self.assertEqual(x, "52°31'14.9\"N+13°24'34.0\"E")

    def test_south_west(self):
        x = ownfunctions.coords_minutes_to_seconds("S 52°31.249, W 013°24.567")
        self.assertEqual(x, "52°31'14.9\"S+13°24'34.0\"W")

    def test_equator(self):
        x = ownfunctions.coords_minutes_to_seconds("N 00°00.000, E 013°24.567")
        self.assertEqual(x, "0°0'0.0\"N+13°24'34.0\"E")

    def test_zero_meridian(self):
        x = ownfunctions.coords_minutes_to_seconds("N 52°31.249, E 000°00.000")
        self.assertEqual(x, "52°31'14.9\"N+0°0'0.0\"E")

    def test_north_bigger_than_90(self):
        self.assertEqual(ownfunctions.coords_minutes_to_seconds("N 90°31.249, E 013°24.567"), None)

    def test_east_bigger_than_180(self):
        self.assertEqual(ownfunctions.coords_minutes_to_seconds("N 52°31.249, E 213°24.567"), None)

    def test_north_bigger_than_90_south(self):
        self.assertEqual(ownfunctions.coords_minutes_to_seconds("S 92°31.249, E 013°24.567"), None)

    def test_east_bigger_than_180_west(self):
        self.assertEqual(ownfunctions.coords_minutes_to_seconds("N 52°31.249, W 213°24.567"), None)

    def test_small_mistake_in_unicode(self):
        self.assertEqual(ownfunctions.coords_minutes_to_seconds("N 92°310249, E 013°24.567"), None)

    def test_list_instead_of_unicode(self):
        self.assertRaises(TypeError, ownfunctions.coords_minutes_to_seconds, ["N 52°31.249, E 013°24.567"])


class TestCoordsUrlToDecimal(unittest.TestCase):
    def test_gc_north_east(self):
        x = ownfunctions.coords_url_to_decimal("https://www.geocaching.com/map/#?ll=49.7821,9.87731&z=14S")
        self.assertEqual(x, [49.7821, 9.87731])

    def test_gc_south_west(self):
        x = ownfunctions.coords_url_to_decimal("https://www.geocaching.com/map/#?ll=-32.54681,-23.20312&z=2")
        self.assertEqual(x, [-32.54681, -23.20312])

    def test_gc_from_special_location(self):
        x = ownfunctions.coords_url_to_decimal("https://www.geocaching.com/map/default.aspx?"
                                               "lat=49.81&lng=9.936667#?ll=49.77877,9.9131&z=14")
        self.assertEqual(x, [49.77877, 9.9131])

    def test_gc_equator(self):
        x = ownfunctions.coords_url_to_decimal("https://www.geocaching.com/map/#?ll=0,-68.49309&z=18")
        self.assertEqual(x, [0.0, -68.49309])

    def test_googlemaps_north_east(self):
        x = ownfunctions.coords_url_to_decimal("https://www.google.de/maps/@49.780988,9.9699965,14z")
        self.assertEqual(x, [49.780988, 9.9699965])

    def test_googlemaps_south_west(self):
        x = ownfunctions.coords_url_to_decimal("https://www.google.de/maps/place/Rio+de+Janeiro,+Brasilien/"
                                               "@-22.9108558,-43.5884197,11z/data=!3m1!4b1!4m5!3m4!1s0x9bde559108a05b:"
                                               "0x50dc426c672fd24e!8m2!3d-22.9068467!4d-43.1728965")
        self.assertEqual(x, [-22.9108558, -43.5884197])

    def test_googlemaps_equator(self):
        x = ownfunctions.coords_url_to_decimal("https://www.google.de/maps/place/0%C2%B000'00.0%22N+34%C2%B027'07.3%22E/"
                                               "@0,34.4497481,17z/data=!4m4!3m3!1s0x0:0x0!8m1!4d34.4520333")
        self.assertEqual(x, [0.0, 34.4497481])

    def test_different_website(self):
        self.assertEqual(ownfunctions.coords_minutes_to_seconds("https://www.google.de/"), None)

    def test_different_input_type(self):
        self.assertRaises(TypeError, ownfunctions.coords_minutes_to_seconds, 42)


class TestCoordsStringToDecimal(unittest.TestCase):
    def test_manual_coords(self):
        x = ownfunctions.coords_string_to_decimal("N 52°31.249, E 013°24.567")
        n = round(x[0], 6)
        e = round(x[1], 5)
        self.assertEqual([n, e], [52.520817, 13.40945])

    def test_geocachingcom_coords(self):
        x = ownfunctions.coords_string_to_decimal("https://www.geocaching.com/map/#?ll=49.7821,9.87731&z=14S")
        self.assertEqual(x, [49.7821, 9.87731])

    def test_googlemaps_coords(self):
        x = ownfunctions.coords_string_to_decimal("https://www.google.de/maps/place/Rio+de+Janeiro,+Brasilien/"
                                                  "@-22.9108558,-43.5884197,11z/data=!3m1!4b1!4m5!3m4!1s0x9bde559108a05b"
                                                  ":0x50dc426c672fd24e!8m2!3d-22.9068467!4d-43.1728965")
        self.assertEqual(x, [-22.9108558, -43.5884197])

    def test_bullshitstring_givesNone(self):
        x = ownfunctions.coords_string_to_decimal("grwttqq")
        self.assertEqual(x, None)

    def test_nostring_givesError(self):
        self.assertRaises(TypeError, ownfunctions.coords_string_to_decimal, 42)


class TestCalculateDistance(unittest.TestCase):
    def test_both_north_east(self):
        x = ownfunctions.calculate_distance([49.7781628, 9.8729888], [50.3342402, 10.1413188])
        x = round(x, 1)
        self.assertEqual(x, 64.7)

    def test_both_south_west(self):
        x = ownfunctions.calculate_distance([-49.7781628, -9.8729888], [-50.3342402, -10.1413188])
        x = round(x, 1)
        self.assertEqual(x, 64.7)

    def test_both_identical(self):
        x = ownfunctions.calculate_distance([49.7781628, 9.8729888], [49.7781628, 9.8729888])
        self.assertEqual(x, 0)

    def test_one_north_one_south(self):
        x = ownfunctions.calculate_distance([0.1245831, 29.2351313], [-0.0968813, 29.2067241])
        x = round(x, 1)
        self.assertEqual(x, 24.8)

    def test_one_east_one_west(self):
        x = ownfunctions.calculate_distance([51.4819611, -0.0030331], [51.476207, 0.0216696])
        x = round(x, 1)
        self.assertEqual(x, 1.8)

    def test_both_sides_of_dateline(self):
        x = ownfunctions.calculate_distance([-16.9008043, 179.9575312], [-16.826478, -179.9430943])
        x = round(x, 1)
        self.assertEqual(x, 13.4)

    def test_north_bigger_than_90(self):
        self.assertRaises(ValueError, ownfunctions.calculate_distance, [92.520817, 13.40945], [49.7781628, 9.8729888])

    def test_east_bigger_than_180(self):
        self.assertRaises(ValueError, ownfunctions.calculate_distance, [52.520817, 200.40945], [49.7781628, 9.8729888])

    def test_north_smaller_than_minus90(self):
        self.assertRaises(ValueError, ownfunctions.calculate_distance, [49.7781628, 9.8729888], [-92.520817, 13.40945])

    def test_east_smaller_than_minus180(self):
        self.assertRaises(ValueError, ownfunctions.calculate_distance, [49.7781628, 9.8729888], [52.520817, -200.40945])

    def test_one_coord_is_shit(self):
        self.assertRaises(TypeError, ownfunctions.calculate_distance, [52.520817, "bla"], [49.7781628, 9.8729888])

    def test_string_instead_of_list(self):
        self.assertRaises(TypeError, ownfunctions.calculate_distance, [49.7781628, 9.8729888], "12")

    def test_list_of_wrong_length(self):
        self.assertRaises(TypeError, ownfunctions.calculate_distance, [52.520817, 13.40945, 42.42],
                          [49.7781628, 9.8729888])


class TestGetYearWithoutCentury(unittest.TestCase):

    def test_1998(self):
        self.assertEqual(ownfunctions.get_year_without_century(1998), 98)

    def test_2000(self):
        self.assertEqual(ownfunctions.get_year_without_century(2000), 00)

    def test_2017(self):
        self.assertEqual(ownfunctions.get_year_without_century(2017), 17)

    def test_827(self):
        self.assertEqual(ownfunctions.get_year_without_century(827), 27)

    def test_float(self):
        self.assertRaises(TypeError, ownfunctions.get_year_without_century, 490.67)

    def test_list(self):
        self.assertRaises(TypeError, ownfunctions.get_year_without_century, [1, 2, 3, 4])

    def test_string(self):
        self.assertRaises(TypeError, ownfunctions.get_year_without_century, "2017")


class TestGetMonthNumber(unittest.TestCase):
    def test_january(self):
        x = ownfunctions.get_month_number("Jan")
        self.assertEqual(x, 1)

    def test_february(self):
        x = ownfunctions.get_month_number("Feb")
        self.assertEqual(x, 2)

    def test_march(self):
        x = ownfunctions.get_month_number("Mar")
        self.assertEqual(x, 3)

    def test_march_ger(self):
        x = ownfunctions.get_month_number("Mrz")
        self.assertEqual(x, 3)

    def test_april(self):
        x = ownfunctions.get_month_number("Apr")
        self.assertEqual(x, 4)

    def test_may(self):
        x = ownfunctions.get_month_number("May")
        self.assertEqual(x, 5)

    def test_june(self):
        x = ownfunctions.get_month_number("Jun")
        self.assertEqual(x, 6)

    def test_july(self):
        x = ownfunctions.get_month_number("Jul")
        self.assertEqual(x, 7)

    def test_august(self):
        x = ownfunctions.get_month_number("Aug")
        self.assertEqual(x, 8)

    def test_september(self):
        x = ownfunctions.get_month_number("Sep")
        self.assertEqual(x, 9)

    def test_october(self):
        x = ownfunctions.get_month_number("Oct")
        self.assertEqual(x, 10)

    def test_october_ger(self):
        x = ownfunctions.get_month_number("Okt")
        self.assertEqual(x, 10)

    def test_november(self):
        x = ownfunctions.get_month_number("Nov")
        self.assertEqual(x, 11)

    def test_december(self):
        x = ownfunctions.get_month_number("Dec")
        self.assertEqual(x, 12)

    def test_december_ger(self):
        x = ownfunctions.get_month_number("Dez")
        self.assertEqual(x, 12)

    def test_other_string_givesNone(self):
        x = ownfunctions.get_month_number("bla")
        self.assertEqual(x, None)

    def test_other_type_givesNone(self):
        x = ownfunctions.get_month_number(42)
        self.assertEqual(x, None)


class TestGetMonth(unittest.TestCase):
    def test_january(self):
        x = ownfunctions.get_month(1)
        self.assertEqual(x, "Jan")

    def test_february(self):
        x = ownfunctions.get_month(2)
        self.assertEqual(x, "Feb")

    def test_march(self):
        x = ownfunctions.get_month(3)
        self.assertEqual(x, "Mar")

    def test_april(self):
        x = ownfunctions.get_month(4)
        self.assertEqual(x, "Apr")

    def test_may(self):
        x = ownfunctions.get_month(5)
        self.assertEqual(x, "May")

    def test_june(self):
        x = ownfunctions.get_month(6)
        self.assertEqual(x, "Jun")

    def test_july(self):
        x = ownfunctions.get_month(7)
        self.assertEqual(x, "Jul")

    def test_august(self):
        x = ownfunctions.get_month(8)
        self.assertEqual(x, "Aug")

    def test_september(self):
        x = ownfunctions.get_month(9)
        self.assertEqual(x, "Sep")

    def test_october(self):
        x = ownfunctions.get_month(10)
        self.assertEqual(x, "Oct")

    def test_november(self):
        x = ownfunctions.get_month(11)
        self.assertEqual(x, "Nov")

    def test_december(self):
        x = ownfunctions.get_month(12)
        self.assertEqual(x, "Dec")

    def test_other_int_givesNone(self):
        x = ownfunctions.get_month(13)
        self.assertEqual(x, None)

    def test_float_givesNone(self):
        x = ownfunctions.get_month(42.3)
        self.assertEqual(x, None)

    def test_other_type_givesNone(self):
        x = ownfunctions.get_month("bla")
        self.assertEqual(x, None)


class TestStringToDate(unittest.TestCase):
    def test_normal_date(self):
        x = ownfunctions.string_to_date("04.07.1990")
        expected_result = datetime.date(1990, 7, 4)
        self.assertEqual(x, expected_result)

    def test_date_has_too_less_signs(self):
        self.assertRaises(ValueError, ownfunctions.string_to_date, "4.7.1990")

    def test_day_is_zero(self):
        self.assertRaises(ValueError, ownfunctions.string_to_date, "00.07.1990")

    def test_month_is_zero(self):
        self.assertRaises(ValueError, ownfunctions.string_to_date, "04.00.1990")

    def test_year_is_zero(self):
        self.assertRaises(ValueError, ownfunctions.string_to_date, "04.07.0000")

    def test_29th_feb(self):
        self.assertRaises(ValueError, ownfunctions.string_to_date, "29.02.2005")

    def test_29th_feb_leapyear(self):
        x = ownfunctions.string_to_date("29.02.2004")
        expected_result = datetime.date(2004, 2, 29)
        self.assertEqual(x, expected_result)

    def test_wrong_type(self):
        self.assertRaises(TypeError, ownfunctions.string_to_date, 42)

    def test_small_mistake_in_string(self):
        self.assertRaises(ValueError, ownfunctions.string_to_date, "29.x2.2005")


class TestRemoveSpaces(unittest.TestCase):
    def test_text(self):
        x = ownfunctions.remove_spaces("   abc   def   ")
        self.assertEqual(x, "abc def")

    def test_wrong_type(self):
        self.assertRaises(TypeError, ownfunctions.remove_spaces, 42)


class TestStringIsInt(unittest.TestCase):

    def test_yes(self):
        self.assertTrue(ownfunctions.string_is_int("10"))

    def test_no(self):
        self.assertFalse(ownfunctions.string_is_int("bla"))

    def test_no_string(self):
        self.assertRaises(TypeError, ownfunctions.string_is_int, [10])


def create_testsuite():
    """creates a testsuite with out of all tests in this file"""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestReplaceSigns))
    suite.addTest(unittest.makeSuite(TestShowXML))
    suite.addTest(unittest.makeSuite(TestValidateCoordinates))
    suite.addTest(unittest.makeSuite(TestCoordsDecimalToMinutes))
    suite.addTest(unittest.makeSuite(TestCoordsMinutesToDecimal))
    suite.addTest(unittest.makeSuite(TestCoordsMinutesToSeconds))
    suite.addTest(unittest.makeSuite(TestCoordsUrlToDecimal))
    suite.addTest(unittest.makeSuite(TestCoordsStringToDecimal))
    suite.addTest(unittest.makeSuite(TestCalculateDistance))
    suite.addTest(unittest.makeSuite(TestGetYearWithoutCentury))
    suite.addTest(unittest.makeSuite(TestGetMonthNumber))
    suite.addTest(unittest.makeSuite(TestGetMonth))
    suite.addTest(unittest.makeSuite(TestStringToDate))
    suite.addTest(unittest.makeSuite(TestRemoveSpaces))
    suite.addTest(unittest.makeSuite(TestStringIsInt))
    return suite


def main(v):
    """runs the testsuite"""
    return test_frame.run(v, create_testsuite, "ownfunctions.py")


if __name__ == '__main__':
    if len(sys.argv) > 1:  # if script is run with argument
        verbosity = int(sys.argv[1])
    else:  # if no argument -> verbosity 1
        verbosity = 1
    main(verbosity)
