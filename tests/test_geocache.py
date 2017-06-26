#!/usr/bin/python
# -*- coding: utf-8 -*-

"""tests for geocache.py"""

from __future__ import print_function

import unittest
import datetime
import sys
import geocache 

saved_stdout = sys.stdout  # save standard output


class TestSaaletalblick(unittest.TestCase):

    def setUp(self):
        self.gc = geocache.Geocache("examples/GC6K86W.gpx")
        
    def test_gccode(self):
        self.assertEqual(self.gc.gccode, "GC6K86W")
        
    def test_name(self):
        self.assertEqual(self.gc.name, "Saaletalblick")
        
    def test_difficulty(self):
        self.assertEqual(self.gc.difficulty, 2)
        
    def test_terrain(self):
        self.assertEqual(self.gc.terrain, 2)
        
    def test_size(self):
        self.assertEqual(self.gc.size, 1)
        
    def test_size_string(self):
        self.assertEqual(self.gc.size_string, "micro")
        
    def test_type(self):
        self.assertEqual(self.gc.type, "Traditional Cache")
        
    def test_longtype(self):
        self.assertEqual(self.gc.longtype, "Traditional Cache")
        
    def test_description(self):
        expected = u"\n\nNach einem kleinen Spaziergang und dem Finden des Döschens werdet ihr mit einem tollen Blick "
        expected += u"ins Saaletal und auf die Saalewiesen belohnt! FTF: Jobi Voma STF: JoLoClMa TTF: Mone216\n\n\t\t\t"
        self.assertEqual(self.gc.description, expected)
    
    def test_hint(self):
        self.assertEqual(self.gc.hint, "Und ab durch die Hecke!")
        
    def test_owner(self):
        self.assertEqual(self.gc.owner, "bigkruemel")
        
    def test_url(self):
        self.assertEqual(self.gc.url, "https://www.geocaching.com/geocache/GC6K86W_saaletalblick")
        
    def test_coordinates(self):
        self.assertEqual(self.gc.coordinates, [50.318883, 10.1936])
        
    def test_coordinates_string(self):
        self.assertEqual(self.gc.coordinates_string, u"N 50°19.133, E 010°11.616")
        
    def test_attributes(self):
        self.assertEqual(self.gc.attributes, ["no camping", "no parking available", "not wheelchair accessible",
                                              "kid friendly", "hike shorter than 1km", "stroller accessible"])
    
    def test_logs(self):
        expected_logs = [['2016-07-16', 'Found it', 'Ziaepf'], ['2016-07-10', "Didn't find it", 'NES-GN 310362'],
                         ['2016-06-20', 'Found it', 'HerbieWo'], ['2016-06-15', 'Found it', "Fantastic'4"],
                         ['2016-06-11', 'Found it', 'vicmouse'], ['2016-06-11', 'Found it', 'melimouse'],
                         ['2016-06-10', 'Found it', 'Mone216'], ['2016-06-08', 'Found it', 'JoLoClMa'],
                         ['2016-06-08', 'Found it', 'Jobi Voma'], ['2016-06-07', 'Publish Listing', 'Sabbelwasser']]
        self.assertEqual(self.gc.logs, expected_logs)
        
    def test_available(self):
        self.assertEqual(self.gc.available, True)
        
    def test_downloaddate(self):
        expected_date = datetime.date(2016, 8, 4)
        self.assertEqual(self.gc.downloaddate, expected_date)
        
    def test_downloaddate_string(self):
        self.assertEqual(self.gc.downloaddate_string, "04 Aug 2016")
        
    def test_shortinfo(self):
        x = self.gc.shortinfo()
        expected = u"GC6K86W | N 50°19.133, E 010°11.616 | Traditional Cache | D 2.0 | T 2.0 | micro   | True  "
        expected += u"| 04 Aug 2016 | Saaletalblick"
        self.assertEqual(x, expected)
        
    def test_longinfo(self):
        x = self.gc.longinfo()
        z1 = u"\nGC6K86W : Saaletalblick"
        z2 = "\n------------------------"
        z3 = u"\nSchwierigkeit: 2.0, Gelaende: 2.0, Groesse: micro, Typ: Traditional Cache"
        z4 = u"\nKoordinaten: N 50°19.133, E 010°11.616"
        z5 = u"\nOwner: bigkruemel"
        z6 = u"\nAttribute: no camping, no parking available, not wheelchair accessible, kid friendly, "
        z6 += u"hike shorter than 1km, stroller accessible"
        z7 = u"\nCache ist aktiv: True, Stand: 04 Aug 2016"
        z8 = u"\nLink: https://www.geocaching.com/geocache/GC6K86W_saaletalblick"
        z9 = u"\n\n\n\nNach einem kleinen Spaziergang und dem Finden des Döschens werdet ihr mit einem tollen Blick ins "
        z9 += u"Saaletal und auf die Saalewiesen belohnt! FTF: Jobi Voma STF: JoLoClMa TTF: Mone216\n\n\t\t\t"
        z10 = u"\nHinweis: Und ab durch die Hecke!"
        z11 = u"\n\n"
        z12 = u"2016-07-16: Found it by Ziaepf\n"
        z13 = u"2016-07-10: Didn't find it by NES-GN 310362\n"
        z14 = u"2016-06-20: Found it by HerbieWo\n"
        z15 = u"2016-06-15: Found it by Fantastic'4\n"
        z16 = u"2016-06-11: Found it by vicmouse\n"
        z17 = u"2016-06-11: Found it by melimouse\n"
        z18 = u"2016-06-10: Found it by Mone216\n"
        z19 = u"2016-06-08: Found it by JoLoClMa\n"
        z20 = u"2016-06-08: Found it by Jobi Voma\n" 
        z21 = u"2016-06-07: Publish Listing by Sabbelwasser\n"
        expected = z1 + z2 + z3 + z4 + z5 + z6 + z7 + z8 + z9 + z10
        expected += z11 + z12 + z13 + z14 + z15 + z16 + z17 + z18 + z19 + z20 + z21
        self.assertEqual(x, expected)


