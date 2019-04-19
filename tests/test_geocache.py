#!/usr/bin/python
# -*- coding: utf-8 -*-

"""tests for geocache.py"""

import unittest
import datetime
import sys
import xml.etree.ElementTree as ElementTree
import test_frame
import geocache


class TestSaaletalblick(unittest.TestCase):

    def setUp(self):
        """creates a geocache object for the tests"""
        self.gc = geocache.Geocache("../tests/examples/GC6K86W.gpx")

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
        expected = "\n\nNach einem kleinen Spaziergang und dem Finden des Döschens werdet ihr mit einem tollen Blick "
        expected += "ins Saaletal und auf die Saalewiesen belohnt! FTF: Jobi Voma STF: JoLoClMa TTF: Mone216\n\n\t\t\t"
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
        self.assertEqual(self.gc.coordinates_string, "N 50°19.133, E 010°11.616")

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

    def test_date(self):
        expected_date = datetime.date(2016, 8, 4)
        self.assertEqual(self.gc.date, expected_date)

    def test_date_string(self):
        self.assertEqual(self.gc.date_string, "04 Aug 2016")

    def test_shortinfo(self):
        x = self.gc.shortinfo()
        expected = "GC6K86W | N 50°19.133, E 010°11.616 | Traditional Cache | D 2.0 | T 2.0 | micro   | True  "
        expected += "| 04 Aug 2016 | Saaletalblick"
        self.assertEqual(x, expected)

    def test_longinfo(self):
        x = self.gc.longinfo()
        z1 = "\nGC6K86W : Saaletalblick"
        z2 = "\n------------------------"
        z3 = "\nSchwierigkeit: 2.0, Gelaende: 2.0, Groesse: micro, Typ: Traditional Cache"
        z4 = "\nKoordinaten: N 50°19.133, E 010°11.616"
        z5 = "\nOwner: bigkruemel"
        z6 = "\nAttribute: no camping, no parking available, not wheelchair accessible, kid friendly, "
        z6 += "hike shorter than 1km, stroller accessible"
        z7 = "\nCache ist aktiv: True, Stand: 04 Aug 2016"
        z8 = "\nLink: https://www.geocaching.com/geocache/GC6K86W_saaletalblick"
        z9 = "\n\n\n\nNach einem kleinen Spaziergang und dem Finden des Döschens werdet ihr mit einem tollen Blick ins "
        z9 += "Saaletal und auf die Saalewiesen belohnt! FTF: Jobi Voma STF: JoLoClMa TTF: Mone216\n\n\t\t\t"
        z10 = "\nHinweis: Und ab durch die Hecke!"
        z11 = "\n\n"
        z12 = "2016-07-16: Found it by Ziaepf\n"
        z13 = "2016-07-10: Didn't find it by NES-GN 310362\n"
        z14 = "2016-06-20: Found it by HerbieWo\n"
        z15 = "2016-06-15: Found it by Fantastic'4\n"
        z16 = "2016-06-11: Found it by vicmouse\n"
        z17 = "2016-06-11: Found it by melimouse\n"
        z18 = "2016-06-10: Found it by Mone216\n"
        z19 = "2016-06-08: Found it by JoLoClMa\n"
        z20 = "2016-06-08: Found it by Jobi Voma\n"
        z21 = "2016-06-07: Publish Listing by Sabbelwasser\n"
        expected = z1 + z2 + z3 + z4 + z5 + z6 + z7 + z8 + z9 + z10
        expected += z11 + z12 + z13 + z14 + z15 + z16 + z17 + z18 + z19 + z20 + z21
        self.assertEqual(x, expected)


class TestUpdateDate(unittest.TestCase):

    def setUp(self):
        """creates a geocache object for the tests"""
        self.gc = geocache.Geocache("../tests/examples/GC6K86W.gpx")

    def test_update_date_format1(self):
        self.gc.update_date("04.07.1990")
        self.assertEqual(self.gc.date, datetime.date(1990, 7, 4))
        self.assertEqual(self.gc.date_string, "04 Jul 1990")

    def test_update_date_format2(self):
        self.gc.update_date("04 Jul 1990")
        self.assertEqual(self.gc.date, datetime.date(1990, 7, 4))
        self.assertEqual(self.gc.date_string, "04 Jul 1990")

    def test_update_date_format3(self):
        self.gc.update_date("1990-07-04")
        self.assertEqual(self.gc.date, datetime.date(1990, 7, 4))
        self.assertEqual(self.gc.date_string, "04 Jul 1990")

    def test_unvalid_date_gives_error(self):
        self.assertRaises(ValueError, self.gc.update_date, "4.7.90")


