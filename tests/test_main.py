import unittest
import mock
import sys
import shutil
import os
sys.path.append('../src/') # path to source file (geotooly.py)
from StringIO import StringIO

import ownfunctions
import geocache
import main as geotooly

saved_stdout = sys.stdout # save standard output

class TestInitNoLogfile(unittest.TestCase):

    def setUp(self):
        self.x = geotooly.GPS_content(r"examples\no_logfile")

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
        self.x = geotooly.GPS_content(r"examples\only_found")

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
        self.x = geotooly.GPS_content(r"examples\only_notfound")

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
        self.x = geotooly.GPS_content(r"examples\not_only_found")

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
        self.x = geotooly.GPS_content(r"examples\found_not_on_gps")

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
        self.x = geotooly.GPS_content(r"examples\not_found_not_on_gps")

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
        self.x = geotooly.GPS_content(r"examples\error_in_gpx")

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
        self.x = geotooly.GPS_content(r"examples\only_found")
        
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
        self.x = geotooly.GPS_content(r"examples\not_only_found")
        
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
        self.x = geotooly.GPS_content(r"examples\only_notfound")
        
    def test_logged_caches(self):
        logged_caches = self.x.get_logged_and_found_caches()[0]
        expected = [["GC1XRPM","2016-09-03T09:40Z","unattempted"],["GC5G5F5","2016-09-03T09:40Z","unattempted"]]
        self.assertEqual(logged_caches, expected)
        
    def test_found_caches(self):
        found_caches = self.x.get_logged_and_found_caches()[1]
        self.assertEqual(len(found_caches),0)
        
class TestGetLoggedAndFoundCachesFoundNotOnGPS(unittest.TestCase):

    def setUp(self):
        self.x = geotooly.GPS_content(r"examples\found_not_on_gps")
        
    def test_logged_caches(self):
        logged_caches = self.x.get_logged_and_found_caches()[0]
        expected = [["GC5G5F5","2016-09-03T09:40Z","Found it"]]
        
    def test_found_caches(self):
        found_caches = self.x.get_logged_and_found_caches()[1]
        self.assertEqual(len(found_caches),1)
        self.assertEqual(found_caches[0].gccode, "GC5G5F5")
        
class TestGetLoggedAndFoundCachesNotFoundNotOnGPS(unittest.TestCase):

    def setUp(self):
        self.x = geotooly.GPS_content(r"examples\not_found_not_on_gps")
        
    def test_logged_caches(self):
        logged_caches = self.x.get_logged_and_found_caches()[0]
        expected = [["GC5G5F5","2016-09-03T09:40Z","unattempted"]]
        
    def test_found_caches(self):
        found_caches = self.x.get_logged_and_found_caches()[1]
        self.assertEqual(len(found_caches),1)
        self.assertEqual(found_caches[0].gccode, "GC5G5F5")
        
class TestSortierenUndAnzeigen(unittest.TestCase):

    def setUp(self):
        self.x = geotooly.GPS_content(r"examples\no_logfile")
        
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
        x = geotooly.GPS_content(r"examples\empty")
        self.assertEqual(x.alle_anzeigen(), "Keine Caches auf dem Geraet.") 

    def test_anzeigen(self):
        x = geotooly.GPS_content(r"examples\no_logfile")
        expected = u"GC1XRPM | N 49°48.559, E 009°56.019 | Multi-cache       | D 2.5 | T 3.5 | micro   | True  | 06 Sep 2016 | Im Auftrag ihrer Majestät – Der Märchenstuhl\n"
        expected = expected + u"GC33QGC | S 43°41.726, W 066°27.090 | Traditional Cache | D 2.0 | T 3.0 | small   | True  | 11 Sep 2016 | Tesoro Ameghino\n"
        expected = expected + u"GC5N23T | N 49°48.457, E 009°54.727 | Mystery Cache     | D 3.0 | T 4.0 | micro   | False | 05 Mar 2017 | 67 - MedTrix - {}\n".format(u"\u001a"+u"\u001a"+u"\u001a"+u"\u001a"+u"\u001a")
        expected = expected + u"GC6K86W | N 50°19.133, E 010°11.616 | Traditional Cache | D 2.0 | T 2.0 | micro   | True  | 04 Aug 2016 | Saaletalblick\n"
        expected = expected + u"GC6RNTX | N 49°47.670, E 009°56.456 | Mystery Cache     | D 2.0 | T 1.5 | micro   | True  | 08 Oct 2016 | Hochschule für Musik 1\n"
        expected = expected + u"GCJJ20  | N 49°47.688, E 009°55.816 | Unknown Type      | D 1.0 | T 1.0 | other   | True  | 29 Oct 2016 | Wuerzburger webcam\n"
        self.assertEqual(x.alle_anzeigen(), expected)    