class TestMaerchenstuhl(unittest.TestCase):

    def setUp(self):
        self.gc = geocache.Geocache("examples/GC1XRPM.gpx")
        
    def test_gccode(self):
        self.assertEqual(self.gc.gccode, "GC1XRPM")
        
    def test_name(self):
        self.assertEqual(self.gc.name, u"Im Auftrag ihrer Majestät – Der Märchenstuhl")
        
    def test_difficulty(self):
        self.assertEqual(self.gc.difficulty, 2.5)
        
    def test_terrain(self):
        self.assertEqual(self.gc.terrain, 3.5)
        
    def test_size(self):
        self.assertEqual(self.gc.size, 1)
        
    def test_size_string(self):
        self.assertEqual(self.gc.size_string, "micro")
        
    def test_type(self):
        self.assertEqual(self.gc.type, "Multi-cache")
        
    def test_longtype(self):
        self.assertEqual(self.gc.longtype, "Multi-cache")
        
    def test_hint(self):
        self.assertEqual(self.gc.hint, "Stage 1: Nicht Holz")
        
    def test_owner(self):
        self.assertEqual(self.gc.owner, "team-pandora")
        
    def test_url(self):
        url = "https://www.geocaching.com/geocache/GC1XRPM_im-auftrag-ihrer-majestat-der-marchenstuhl"
        self.assertEqual(self.gc.url, url)
        
    def test_coordinates(self):
        self.assertEqual(self.gc.coordinates, [49.809317, 9.93365])
        
    def test_available(self):
        self.assertEqual(self.gc.available, True)
        
    def test_downloaddate(self):
        expected_date = datetime.date(2016, 9, 6)
        self.assertEqual(self.gc.downloaddate, expected_date)
        
    def test_downloaddate_string(self):
        self.assertEqual(self.gc.downloaddate_string, "06 Sep 2016")
        
    def test_shortinfo(self):
        x = self.gc.shortinfo()
        expected = u"GC1XRPM | N 49°48.559, E 009°56.019 | Multi-cache       | D 2.5 | T 3.5 | micro   | True  "
        expected += u"| 06 Sep 2016 | Im Auftrag ihrer Majestät – Der Märchenstuhl"
        self.assertEqual(x, expected)