class TestGeocacheWaypoints(unittest.TestCase):

    def setUp(self):
        """creates a geocache object for the tests"""
        self.gc = geocache.Geocache("../tests/examples/GC6K86W.gpx")
        self.w = geocache.Waypoint("name (GC6K86W)", [50.328883, 10.1536])
        self.w.find_shown_name_and_distance(self.gc)
        self.w2 = geocache.Waypoint("waypoint2 (GC6K86W)", [50.325883, 10.1546])
        self.w2.find_shown_name_and_distance(self.gc)
        self.gc.add_waypoint(self.w)
        self.gc.add_waypoint(self.w2)

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
        expected = "\n\nNach einem kleinen Spaziergang und dem Finden des Döschens werdet ihr mit einem tollen Blick "
        expected += "ins Saaletal und auf die Saalewiesen belohnt! FTF: Jobi Voma STF: JoLoClMa TTF: Mone216\n\n\t\t\t"
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
        self.assertEqual(self.gc.coordinates_string, "N 50°19.133, E 010°11.616")

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

    def test_date(self):
        expected_date = datetime.date(2016, 8, 4)
        self.assertEqual(self.gc.date, expected_date)

    def test_date_string(self):
        self.assertEqual(self.gc.date_string, "04 Aug 2016")

    def test_waypoints(self):
        self.assertEqual(self.gc.waypoints, [self.w, self.w2])

    def test_add_waypoint(self):
        w_neu = geocache.Waypoint("neu (GC6K86W)", [50.418883, 10.2])
        self.gc.add_waypoint(w_neu)
        self.assertEqual(w_neu.shown_name, "NEU")
        self.assertEqual(self.gc.waypoints, [self.w, self.w2, w_neu])

    def test_add_waypoint_not_a_waypoint(self):
        self.assertRaises(TypeError, self.gc.add_waypoint, "w_neu")

    def test_shortinfo(self):
        x = self.gc.shortinfo()
        expected = "GC6K86W | N 50°19.133, E 010°11.616 | Traditional Cache | D 2.0 | T 2.0 | micro   | True  "
        expected += "| 04 Aug 2016 | Saaletalblick"
        expected += "\n        | N 50°19.733, E 010°09.216 | NAME (3.0km)"
        expected += "\n        | N 50°19.553, E 010°09.276 | WAYPOINT2 (2.9km)"
        self.assertEqual(x, expected)

    def test_shortinfo_spaces(self):
        x = self.gc.shortinfo(5)
        expected = "GC6K86W | N 50°19.133, E 010°11.616 | Traditional Cache | D 2.0 | T 2.0 | micro   | True  "
        expected += "| 04 Aug 2016 | Saaletalblick"
        expected += "\n             | N 50°19.733, E 010°09.216 | NAME (3.0km)"
        expected += "\n             | N 50°19.553, E 010°09.276 | WAYPOINT2 (2.9km)"
        self.assertEqual(x, expected)

    def test_longinfo(self):
        x = self.gc.longinfo()
        z1 = "\nGC6K86W : Saaletalblick"
        z2 = "\n------------------------"
        z3 = "\nSchwierigkeit: 2.0, Gelaende: 2.0, Groesse: micro, Typ: Traditional Cache"
        z4 = "\nKoordinaten: N 50°19.133, E 010°11.616, "
        z4 += "Wegpunkte: NAME (N 50°19.733, E 010°09.216), WAYPOINT2 (N 50°19.553, E 010°09.276)"
        z5 = "\nOwner: bigkruemel"
        z6 = "\nAttribute: no camping, no parking available, not wheelchair accessible, kid friendly, "
        z6 += "hike shorter than 1km, stroller accessible"
        z7 = "\nCache ist aktiv: True, Stand: 04 Aug 2016"
        z8 = "\nLink: https://www.geocaching.com/geocache/GC6K86W_saaletalblick"
        z9 = "\n\n\n\nNach einem kleinen Spaziergang und dem Finden des Döschens werdet ihr mit einem tollen Blick ins "
        z9 += "Saaletal und auf die Saalewiesen belohnt! FTF: Jobi Voma STF: JoLoClMa TTF: Mone216\n\n\t\t\t"
        z10 = "\nHinweis: Und ab durch die Hecke!"
        z11 = "\n\n"
        z12 = "2016-07-16: Found it by Ziaepf\n"
        z13 = "2016-07-10: Didn't find it by NES-GN 310362\n"
        z14 = "2016-06-20: Found it by HerbieWo\n"
        z15 = "2016-06-15: Found it by Fantastic'4\n"
        z16 = "2016-06-11: Found it by vicmouse\n"
        z17 = "2016-06-11: Found it by melimouse\n"
        z18 = "2016-06-10: Found it by Mone216\n"
        z19 = "2016-06-08: Found it by JoLoClMa\n"
        z20 = "2016-06-08: Found it by Jobi Voma\n"
        z21 = "2016-06-07: Publish Listing by Sabbelwasser\n"
        expected = z1 + z2 + z3 + z4 + z5 + z6 + z7 + z8 + z9 + z10
        expected += z11 + z12 + z13 + z14 + z15 + z16 + z17 + z18 + z19 + z20 + z21
        self.assertEqual(x, expected)


