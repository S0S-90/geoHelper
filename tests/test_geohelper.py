import unittest
import mock
import sys
import shutil
sys.path.append('../src/') # path to source file (geohelper.py)
from StringIO import StringIO

import ownfunctions
import geohelper

saved_stdout = sys.stdout # save standard output

class TestInitNoLogfile(unittest.TestCase):

    def setUp(self):
        self.x = geohelper.GPS_content(r"examples\no_logfile")

    def test_geocaches(self):
        number_of_geocaches = len(self.x.geocaches)
        self.assertEqual(number_of_geocaches,6)
        
    def test_attributes(self):
        expected_output = ['available 24-7', 'available in winter', 'bikes allowed', 'dangerous area', 'difficult climbing', 'dogs allowed', 'flashlight required', 'hike shorter than 1km', 'kid friendly', 'needs maintenance', 'no camping', 'no kids', 'no parking available', 'not stroller accessible', 'not wheelchair accessible', 'parking available', 'picnic tables available', 'public transit available', 'restrooms available', 'special tool required', 'stealth required', 'stroller accessible', 'takes less than 1 hour', 'teamwork required', 'thorns!', 'ticks!', 'tree climbing required', 'wheelchair accessible']
        self.assertEqual(self.x.existing_attributes, expected_output)
        
    def test_found_exists(self):
        self.assertEqual(self.x.found_exists, False)
        
    def test_warning(self):
        self.assertEqual(self.x.warning, False)
        
    def test_logged_and_found_caches_fails(self):
        self.assertRaises(IOError, self.x.get_logged_and_found_caches)
        
class TestInitOnlyFound(unittest.TestCase):
        
    def setUp(self):
        self.x = geohelper.GPS_content(r"examples\only_found")

    def test_geocaches(self):
        number_of_geocaches = len(self.x.geocaches)
        self.assertEqual(number_of_geocaches,7)
        
    def test_attributes(self):
        expected_output = ['available 24-7', 'available in winter', 'bikes allowed', 'dangerous area', 'difficult climbing', 'dogs allowed', 'flashlight required', 'hike shorter than 1km', 'kid friendly', 'needs maintenance', 'no camping', 'no kids', 'no parking available', 'not stroller accessible', 'not wheelchair accessible', 'parking available', 'picnic tables available', 'public transit available', 'restrooms available', 'special tool required', 'stealth required', 'stroller accessible', 'takes less than 1 hour', 'teamwork required', 'thorns!', 'ticks!', 'tree climbing required', 'wheelchair accessible']
        self.assertEqual(self.x.existing_attributes, expected_output)
        
    def test_found_exists(self):
        self.assertEqual(self.x.found_exists, True)
        
    def test_warning(self):
        self.assertEqual(self.x.warning, False)
        
class TestInitOnlyNotFound(unittest.TestCase):

    def setUp(self):
        self.x = geohelper.GPS_content(r"examples\only_notfound")

    def test_geocaches(self):
        number_of_geocaches = len(self.x.geocaches)
        self.assertEqual(number_of_geocaches,7)
        
    def test_attributes(self):
        expected_output = ['available 24-7', 'available in winter', 'bikes allowed', 'dangerous area', 'difficult climbing', 'dogs allowed', 'flashlight required', 'hike shorter than 1km', 'kid friendly', 'needs maintenance', 'no camping', 'no kids', 'no parking available', 'not stroller accessible', 'not wheelchair accessible', 'parking available', 'picnic tables available', 'public transit available', 'restrooms available', 'special tool required', 'stealth required', 'stroller accessible', 'takes less than 1 hour', 'teamwork required', 'thorns!', 'ticks!', 'tree climbing required', 'wheelchair accessible']
        self.assertEqual(self.x.existing_attributes, expected_output)
        
    def test_found_exists(self):
        self.assertEqual(self.x.found_exists, False)
        
    def test_warning(self):
        self.assertEqual(self.x.warning, True)
        