class TestTesoroAmeghino(unittest.TestCase):

    def setUp(self):
        self.gc = geocache.Geocache("examples/GC33QGC.gpx")
        
    def test_gccode(self):
        self.assertEqual(self.gc.gccode, "GC33QGC")
        
    def test_name(self):
        self.assertEqual(self.gc.name, u"Tesoro Ameghino")
        
    def test_difficulty(self):
        self.assertEqual(self.gc.difficulty, 2)
        
    def test_terrain(self):
        self.assertEqual(self.gc.terrain, 3)
        
    def test_size(self):
        self.assertEqual(self.gc.size, 2)
        
    def test_size_string(self):
        self.assertEqual(self.gc.size_string, "small")
        
    def test_type(self):
        self.assertEqual(self.gc.type, "Traditional Cache")
        
    def test_longtype(self):
        self.assertEqual(self.gc.longtype, "Traditional Cache")
        
    def test_hint(self):
        hint = "En la entrada de una cueva, bajo piedras. Cerca del camino\nNear the way in a cave entrance, under rocks"
        self.assertEqual(self.gc.hint, hint)
        
    def test_owner(self):
        self.assertEqual(self.gc.owner, u"kariher y familia")
        
    def test_url(self):
        self.assertEqual(self.gc.url, "https://www.geocaching.com/geocache/GC33QGC_tesoro-ameghino")
        
    def test_coordinates(self):
        self.assertEqual(self.gc.coordinates, [-43.695433, -66.4515])
        
    def test_coordinates_string(self):
        self.assertEqual(self.gc.coordinates_string, u"S 43°41.726, W 066°27.090")
        
    def test_available(self):
        self.assertEqual(self.gc.available, True)
        
    def test_downloaddate(self):
        expected_date = datetime.date(2016, 9, 11)
        self.assertEqual(self.gc.downloaddate, expected_date)
        
    def test_downloaddate_string(self):
        self.assertEqual(self.gc.downloaddate_string, "11 Sep 2016")
        
    def test_shortinfo(self):
        x = self.gc.shortinfo()
        expected = u"GC33QGC | S 43°41.726, W 066°27.090 | Traditional Cache | D 2.0 | T 3.0 | small   | True  "
        expected += u"| 11 Sep 2016 | Tesoro Ameghino"
        self.assertEqual(x, expected)


class TestMusikhochschule(unittest.TestCase):

    def setUp(self):
        self.gc = geocache.Geocache("examples/GC6RNTX.gpx")
        
    def test_gccode(self):
        self.assertEqual(self.gc.gccode, "GC6RNTX")
        
    def test_name(self):
        self.assertEqual(self.gc.name, u"Hochschule für Musik 1")
        
    def test_difficulty(self):
        self.assertEqual(self.gc.difficulty, 2)
        
    def test_terrain(self):
        self.assertEqual(self.gc.terrain, 1.5)
        
    def test_size(self):
        self.assertEqual(self.gc.size, 1)
        
    def test_size_string(self):
        self.assertEqual(self.gc.size_string, "micro")
        
    def test_type(self):
        self.assertEqual(self.gc.type, "Mystery Cache")
        
    def test_longtype(self):
        self.assertEqual(self.gc.longtype, "Mystery Cache")
        
    def test_hint(self):
        self.assertEqual(self.gc.hint, "Licht!")
        
    def test_owner(self):
        self.assertEqual(self.gc.owner, u"Müllipützchen")
        
    def test_url(self):
        self.assertEqual(self.gc.url, "https://www.geocaching.com/geocache/GC6RNTX_hochschule-fur-musik-1")
        
    def test_coordinates(self):
        self.assertEqual(self.gc.coordinates, [49.794497, 9.94094])
        
    def test_available(self):
        self.assertEqual(self.gc.available, True)
        
    def test_downloaddate(self):
        expected_date = datetime.date(2016, 10, 8)
        self.assertEqual(self.gc.downloaddate, expected_date)
        
    def test_downloaddate_string(self):
        self.assertEqual(self.gc.downloaddate_string, "08 Oct 2016")