class TestAlleAnzeigenDist(unittest.TestCase): 

    def test_nix_anzeigen(self):
        x = geotooly.GPS_content(r"examples\empty")
        self.assertEqual(x.alle_anzeigen(), "Keine Caches auf dem Geraet.") 

    def test_anzeigen(self):
        x = geotooly.GPS_content(r"examples\no_logfile")
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
        self.x = geotooly.GPS_content(r"examples\no_logfile")

    def test_not_existing_cache(self):
        with mock.patch('__builtin__.raw_input', return_value= "GC12345"):
            out = StringIO()
            sys.stdout = out
            self.x.einen_anzeigen()
            output = out.getvalue().strip()
            self.assertEqual(output, "Dieser GC-Code existiert nicht.")
            
    def test_loeschen(self):
        shutil.copy2(r"examples\no_logfile\GPX\GC1XRPM.gpx", r"examples\temp\GC1XRPM.gpx")  # copy file that is to be removed
        with mock.patch('__builtin__.raw_input', side_effect=["GC1XRPM","1","y"]):
            self.x.einen_anzeigen()
            self.assertEqual(len(self.x.geocaches), 5)
        shutil.move(r"examples\temp\GC1XRPM.gpx", r"examples\no_logfile\GPX\GC1XRPM.gpx") # move deleted file back to GPX folder
            
    def test_nicht_loeschen(self):
        with mock.patch('__builtin__.raw_input', side_effect=["GC1XRPM","1","n"]):
            self.x.einen_anzeigen()
            self.assertEqual(len(self.x.geocaches), 6)
            
class TestGCAuswahlAnzeigen(unittest.TestCase):

    def setUp(self):
        self.x = geotooly.GPS_content(r"examples\no_logfile")
        
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
        
class TestGCAuswahlAnzeigenDist(unittest.TestCase):

    def setUp(self):
        self.x = geotooly.GPS_content(r"examples\no_logfile")
        for gc in self.x.geocaches:
            gc.distance = ownfunctions.calculate_distance(gc.koordinaten, [49.8414697,9.8579699])
        
    def test_nix_anzeigen(self):
        self.assertEqual(self.x.gc_auswahl_anzeigen_dist([]), "")
        
    def test_auswahl_anzeigen(self):
        selection = self.x.geocaches[3:5]
        expected = u"   58.2km | GC6K86W | N 50°19.133, E 010°11.616 | Traditional Cache | D 2.0 | T 2.0 | micro   | True  | 04 Aug 2016 | Saaletalblick\n"
        expected = expected + u"    7.9km | GC6RNTX | N 49°47.670, E 009°56.456 | Mystery Cache     | D 2.0 | T 1.5 | micro   | True  | 08 Oct 2016 | Hochschule für Musik 1\n"
        self.assertEqual(self.x.gc_auswahl_anzeigen_dist(selection), expected)
        
    def test_bullshitlist(self):
        selection = ["13",6]
        self.assertRaises(TypeError, self.x.gc_auswahl_anzeigen_dist, selection)
        