class TestInitNotOnlyFound(unittest.TestCase):

    def setUp(self):
        self.x = geohelper.GPS_content(r"examples\not_only_found")

    def test_geocaches(self):
        number_of_geocaches = len(self.x.geocaches)
        self.assertEqual(number_of_geocaches,7)
        
    def test_attributes(self):
        expected_output = ['available 24-7', 'available in winter', 'bikes allowed', 'dangerous area', 'difficult climbing', 'dogs allowed', 'flashlight required', 'hike shorter than 1km', 'kid friendly', 'needs maintenance', 'no camping', 'no kids', 'no parking available', 'not stroller accessible', 'not wheelchair accessible', 'parking available', 'picnic tables available', 'public transit available', 'restrooms available', 'special tool required', 'stealth required', 'stroller accessible', 'takes less than 1 hour', 'teamwork required', 'thorns!', 'ticks!', 'tree climbing required', 'wheelchair accessible']
        self.assertEqual(self.x.existing_attributes, expected_output)
        
    def test_found_exists(self):
        self.assertEqual(self.x.found_exists, True)
        
    def test_warning(self):
        self.assertEqual(self.x.warning, True)

class TestInitFoundNotOnGPS(unittest.TestCase):

    def setUp(self):
        self.x = geohelper.GPS_content(r"examples\found_not_on_gps")

    def test_geocaches(self):
        number_of_geocaches = len(self.x.geocaches)
        self.assertEqual(number_of_geocaches,6)
        
    def test_attributes(self):
        expected_output = ['available 24-7', 'available in winter', 'bikes allowed', 'difficult climbing', 'dogs allowed', 'flashlight required', 'hike shorter than 1km', 'kid friendly', 'no camping', 'no parking available', 'not wheelchair accessible', 'parking available', 'picnic tables available', 'public transit available', 'restrooms available', 'special tool required', 'stealth required', 'stroller accessible', 'takes less than 1 hour', 'teamwork required', 'thorns!', 'ticks!', 'tree climbing required', 'wheelchair accessible']
        self.assertEqual(self.x.existing_attributes, expected_output)
        
    def test_found_exists(self):
        self.assertEqual(self.x.found_exists, True)
        
    def test_warning(self):
        self.assertEqual(self.x.warning, False)

class TestInitNotFoundNotOnGPS(unittest.TestCase):

    def setUp(self):
        self.x = geohelper.GPS_content(r"examples\not_found_not_on_gps")

    def test_geocaches(self):
        number_of_geocaches = len(self.x.geocaches)
        self.assertEqual(number_of_geocaches,6)
        
    def test_attributes(self):
        expected_output = ['available 24-7', 'available in winter', 'bikes allowed', 'difficult climbing', 'dogs allowed', 'flashlight required', 'hike shorter than 1km', 'kid friendly', 'no camping', 'no parking available', 'not wheelchair accessible', 'parking available', 'picnic tables available', 'public transit available', 'restrooms available', 'special tool required', 'stealth required', 'stroller accessible', 'takes less than 1 hour', 'teamwork required', 'thorns!', 'ticks!', 'tree climbing required', 'wheelchair accessible']
        self.assertEqual(self.x.existing_attributes, expected_output)
        
    def test_found_exists(self):
        self.assertEqual(self.x.found_exists, True)
        
    def test_warning(self):
        self.assertEqual(self.x.warning, False)      

class TestInitErrorInGPX(unittest.TestCase):

    def setUp(self):
        self.x = geohelper.GPS_content(r"examples\error_in_gpx")

    def test_geocaches(self):
        number_of_geocaches = len(self.x.geocaches)
        self.assertEqual(number_of_geocaches,6)
        
    def test_attributes(self):
        expected_output = ['available 24-7', 'available in winter', 'bikes allowed', 'dangerous area', 'difficult climbing', 'dogs allowed', 'flashlight required', 'hike shorter than 1km', 'kid friendly', 'needs maintenance', 'no camping', 'no kids', 'no parking available', 'not stroller accessible', 'not wheelchair accessible', 'parking available', 'picnic tables available', 'public transit available', 'restrooms available', 'special tool required', 'stealth required', 'stroller accessible', 'takes less than 1 hour', 'teamwork required', 'thorns!', 'ticks!', 'tree climbing required', 'wheelchair accessible']
        self.assertEqual(self.x.existing_attributes, expected_output)
        
    def test_found_exists(self):
        self.assertEqual(self.x.found_exists, False)
        
    def test_warning(self):
        self.assertEqual(self.x.warning, False)        
        