class TestWuerzburgerWebcam(unittest.TestCase):

    def setUp(self):
        self.gc = geocache.Geocache("examples/GCJJ20.gpx")
        
    def test_gccode(self):
        self.assertEqual(self.gc.gccode, "GCJJ20")
        
    def test_name(self):
        self.assertEqual(self.gc.name, "Wuerzburger webcam")
        
    def test_difficulty(self):
        self.assertEqual(self.gc.difficulty, 1)
        
    def test_terrain(self):
        self.assertEqual(self.gc.terrain, 1)
        
    def test_size(self):
        self.assertEqual(self.gc.size, 0)
        
    def test_size_string(self):
        self.assertEqual(self.gc.size_string, "other")
        
    def test_type(self):
        self.assertEqual(self.gc.type, "Unknown Type")
        
    def test_longtype(self):
        self.assertEqual(self.gc.longtype, "Webcam Cache")
        
    def test_hint(self):
        self.assertEqual(self.gc.hint, "No hints available.")
        
    def test_owner(self):
        self.assertEqual(self.gc.owner, "Kea (Buddl&Joddl)")
        
    def test_url(self):
        self.assertEqual(self.gc.url, "https://www.geocaching.com/geocache/GCJJ20_wuerzburger-webcam")
        
    def test_coordinates(self):
        self.assertEqual(self.gc.coordinates, [49.7948, 9.930267])
        
    def test_available(self):
        self.assertEqual(self.gc.available, True)
        
    def test_downloaddate(self):
        expected_date = datetime.date(2016, 10, 29)
        self.assertEqual(self.gc.downloaddate, expected_date)
        
    def test_downloaddate_string(self):
        self.assertEqual(self.gc.downloaddate_string, "29 Oct 2016")
        
    def test_shortinfo(self):
        x = self.gc.shortinfo()
        expected = u"GCJJ20  | N 49°47.688, E 009°55.816 | Unknown Type      | D 1.0 | T 1.0 | other   | True  "
        expected += u"| 29 Oct 2016 | Wuerzburger webcam"
        self.assertEqual(x, expected)
        
    def test_longinfo(self):
        x = self.gc.longinfo()
        z1 = u"\nGCJJ20 : Wuerzburger webcam"
        z2 = "\n----------------------------"
        z3 = u"\nSchwierigkeit: 1.0, Gelaende: 1.0, Groesse: other, Typ: Webcam Cache"
        z4 = u"\nKoordinaten: N 49°47.688, E 009°55.816"
        z5 = u"\nOwner: Kea (Buddl&Joddl)"
        z6 = u"\nAttribute: wheelchair accessible, available in winter, available 24-7, public transit available, "
        z6 += u"parking available, takes less than 1 hour, kid friendly, stroller accessible, dogs allowed"
        z7 = u"\nCache ist aktiv: True, Stand: 29 Oct 2016"
        z8 = u"\nLink: https://www.geocaching.com/geocache/GCJJ20_wuerzburger-webcam"
        z9 = u"\n\n{}".format(self.gc.description)
        z10 = u"\nHinweis: No hints available."
        z11 = u"\n\n"
        for l in self.gc.logs:
            z11 += u"{}: {} by {}\n".format(l[0], l[1], l[2])
        expected = z1 + z2 + z3 + z4 + z5 + z6 + z7 + z8 + z9 + z10 + z11
        self.assertEqual(x, expected)