class TestMaerchenstuhl(unittest.TestCase):

    def setUp(self):
        """creates a geocache object for the tests"""
        self.gc = geocache.Geocache("../tests/examples/GC1XRPM.gpx")

    def test_gccode(self):
        self.assertEqual(self.gc.gccode, "GC1XRPM")

    def test_name(self):
        self.assertEqual(self.gc.name, "Im Auftrag ihrer Majestät – Der Märchenstuhl")

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

    def test_date(self):
        expected_date = datetime.date(2016, 9, 6)
        self.assertEqual(self.gc.date, expected_date)

    def test_date_string(self):
        self.assertEqual(self.gc.date_string, "06 Sep 2016")

    def test_shortinfo(self):
        x = self.gc.shortinfo()
        expected = "GC1XRPM | N 49°48.559, E 009°56.019 | Multi-cache       | D 2.5 | T 3.5 | micro   | True  "
        expected += "| 06 Sep 2016 | Im Auftrag ihrer Majestät – Der Märchenstuhl"
        self.assertEqual(x, expected)


class TestTesoroAmeghino(unittest.TestCase):

    def setUp(self):
        """creates a geocache object for the tests"""
        self.gc = geocache.Geocache("../tests/examples/GC33QGC.gpx")

    def test_gccode(self):
        self.assertEqual(self.gc.gccode, "GC33QGC")

    def test_name(self):
        self.assertEqual(self.gc.name, "Tesoro Ameghino")

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
        self.assertEqual(self.gc.owner, "kariher y familia")

    def test_url(self):
        self.assertEqual(self.gc.url, "https://www.geocaching.com/geocache/GC33QGC_tesoro-ameghino")

    def test_coordinates(self):
        self.assertEqual(self.gc.coordinates, [-43.695433, -66.4515])

    def test_coordinates_string(self):
        self.assertEqual(self.gc.coordinates_string, "S 43°41.726, W 066°27.090")

    def test_available(self):
        self.assertEqual(self.gc.available, True)

    def test_date(self):
        expected_date = datetime.date(2016, 9, 11)
        self.assertEqual(self.gc.date, expected_date)

    def test_date_string(self):
        self.assertEqual(self.gc.date_string, "11 Sep 2016")

    def test_shortinfo(self):
        x = self.gc.shortinfo()
        expected = "GC33QGC | S 43°41.726, W 066°27.090 | Traditional Cache | D 2.0 | T 3.0 | small   | True  "
        expected += "| 11 Sep 2016 | Tesoro Ameghino"
        self.assertEqual(x, expected)


class TestMusikhochschule(unittest.TestCase):
    def setUp(self):
        """creates a geocache object for the tests"""
        self.gc = geocache.Geocache("../tests/examples/GC6RNTX.gpx")

    def test_gccode(self):
        self.assertEqual(self.gc.gccode, "GC6RNTX")

    def test_name(self):
        self.assertEqual(self.gc.name, "Hochschule für Musik 1")

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
        self.assertEqual(self.gc.owner, "Müllipützchen")

    def test_url(self):
        self.assertEqual(self.gc.url, "https://www.geocaching.com/geocache/GC6RNTX_hochschule-fur-musik-1")

    def test_coordinates(self):
        self.assertEqual(self.gc.coordinates, [49.794497, 9.94094])

    def test_available(self):
        self.assertEqual(self.gc.available, True)

    def test_date(self):
        expected_date = datetime.date(2016, 10, 8)
        self.assertEqual(self.gc.date, expected_date)

    def test_date_string(self):
        self.assertEqual(self.gc.date_string, "08 Oct 2016")


class TestWuerzburgerWebcam(unittest.TestCase):
    def setUp(self):
        """creates a geocache object for the tests"""
        self.gc = geocache.Geocache("../tests/examples/GCJJ20.gpx")

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

    def test_date(self):
        expected_date = datetime.date(2016, 10, 29)
        self.assertEqual(self.gc.date, expected_date)

    def test_date_string(self):
        self.assertEqual(self.gc.date_string, "29 Oct 2016")

    def test_shortinfo(self):
        x = self.gc.shortinfo()
        expected = "GCJJ20  | N 49°47.688, E 009°55.816 | Unknown Type      | D 1.0 | T 1.0 | other   | True  "
        expected += "| 29 Oct 2016 | Wuerzburger webcam"
        self.assertEqual(x, expected)

    def test_longinfo(self):
        x = self.gc.longinfo()
        z1 = "\nGCJJ20 : Wuerzburger webcam"
        z2 = "\n----------------------------"
        z3 = "\nSchwierigkeit: 1.0, Gelaende: 1.0, Groesse: other, Typ: Webcam Cache"
        z4 = "\nKoordinaten: N 49°47.688, E 009°55.816"
        z5 = "\nOwner: Kea (Buddl&Joddl)"
        z6 = "\nAttribute: wheelchair accessible, available in winter, available 24-7, public transit available, "
        z6 += "parking available, takes less than 1 hour, kid friendly, stroller accessible, dogs allowed"
        z7 = "\nCache ist aktiv: True, Stand: 29 Oct 2016"
        z8 = "\nLink: https://www.geocaching.com/geocache/GCJJ20_wuerzburger-webcam"
        z9 = "\n\n{}".format(self.gc.description)
        z10 = "\nHinweis: No hints available."
        z11 = "\n\n"
        for l in self.gc.logs:
            z11 += "{}: {} by {}\n".format(l[0], l[1], l[2])
        expected = z1 + z2 + z3 + z4 + z5 + z6 + z7 + z8 + z9 + z10 + z11
        self.assertEqual(x, expected)