class TestGetLoggedAndFoundCachesOnlyFound(unittest.TestCase):

    def setUp(self):
        self.x = geohelper.GPS_content(r"examples\only_found")
        
    def test_logged_caches(self):
        logged_caches = self.x.get_logged_and_found_caches()[0]
        expected = [["GC1XRPM","2016-09-03T09:40Z","Found it"], ["GC5G5F5","2016-09-03T09:40Z","Found it"]]
        self.assertEqual(logged_caches, expected)
        
    def test_found_caches(self):
        found_caches = self.x.get_logged_and_found_caches()[1]
        self.assertEqual(len(found_caches),2)
        self.assertEqual(found_caches[0].gccode, "GC1XRPM")
        self.assertEqual(found_caches[1].gccode, "GC5G5F5")
        
class TestGetLoggedAndFoundCachesNotOnlyFound(unittest.TestCase):

    def setUp(self):
        self.x = geohelper.GPS_content(r"examples\not_only_found")
        
    def test_logged_caches(self):
        logged_caches = self.x.get_logged_and_found_caches()[0]
        expected = [["GC1XRPM","2016-09-03T09:40Z","Found it"],["GC5G5F5","2016-09-03T09:40Z","unattempted"],["GC5N23T","2017-02-12T09:40Z","Found it"]]
        self.assertEqual(logged_caches, expected)
        
    def test_found_caches(self):
        found_caches = self.x.get_logged_and_found_caches()[1]
        self.assertEqual(len(found_caches),2)
        self.assertEqual(found_caches[0].gccode, "GC1XRPM")
        self.assertEqual(found_caches[1].gccode, "GC5N23T")
        
class TestGetLoggedAndFoundCachesOnlyNotFound(unittest.TestCase):

    def setUp(self):
        self.x = geohelper.GPS_content(r"examples\only_notfound")
        
    def test_logged_caches(self):
        logged_caches = self.x.get_logged_and_found_caches()[0]
        expected = [["GC1XRPM","2016-09-03T09:40Z","unattempted"],["GC5G5F5","2016-09-03T09:40Z","unattempted"]]
        self.assertEqual(logged_caches, expected)
        
    def test_found_caches(self):
        found_caches = self.x.get_logged_and_found_caches()[1]
        self.assertEqual(len(found_caches),0)
        
class TestGetLoggedAndFoundCachesFoundNotOnGPS(unittest.TestCase):

    def setUp(self):
        self.x = geohelper.GPS_content(r"examples\found_not_on_gps")
        
    def test_logged_caches(self):
        logged_caches = self.x.get_logged_and_found_caches()[0]
        expected = [["GC5G5F5","2016-09-03T09:40Z","Found it"]]
        
    def test_found_caches(self):
        found_caches = self.x.get_logged_and_found_caches()[1]
        self.assertEqual(len(found_caches),1)
        self.assertEqual(found_caches[0].gccode, "GC5G5F5")
        
class TestGetLoggedAndFoundCachesNotFoundNotOnGPS(unittest.TestCase):

    def setUp(self):
        self.x = geohelper.GPS_content(r"examples\not_found_not_on_gps")
        
    def test_logged_caches(self):
        logged_caches = self.x.get_logged_and_found_caches()[0]
        expected = [["GC5G5F5","2016-09-03T09:40Z","unattempted"]]
        
    def test_found_caches(self):
        found_caches = self.x.get_logged_and_found_caches()[1]
        self.assertEqual(len(found_caches),1)
        self.assertEqual(found_caches[0].gccode, "GC5G5F5")
        