class TestMedrixErnos(unittest.TestCase):

    def setUp(self):
        self.gc = geocache.Geocache("examples/GC5N23T.gpx")
        
    def test_gccode(self):
        self.assertEqual(self.gc.gccode, "GC5N23T")
        
    def test_name(self):
        self.assertEqual(self.gc.name, u"67 - MedTrix - \u001a\u001a\u001a\u001a\u001a")
        
    def test_difficulty(self):
        self.assertEqual(self.gc.difficulty, 3)
        
    def test_terrain(self):
        self.assertEqual(self.gc.terrain, 4)
        
    def test_size(self):
        self.assertEqual(self.gc.size, 1)
        
    def test_size_string(self):
        self.assertEqual(self.gc.size_string, "micro")
        
    def test_type(self):
        self.assertEqual(self.gc.type, "Mystery Cache")
        
    def test_longtype(self):
        self.assertEqual(self.gc.longtype, "Mystery Cache")
        
    def test_description(self):
        description = u'\n\n<h2 style="font-style:italic;">... unerwartet....plötzlich.... mit einem Hammerschlag.... '
        description += u'JETZT ist sie da: ....<span style="color:#FF0000;">MedTrix</span><span class="marker">, '
        description += u'die erste Würzburger Mystery-Matrix.... 81 Caches, 81 Mysteries, 81 mal ultimativer '
        description += u'Cachingspaß...... Alle D und T Kategorien..... alle Kombinationen..... und alles Rätsel aus '
        description += u'der Kombination von Medizin und Kryptographie... unserem gemeinsamen Spezialgebiet.... '
        description += u'dem Gebiet der 4Ma-Trickser.....</span></h2>\n<h2 style="font-style:italic;">'
        description += u'<span class="marker">und nun viel Spaß</span>!!!</h2>\n<h2 style="font-style:italic;">&nbsp;'
        description += u'</h2>\n<h2 style="font-style:italic;text-align:center;"><strong><u>Hier das Rätsel:</u>'
        description += u'</strong></h2>\n<p>&nbsp;</p>\n<span><br>\n<br>\n<font face="ARIAL" size="3">'
        description += u'Die Hernien sind angeborene oder erworbene Lücken in den tragenden Bauchwandschichten. '
        description += u'Im deutschen bezeichnet man diese als Bruch. Um diese operativ zu versorgen, gibt es mehrere '
        description += u'Möglichkeiten: Eine der ersten war die OP nach ___A___(7). Dabei werden Bauchmuskeln, '
        description += u'Leistenband und Schambeinperiost vernäht. Die Weiterentwicklung davon ist die OP nach '
        description += u'___B___(9), wo über der Bruchlücke eine Fasziendopplung durchgeführt wird. Die OP nach '
        description += u'___C___(12) ist eine weitere Art der Hernienversorgung, in der ein Kunststoffnetz eingesetzt '
        description += u'wird und mit der Muskulatur vernäht, um die Bruchwand hinter dem Leistenkanal zu verstärken. '
        description += u'Zu den neueren Arten der Hernienversorgung zählen die ___D___ (16). Hier unterscheidet man '
        description += u'drei Methoden: Bei der __E__ (4) wird ein Pneumoperitoneum angelegt, wo ein Netz innenseitig '
        description += u'zwischen Bruchpforte und Bauchwand fixiert wird. Im Gegensatz dazu wird bei der ___F___ (3) '
        description += u'außerhalb des Bauchraumes operiert und ein Netz zwischen Muskulatur und Bauchwand eingelegt, '
        description += u'um die Bruchpforte zu verschließen. Die ___G___ (4)-Methode beschreibt eine Hernienversorgung '
        description += u'mittels Netzeinlage direkt an das Bauchfell. Dafür gibt es spezielle Netze, die auf der '
        description += u'viszeralen Seite besonders beschichtet sind. Das Ziel der operativen Versorgung ist die '
        description += u'Behebung der Hernie und die Vermeidung von Rezidiven. &nbsp;</font></span>\n<p><span><span>'
        description += u'<span><br>\n<br>\n<font face="ARIAL" size="3">Findet die Wörter aus dem Lückentext und bildet '
        description += u'dann die Buchstabenwortwerte! Setzt sie dann in unten stehende Formel ein!</font></span><br>\n'
        description += u'<br></span></span></p>\n<p><span><span><br>\n<br>\n<font face="Tahoma" size="3">Formel zur '
        description += u'Berechnung des Finals:<br>\n<br>\n<b>N 49°(AxB/146). sum(A, B, D, E, G) // '
        description += u'E 009°(sqrt(E*G+C-31). E*G-E*F + D/2</b></font></span><br>\n<br></span></p>\n<br>\n<br>\n'
        description += u'<a href="http://geocheck.org/geo_inputchkcoord.php?gid=620474120c36e28-b765-4ff6-a6e4-'
        description += u'b2f00c504981"><img src="http://geocheck.org/geocheck_large.php?gid=620474120c36e28-b765-'
        description += u'4ff6-a6e4-b2f00c504981" title="Prüfe Deine Lösung" border="0"></a>\n\n\t\t\t'
        self.assertEqual(self.gc.description, description)

    def test_hint(self):
        hint = "Indoor: die Zahlen in Klammern sind die Anzahl der Buchstaben\nOutdoor: oben :-) Mit Leiter"
        self.assertEqual(self.gc.hint, hint)
        
    def test_owner(self):
        self.assertEqual(self.gc.owner, ":-)Biene@85")
        
    def test_url(self):
        self.assertEqual(self.gc.url, "https://www.geocaching.com/geocache/GC5N23T_67-medtrix")
        
    def test_coordinates(self):
        self.assertEqual(self.gc.coordinates, [49.80761666666667, 9.912116666666666])
        
    def test_logs(self):
        expected_logs = [['2016-07-03', 'Found it', ':-)Mitchsa & firefly70'], ['2016-04-03', "Found it", 'Hackstock']]
        self.assertEqual(self.gc.logs, expected_logs)
        
    def test_available(self):
        self.assertEqual(self.gc.available, True)
        
    def test_downloaddate(self):
        expected_date = datetime.date(2017, 1, 9)
        self.assertEqual(self.gc.downloaddate, expected_date)
        
    def test_downloaddate_string(self):
        self.assertEqual(self.gc.downloaddate_string, "09 Jan 2017")


