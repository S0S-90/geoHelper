﻿import unittest
import datetime
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
        
    def test_found_caches(self):
        found_caches = self.x.get_logged_and_found_caches()[0]
        #hier weiter!!!
        
    def test_found_caches(self):
        found_caches = self.x.get_logged_and_found_caches()[1]
        self.assertEqual(len(found_caches),2)
        self.assertEqual(found_caches[0].gccode, "GC1XRPM")
        self.assertEqual(found_caches[1].gccode, "GC5G5F5")

        
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