class TestSortierenUndAnzeigen(unittest.TestCase):

    def setUp(self):
        self.x = geohelper.GPS_content(r"examples\no_logfile")
        
    def test_gccode_up(self):
        with mock.patch('__builtin__.raw_input', side_effect=['1', '1']):
            expected = ["GC1XRPM","GC33QGC","GC5N23T","GC6K86W","GC6RNTX","GCJJ20"]
            self.x.sortieren_und_anzeigen()
            sorted = []
            for g in self.x.geocaches:
                sorted.append(g.gccode)
            self.assertEqual(sorted, expected)
            
    def test_gccode_down(self):
        with mock.patch('__builtin__.raw_input', side_effect=['1', '2']):
            expected = ["GCJJ20","GC6RNTX","GC6K86W","GC5N23T","GC33QGC","GC1XRPM"]
            self.x.sortieren_und_anzeigen()
            sorted = []
            for g in self.x.geocaches:
                sorted.append(g.gccode)
            self.assertEqual(sorted, expected)
            
    def test_name_up(self):
        with mock.patch('__builtin__.raw_input', side_effect=['2', '1']):
            expected = ["GC5N23T","GC6RNTX","GC1XRPM","GC6K86W","GC33QGC","GCJJ20"]
            self.x.sortieren_und_anzeigen()
            sorted = []
            for g in self.x.geocaches:
                sorted.append(g.gccode)
            self.assertEqual(sorted, expected)
            
    def test_name_down(self):
        with mock.patch('__builtin__.raw_input', side_effect=['2', '2']):
            expected = ["GCJJ20","GC33QGC","GC6K86W","GC1XRPM","GC6RNTX","GC5N23T"]
            self.x.sortieren_und_anzeigen()
            sorted = []
            for g in self.x.geocaches:
                sorted.append(g.gccode)
            self.assertEqual(sorted, expected)
            
    def test_typ_up(self):
        with mock.patch('__builtin__.raw_input', side_effect=['3', '1']):
            expected = ["GC1XRPM","GC5N23T","GC6RNTX","GC33QGC","GC6K86W","GCJJ20"]
            self.x.sortieren_und_anzeigen()
            sorted = []
            for g in self.x.geocaches:
                sorted.append(g.gccode)
            self.assertEqual(sorted, expected)
            
    def test_typ_down(self):
        with mock.patch('__builtin__.raw_input', side_effect=['3', '2']):
            expected = ["GCJJ20","GC33QGC","GC6K86W","GC5N23T","GC6RNTX","GC1XRPM"]
            self.x.sortieren_und_anzeigen()
            sorted = []
            for g in self.x.geocaches:
                sorted.append(g.gccode)
            self.assertEqual(sorted, expected)
            
    def test_difficulty_up(self):
        with mock.patch('__builtin__.raw_input', side_effect=['4', '1']):
            expected = ["GCJJ20","GC33QGC","GC6K86W","GC6RNTX","GC1XRPM","GC5N23T"]
            self.x.sortieren_und_anzeigen()
            sorted = []
            for g in self.x.geocaches:
                sorted.append(g.gccode)
            self.assertEqual(sorted, expected)  

    def test_difficulty_down(self):
        with mock.patch('__builtin__.raw_input', side_effect=['4', '2']):
            expected = ["GC5N23T","GC1XRPM","GC33QGC","GC6K86W","GC6RNTX","GCJJ20"]
            self.x.sortieren_und_anzeigen()
            sorted = []
            for g in self.x.geocaches:
                sorted.append(g.gccode)
            self.assertEqual(sorted, expected)  

    def test_terrain_up(self):
        with mock.patch('__builtin__.raw_input', side_effect=['5', '1']):
            expected = ["GCJJ20","GC6RNTX","GC6K86W","GC33QGC","GC1XRPM","GC5N23T"]
            self.x.sortieren_und_anzeigen()
            sorted = []
            for g in self.x.geocaches:
                sorted.append(g.gccode)
            self.assertEqual(sorted, expected) 

    def test_terrain_down(self):
        with mock.patch('__builtin__.raw_input', side_effect=['5', '2']):
            expected = ["GC5N23T","GC1XRPM","GC33QGC","GC6K86W","GC6RNTX","GCJJ20"]
            self.x.sortieren_und_anzeigen()
            sorted = []
            for g in self.x.geocaches:
                sorted.append(g.gccode)
            self.assertEqual(sorted, expected) 

    def test_size_up(self):
        with mock.patch('__builtin__.raw_input', side_effect=['6', '1']):
            expected = ["GCJJ20","GC1XRPM","GC5N23T","GC6K86W","GC6RNTX","GC33QGC"]
            self.x.sortieren_und_anzeigen()
            sorted = []
            for g in self.x.geocaches:
                sorted.append(g.gccode)
            self.assertEqual(sorted, expected) 

    def test_size_down(self):
        with mock.patch('__builtin__.raw_input', side_effect=['6', '2']):
            expected = ["GC33QGC","GC1XRPM","GC5N23T","GC6K86W","GC6RNTX","GCJJ20"]
            self.x.sortieren_und_anzeigen()
            sorted = []
            for g in self.x.geocaches:
                sorted.append(g.gccode)
            self.assertEqual(sorted, expected) 

    def test_downloaddate_up(self):
        with mock.patch('__builtin__.raw_input', side_effect=['7', '1']):
            expected = ["GC6K86W","GC1XRPM","GC33QGC","GC6RNTX","GCJJ20","GC5N23T"]
            self.x.sortieren_und_anzeigen()
            sorted = []
            for g in self.x.geocaches:
                sorted.append(g.gccode)
            self.assertEqual(sorted, expected) 

    def test_downloaddate_down(self):
        with mock.patch('__builtin__.raw_input', side_effect=['7', '2']):
            expected = ["GC5N23T","GCJJ20","GC6RNTX","GC33QGC","GC1XRPM","GC6K86W"]
            self.x.sortieren_und_anzeigen()
            sorted = []
            for g in self.x.geocaches:
                sorted.append(g.gccode)
            self.assertEqual(sorted, expected) 

    def test_available_up(self):
        with mock.patch('__builtin__.raw_input', side_effect=['8', '1']):
            expected = ["GC5N23T","GC1XRPM","GC33QGC","GC6K86W","GC6RNTX","GCJJ20"]
            self.x.sortieren_und_anzeigen()
            sorted = []
            for g in self.x.geocaches:
                sorted.append(g.gccode)
            self.assertEqual(sorted, expected) 

    def test_available_down(self):
        with mock.patch('__builtin__.raw_input', side_effect=['8', '2']):
            expected = ["GC1XRPM","GC33QGC","GC6K86W","GC6RNTX","GCJJ20","GC5N23T"]
            self.x.sortieren_und_anzeigen()
            sorted = []
            for g in self.x.geocaches:
                sorted.append(g.gccode)
            self.assertEqual(sorted, expected) 

    def test_distance_up(self):
        with mock.patch('__builtin__.raw_input', side_effect=['9', '1', 'https://www.google.de/maps/place/97209+Veitsh%C3%B6chheim/@49.8414697,9.8579699,13z/data=!3m1!4b1!4m5!3m4!1s0x47a2915cbab1bfe3:0xdbe76ec582bb3aa5!8m2!3d49.8312701!4d9.8803666']):
            expected = ["GC5N23T","GC1XRPM","GCJJ20","GC6RNTX","GC6K86W","GC33QGC"]
            self.x.sortieren_und_anzeigen()
            sorted = []
            for g in self.x.geocaches:
                sorted.append(g.gccode)
            self.assertEqual(sorted, expected)   

    def test_distance_down(self):
        with mock.patch('__builtin__.raw_input', side_effect=['9', '2', 'https://www.google.de/maps/place/97209+Veitsh%C3%B6chheim/@49.8414697,9.8579699,13z/data=!3m1!4b1!4m5!3m4!1s0x47a2915cbab1bfe3:0xdbe76ec582bb3aa5!8m2!3d49.8312701!4d9.8803666']):
            expected = ["GC33QGC","GC6K86W","GC6RNTX","GCJJ20","GC1XRPM","GC5N23T"]
            self.x.sortieren_und_anzeigen()
            sorted = []
            for g in self.x.geocaches:
                sorted.append(g.gccode)
            self.assertEqual(sorted, expected)            
            