class TestMedrixErnos(unittest.TestCase):
    def setUp(self):
        """creates a geocache object for the tests"""
        self.gc = geocache.Geocache("../tests/examples/GC5N23T.gpx")

    def test_gccode(self):
        self.assertEqual(self.gc.gccode, "GC5N23T")

    def test_name(self):
        self.assertEqual(self.gc.name, "67 - MedTrix - \u001a\u001a\u001a\u001a\u001a")

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
        description = '\n\n<h2 style="font-style:italic;">... unerwartet....plötzlich.... mit einem Hammerschlag.... '
        description += 'JETZT ist sie da: ....<span style="color:#FF0000;">MedTrix</span><span class="marker">, '
        description += 'die erste Würzburger Mystery-Matrix.... 81 Caches, 81 Mysteries, 81 mal ultimativer '
        description += 'Cachingspaß...... Alle D und T Kategorien..... alle Kombinationen..... und alles Rätsel aus '
        description += 'der Kombination von Medizin und Kryptographie... unserem gemeinsamen Spezialgebiet.... '
        description += 'dem Gebiet der 4Ma-Trickser.....</span></h2>\n<h2 style="font-style:italic;">'
        description += '<span class="marker">und nun viel Spaß</span>!!!</h2>\n<h2 style="font-style:italic;">&nbsp;'
        description += '</h2>\n<h2 style="font-style:italic;text-align:center;"><strong><u>Hier das Rätsel:</u>'
        description += '</strong></h2>\n<p>&nbsp;</p>\n<span><br>\n<br>\n<font face="ARIAL" size="3">'
        description += 'Die Hernien sind angeborene oder erworbene Lücken in den tragenden Bauchwandschichten. '
        description += 'Im deutschen bezeichnet man diese als Bruch. Um diese operativ zu versorgen, gibt es mehrere '
        description += 'Möglichkeiten: Eine der ersten war die OP nach ___A___(7). Dabei werden Bauchmuskeln, '
        description += 'Leistenband und Schambeinperiost vernäht. Die Weiterentwicklung davon ist die OP nach '
        description += '___B___(9), wo über der Bruchlücke eine Fasziendopplung durchgeführt wird. Die OP nach '
        description += '___C___(12) ist eine weitere Art der Hernienversorgung, in der ein Kunststoffnetz eingesetzt '
        description += 'wird und mit der Muskulatur vernäht, um die Bruchwand hinter dem Leistenkanal zu verstärken. '
        description += 'Zu den neueren Arten der Hernienversorgung zählen die ___D___ (16). Hier unterscheidet man '
        description += 'drei Methoden: Bei der __E__ (4) wird ein Pneumoperitoneum angelegt, wo ein Netz innenseitig '
        description += 'zwischen Bruchpforte und Bauchwand fixiert wird. Im Gegensatz dazu wird bei der ___F___ (3) '
        description += 'außerhalb des Bauchraumes operiert und ein Netz zwischen Muskulatur und Bauchwand eingelegt, '
        description += 'um die Bruchpforte zu verschließen. Die ___G___ (4)-Methode beschreibt eine Hernienversorgung '
        description += 'mittels Netzeinlage direkt an das Bauchfell. Dafür gibt es spezielle Netze, die auf der '
        description += 'viszeralen Seite besonders beschichtet sind. Das Ziel der operativen Versorgung ist die '
        description += 'Behebung der Hernie und die Vermeidung von Rezidiven. &nbsp;</font></span>\n<p><span><span>'
        description += '<span><br>\n<br>\n<font face="ARIAL" size="3">Findet die Wörter aus dem Lückentext und bildet '
        description += 'dann die Buchstabenwortwerte! Setzt sie dann in unten stehende Formel ein!</font></span><br>\n'
        description += '<br></span></span></p>\n<p><span><span><br>\n<br>\n<font face="Tahoma" size="3">Formel zur '
        description += 'Berechnung des Finals:<br>\n<br>\n<b>N 49°(AxB/146). sum(A, B, D, E, G) // '
        description += 'E 009°(sqrt(E*G+C-31). E*G-E*F + D/2</b></font></span><br>\n<br></span></p>\n<br>\n<br>\n'
        description += '<a href="http://geocheck.org/geo_inputchkcoord.php?gid=620474120c36e28-b765-4ff6-a6e4-'
        description += 'b2f00c504981"><img src="http://geocheck.org/geocheck_large.php?gid=620474120c36e28-b765-'
        description += '4ff6-a6e4-b2f00c504981" title="Prüfe Deine Lösung" border="0"></a>\n\n\t\t\t'
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

    def test_date(self):
        expected_date = datetime.date(2017, 1, 9)
        self.assertEqual(self.gc.date, expected_date)

    def test_date_string(self):
        self.assertEqual(self.gc.date_string, "09 Jan 2017")