class TestSuchen(unittest.TestCase):

    def setUp(self):
        self.x = geotooly.GPS_content(r"examples\no_logfile")

    def test_name(self):
        with mock.patch('__builtin__.raw_input', side_effect = ["1","A"]): 
            expected = [self.x.geocaches[0], self.x.geocaches[1]]
            self.assertEqual(self.x.suchen(), expected) 

    def test_beschreibung(self):
        with mock.patch('__builtin__.raw_input', side_effect = ["2","ist"]): 
            expected = [self.x.geocaches[0], self.x.geocaches[1], self.x.geocaches[2], self.x.geocaches[5]]
            self.assertEqual(self.x.suchen(), expected)     

    def test_cachetyp(self):   
        with mock.patch('__builtin__.raw_input', side_effect = ["3","Mystery Cache"]): 
            expected = [self.x.geocaches[2], self.x.geocaches[4]]
            self.assertEqual(self.x.suchen(), expected)

    def test_cachetyp_invalid(self):   
        with mock.patch('__builtin__.raw_input', side_effect = ["3","Mystery"]): 
            self.assertEqual(self.x.suchen(), [])  

    def test_difficulty(self):   
        with mock.patch('__builtin__.raw_input', side_effect = ["4","2, 2.5"]): 
            expected = [self.x.geocaches[0], self.x.geocaches[1], self.x.geocaches[3], self.x.geocaches[4]]
            self.assertEqual(self.x.suchen(), expected) 

    def test_difficulty_without_space(self):   
        with mock.patch('__builtin__.raw_input', side_effect = ["4","2,2.5"]): 
            expected = [self.x.geocaches[0], self.x.geocaches[1], self.x.geocaches[3], self.x.geocaches[4]]
            self.assertEqual(self.x.suchen(), expected)     

    def test_difficulty_error(self):   
        with mock.patch('__builtin__.raw_input', side_effect = ["4","2.5,2"]): 
            self.assertEqual(self.x.suchen(), []) 

    def test_difficulty_error2(self):   
        with mock.patch('__builtin__.raw_input', side_effect = ["4","2.5,7"]): 
            self.assertEqual(self.x.suchen(), [])  

    def test_terrain(self):   
        with mock.patch('__builtin__.raw_input', side_effect = ["5","1.5, 2"]): 
            expected = [self.x.geocaches[3], self.x.geocaches[4]]
            self.assertEqual(self.x.suchen(), expected)   

    def test_size(self):   
        with mock.patch('__builtin__.raw_input', side_effect = ["6","micro, small"]): 
            expected = [self.x.geocaches[0], self.x.geocaches[1], self.x.geocaches[2], self.x.geocaches[3], self.x.geocaches[4]]
            self.assertEqual(self.x.suchen(), expected)     

    def test_size_without_space(self):   
        with mock.patch('__builtin__.raw_input', side_effect = ["6","micro,small"]): 
            expected = [self.x.geocaches[0], self.x.geocaches[1], self.x.geocaches[2], self.x.geocaches[3], self.x.geocaches[4]]
            self.assertEqual(self.x.suchen(), expected) 

    def test_size_error(self):   
        with mock.patch('__builtin__.raw_input', side_effect = ["6","small, micro"]): 
            self.assertEqual(self.x.suchen(), [])  

    def test_downloaddate(self):   
        with mock.patch('__builtin__.raw_input', side_effect = ["7","01.10.2016, 31.10.2016"]): 
            expected = [self.x.geocaches[4], self.x.geocaches[5]]
            self.assertEqual(self.x.suchen(), expected)  

    def test_downloaddate_without_space(self):   
        with mock.patch('__builtin__.raw_input', side_effect = ["7","01.10.2016,31.10.2016"]): 
            expected = [self.x.geocaches[4], self.x.geocaches[5]]
            self.assertEqual(self.x.suchen(), expected)  

    def test_downloaddate_error(self):   
        with mock.patch('__builtin__.raw_input', side_effect = ["7","1.10.2016, 31.10.2016"]): 
            self.assertEqual(self.x.suchen(), [])   

    def test_downloaddate_error2(self):   
        with mock.patch('__builtin__.raw_input', side_effect = ["7","31.10.2016, 01.10.2016"]): 
            self.assertEqual(self.x.suchen(), [])  

    def test_not_available(self):   
        with mock.patch('__builtin__.raw_input', side_effect = ["8","n"]): 
            expected = [self.x.geocaches[2]]
            self.assertEqual(self.x.suchen(), expected) 

    def test_available(self):   
        with mock.patch('__builtin__.raw_input', side_effect = ["8","y"]): 
            expected = [self.x.geocaches[0], self.x.geocaches[1], self.x.geocaches[3], self.x.geocaches[4], self.x.geocaches[5]]
            self.assertEqual(self.x.suchen(), expected)  

    def test_available_by_bullshit(self):   
        with mock.patch('__builtin__.raw_input', side_effect = ["8","dfghj"]): 
            expected = [self.x.geocaches[0], self.x.geocaches[1], self.x.geocaches[3], self.x.geocaches[4], self.x.geocaches[5]]
            self.assertEqual(self.x.suchen(), expected)    

    def test_attributes(self):   
        with mock.patch('__builtin__.raw_input', side_effect = ["9","available 24-7"]): 
            expected = [self.x.geocaches[2], self.x.geocaches[4], self.x.geocaches[5]]
            self.assertEqual(self.x.suchen(), expected)  

    def test_attribute_that_doesnt_exist(self):   
        with mock.patch('__builtin__.raw_input', side_effect = ["9","No attributes specified by the author"]): 
            self.assertEqual(self.x.suchen(), [])  

    def test_distance(self):   
        with mock.patch('__builtin__.raw_input', side_effect = ["10","https://www.google.de/maps/place/97209+Veitsh%C3%B6chheim/@49.8414697,9.8579699,13z/data=!3m1!4b1!4m5!3m4!1s0x47a2915cbab1bfe3:0xdbe76ec582bb3aa5!8m2!3d49.8312701!4d9.8803666", "6.4, 7.4"]): 
            expected = [self.x.geocaches[0], self.x.geocaches[5]]
            self.assertEqual(self.x.suchen(), expected) 

    def test_distance_without_space(self):   
        with mock.patch('__builtin__.raw_input', side_effect = ["10","https://www.google.de/maps/place/97209+Veitsh%C3%B6chheim/@49.8414697,9.8579699,13z/data=!3m1!4b1!4m5!3m4!1s0x47a2915cbab1bfe3:0xdbe76ec582bb3aa5!8m2!3d49.8312701!4d9.8803666", "6.4,7.4"]): 
            expected = [self.x.geocaches[0], self.x.geocaches[5]]
            self.assertEqual(self.x.suchen(), expected)  

    def test_distance_error(self):   
        with mock.patch('__builtin__.raw_input', side_effect = ["10","https://www.gooe/maps/place/97209+Veitsh%C3%B6chheim/@49.8414697,9.8579699,13z/data=!3m1!4b1!4m5!3m4!1s0x47a2915cbab1bfe3:0xdbe76ec582bb3aa5!8m2!3d49.8312701!4d9.8803666", "6.4,7.4"]): 
            self.assertEqual(self.x.suchen(), [])    

    def test_distance_error2(self):   
        with mock.patch('__builtin__.raw_input', side_effect = ["10","https://www.google.de/maps/place/97209+Veitsh%C3%B6chheim/@49.8414697,9.8579699,13z/data=!3m1!4b1!4m5!3m4!1s0x47a2915cbab1bfe3:0xdbe76ec582bb3aa5!8m2!3d49.8312701!4d9.8803666", "hh, 7.4"]): 
            self.assertEqual(self.x.suchen(), [])  

    def test_distance_error3(self):   
        with mock.patch('__builtin__.raw_input', side_effect = ["10","https://www.google.de/maps/place/97209+Veitsh%C3%B6chheim/@49.8414697,9.8579699,13z/data=!3m1!4b1!4m5!3m4!1s0x47a2915cbab1bfe3:0xdbe76ec582bb3aa5!8m2!3d49.8312701!4d9.8803666", "10.3, 7.4"]): 
            self.assertEqual(self.x.suchen(), [])   