class TestAlleAnzeigen(unittest.TestCase):

    def test_nix_anzeigen(self):
        x = geohelper.GPS_content(r"examples\empty")
        self.assertEqual(x.alle_anzeigen(), "Keine Caches auf dem Geraet.") 

    def test_anzeigen(self):
        x = geohelper.GPS_content(r"examples\no_logfile")
        expected = u"GC1XRPM | N 49°48.559, E 009°56.019 | Multi-cache       | D 2.5 | T 3.5 | micro   | True  | 06 Sep 2016 | Im Auftrag ihrer Majestät – Der Märchenstuhl\n"
        expected = expected + u"GC33QGC | S 43°41.726, W 066°27.090 | Traditional Cache | D 2.0 | T 3.0 | small   | True  | 11 Sep 2016 | Tesoro Ameghino\n"
        expected = expected + u"GC5N23T | N 49°48.457, E 009°54.727 | Mystery Cache     | D 3.0 | T 4.0 | micro   | False | 05 Mar 2017 | 67 - MedTrix - {}\n".format(u"\u001a"+u"\u001a"+u"\u001a"+u"\u001a"+u"\u001a")
        expected = expected + u"GC6K86W | N 50°19.133, E 010°11.616 | Traditional Cache | D 2.0 | T 2.0 | micro   | True  | 04 Aug 2016 | Saaletalblick\n"
        expected = expected + u"GC6RNTX | N 49°47.670, E 009°56.456 | Mystery Cache     | D 2.0 | T 1.5 | micro   | True  | 08 Oct 2016 | Hochschule für Musik 1\n"
        expected = expected + u"GCJJ20  | N 49°47.688, E 009°55.816 | Unknown Type      | D 1.0 | T 1.0 | other   | True  | 29 Oct 2016 | Wuerzburger webcam\n"
        self.assertEqual(x.alle_anzeigen(), expected)    