class TestEntenteichGPXFromGeocachingCom(unittest.TestCase):

    def setUp(self):
        """creates a geocache object for the tests"""
        self.gc = geocache.Geocache("../tests/examples/GC7FB56.gpx")

    def test_gccode(self):
        self.assertEqual(self.gc.gccode, "GC7FB56")

    def test_name(self):
        self.assertEqual(self.gc.name, "Ententeich")

    def test_difficulty(self):
        self.assertEqual(self.gc.difficulty, 1)

    def test_terrain(self):
        self.assertEqual(self.gc.terrain, 1.5)

    def test_size(self):
        self.assertEqual(self.gc.size, 1)

    def test_size_string(self):
        self.assertEqual(self.gc.size_string, "micro")

    def test_type(self):
        self.assertEqual(self.gc.type, "Traditional Cache")

    def test_longtype(self):
        self.assertEqual(self.gc.longtype, "Traditional Cache")

    def test_description(self):
        expected = "Mein erster versteckter Cache.\n\n\nDer Ententeich ist ein künstlich entstandenes Gewässer im " \
                   "Stadtbezirk Lindleinsmühle. Namensgeber sind die dort ansässigen Enten. Der Teich hat eine " \
                   "Grundfläche von rund 150 auf 40 Meter und wird durch die vorbeifließende Pleichach gespeist. " \
                   "Quelle: WürzburgWiki Dies ist mein erster versteckter Cache. Ich habe diesen Ort ausgesucht, " \
                   "weil wir hier oft mit unserem kleinen Sohn vorbeikommen. Er liebt die Enten:). Ein schöner Ort zum" \
                   " Spazierengehen, Spielen (Spielplatz) oder Ausruhen (Bänke) Das Versteck befindet sich in " \
                   "unmittelbarer Nähe einer Schule. Auf Muggels achten! Das Logbuch bitte erst in den Deckel stecken" \
                   " und dann erst zumachen. Viel Spaß beim Suchen\n"
        self.assertEqual(self.gc.description, expected)

    def test_hint(self):
        self.assertEqual(self.gc.hint, "magnetisch")

    def test_owner(self):
        self.assertEqual(self.gc.owner, "HunterSmurf")

    def test_url(self):
        self.assertEqual(self.gc.url,
                         "https://www.geocaching.com/seek/cache_details.aspx?guid=50e69a74-3a85-46b7-a99b-f8c43efc3a61")

    def test_coordinates(self):
        self.assertEqual(self.gc.coordinates, [49.80985, 9.9648])

    def test_coordinates_string(self):
        self.assertEqual(self.gc.coordinates_string, "N 49°48.591, E 009°57.888")

    def test_attributes(self):
        self.assertEqual(self.gc.attributes, ["Dogs", "Available at all times", "Bicycles", "Parking available",
                                              "Stroller accessible", "Stealth required", "Short hike (less than 1km)"])

    def test_logs(self):
        log1 = ['2017-12-06', 'Found it', 'Monti76', "Schneller Fund! Danke für's Legen und Pflegen des Caches. Tftc #921"]
        text2 = 'Da wir auf anderer Mission ganz in der Nähe waren, haben wir noch einen kurzen Abstecher zum ' \
                'Ententeich gemacht.\n\nDie GZ war schnell ausgemacht und nach ein wenig Fummeln an den üblichen ' \
                'Stellen zeigte sich die kleine Dose auch sofort.\n\nTFTC!'
        log2 = ['2017-12-03', 'Found it', 'famerlor_dragon', text2]
        text3 = 'Nach kurzer Suche hielt famerlor_dragon die Dose in den Händen und wir konnten bei schönstem ' \
                'Winterwetter unsere Stempel im Logbuch verewigen. \n\nTFTC geovi'
        log3 = ['2017-12-04', 'Found it', 'geovi', text3]
        log4 = ['2017-12-03', 'Found it', 'mawil66', 'Schnell gefunden. Diesen Ort kannten wir noch nicht']
        log5 = ['2017-11-27', 'Found it', 'mapaluco',
                'Bekannte location, habs halt ums verrecken nicht aufs Treppchen geschafft!']
        text6 = 'Auf dem Heimweg ging es noch zu diesem Ententeich.\nDas Döschen war, trotz genauer Koordinaten gar ' \
                'nicht so leicht zu entdecken.\nVielen Dank fürs Verstecken.'
        log6 = ['2017-11-27', 'Found it', 'funnymax', text6]
        text7 = 'Auf dem Weg zum Baumarkt haben wir einen kleinen Abstecher hierher gemacht.\nUnser Hobby hat uns schon' \
                ' mehrmals zu diesem Teich geführt und so sind wir auch heute gerne wieder hierher gekommen.\nHoffen wir' \
                ' mal, dass diese Dose etwas länger überlebt als ihre Vorgänger!\n\nVielen Dank fürs erneute Herlocken,' \
                ' den TTF und die Dose vor Ort!'
        log7 = ['2017-11-27', 'Found it', 'NobSim', text7]
        text8 = '[:D][:D][:D] [FTF] [:D][:D][:D]\nAls ich gerade auf der Geocachingkarte herumstöberte, entdeckte ich ' \
                'diesen neuen Tradi. E-Mails gecheckt… Hääää, keine Benachrichtigung?! Haegaer angefragt, ob er was ' \
                'bekommen hat – auch nicht! So ging es zur bekannten Örtlichkeit, wo das Döschen nach kurzer Suche ' \
                'gefunden und ein jungfräuliches Logbuch signiert werden konnte. Danke für’s Herführen & TFTC'
        log8 = ['2017-11-27', 'Found it', 'Alokasie', text8]
        log9 = ['2017-11-27', 'Publish Listing', 'tabula.rasa', 'Published']
        expected_logs = [log1, log2, log3, log4, log5, log6, log7, log8, log9]
        self.assertEqual(self.gc.logs, expected_logs)

    def test_available(self):
        self.assertEqual(self.gc.available, True)

    def test_date(self):
        expected_date = datetime.date(2017, 12, 10)
        self.assertEqual(self.gc.date, expected_date)

    def test_date_string(self):
        self.assertEqual(self.gc.date_string, "10 Dec 2017")

    def test_shortinfo(self):
        x = self.gc.shortinfo()
        expected = "GC7FB56 | N 49°48.591, E 009°57.888 | Traditional Cache | D 1.0 | T 1.5 | micro   | True  "
        expected += "| 10 Dec 2017 | Ententeich"
        self.assertEqual(x, expected)

    def test_longinfo(self):
        x = self.gc.longinfo()
        z1 = "\nGC7FB56 : Ententeich"
        z2 = "\n---------------------"
        z3 = "\nSchwierigkeit: 1.0, Gelaende: 1.5, Groesse: micro, Typ: Traditional Cache"
        z4 = "\nKoordinaten: N 49°48.591, E 009°57.888"
        z5 = "\nOwner: HunterSmurf"
        z6 = "\nAttribute: Dogs, Available at all times, Bicycles, Parking available, Stroller accessible, Stealth " \
             "required, Short hike (less than 1km)"
        z7 = "\nCache ist aktiv: True, Stand: 10 Dec 2017"
        z8 = "\nLink: https://www.geocaching.com/seek/cache_details.aspx?guid=50e69a74-3a85-46b7-a99b-f8c43efc3a61"
        z9 = "\n\nMein erster versteckter Cache.\n\n\nDer Ententeich ist ein künstlich entstandenes Gewässer im " \
             "Stadtbezirk Lindleinsmühle. Namensgeber sind die dort ansässigen Enten. Der Teich hat eine " \
             "Grundfläche von rund 150 auf 40 Meter und wird durch die vorbeifließende Pleichach gespeist. " \
             "Quelle: WürzburgWiki Dies ist mein erster versteckter Cache. Ich habe diesen Ort ausgesucht, " \
             "weil wir hier oft mit unserem kleinen Sohn vorbeikommen. Er liebt die Enten:). Ein schöner Ort zum" \
             " Spazierengehen, Spielen (Spielplatz) oder Ausruhen (Bänke) Das Versteck befindet sich in " \
             "unmittelbarer Nähe einer Schule. Auf Muggels achten! Das Logbuch bitte erst in den Deckel stecken" \
             " und dann erst zumachen. Viel Spaß beim Suchen\n"
        z10 = "\nHinweis: magnetisch"
        z11 = "\n\n"
        z12 = "2017-12-06: Found it by Monti76\n"
        z12 += "Schneller Fund! Danke für's Legen und Pflegen des Caches. Tftc #921\n\n"
        z13 = "2017-12-03: Found it by famerlor_dragon\n"
        z13 += 'Da wir auf anderer Mission ganz in der Nähe waren, haben wir noch einen kurzen Abstecher zum ' \
               'Ententeich gemacht.\n\nDie GZ war schnell ausgemacht und nach ein wenig Fummeln an den üblichen ' \
               'Stellen zeigte sich die kleine Dose auch sofort.\n\nTFTC!\n\n'
        z14 = "2017-12-04: Found it by geovi\n"
        z14 += 'Nach kurzer Suche hielt famerlor_dragon die Dose in den Händen und wir konnten bei schönstem ' \
               'Winterwetter unsere Stempel im Logbuch verewigen. \n\nTFTC geovi\n\n'
        z15 = "2017-12-03: Found it by mawil66\n"
        z15 += 'Schnell gefunden. Diesen Ort kannten wir noch nicht\n\n'
        z16 = "2017-11-27: Found it by mapaluco\n"
        z16 += 'Bekannte location, habs halt ums verrecken nicht aufs Treppchen geschafft!\n\n'
        z17 = "2017-11-27: Found it by funnymax\n"
        z17 += 'Auf dem Heimweg ging es noch zu diesem Ententeich.\nDas Döschen war, trotz genauer Koordinaten gar ' \
               'nicht so leicht zu entdecken.\nVielen Dank fürs Verstecken.\n\n'
        z18 = "2017-11-27: Found it by NobSim\n"
        z18 += 'Auf dem Weg zum Baumarkt haben wir einen kleinen Abstecher hierher gemacht.\nUnser Hobby hat uns schon' \
               ' mehrmals zu diesem Teich geführt und so sind wir auch heute gerne wieder hierher gekommen.\nHoffen wir' \
               ' mal, dass diese Dose etwas länger überlebt als ihre Vorgänger!\n\nVielen Dank fürs erneute Herlocken,' \
               ' den TTF und die Dose vor Ort!\n\n'
        z19 = "2017-11-27: Found it by Alokasie\n"
        z19 += '[:D][:D][:D] [FTF] [:D][:D][:D]\nAls ich gerade auf der Geocachingkarte herumstöberte, entdeckte ich ' \
               'diesen neuen Tradi. E-Mails gecheckt… Hääää, keine Benachrichtigung?! Haegaer angefragt, ob er was ' \
               'bekommen hat – auch nicht! So ging es zur bekannten Örtlichkeit, wo das Döschen nach kurzer Suche ' \
               'gefunden und ein jungfräuliches Logbuch signiert werden konnte. Danke für’s Herführen & TFTC\n\n'
        z20 = "2017-11-27: Publish Listing by tabula.rasa\n"
        z20 += 'Published\n\n'
        expected = z1 + z2 + z3 + z4 + z5 + z6 + z7 + z8 + z9 + z10
        expected += z11 + z12 + z13 + z14 + z15 + z16 + z17 + z18 + z19 + z20
        self.assertEqual(x, expected)