class TestGefundeneAnzeigenNoFoundCaches(unittest.TestCase):  

    def setUp(self):
        self.x = geotooly.GPS_content(r"examples\no_logfile")  
        
    def test_gives_error(self):
        self.assertRaises(ValueError, self.x.gefundene_anzeigen)
        
class TestGefundeneAnzeigenOnlyFound(unittest.TestCase):  

    def setUp(self):
        self.x = geotooly.GPS_content(r"examples\only_found")  
        
    def test_anzeigen(self):
        with mock.patch('__builtin__.raw_input', return_value = ["anything_except_for_1"]):
            out = StringIO()
            sys.stdout = out                                                    
            self.x.gefundene_anzeigen() 
            output = out.getvalue().strip()  
            expected = u"GC1XRPM | N 49°48.559, E 009°56.019 | Multi-cache       | D 2.5 | T 3.5 | micro   | True  | 06 Sep 2016 | Im Auftrag ihrer Majestät – Der Märchenstuhl\n"
            expected = expected + u"GC5G5F5 | N 49°47.955, E 009°58.566 | Traditional Cache | D 1.5 | T 4.0 | small   | True  | 08 Oct 2016 | Urban Buildering\n\n" 
            expected = expected +  "\nWas moechtest du als naechstes tun?\n"
            expected = expected + "1: Alle gefundenen Caches loeschen (vorher Loggen auf geocaching.com moeglich)\n"
            expected = expected + "2: zurueck"            
            self.assertEqual(output, expected)
            
    def test_loeschen(self):
        shutil.copy2(r"examples\only_found\GPX\GC1XRPM.gpx", r"examples\temp\GC1XRPM.gpx")              # copy files that are to be removed
        shutil.copy2(r"examples\only_found\GPX\GC5G5F5.gpx", r"examples\temp\GC5G5F5.gpx")
        shutil.copy2(r"examples\only_found\geocache_visits.txt", r"examples\temp\geocache_visits.txt")
        shutil.copy2(r"examples\only_found\geocache_logs.xml", r"examples\temp\geocache_logs.xml")
        
        with mock.patch('__builtin__.raw_input', side_effect = ["1","n","y"]):
            self.x.gefundene_anzeigen()
            self.assertEqual(len(self.x.geocaches), 5)   # less geocaches
            self.assertFalse(os.path.isfile(r"examples\only_found\geocache_visits.txt"))  # logfiles deleted
            self.assertFalse(os.path.isfile(r"examples\only_found\geocache_logs.xml"))
        
        shutil.move(r"examples\temp\GC1XRPM.gpx", r"examples\only_found\GPX\GC1XRPM.gpx") # move deleted files back
        shutil.move(r"examples\temp\GC5G5F5.gpx", r"examples\only_found\GPX\GC5G5F5.gpx")
        shutil.move(r"examples\temp\geocache_visits.txt", r"examples\only_found\geocache_visits.txt")
        shutil.move(r"examples\temp\geocache_logs.xml", r"examples\only_found\geocache_logs.xml")
        