class TestAlleAnzeigenDist(unittest.TestCase): 

    def test_nix_anzeigen(self):
        x = geohelper.GPS_content(r"examples\empty")
        self.assertEqual(x.alle_anzeigen(), "Keine Caches auf dem Geraet.") 

    def test_anzeigen(self):
        x = geohelper.GPS_content(r"examples\no_logfile")
        for gc in x.geocaches:
            gc.distance = ownfunctions.calculate_distance(gc.koordinaten, [49.8414697,9.8579699])
        expected = u"    6.5km | GC1XRPM | N 49°48.559, E 009°56.019 | Multi-cache       | D 2.5 | T 3.5 | micro   | True  | 06 Sep 2016 | Im Auftrag ihrer Majestät – Der Märchenstuhl\n"
        expected = expected + u"12746.3km | GC33QGC | S 43°41.726, W 066°27.090 | Traditional Cache | D 2.0 | T 3.0 | small   | True  | 11 Sep 2016 | Tesoro Ameghino\n"
        expected = expected + u"    5.4km | GC5N23T | N 49°48.457, E 009°54.727 | Mystery Cache     | D 3.0 | T 4.0 | micro   | False | 05 Mar 2017 | 67 - MedTrix - {}\n".format(u"\u001a"+u"\u001a"+u"\u001a"+u"\u001a"+u"\u001a")
        expected = expected + u"   58.2km | GC6K86W | N 50°19.133, E 010°11.616 | Traditional Cache | D 2.0 | T 2.0 | micro   | True  | 04 Aug 2016 | Saaletalblick\n"
        expected = expected + u"    7.9km | GC6RNTX | N 49°47.670, E 009°56.456 | Mystery Cache     | D 2.0 | T 1.5 | micro   | True  | 08 Oct 2016 | Hochschule für Musik 1\n"
        expected = expected + u"    7.3km | GCJJ20  | N 49°47.688, E 009°55.816 | Unknown Type      | D 1.0 | T 1.0 | other   | True  | 29 Oct 2016 | Wuerzburger webcam\n"
        self.assertEqual(x.alle_anzeigen_dist(), expected)        
        