class TestInvalidInput(unittest.TestCase):
    def test_wrong_type(self):
        self.assertRaises(TypeError, geocache.Geocache, [4, 2])

    def test_not_existing_file(self):
        self.assertRaises(IOError, geocache.Geocache, "../tests/examples/dfgjlg.gpx")

    def test_broken_file(self):
        exception = False  # has to be that complicated because ParseError unknown
        try:
            geocache.Geocache("../tests/examples/GC6V4PN.gpx")
        except ElementTree.ParseError:
            exception = True
        self.assertTrue(exception)

    def test_missing_attributes(self):
        self.assertRaises(AttributeError, geocache.Geocache, "../tests/examples/GC6V793.gpx")


class TestWaypointInit(unittest.TestCase):

    def test_normal(self):
        w = geocache.Waypoint("NAME", [49.80761666666667, 9.912116666666666])
        self.assertEqual(w.name, "NAME")
        self.assertEqual(w.shown_name, "NAME")
        self.assertEqual(w.coordinates, [49.80761666666667, 9.912116666666666])
        self.assertEqual(w.coordinates_string, "N 49°48.457, E 009°54.727")
        self.assertIsNone(w.distance)

    def test_lowercase_letters_in_name(self):
        w = geocache.Waypoint("nAmE", [49.80761666666667, 9.912116666666666])
        self.assertEqual(w.name, "NAME")
        self.assertEqual(w.shown_name, "NAME")

    def test_strange_signs_in_name(self):
        self.assertRaises(TypeError, geocache.Waypoint, "abc§def", [49.80761666666667, 9.912116666666666])

    def test_name_is_not_a_string(self):
        self.assertRaises(TypeError, geocache.Waypoint, 42, [49.80761666666667, 9.912116666666666])

    def test_coordinates_south_west(self):
        w = geocache.Waypoint("NAME", [-52.520817, -13.40945])
        self.assertEqual(w.coordinates, [-52.520817, -13.40945])
        self.assertEqual(w.coordinates_string, "S 52°31.249, W 013°24.567")

    def test_coordinates_equator(self):
        w = geocache.Waypoint("NAME", [0, 13.40945])
        self.assertEqual(w.coordinates, [0, 13.40945])
        self.assertEqual(w.coordinates_string, "N 00°00.000, E 013°24.567")

    def test_coordinates_zero_meridian(self):
        w = geocache.Waypoint("NAME", [52.520817, 0])
        self.assertEqual(w.coordinates, [52.520817, 0])
        self.assertEqual(w.coordinates_string, "N 52°31.249, E 000°00.000")

    def test_coordinates_north_bigger_than_90(self):
        self.assertRaises(ValueError, geocache.Waypoint, "NAME", [92.520817, 13.40945])

    def test_coordinates_east_bigger_than_180(self):
        self.assertRaises(ValueError, geocache.Waypoint, "NAME", [52.520817, 200.40945])

    def test_coordinates_north_smaller_than_minus90(self):
        self.assertRaises(ValueError, geocache.Waypoint, "NAME", [-92.520817, 13.40945])

    def test_coordinates_east_smaller_than_minus180(self):
        self.assertRaises(ValueError, geocache.Waypoint, "NAME", [52.520817, -200.40945])

    def test_coordinates_one_coord_is_shit(self):
        self.assertRaises(TypeError, geocache.Waypoint, "NAME", [52.520817, "bla"])

    def test_coordinates_string_instead_of_list(self):
        self.assertRaises(TypeError, geocache.Waypoint, "NAME", "12")

    def test_coordinates_list_of_wrong_length(self):
        self.assertRaises(TypeError, geocache.Waypoint, "NAME", [52.520817, 13.40945, 42.42])

    def test_wrong_number_of_arguments(self):
        self.assertRaises(TypeError, geocache.Waypoint, "NAME", [52.520817, 0], "bla")