class TestInvalidInput(unittest.TestCase):
        
    def test_wrong_type(self):
        self.assertRaises(TypeError, geocache.Geocache, [4, 2])
        
    def test_not_existing_file(self):
        self.assertRaises(IOError, geocache.Geocache, "examples/dfgjlg.gpx")
        
    def test_broken_file(self):
        exception = False             # has to be that complicated because ParseError unknown 
        # noinspection PyBroadException
        try:
            geocache.Geocache("examples/GC6V4PN.gpx")
        except:   # broad exception because ParseError unknown
            exception = True
        self.assertTrue(exception)
        
    def test_missing_attributes(self):
        self.assertRaises(AttributeError, geocache.Geocache, "examples/GC6V793.gpx")


def create_testsuite():
    """creates a testsuite with out of all tests in this file"""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSaaletalblick))
    suite.addTest(unittest.makeSuite(TestMaerchenstuhl))
    suite.addTest(unittest.makeSuite(TestTesoroAmeghino))
    suite.addTest(unittest.makeSuite(TestMusikhochschule))
    suite.addTest(unittest.makeSuite(TestWuerzburgerWebcam))
    suite.addTest(unittest.makeSuite(TestMedrixErnos))
    suite.addTest(unittest.makeSuite(TestInvalidInput))
    return suite


def main(v):
    """runs the testsuite"""
    sys.stdout = saved_stdout  # print output to display
    print("\nTesting geocache.py")
    testsuite = create_testsuite()
    x = unittest.TextTestRunner(verbosity=v).run(testsuite) 
    return x.testsRun, len(x.failures), len(x.errors)

if __name__ == '__main__':
    main(2)