class TestGefundeneAnzeigenOnlyNotFound(unittest.TestCase):  

    def setUp(self):
        self.x = geotooly.GPS_content(r"examples\only_notfound")  
        
    def test_gives_error(self):
        self.assertRaises(ValueError, self.x.gefundene_anzeigen)
        
class TestGefundeneAnzeigenNotOnlyFound(unittest.TestCase):  

    def setUp(self):
        self.x = geotooly.GPS_content(r"examples\not_only_found")  
        
    def test_anzeigen(self):
        with mock.patch('__builtin__.raw_input', return_value = ["anything_except_for_1"]):
            out = StringIO()
            sys.stdout = out                                                    
            self.x.gefundene_anzeigen() 
            output = out.getvalue().strip()  
            expected = u"GC1XRPM | N 49°48.559, E 009°56.019 | Multi-cache       | D 2.5 | T 3.5 | micro   | True  | 06 Sep 2016 | Im Auftrag ihrer Majestät – Der Märchenstuhl\n"
            expected = expected + u"GC5N23T | N 49°48.457, E 009°54.727 | Mystery Cache     | D 3.0 | T 4.0 | micro   | True  | 09 Jan 2017 | 67 - MedTrix - \u001a\u001a\u001a\u001a\u001a\n\n" 
            expected = expected +  "\nWas moechtest du als naechstes tun?\n"
            expected = expected + "1: Alle gefundenen Caches loeschen (vorher Loggen auf geocaching.com moeglich)\n"
            expected = expected + "2: zurueck"            
            self.assertEqual(output, expected)
            
    def test_loeschen(self):
        shutil.copy2(r"examples\not_only_found\GPX\GC1XRPM.gpx", r"examples\temp\GC1XRPM.gpx")              # copy files that are to be removed
        shutil.copy2(r"examples\not_only_found\GPX\GC5N23T.gpx", r"examples\temp\GC5N23T.gpx")
        shutil.copy2(r"examples\not_only_found\geocache_visits.txt", r"examples\temp\geocache_visits.txt")
        shutil.copy2(r"examples\not_only_found\geocache_logs.xml", r"examples\temp\geocache_logs.xml")
        
        with mock.patch('__builtin__.raw_input', side_effect = ["1","n","y"]):
            self.x.gefundene_anzeigen()
            self.assertEqual(len(self.x.geocaches), 5)   # less geocaches
            self.assertFalse(os.path.isfile(r"examples\not_only_found\geocache_visits.txt"))  # logfiles deleted
            self.assertFalse(os.path.isfile(r"examples\not_only_found\geocache_logs.xml"))
        
        shutil.move(r"examples\temp\GC1XRPM.gpx", r"examples\not_only_found\GPX\GC1XRPM.gpx") # move deleted files back
        shutil.move(r"examples\temp\GC5N23T.gpx", r"examples\not_only_found\GPX\GC5N23T.gpx")
        shutil.move(r"examples\temp\geocache_visits.txt", r"examples\not_only_found\geocache_visits.txt")
        shutil.move(r"examples\temp\geocache_logs.xml", r"examples\not_only_found\geocache_logs.xml")
        