class TestWaypointFindShownNameAndDistance(unittest.TestCase):

    def test_everything_fine(self):
        g = geocache.Geocache("../tests/examples/GC6K86W.gpx")
        w = geocache.Waypoint("name (GC6K86W)", [49.80761666666667, 9.912116666666666])
        w.find_shown_name_and_distance(g)
        self.assertEqual(w.shown_name, "NAME")
        self.assertEqual(w.distance, 60.26787767312747)

    def test_wrong_geocache(self):
        g = geocache.Geocache("../tests/examples/GC6K86W.gpx")
        w = geocache.Waypoint("name (GC6K77W)", [49.80761666666667, 9.912116666666666])
        self.assertRaises(TypeError, w.find_shown_name_and_distance, g)

    def test_first_bracket_is_missing(self):
        g = geocache.Geocache("../tests/examples/GC6K86W.gpx")
        w = geocache.Waypoint("name GC6K86W)", [49.80761666666667, 9.912116666666666])
        self.assertRaises(TypeError, w.find_shown_name_and_distance, g)

    def test_second_bracket_is_missing(self):
        g = geocache.Geocache("../tests/examples/GC6K86W.gpx")
        w = geocache.Waypoint("name (GC6K86)", [49.80761666666667, 9.912116666666666])
        self.assertRaises(TypeError, w.find_shown_name_and_distance, g)

    def test_gc_is_wrong(self):
        g = geocache.Geocache("../tests/examples/GC6K86W.gpx")
        w = geocache.Waypoint("name (G6K86)", [49.80761666666667, 9.912116666666666])
        self.assertRaises(TypeError, w.find_shown_name_and_distance, g)

    def test_everything_is_wrong(self):
        g = geocache.Geocache("../tests/examples/GC6K86W.gpx")
        w = geocache.Waypoint("name", [49.80761666666667, 9.912116666666666])
        self.assertRaises(TypeError, w.find_shown_name_and_distance, g)


