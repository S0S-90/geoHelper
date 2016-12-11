import unittest
import datetime
import sys
sys.path.append('../src/') # path to source file (ownfunctions.py)

import geocache 
    
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
        
    def test_size_anzeige(self):
        self.assertEqual(self.gc.size_anzeige, "micro")
        
    def test_type(self):
        self.assertEqual(self.gc.type, "Traditional Cache")
        
    def test_longtype(self):
        self.assertEqual(self.gc.longtype, "Traditional Cache")
        
    def test_beschreibung(self):
        self.assertEqual(self.gc.beschreibung, u"\n\nNach einem kleinen Spaziergang und dem Finden des Döschens werdet ihr mit einem tollen Blick ins Saaletal und auf die Saalewiesen belohnt! FTF: Jobi Voma STF: JoLoClMa TTF: Mone216\n\n\t\t\t")
    
    def test_hint(self):
        self.assertEqual(self.gc.hint, "Und ab durch die Hecke!")
        
    def test_owner(self):
        self.assertEqual(self.gc.owner, "bigkruemel")
        
    def test_url(self):
        self.assertEqual(self.gc.url, "https://www.geocaching.com/geocache/GC6K86W_saaletalblick")
        
    def test_koordinaten(self):
        self.assertEqual(self.gc.koordinaten, [50.318883,10.1936])
        
    def test_koordinatenanzeige(self):
        self.assertEqual(self.gc.koordinatenanzeige, u"N 50°19.133, E 010°11.616")
        
    def test_attribute(self):
        self.assertEqual(self.gc.attribute, ["no camping", "no parking available", "not wheelchair accessible", "kid friendly", "hike shorter than 1km", "stroller accessible"])
    
    def test_logs(self):
        expected_logs = [['2016-07-16', 'Found it', 'Ziaepf'], ['2016-07-10', "Didn't find it", 'NES-GN 310362'], ['2016-06-20', 'Found it', 'HerbieWo'], ['2016-06-15', 'Found it', "Fantastic'4"], ['2016-06-11', 'Found it', 'vicmouse'], ['2016-06-11', 'Found it', 'melimouse'], ['2016-06-10', 'Found it', 'Mone216'], ['2016-06-08', 'Found it', 'JoLoClMa'], ['2016-06-08', 'Found it', 'Jobi Voma'], ['2016-06-07', 'Publish Listing', 'Sabbelwasser']]
        self.assertEqual(self.gc.logs, expected_logs)
        
    def test_available(self):
        self.assertEqual(self.gc.available, True)
        
    def test_downloaddate(self):
        expected_date = datetime.date(2016,8,4)
        self.assertEqual(self.gc.downloaddate, expected_date)
        
    def test_downloaddate_anzeige(self):
        self.assertEqual(self.gc.downloaddate_anzeige, "04 Aug 2016")
        
    def test_kurzinfo(self):
        x = self.gc.kurzinfo()
        expected = u"GC6K86W | N 50°19.133, E 010°11.616 | Traditional Cache | D 2.0 | T 2.0 | micro   | True  | 04 Aug 2016 | Saaletalblick"
        self.assertEqual(x, expected)
        
    def test_langinfo(self):
        x = self.gc.langinfo()
        z1 = u"\nGC6K86W : Saaletalblick"
        z2 =  "\n------------------------"
        z3 = u"\nSchwierigkeit: 2.0, Gelaende: 2.0, Groesse: micro, Typ: Traditional Cache"
        z4 = u"\nKoordinaten: N 50°19.133, E 010°11.616"
        z5 = u"\nOwner: bigkruemel"
        z6 = u"\nAttribute: no camping, no parking available, not wheelchair accessible, kid friendly, hike shorter than 1km, stroller accessible"
        z7 = u"\nCache ist aktiv: True, Stand: 04 Aug 2016"
        z8 = u"\nLink: https://www.geocaching.com/geocache/GC6K86W_saaletalblick"
        z9 = u"\n\n\n\nNach einem kleinen Spaziergang und dem Finden des Döschens werdet ihr mit einem tollen Blick ins Saaletal und auf die Saalewiesen belohnt! FTF: Jobi Voma STF: JoLoClMa TTF: Mone216\n\n\t\t\t"
        z10 = u"\nHinweise: Und ab durch die Hecke!"
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
        expected = z1 + z2 + z3 + z4 + z5 + z6 + z7 + z8 + z9 + z10 + z11 + z12 + z13 + z14 + z15 + z16 + z17 + z18 + z19 + z20 + z21
        self.assertEqual(x, expected)
    
def create_testsuite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSaaletalblick))
    return suite

if __name__ == '__main__':
    testsuite = create_testsuite()
    unittest.TextTestRunner(verbosity=2).run(testsuite)   # set verbosity to 2 if you want to see the name and result of every test and to 1 if you don't
