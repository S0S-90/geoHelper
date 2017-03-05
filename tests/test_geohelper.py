import unittest
import mock
import sys
sys.path.append('../src/') # path to source file (geohelper.py)
from StringIO import StringIO

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