class TestWaypointInfo(unittest.TestCase):

    def test_without_geocache(self):
        w = geocache.Waypoint("name (GC6K86W)", [49.80761666666667, 9.912116666666666])
        self.assertEqual(w.info(), "        | N 49°48.457, E 009°54.727 | NAME (GC6K86W)")

    def test_with_geocache(self):
        w = geocache.Waypoint("name (GC6K86W)", [49.80761666666667, 9.912116666666666])
        g = geocache.Geocache("../tests/examples/GC6K86W.gpx")
        w.find_shown_name_and_distance(g)
        self.assertEqual(w.info(), "        | N 49°48.457, E 009°54.727 | NAME (60.3km)")


def create_testsuite():
    """creates a testsuite with out of all tests in this file"""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSaaletalblick))
    suite.addTest(unittest.makeSuite(TestUpdateDate))
    suite.addTest(unittest.makeSuite(TestGeocacheWaypoints))
    suite.addTest(unittest.makeSuite(TestMaerchenstuhl))
    suite.addTest(unittest.makeSuite(TestTesoroAmeghino))
    suite.addTest(unittest.makeSuite(TestMusikhochschule))
    suite.addTest(unittest.makeSuite(TestWuerzburgerWebcam))
    suite.addTest(unittest.makeSuite(TestMedrixErnos))
    suite.addTest(unittest.makeSuite(TestEntenteichGPXFromGeocachingCom))
    suite.addTest(unittest.makeSuite(TestInvalidInput))
    suite.addTest(unittest.makeSuite(TestWaypointInit))
    suite.addTest(unittest.makeSuite(TestWaypointFindShownNameAndDistance))
    suite.addTest(unittest.makeSuite(TestWaypointInfo))
    return suite


def main(v):
    """runs the testsuite"""
    return test_frame.run(v, create_testsuite, "geocache.py")


if __name__ == '__main__':
    if len(sys.argv) > 1:  # if script is run with argument
        verbosity = int(sys.argv[1])
    else:  # if no argument -> verbosity 1
        verbosity = 1
    main(verbosity)