class TestGefundeneAnzeigenFoundNotOnGPS(unittest.TestCase):  

    def setUp(self):
        self.x = geotooly.GPS_content(r"examples\found_not_on_gps")  
        
    def test_anzeigen(self):
        with mock.patch('__builtin__.raw_input', return_value = ["anything_except_for_1"]):
            out = StringIO()
            sys.stdout = out                                                    
            self.x.gefundene_anzeigen() 
            output = out.getvalue().strip()  
            expected = u"GC5G5F5 | N 49°47.955, E 009°58.566 | Traditional Cache | D 1.5 | T 4.0 | small   | True  | 08 Oct 2016 | Urban Buildering\n\n"
            expected = expected +  "\nWas moechtest du als naechstes tun?\n"
            expected = expected + "1: Alle gefundenen Caches loeschen (vorher Loggen auf geocaching.com moeglich)\n"
            expected = expected + "2: zurueck"            
            self.assertEqual(output, expected)
            
    def test_loeschen(self):
        shutil.copy2(r"examples\found_not_on_gps\GPX\GC5G5F5.gpx", r"examples\temp\GC5G5F5.gpx")              # copy files that are to be removed
        shutil.copy2(r"examples\found_not_on_gps\geocache_visits.txt", r"examples\temp\geocache_visits.txt")
        shutil.copy2(r"examples\found_not_on_gps\geocache_logs.xml", r"examples\temp\geocache_logs.xml")
        
        with mock.patch('__builtin__.raw_input', side_effect = ["1","n","y"]):
            self.x.gefundene_anzeigen()
            self.assertEqual(len(self.x.geocaches), 5)   # less geocaches
            self.assertFalse(os.path.isfile(r"examples\found_not_on_gps\geocache_visits.txt"))  # logfiles deleted
            self.assertFalse(os.path.isfile(r"examples\found_not_on_gps\geocache_logs.xml"))
        
        shutil.move(r"examples\temp\GC5G5F5.gpx", r"examples\found_not_on_gps\GPX\GC5G5F5.gpx") # move deleted files back
        shutil.move(r"examples\temp\geocache_visits.txt", r"examples\found_not_on_gps\geocache_visits.txt")
        shutil.move(r"examples\temp\geocache_logs.xml", r"examples\found_not_on_gps\geocache_logs.xml")
        