class TestEinenAnzeigen(unittest.TestCase): 

    def setUp(self):
        self.x = geohelper.GPS_content(r"examples\no_logfile")

    def test_not_existing_cache(self):
        with mock.patch('__builtin__.raw_input', return_value= "GC12345"):
            out = StringIO()
            sys.stdout = out
            self.x.einen_anzeigen()
            output = out.getvalue().strip()
            self.assertEqual(output, "Dieser GC-Code existiert nicht.")
            
    def test_loeschen(self):
        shutil.copy2(r"examples\no_logfile\GPX\GC1XRPM.gpx", r"examples\no_logfile\GC1XRPM.gpx")  # copy file that is to be removed
        with mock.patch('__builtin__.raw_input', side_effect=["GC1XRPM","1","y"]):
            self.x.einen_anzeigen()
            self.assertEqual(len(self.x.geocaches), 5)
            shutil.move(r"examples\no_logfile\GC1XRPM.gpx", r"examples\no_logfile\GPX\GC1XRPM.gpx") # move deleted file back to GPX folder
            
    def test_nicht_loeschen(self):
        with mock.patch('__builtin__.raw_input', side_effect=["GC1XRPM","1","n"]):
            self.x.einen_anzeigen()
            self.assertEqual(len(self.x.geocaches), 6)
            
class TestGCAuswahlAnzeigen(unittest.TestCase):

    def setUp(self):
        self.x = geohelper.GPS_content(r"examples\no_logfile")
        
    def test_nix_anzeigen(self):
        self.assertEqual(self.x.gc_auswahl_anzeigen([]), "")
        
    def test_auswahl_anzeigen(self):
        selection = self.x.geocaches[3:5]
        expected = u"GC6K86W | N 50°19.133, E 010°11.616 | Traditional Cache | D 2.0 | T 2.0 | micro   | True  | 04 Aug 2016 | Saaletalblick\n"
        expected = expected + u"GC6RNTX | N 49°47.670, E 009°56.456 | Mystery Cache     | D 2.0 | T 1.5 | micro   | True  | 08 Oct 2016 | Hochschule für Musik 1\n"
        self.assertEqual(self.x.gc_auswahl_anzeigen(selection), expected)
        
    def test_bullshitlist(self):
        selection = ["13",6]
        self.assertRaises(TypeError, self.x.gc_auswahl_anzeigen, selection)
        
# weiter mit gc_auswahl_anzeigen_dist
        
def create_testsuite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestInitNoLogfile))
    suite.addTest(unittest.makeSuite(TestInitOnlyFound))
    suite.addTest(unittest.makeSuite(TestInitOnlyNotFound))
    suite.addTest(unittest.makeSuite(TestInitNotOnlyFound))
    suite.addTest(unittest.makeSuite(TestInitFoundNotOnGPS))
    suite.addTest(unittest.makeSuite(TestInitNotFoundNotOnGPS))
    suite.addTest(unittest.makeSuite(TestInitErrorInGPX))
    suite.addTest(unittest.makeSuite(TestGetLoggedAndFoundCachesOnlyFound))
    suite.addTest(unittest.makeSuite(TestGetLoggedAndFoundCachesNotOnlyFound))
    suite.addTest(unittest.makeSuite(TestGetLoggedAndFoundCachesOnlyNotFound))
    suite.addTest(unittest.makeSuite(TestGetLoggedAndFoundCachesFoundNotOnGPS))
    suite.addTest(unittest.makeSuite(TestGetLoggedAndFoundCachesNotFoundNotOnGPS))
    suite.addTest(unittest.makeSuite(TestSortierenUndAnzeigen))
    suite.addTest(unittest.makeSuite(TestAlleAnzeigen))
    suite.addTest(unittest.makeSuite(TestAlleAnzeigenDist))
    suite.addTest(unittest.makeSuite(TestEinenAnzeigen))
    suite.addTest(unittest.makeSuite(TestGCAuswahlAnzeigen))
    return suite

def main(v):
    sys.stdout = saved_stdout  # print output to display
    print "\nTesting geohelper.py"
    out = StringIO()
    sys.stdout = out   # don't print output
    testsuite = create_testsuite()
    x = unittest.TextTestRunner(verbosity=v).run(testsuite) 
    sys.stdout = saved_stdout  # print output to display
    return x.testsRun, len(x.failures) 

if __name__ == '__main__':
    main(2)