class TestLoeschen(unittest.TestCase):  

    def setUp(self):
        self.x = geotooly.GPS_content(r"examples\no_logfile") 
        
    def test_nicht_loeschen(self):
        cache = geocache.Geocache(r"examples\no_logfile\GPX\GC5N23T.gpx")
        with mock.patch('__builtin__.raw_input', return_value = "anything_except_for_y"):
            self.x.loeschen([cache])
            self.assertEqual(len(self.x.geocaches), 6)
        
    def test_einen_loeschen(self):
        cache = geocache.Geocache(r"examples\no_logfile\GPX\GC5N23T.gpx")
        shutil.copy2(r"examples\no_logfile\GPX\GC5N23T.gpx", r"examples\temp\GC5N23T.gpx")      # copy file that is to be removed
        with mock.patch('__builtin__.raw_input', return_value = "y"):
            self.x.loeschen([cache])
            self.assertEqual(len(self.x.geocaches), 5)
            self.assertFalse(os.path.isfile(r"examples\no_logfile\GPX\GC5N23T.gpx"))
        shutil.move(r"examples\temp\GC5N23T.gpx", r"examples\no_logfile\GPX\GC5N23T.gpx")       # move deleted file back
        
    def test_mehrere_loeschen(self):
        cache1 = geocache.Geocache(r"examples\no_logfile\GPX\GC5N23T.gpx")
        cache2 = geocache.Geocache(r"examples\no_logfile\GPX\GC1XRPM.gpx")
        shutil.copy2(r"examples\no_logfile\GPX\GC5N23T.gpx", r"examples\temp\GC5N23T.gpx")      # copy files that are to be removed
        shutil.copy2(r"examples\no_logfile\GPX\GC1XRPM.gpx", r"examples\temp\GC1XRPM.gpx")
        with mock.patch('__builtin__.raw_input', return_value = "y"):
            self.x.loeschen([cache1, cache2])
            self.assertEqual(len(self.x.geocaches), 4)
            self.assertFalse(os.path.isfile(r"examples\no_logfile\GPX\GC5N23T.gpx"))
            self.assertFalse(os.path.isfile(r"examples\no_logfile\GPX\GC1XRPM.gpx"))
        shutil.move(r"examples\temp\GC5N23T.gpx", r"examples\no_logfile\GPX\GC5N23T.gpx")       # move deleted files back
        shutil.move(r"examples\temp\GC1XRPM.gpx", r"examples\no_logfile\GPX\GC1XRPM.gpx")
        
    def test_bullshit_cacheliste_gives_error(self):
        with mock.patch('__builtin__.raw_input', return_value = "y"):
            self.assertRaises(AttributeError, self.x.loeschen, [42, "hallo"]) 
 
        
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
    suite.addTest(unittest.makeSuite(TestGCAuswahlAnzeigenDist))
    suite.addTest(unittest.makeSuite(TestSuchen))
    suite.addTest(unittest.makeSuite(TestGefundeneAnzeigenNoFoundCaches))
    suite.addTest(unittest.makeSuite(TestGefundeneAnzeigenOnlyFound))
    suite.addTest(unittest.makeSuite(TestGefundeneAnzeigenOnlyNotFound))
    suite.addTest(unittest.makeSuite(TestGefundeneAnzeigenNotOnlyFound))
    suite.addTest(unittest.makeSuite(TestGefundeneAnzeigenFoundNotOnGPS))
    suite.addTest(unittest.makeSuite(TestLoeschen))
    return suite

def main(v):
    sys.stdout = saved_stdout  # print output to display
    print "\nTesting main.py"
    out = StringIO()
    sys.stdout = out   # don't print output
    testsuite = create_testsuite()
    x = unittest.TextTestRunner(verbosity=v).run(testsuite) 
    sys.stdout = saved_stdout  # print output to display
    return x.testsRun, len(x.failures), len(x.errors)

if __name__ == '__main__':
    main(2)
