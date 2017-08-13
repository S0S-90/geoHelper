#!/usr/bin/python
# -*- coding: utf-8 -*-

"""tests for gpscontent.py"""

import unittest
import mock
import sys
import shutil
import os
# noinspection PyCompatibility
from StringIO import StringIO  # module not existent in python 3
import test_frame
import ownfunctions
import geocache
import gpscontent


class TestInitNoLogfile(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"..\tests\examples\no_logfile")

    def test_geocaches(self):
        number_of_geocaches = len(self.x.geocaches)
        self.assertEqual(number_of_geocaches, 6)

    def test_attributes(self):
        expected_output = ['available 24-7', 'available in winter', 'bikes allowed', 'dangerous area',
                           'difficult climbing', 'dogs allowed', 'flashlight required', 'hike shorter than 1km',
                           'kid friendly', 'needs maintenance', 'no camping', 'no kids', 'no parking available',
                           'not stroller accessible', 'not wheelchair accessible', 'parking available',
                           'picnic tables available', 'public transit available', 'restrooms available',
                           'special tool required', 'stealth required', 'stroller accessible', 'takes less than 1 hour',
                           'teamwork required', 'thorns!', 'ticks!', 'tree climbing required', 'wheelchair accessible']
        self.assertEqual(self.x.existing_attributes, expected_output)

    def test_found_exists(self):
        self.assertEqual(self.x.found_exists, False)

    def test_warning(self):
        self.assertEqual(self.x.warning, False)

    def test_logged_and_found_caches_fails(self):
        self.assertRaises(IOError, self.x._get_logged_and_found_caches)

    def test_waypoints(self):
        self.assertEqual(self.x.waypoints, [])


class TestInitWaypoints(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"..\tests\examples\no_logfile_waypoints")

    def test_geocaches(self):
        number_of_geocaches = len(self.x.geocaches)
        self.assertEqual(number_of_geocaches, 6)

    def test_attributes(self):
        expected_output = ['available 24-7', 'available in winter', 'bikes allowed', 'dangerous area',
                           'difficult climbing', 'dogs allowed', 'flashlight required', 'hike shorter than 1km',
                           'kid friendly', 'needs maintenance', 'no camping', 'no kids', 'no parking available',
                           'not stroller accessible', 'not wheelchair accessible', 'parking available',
                           'picnic tables available', 'public transit available', 'restrooms available',
                           'special tool required', 'stealth required', 'stroller accessible', 'takes less than 1 hour',
                           'teamwork required', 'thorns!', 'ticks!', 'tree climbing required', 'wheelchair accessible']
        self.assertEqual(self.x.existing_attributes, expected_output)

    def test_found_exists(self):
        self.assertEqual(self.x.found_exists, False)

    def test_warning(self):
        self.assertEqual(self.x.warning, False)

    def test_logged_and_found_caches_fails(self):
        self.assertRaises(IOError, self.x._get_logged_and_found_caches)

    def test_waypoints(self):
        self.assertEqual(len(self.x.waypoints), 2)

    def test_waypoint_in_cache(self):
        for gc in self.x.geocaches:
            if gc.gccode == "sGC1XRPM":
                self.assertEqual(len(gc.waypoints), 1)
                self.assertEqual(gc.waypoints[0].name, "MÄRCHENSTUHL")


class TestInitOnlyFound(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"..\tests\examples\only_found")

    def test_geocaches(self):
        number_of_geocaches = len(self.x.geocaches)
        self.assertEqual(number_of_geocaches, 7)

    def test_attributes(self):
        expected_output = ['available 24-7', 'available in winter', 'bikes allowed', 'dangerous area',
                           'difficult climbing', 'dogs allowed', 'flashlight required', 'hike shorter than 1km',
                           'kid friendly', 'needs maintenance', 'no camping', 'no kids', 'no parking available',
                           'not stroller accessible', 'not wheelchair accessible', 'parking available',
                           'picnic tables available', 'public transit available', 'restrooms available',
                           'special tool required', 'stealth required', 'stroller accessible', 'takes less than 1 hour',
                           'teamwork required', 'thorns!', 'ticks!', 'tree climbing required', 'wheelchair accessible']
        self.assertEqual(self.x.existing_attributes, expected_output)

    def test_found_exists(self):
        self.assertEqual(self.x.found_exists, True)

    def test_warning(self):
        self.assertEqual(self.x.warning, False)

    def test_waypoints(self):
        self.assertEqual(self.x.waypoints, [])


class TestInitOnlyNotFound(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"..\tests\examples\only_notfound")

    def test_geocaches(self):
        number_of_geocaches = len(self.x.geocaches)
        self.assertEqual(number_of_geocaches, 7)

    def test_attributes(self):
        expected_output = ['available 24-7', 'available in winter', 'bikes allowed', 'dangerous area',
                           'difficult climbing', 'dogs allowed', 'flashlight required', 'hike shorter than 1km',
                           'kid friendly', 'needs maintenance', 'no camping', 'no kids', 'no parking available',
                           'not stroller accessible', 'not wheelchair accessible', 'parking available',
                           'picnic tables available', 'public transit available', 'restrooms available',
                           'special tool required', 'stealth required', 'stroller accessible', 'takes less than 1 hour',
                           'teamwork required', 'thorns!', 'ticks!', 'tree climbing required', 'wheelchair accessible']
        self.assertEqual(self.x.existing_attributes, expected_output)

    def test_found_exists(self):
        self.assertEqual(self.x.found_exists, False)

    def test_warning(self):
        self.assertEqual(self.x.warning, True)

    def test_waypoints(self):
        self.assertEqual(self.x.waypoints, [])


class TestInitNotOnlyFound(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"..\tests\examples\not_only_found")

    def test_geocaches(self):
        number_of_geocaches = len(self.x.geocaches)
        self.assertEqual(number_of_geocaches, 7)

    def test_attributes(self):
        expected_output = ['available 24-7', 'available in winter', 'bikes allowed', 'dangerous area',
                           'difficult climbing', 'dogs allowed', 'flashlight required', 'hike shorter than 1km',
                           'kid friendly', 'needs maintenance', 'no camping', 'no kids', 'no parking available',
                           'not stroller accessible', 'not wheelchair accessible', 'parking available',
                           'picnic tables available', 'public transit available', 'restrooms available',
                           'special tool required', 'stealth required', 'stroller accessible', 'takes less than 1 hour',
                           'teamwork required', 'thorns!', 'ticks!', 'tree climbing required', 'wheelchair accessible']
        self.assertEqual(self.x.existing_attributes, expected_output)

    def test_found_exists(self):
        self.assertEqual(self.x.found_exists, True)

    def test_warning(self):
        self.assertEqual(self.x.warning, True)

    def test_waypoints(self):
        self.assertEqual(self.x.waypoints, [])


class TestInitFoundNotOnGPS(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"..\tests\examples\found_not_on_gps")

    def test_geocaches(self):
        number_of_geocaches = len(self.x.geocaches)
        self.assertEqual(number_of_geocaches, 6)

    def test_attributes(self):
        expected_output = ['available 24-7', 'available in winter', 'bikes allowed', 'difficult climbing',
                           'dogs allowed', 'flashlight required', 'hike shorter than 1km', 'kid friendly', 'no camping',
                           'no parking available', 'not wheelchair accessible', 'parking available',
                           'picnic tables available', 'public transit available', 'restrooms available',
                           'special tool required', 'stealth required', 'stroller accessible', 'takes less than 1 hour',
                           'teamwork required', 'thorns!', 'ticks!', 'tree climbing required', 'wheelchair accessible']
        self.assertEqual(self.x.existing_attributes, expected_output)

    def test_found_exists(self):
        self.assertEqual(self.x.found_exists, True)

    def test_warning(self):
        self.assertEqual(self.x.warning, False)

    def test_waypoints(self):
        self.assertEqual(self.x.waypoints, [])


class TestInitNotFoundNotOnGPS(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"..\tests\examples\not_found_not_on_gps")

    def test_geocaches(self):
        number_of_geocaches = len(self.x.geocaches)
        self.assertEqual(number_of_geocaches, 6)

    def test_attributes(self):
        expected_output = ['available 24-7', 'available in winter', 'bikes allowed', 'difficult climbing',
                           'dogs allowed', 'flashlight required', 'hike shorter than 1km', 'kid friendly', 'no camping',
                           'no parking available', 'not wheelchair accessible', 'parking available',
                           'picnic tables available', 'public transit available', 'restrooms available',
                           'special tool required', 'stealth required', 'stroller accessible', 'takes less than 1 hour',
                           'teamwork required', 'thorns!', 'ticks!', 'tree climbing required', 'wheelchair accessible']
        self.assertEqual(self.x.existing_attributes, expected_output)

    def test_found_exists(self):
        self.assertEqual(self.x.found_exists, True)

    def test_warning(self):
        self.assertEqual(self.x.warning, False)

    def test_waypoints(self):
        self.assertEqual(self.x.waypoints, [])


class TestInitErrorInGPX(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"..\tests\examples\error_in_gpx")

    def test_geocaches(self):
        number_of_geocaches = len(self.x.geocaches)
        self.assertEqual(number_of_geocaches, 6)

    def test_attributes(self):
        expected_output = ['available 24-7', 'available in winter', 'bikes allowed', 'dangerous area',
                           'difficult climbing', 'dogs allowed', 'flashlight required', 'hike shorter than 1km',
                           'kid friendly', 'needs maintenance', 'no camping', 'no kids', 'no parking available',
                           'not stroller accessible', 'not wheelchair accessible', 'parking available',
                           'picnic tables available', 'public transit available', 'restrooms available',
                           'special tool required', 'stealth required', 'stroller accessible', 'takes less than 1 hour',
                           'teamwork required', 'thorns!', 'ticks!', 'tree climbing required', 'wheelchair accessible']
        self.assertEqual(self.x.existing_attributes, expected_output)

    def test_found_exists(self):
        self.assertEqual(self.x.found_exists, False)

    def test_warning(self):
        self.assertEqual(self.x.warning, False)

    def test_waypoints(self):
        self.assertEqual(self.x.waypoints, [])


class TestGetLoggedAndFoundCachesOnlyFound(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"..\tests\examples\only_found")

    def test_logged_caches(self):
        logged_caches = self.x._get_logged_and_found_caches()[0]
        expected = [["GC1XRPM", "2016-09-03T09:40Z", "Found it"], ["GC5G5F5", "2016-09-03T09:40Z", "Found it"]]
        self.assertEqual(logged_caches, expected)

    def test_found_caches(self):
        found_caches = self.x._get_logged_and_found_caches()[1]
        self.assertEqual(len(found_caches), 2)
        self.assertEqual(found_caches[0].gccode, "GC1XRPM")
        self.assertEqual(found_caches[1].gccode, "GC5G5F5")


class TestGetLoggedAndFoundCachesNotOnlyFound(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"..\tests\examples\not_only_found")

    def test_logged_caches(self):
        logged_caches = self.x._get_logged_and_found_caches()[0]
        expected = [["GC1XRPM", "2016-09-03T09:40Z", "Found it"], ["GC5G5F5", "2016-09-03T09:40Z", "unattempted"],
                    ["GC5N23T", "2017-02-12T09:40Z", "Found it"]]
        self.assertEqual(logged_caches, expected)

    def test_found_caches(self):
        found_caches = self.x._get_logged_and_found_caches()[1]
        self.assertEqual(len(found_caches), 2)
        self.assertEqual(found_caches[0].gccode, "GC1XRPM")
        self.assertEqual(found_caches[1].gccode, "GC5N23T")


class TestGetLoggedAndFoundCachesOnlyNotFound(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"..\tests\examples\only_notfound")

    def test_logged_caches(self):
        logged_caches = self.x._get_logged_and_found_caches()[0]
        expected = [["GC1XRPM", "2016-09-03T09:40Z", "unattempted"], ["GC5G5F5", "2016-09-03T09:40Z", "unattempted"]]
        self.assertEqual(logged_caches, expected)

    def test_found_caches(self):
        found_caches = self.x._get_logged_and_found_caches()[1]
        self.assertEqual(len(found_caches), 0)


class TestGetLoggedAndFoundCachesFoundNotOnGPS(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"..\tests\examples\found_not_on_gps")

    def test_logged_caches(self):
        logged_caches = self.x._get_logged_and_found_caches()[0]
        expected = [["GC5G5F5", "2016-09-03T09:40Z", "Found it"]]
        self.assertEqual(logged_caches, expected)

    def test_found_caches(self):
        found_caches = self.x._get_logged_and_found_caches()[1]
        self.assertEqual(len(found_caches), 1)
        self.assertEqual(found_caches[0].gccode, "GC5G5F5")


class TestGetLoggedAndFoundCachesNotFoundNotOnGPS(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"..\tests\examples\not_found_not_on_gps")

    def test_logged_caches(self):
        logged_caches = self.x._get_logged_and_found_caches()[0]
        expected = [["GC5G5F5", "2016-09-03T09:40Z", "Found it"]]
        self.assertEqual(logged_caches, expected)

    def test_found_caches(self):
        found_caches = self.x._get_logged_and_found_caches()[1]
        self.assertEqual(len(found_caches), 1)
        self.assertEqual(found_caches[0].gccode, "GC5G5F5")


class TestReadWaypoints(unittest.TestCase):

    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"..\tests\examples\no_logfile_waypoints")

    def test_readfile(self):
        wpts = self.x._read_waypoints(r"..\tests\examples\no_logfile_waypoints\GPX\Wegpunkte_14-JAN-17.gpx")
        self.assertEqual(len(wpts), 1)  # reads only the waypoint that does not belong to a cache

    def test_broken_wptfile(self):
        exception = False  # has to be that complicated because ParseError unknown
        # noinspection PyBroadException
        try:
            self.x._read_waypoints(r"..\tests\examples\no_logfile_waypoints\GPX\Wegpunkte_08-OKT-16.gpx")
        except:  # broad exception because ParseError unknown
            exception = True
        self.assertTrue(exception)


class TestSortAndShowCaches(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"..\tests\examples\no_logfile")

    def test_gccode_up(self):
        with mock.patch('__builtin__.raw_input', side_effect=['1', '1']):
            expected = ["GC1XRPM", "GC33QGC", "GC5N23T", "GC6K86W", "GC6RNTX", "GCJJ20"]
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            self.assertEqual(sorted_caches, expected)

    def test_gccode_down(self):
        with mock.patch('__builtin__.raw_input', side_effect=['1', '2']):
            expected = ["GCJJ20", "GC6RNTX", "GC6K86W", "GC5N23T", "GC33QGC", "GC1XRPM"]
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            self.assertEqual(sorted_caches, expected)

    def test_name_up(self):
        with mock.patch('__builtin__.raw_input', side_effect=['2', '1']):
            expected = ["GC5N23T", "GC6RNTX", "GC1XRPM", "GC6K86W", "GC33QGC", "GCJJ20"]
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            self.assertEqual(sorted_caches, expected)

    def test_name_down(self):
        with mock.patch('__builtin__.raw_input', side_effect=['2', '2']):
            expected = ["GCJJ20", "GC33QGC", "GC6K86W", "GC1XRPM", "GC6RNTX", "GC5N23T"]
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            self.assertEqual(sorted_caches, expected)

    def test_type_up(self):
        with mock.patch('__builtin__.raw_input', side_effect=['3', '1']):
            expected = ["GC1XRPM", "GC5N23T", "GC6RNTX", "GC33QGC", "GC6K86W", "GCJJ20"]
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            self.assertEqual(sorted_caches, expected)

    def test_type_down(self):
        with mock.patch('__builtin__.raw_input', side_effect=['3', '2']):
            expected = ["GCJJ20", "GC33QGC", "GC6K86W", "GC5N23T", "GC6RNTX", "GC1XRPM"]
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            self.assertEqual(sorted_caches, expected)

    def test_difficulty_up(self):
        with mock.patch('__builtin__.raw_input', side_effect=['4', '1']):
            expected = ["GCJJ20", "GC33QGC", "GC6K86W", "GC6RNTX", "GC1XRPM", "GC5N23T"]
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            self.assertEqual(sorted_caches, expected)

    def test_difficulty_down(self):
        with mock.patch('__builtin__.raw_input', side_effect=['4', '2']):
            expected = ["GC5N23T", "GC1XRPM", "GC33QGC", "GC6K86W", "GC6RNTX", "GCJJ20"]
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            self.assertEqual(sorted_caches, expected)

    def test_terrain_up(self):
        with mock.patch('__builtin__.raw_input', side_effect=['5', '1']):
            expected = ["GCJJ20", "GC6RNTX", "GC6K86W", "GC33QGC", "GC1XRPM", "GC5N23T"]
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            self.assertEqual(sorted_caches, expected)

    def test_terrain_down(self):
        with mock.patch('__builtin__.raw_input', side_effect=['5', '2']):
            expected = ["GC5N23T", "GC1XRPM", "GC33QGC", "GC6K86W", "GC6RNTX", "GCJJ20"]
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            self.assertEqual(sorted_caches, expected)

    def test_size_up(self):
        with mock.patch('__builtin__.raw_input', side_effect=['6', '1']):
            expected = ["GCJJ20", "GC1XRPM", "GC5N23T", "GC6K86W", "GC6RNTX", "GC33QGC"]
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            self.assertEqual(sorted_caches, expected)

    def test_size_down(self):
        with mock.patch('__builtin__.raw_input', side_effect=['6', '2']):
            expected = ["GC33QGC", "GC1XRPM", "GC5N23T", "GC6K86W", "GC6RNTX", "GCJJ20"]
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            self.assertEqual(sorted_caches, expected)

    def test_downloaddate_up(self):
        with mock.patch('__builtin__.raw_input', side_effect=['7', '1']):
            expected = ["GC6K86W", "GC1XRPM", "GC33QGC", "GC6RNTX", "GCJJ20", "GC5N23T"]
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            self.assertEqual(sorted_caches, expected)

    def test_downloaddate_down(self):
        with mock.patch('__builtin__.raw_input', side_effect=['7', '2']):
            expected = ["GC5N23T", "GCJJ20", "GC6RNTX", "GC33QGC", "GC1XRPM", "GC6K86W"]
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            self.assertEqual(sorted_caches, expected)

    def test_available_up(self):
        with mock.patch('__builtin__.raw_input', side_effect=['8', '1']):
            expected = ["GC5N23T", "GC1XRPM", "GC33QGC", "GC6K86W", "GC6RNTX", "GCJJ20"]
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            self.assertEqual(sorted_caches, expected)

    def test_available_down(self):
        with mock.patch('__builtin__.raw_input', side_effect=['8', '2']):
            expected = ["GC1XRPM", "GC33QGC", "GC6K86W", "GC6RNTX", "GCJJ20", "GC5N23T"]
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            self.assertEqual(sorted_caches, expected)

    def test_distance_up(self):
        url = 'https://www.google.de/maps/place/97209+Veitsh%C3%B6chheim/@49.8414697,9.8579699,13z/data=!3m1!4b1!4m5!3m4!'
        url += '1s0x47a2915cbab1bfe3:0xdbe76ec582bb3aa5!8m2!3d49.8312701!4d9.8803666'

        with mock.patch('__builtin__.raw_input', side_effect=['9', '1', url]):
            expected = ["GC5N23T", "GC1XRPM", "GCJJ20", "GC6RNTX", "GC6K86W", "GC33QGC"]
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            self.assertEqual(sorted_caches, expected)

    def test_distance_down(self):
        url = 'https://www.google.de/maps/place/97209+Veitsh%C3%B6chheim/@49.8414697,9.8579699,13z/data=!3m1!4b1!4m5!'
        url += '3m4!1s0x47a2915cbab1bfe3:0xdbe76ec582bb3aa5!8m2!3d49.8312701!4d9.8803666'

        with mock.patch('__builtin__.raw_input', side_effect=['9', '2', url]):
            expected = ["GC33QGC", "GC6K86W", "GC6RNTX", "GCJJ20", "GC1XRPM", "GC5N23T"]
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            self.assertEqual(sorted_caches, expected)


class TestShowAll(unittest.TestCase):
    def test_show_nothing(self):
        x = gpscontent.GPSContent(r"..\tests\examples\empty")
        self.assertEqual(x.show_all(), "Keine Caches auf dem Geraet.")

    def test_show_caches(self):
        x = gpscontent.GPSContent(r"..\tests\examples\no_logfile")
        expected = u"GC1XRPM | N 49°48.559, E 009°56.019 | Multi-cache       | D 2.5 | T 3.5 | micro   | True  | "
        expected += u"06 Sep 2016 | Im Auftrag ihrer Majestät – Der Märchenstuhl\n"
        expected += u"GC33QGC | S 43°41.726, W 066°27.090 | Traditional Cache | D 2.0 | T 3.0 | small   | "
        expected += u"True  | 11 Sep 2016 | Tesoro Ameghino\n"
        expected += u"GC5N23T | N 49°48.457, E 009°54.727 | Mystery Cache     | D 3.0 | T 4.0 | micro   | "
        expected += u"False | 05 Mar 2017 | 67 - MedTrix - {}\n".format(u"\u001a" + u"\u001a" + u"\u001a" +
                                                                        u"\u001a" + u"\u001a")
        expected += u"GC6K86W | N 50°19.133, E 010°11.616 | Traditional Cache | D 2.0 | T 2.0 | micro   | "
        expected += u"True  | 04 Aug 2016 | Saaletalblick\n"
        expected += u"GC6RNTX | N 49°47.670, E 009°56.456 | Mystery Cache     | D 2.0 | T 1.5 | micro   | "
        expected += u"True  | 08 Oct 2016 | Hochschule für Musik 1\n"
        expected += u"GCJJ20  | N 49°47.688, E 009°55.816 | Unknown Type      | D 1.0 | T 1.0 | other   | "
        expected += u"True  | 29 Oct 2016 | Wuerzburger webcam\n"
        self.assertEqual(x.show_all(), expected)

    def test_show_caches_with_waypoints(self):
        x = gpscontent.GPSContent(r"..\tests\examples\no_logfile_waypoints")
        expected = u"GC1XRPM | N 49°48.559, E 009°56.019 | Multi-cache       | D 2.5 | T 3.5 | micro   | True  | "
        expected += u"06 Sep 2016 | Im Auftrag ihrer Majestät – Der Märchenstuhl\n"
        expected += u"        | N 49°47.546, E 009°55.934 | MÄRCHENSTUHL 2 (1.9km)\n"
        expected += u"GC33QGC | S 43°41.726, W 066°27.090 | Traditional Cache | D 2.0 | T 3.0 | small   | "
        expected += u"True  | 11 Sep 2016 | Tesoro Ameghino\n"
        expected += u"GC5N23T | N 49°48.457, E 009°54.727 | Mystery Cache     | D 3.0 | T 4.0 | micro   | "
        expected += u"False | 05 Mar 2017 | 67 - MedTrix - {}\n".format(u"\u001a" + u"\u001a" + u"\u001a" +
                                                                        u"\u001a" + u"\u001a")
        expected += u"GC6K86W | N 50°19.133, E 010°11.616 | Traditional Cache | D 2.0 | T 2.0 | micro   | "
        expected += u"True  | 04 Aug 2016 | Saaletalblick\n"
        expected += u"GC6RNTX | N 49°47.670, E 009°56.456 | Mystery Cache     | D 2.0 | T 1.5 | micro   | "
        expected += u"True  | 08 Oct 2016 | Hochschule für Musik 1\n"
        expected += u"GCJJ20  | N 49°47.688, E 009°55.816 | Unknown Type      | D 1.0 | T 1.0 | other   | "
        expected += u"True  | 29 Oct 2016 | Wuerzburger webcam\n"
        self.assertEqual(x.show_all(), expected)


class TestShowAllDist(unittest.TestCase):
    def test_show_nothing(self):
        x = gpscontent.GPSContent(r"..\tests\examples\empty")
        self.assertEqual(x.show_all(), "Keine Caches auf dem Geraet.")

    def test_show_caches(self):
        x = gpscontent.GPSContent(r"..\tests\examples\no_logfile")
        for gc in x.geocaches:
            gc.distance = ownfunctions.calculate_distance(gc.coordinates, [49.8414697, 9.8579699])
        expected = u"    6.5km | GC1XRPM | N 49°48.559, E 009°56.019 | Multi-cache       | D 2.5 | T 3.5 | micro   | "
        expected += u"True  | 06 Sep 2016 | Im Auftrag ihrer Majestät – Der Märchenstuhl\n"
        expected += u"12746.3km | GC33QGC | S 43°41.726, W 066°27.090 | Traditional Cache | D 2.0 | T 3.0 | small   | "
        expected += u"True  | 11 Sep 2016 | Tesoro Ameghino\n"
        expected += u"    5.4km | GC5N23T | N 49°48.457, E 009°54.727 | Mystery Cache     | D 3.0 | T 4.0 | micro   | "
        expected += u"False | 05 Mar 2017 | 67 - MedTrix - {}\n".format(u"\u001a" + u"\u001a" + u"\u001a" +
                                                                        u"\u001a" + u"\u001a")
        expected += u"   58.2km | GC6K86W | N 50°19.133, E 010°11.616 | Traditional Cache | D 2.0 | T 2.0 | micro   "
        expected += u"| True  | 04 Aug 2016 | Saaletalblick\n"
        expected += u"    7.9km | GC6RNTX | N 49°47.670, E 009°56.456 | Mystery Cache     | D 2.0 | T 1.5 | micro   "
        expected += u"| True  | 08 Oct 2016 | Hochschule für Musik 1\n"
        expected += u"    7.3km | GCJJ20  | N 49°47.688, E 009°55.816 | Unknown Type      | D 1.0 | T 1.0 | other   "
        expected += u"| True  | 29 Oct 2016 | Wuerzburger webcam\n"
        self.assertEqual(x.show_all_dist(), expected)

    def test_show_caches_with_waypoints(self):
        x = gpscontent.GPSContent(r"..\tests\examples\no_logfile_waypoints")
        for gc in x.geocaches:
            gc.distance = ownfunctions.calculate_distance(gc.coordinates, [49.8414697, 9.8579699])
        expected = u"    6.5km | GC1XRPM | N 49°48.559, E 009°56.019 | Multi-cache       | D 2.5 | T 3.5 | micro   | "
        expected += u"True  | 06 Sep 2016 | Im Auftrag ihrer Majestät – Der Märchenstuhl\n"
        expected += u"                    | N 49°47.546, E 009°55.934 | MÄRCHENSTUHL 2 (1.9km)\n"
        expected += u"12746.3km | GC33QGC | S 43°41.726, W 066°27.090 | Traditional Cache | D 2.0 | T 3.0 | small   | "
        expected += u"True  | 11 Sep 2016 | Tesoro Ameghino\n"
        expected += u"    5.4km | GC5N23T | N 49°48.457, E 009°54.727 | Mystery Cache     | D 3.0 | T 4.0 | micro   | "
        expected += u"False | 05 Mar 2017 | 67 - MedTrix - {}\n".format(u"\u001a" + u"\u001a" + u"\u001a" +
                                                                        u"\u001a" + u"\u001a")
        expected += u"   58.2km | GC6K86W | N 50°19.133, E 010°11.616 | Traditional Cache | D 2.0 | T 2.0 | micro   "
        expected += u"| True  | 04 Aug 2016 | Saaletalblick\n"
        expected += u"    7.9km | GC6RNTX | N 49°47.670, E 009°56.456 | Mystery Cache     | D 2.0 | T 1.5 | micro   "
        expected += u"| True  | 08 Oct 2016 | Hochschule für Musik 1\n"
        expected += u"    7.3km | GCJJ20  | N 49°47.688, E 009°55.816 | Unknown Type      | D 1.0 | T 1.0 | other   "
        expected += u"| True  | 29 Oct 2016 | Wuerzburger webcam\n"
        self.assertEqual(x.show_all_dist(), expected)


class TestReadCache(unittest.TestCase):

    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"..\tests\examples\no_logfile")

    def test_cache(self):
        with mock.patch('__builtin__.raw_input', return_value="GC5N23T"):
            gc_return = self.x.read_cache()
            gc = geocache.Geocache(r"..\tests\examples\no_logfile\GPX\GC5N23T.gpx")
            self.assertEqual(gc_return, gc)

    def test_not_existing_cache(self):
        with mock.patch('__builtin__.raw_input', return_value="GC12345"):
            out = StringIO()
            sys.stdout = out
            self.x.show_one()
            output = out.getvalue()
            self.assertEqual(output, "Dieser GC-Code existiert nicht.\n")


class TestShowOne(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"..\tests\examples\no_logfile_waypoints")

    def test_not_existing_cache(self):
        with mock.patch('__builtin__.raw_input', return_value="GC12345"):
            out = StringIO()
            sys.stdout = out
            self.x.show_one()
            output = out.getvalue()
            self.assertEqual(output, "Dieser GC-Code existiert nicht.\n")

    def test_delete(self):
        shutil.copy2(r"..\tests\examples\no_logfile_waypoints\GPX\GC5N23T.gpx",
                     r"..\tests\examples\temp\GC5N23T.gpx")  # copy file that is to be removed
        with mock.patch('__builtin__.raw_input', side_effect=["GC5N23T", "1", "y"]):
            self.x.show_one()
            self.assertEqual(len(self.x.geocaches), 5)
        shutil.move(r"..\tests\examples\temp\GC5N23T.gpx",
                    r"..\tests\examples\no_logfile_waypoints\GPX\GC5N23T.gpx")  # move deleted file back to GPX folder

    def test_not_delete(self):
        with mock.patch('__builtin__.raw_input', side_effect=["GC5N23T", "1", "n"]):
            self.x.show_one()
            self.assertEqual(len(self.x.geocaches), 6)

    def test_delete_with_wpt(self):
        shutil.copy2(r"..\tests\examples\no_logfile_waypoints\GPX\GC1XRPM.gpx",
                     r"..\tests\examples\temp\GC1XRPM.gpx")  # copy file that is to be removed
        with mock.patch('__builtin__.raw_input', side_effect=["GC1XRPM", "1", "y"]):
            self.x.show_one()
            self.assertEqual(len(self.x.geocaches), 5)
            # TODO: test if waypoint is deleted from GPS, too
        shutil.move(r"..\tests\examples\temp\GC1XRPM.gpx",
                    r"..\tests\examples\no_logfile_waypoints\GPX\GC1XRPM.gpx")  # move deleted file back to GPX folder


class TestShowGCSelection(unittest.TestCase):

    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"..\tests\examples\no_logfile_waypoints")

    def test_show_nothing(self):
        self.assertEqual(self.x.show_gc_selection([]), "")

    def test_show_selection(self):
        selection = self.x.geocaches[3:5]
        expected = u"GC6K86W | N 50°19.133, E 010°11.616 | Traditional Cache | D 2.0 | T 2.0 | micro   | True  | "
        expected += u"04 Aug 2016 | Saaletalblick\n"
        expected += u"GC6RNTX | N 49°47.670, E 009°56.456 | Mystery Cache     | D 2.0 | T 1.5 | micro   | True  | "
        expected += u"08 Oct 2016 | Hochschule für Musik 1\n"
        self.assertEqual(self.x.show_gc_selection(selection), expected)

    def test_show_selection_waypoint(self):
        selection = self.x.geocaches[:2]
        expected = u"GC1XRPM | N 49°48.559, E 009°56.019 | Multi-cache       | D 2.5 | T 3.5 | micro   | "
        expected += u"True  | 06 Sep 2016 | Im Auftrag ihrer Majestät – Der Märchenstuhl\n"
        expected += u"        | N 49°47.546, E 009°55.934 | MÄRCHENSTUHL 2 (1.9km)\n"
        expected += u"GC33QGC | S 43°41.726, W 066°27.090 | Traditional Cache | D 2.0 | T 3.0 | small   | "
        expected += u"True  | 11 Sep 2016 | Tesoro Ameghino\n"
        self.assertEqual(self.x.show_gc_selection(selection), expected)

    def test_bullshitlist(self):
        selection = ["13", 6]
        self.assertRaises(TypeError, self.x.show_gc_selection, selection)


class TestShowGCSelectionDist(unittest.TestCase):

    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"..\tests\examples\no_logfile_waypoints")
        for gc in self.x.geocaches:
            gc.distance = ownfunctions.calculate_distance(gc.coordinates, [49.8414697, 9.8579699])

    def test_show_nothing(self):
        self.assertEqual(self.x.show_gc_selection_dist([]), "")

    def test_show_selection(self):
        selection = self.x.geocaches[3:5]
        expected = u"   58.2km | GC6K86W | N 50°19.133, E 010°11.616 | Traditional Cache | D 2.0 | T 2.0 | micro   | "
        expected += u"True  | 04 Aug 2016 | Saaletalblick\n"
        expected += u"    7.9km | GC6RNTX | N 49°47.670, E 009°56.456 | Mystery Cache     | D 2.0 | T 1.5 | micro   "
        expected += u"| True  | 08 Oct 2016 | Hochschule für Musik 1\n"
        self.assertEqual(self.x.show_gc_selection_dist(selection), expected)

    def test_show_selection_waypoints(self):
        selection = self.x.geocaches[:2]
        expected = u"    6.5km | GC1XRPM | N 49°48.559, E 009°56.019 | Multi-cache       | D 2.5 | T 3.5 | micro   | "
        expected += u"True  | 06 Sep 2016 | Im Auftrag ihrer Majestät – Der Märchenstuhl\n"
        expected += u"                    | N 49°47.546, E 009°55.934 | MÄRCHENSTUHL 2 (1.9km)\n"
        expected += u"12746.3km | GC33QGC | S 43°41.726, W 066°27.090 | Traditional Cache | D 2.0 | T 3.0 | small   | "
        expected += u"True  | 11 Sep 2016 | Tesoro Ameghino\n"
        self.assertEqual(self.x.show_gc_selection_dist(selection), expected)

    def test_bullshitlist(self):
        selection = ["13", 6]
        self.assertRaises(TypeError, self.x.show_gc_selection_dist, selection)


class TestSearch(unittest.TestCase):

    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"..\tests\examples\no_logfile")

    def test_name(self):
        with mock.patch('__builtin__.raw_input', side_effect=["1", "A"]):
            expected = [self.x.geocaches[0], self.x.geocaches[1]]
            self.assertEqual(self.x.search(), expected)

    def test_description(self):
        with mock.patch('__builtin__.raw_input', side_effect=["2", "ist"]):
            expected = [self.x.geocaches[0], self.x.geocaches[1], self.x.geocaches[2], self.x.geocaches[5]]
            self.assertEqual(self.x.search(), expected)

    def test_cachetype(self):
        with mock.patch('__builtin__.raw_input', side_effect=["3", "Mystery Cache"]):
            expected = [self.x.geocaches[2], self.x.geocaches[4]]
            self.assertEqual(self.x.search(), expected)

    def test_cachetype_invalid(self):
        with mock.patch('__builtin__.raw_input', side_effect=["3", "Mystery"]):
            self.assertEqual(self.x.search(), [])

    def test_difficulty(self):
        with mock.patch('__builtin__.raw_input', side_effect=["4", "2, 2.5"]):
            expected = [self.x.geocaches[0], self.x.geocaches[1], self.x.geocaches[3], self.x.geocaches[4]]
            self.assertEqual(self.x.search(), expected)

    def test_difficulty_without_space(self):
        with mock.patch('__builtin__.raw_input', side_effect=["4", "2,2.5"]):
            expected = [self.x.geocaches[0], self.x.geocaches[1], self.x.geocaches[3], self.x.geocaches[4]]
            self.assertEqual(self.x.search(), expected)

    def test_difficulty_error(self):
        with mock.patch('__builtin__.raw_input', side_effect=["4", "2.5,2"]):
            self.assertEqual(self.x.search(), [])

    def test_difficulty_error2(self):
        with mock.patch('__builtin__.raw_input', side_effect=["4", "2.5,7"]):
            self.assertEqual(self.x.search(), [])

    def test_terrain(self):
        with mock.patch('__builtin__.raw_input', side_effect=["5", "1.5, 2"]):
            expected = [self.x.geocaches[3], self.x.geocaches[4]]
            self.assertEqual(self.x.search(), expected)

    def test_size(self):
        with mock.patch('__builtin__.raw_input', side_effect=["6", "micro, small"]):
            expected = [self.x.geocaches[0], self.x.geocaches[1], self.x.geocaches[2], self.x.geocaches[3],
                        self.x.geocaches[4]]
            self.assertEqual(self.x.search(), expected)

    def test_size_without_space(self):
        with mock.patch('__builtin__.raw_input', side_effect=["6", "micro,small"]):
            expected = [self.x.geocaches[0], self.x.geocaches[1], self.x.geocaches[2], self.x.geocaches[3],
                        self.x.geocaches[4]]
            self.assertEqual(self.x.search(), expected)

    def test_size_error(self):
        with mock.patch('__builtin__.raw_input', side_effect=["6", "small, micro"]):
            self.assertEqual(self.x.search(), [])

    def test_downloaddate(self):
        with mock.patch('__builtin__.raw_input', side_effect=["7", "01.10.2016, 31.10.2016"]):
            expected = [self.x.geocaches[4], self.x.geocaches[5]]
            self.assertEqual(self.x.search(), expected)

    def test_downloaddate_without_space(self):
        with mock.patch('__builtin__.raw_input', side_effect=["7", "01.10.2016,31.10.2016"]):
            expected = [self.x.geocaches[4], self.x.geocaches[5]]
            self.assertEqual(self.x.search(), expected)

    def test_downloaddate_error(self):
        with mock.patch('__builtin__.raw_input', side_effect=["7", "1.10.2016, 31.10.2016"]):
            self.assertEqual(self.x.search(), [])

    def test_downloaddate_error2(self):
        with mock.patch('__builtin__.raw_input', side_effect=["7", "31.10.2016, 01.10.2016"]):
            self.assertEqual(self.x.search(), [])

    def test_not_available(self):
        with mock.patch('__builtin__.raw_input', side_effect=["8", "n"]):
            expected = [self.x.geocaches[2]]
            self.assertEqual(self.x.search(), expected)

    def test_available(self):
        with mock.patch('__builtin__.raw_input', side_effect=["8", "y"]):
            expected = [self.x.geocaches[0], self.x.geocaches[1], self.x.geocaches[3], self.x.geocaches[4],
                        self.x.geocaches[5]]
            self.assertEqual(self.x.search(), expected)

    def test_available_by_bullshit(self):
        with mock.patch('__builtin__.raw_input', side_effect=["8", "dfghj"]):
            expected = [self.x.geocaches[0], self.x.geocaches[1], self.x.geocaches[3], self.x.geocaches[4],
                        self.x.geocaches[5]]
            self.assertEqual(self.x.search(), expected)

    def test_attributes(self):
        with mock.patch('__builtin__.raw_input', side_effect=["9", "available 24-7"]):
            expected = [self.x.geocaches[2], self.x.geocaches[4], self.x.geocaches[5]]
            self.assertEqual(self.x.search(), expected)

    def test_attributes_that_doesnt_exist(self):
        with mock.patch('__builtin__.raw_input', side_effect=["9", "No attributes specified by the author"]):
            self.assertEqual(self.x.search(), [])

    def test_distance(self):
        url = "https://www.google.de/maps/place/97209+Veitsh%C3%B6chheim/@49.8414697,9.8579699,13z/data=!3m1!4b1!4m5!3m4"
        url += "!1s0x47a2915cbab1bfe3:0xdbe76ec582bb3aa5!8m2!3d49.8312701!4d9.8803666"

        with mock.patch('__builtin__.raw_input', side_effect=["10", url, "6.4, 7.4"]):
            expected = [self.x.geocaches[0], self.x.geocaches[5]]
            self.assertEqual(self.x.search(), expected)

    def test_distance_without_space(self):
        url = "https://www.google.de/maps/place/97209+Veitsh%C3%B6chheim/@49.8414697,9.8579699,13z/data=!3m1!4b1!4m5!3m4"
        url += "!1s0x47a2915cbab1bfe3:0xdbe76ec582bb3aa5!8m2!3d49.8312701!4d9.8803666"

        with mock.patch('__builtin__.raw_input', side_effect=["10", url, "6.4,7.4"]):
            expected = [self.x.geocaches[0], self.x.geocaches[5]]
            self.assertEqual(self.x.search(), expected)

    def test_distance_error(self):
        url = "https://www.gooe/maps/place/97209+Veitsh%C3%B6chheim/@49.8414697,9.8579699,13z/data=!3m1!4b1!4m5!3m4!"
        url += "1s0x47a2915cbab1bfe3:0xdbe76ec582bb3aa5!8m2!3d49.8312701!4d9.8803666"

        with mock.patch('__builtin__.raw_input', side_effect=["10", url, "6.4,7.4"]):
            self.assertEqual(self.x.search(), [])

    def test_distance_error2(self):
        url = "https://www.google.de/maps/place/97209+Veitsh%C3%B6chheim/@49.8414697,9.8579699,13z/data=!3m1!4b1!4m5!"
        url += "3m4!1s0x47a2915cbab1bfe3:0xdbe76ec582bb3aa5!8m2!3d49.8312701!4d9.8803666"

        with mock.patch('__builtin__.raw_input', side_effect=["10", url, "hh, 7.4"]):
            self.assertEqual(self.x.search(), [])

    def test_distance_error3(self):
        url = "https://www.google.de/maps/place/97209+Veitsh%C3%B6chheim/@49.8414697,9.8579699,13z/data=!3m1!4b1!4m5!"
        url += "3m4!1s0x47a2915cbab1bfe3:0xdbe76ec582bb3aa5!8m2!3d49.8312701!4d9.8803666"

        with mock.patch('__builtin__.raw_input', side_effect=["10", url, "10.3, 7.4"]):
            self.assertEqual(self.x.search(), [])


class TestShowFoundsNoFoundCaches(unittest.TestCase):

    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"..\tests\examples\no_logfile")

    def test_gives_error(self):
        self.assertRaises(ValueError, self.x.show_founds)


class TestShowFoundsOnlyFound(unittest.TestCase):

    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"..\tests\examples\only_found")

    def test_show_caches(self):
        with mock.patch('__builtin__.raw_input', return_value="3"):
            out = StringIO()
            sys.stdout = out
            self.x.show_founds()
            output = out.getvalue()
            expected = u"GC1XRPM | N 49°48.559, E 009°56.019 | Multi-cache       | D 2.5 | T 3.5 | micro   | True  "
            expected += u"| 06 Sep 2016 | Im Auftrag ihrer Majestät – Der Märchenstuhl\n"
            expected += u"GC5G5F5 | N 49°47.955, E 009°58.566 | Traditional Cache | D 1.5 | T 4.0 | small   | True  "
            expected += u"| 08 Oct 2016 | Urban Buildering\n\n"
            expected += "\nWas moechtest du als naechstes tun?\n"
            expected += "1: Gefundene Caches auf geocaching.com loggen "
            expected += "(ueber den Upload von drafts / fieldnotes, INTERNET!!!)\n"
            expected += "2: Alle gefundenen Caches loeschen\n"
            expected += "3: zurueck\n"
            self.assertEqual(output, expected)

    def test_delete(self):
        shutil.copy2(r"..\tests\examples\only_found\GPX\GC1XRPM.gpx",
                     r"..\tests\examples\temp\GC1XRPM.gpx")  # copy files that are to be removed
        shutil.copy2(r"..\tests\examples\only_found\GPX\GC5G5F5.gpx", r"..\tests\examples\temp\GC5G5F5.gpx")
        shutil.copy2(r"..\tests\examples\only_found\geocache_visits.txt", r"..\tests\examples\temp\geocache_visits.txt")
        shutil.copy2(r"..\tests\examples\only_found\geocache_logs.xml", r"..\tests\examples\temp\geocache_logs.xml")

        with mock.patch('__builtin__.raw_input', side_effect=["2", "y"]):
            self.x.show_founds()
            self.assertEqual(len(self.x.geocaches), 5)  # less geocaches
            self.assertFalse(os.path.isfile(r"..\tests\examples\only_found\geocache_visits.txt"))  # logfiles deleted
            self.assertFalse(os.path.isfile(r"..\tests\examples\only_found\geocache_logs.xml"))

        # move deleted files back
        shutil.move(r"..\tests\examples\temp\GC1XRPM.gpx", r"..\tests\examples\only_found\GPX\GC1XRPM.gpx")
        shutil.move(r"..\tests\examples\temp\GC5G5F5.gpx", r"..\tests\examples\only_found\GPX\GC5G5F5.gpx")
        shutil.move(r"..\tests\examples\temp\geocache_visits.txt", r"..\tests\examples\only_found\geocache_visits.txt")
        shutil.move(r"..\tests\examples\temp\geocache_logs.xml", r"..\tests\examples\only_found\geocache_logs.xml")


class TestShowFoundsOnlyNotFound(unittest.TestCase):

    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"..\tests\examples\only_notfound")

    def test_gives_error(self):
        self.assertRaises(ValueError, self.x.show_founds)


class TestShowFoundsNotOnlyFound(unittest.TestCase):

    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"..\tests\examples\not_only_found")

    def test_show_caches(self):
        with mock.patch('__builtin__.raw_input', return_value="3"):
            out = StringIO()
            sys.stdout = out
            self.x.show_founds()
            output = out.getvalue()
            expected = u"GC1XRPM | N 49°48.559, E 009°56.019 | Multi-cache       | D 2.5 | T 3.5 | micro   | True  "
            expected += u"| 06 Sep 2016 | Im Auftrag ihrer Majestät – Der Märchenstuhl\n"
            expected += u"GC5N23T | N 49°48.457, E 009°54.727 | Mystery Cache     | D 3.0 | T 4.0 | micro   | True  "
            expected += u"| 09 Jan 2017 | 67 - MedTrix - \u001a\u001a\u001a\u001a\u001a\n\n"
            expected += "\nWas moechtest du als naechstes tun?\n"
            expected += "1: Gefundene Caches auf geocaching.com loggen "
            expected += "(ueber den Upload von drafts / fieldnotes, INTERNET!!!)\n"
            expected += "2: Alle gefundenen Caches loeschen\n"
            expected += "3: zurueck\n"
            self.assertEqual(output, expected)

    def test_delete(self):
        shutil.copy2(r"..\tests\examples\not_only_found\GPX\GC1XRPM.gpx",
                     r"..\tests\examples\temp\GC1XRPM.gpx")  # copy files that are to be removed
        shutil.copy2(r"..\tests\examples\not_only_found\GPX\GC5N23T.gpx", r"..\tests\examples\temp\GC5N23T.gpx")
        shutil.copy2(r"..\tests\examples\not_only_found\geocache_visits.txt",
                     r"..\tests\examples\temp\geocache_visits.txt")
        shutil.copy2(r"..\tests\examples\not_only_found\geocache_logs.xml", r"..\tests\examples\temp\geocache_logs.xml")

        with mock.patch('__builtin__.raw_input', side_effect=["2", "y"]):
            self.x.show_founds()
            self.assertEqual(len(self.x.geocaches), 5)  # less geocaches
            self.assertFalse(os.path.isfile(r"..\tests\examples\not_only_found\geocache_visits.txt"))  # logfiles deleted
            self.assertFalse(os.path.isfile(r"..\tests\examples\not_only_found\geocache_logs.xml"))

        # move deleted files back
        shutil.move(r"..\tests\examples\temp\GC1XRPM.gpx", r"..\tests\examples\not_only_found\GPX\GC1XRPM.gpx")
        shutil.move(r"..\tests\examples\temp\GC5N23T.gpx", r"..\tests\examples\not_only_found\GPX\GC5N23T.gpx")
        shutil.move(r"..\tests\examples\temp\geocache_visits.txt", r"..\tests\examples\not_only_found\geocache_visits.txt")
        shutil.move(r"..\tests\examples\temp\geocache_logs.xml", r"..\tests\examples\not_only_found\geocache_logs.xml")


class TestShowFoundsFoundNotOnGPS(unittest.TestCase):

    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"..\tests\examples\found_not_on_gps")

    def test_show_caches(self):
        with mock.patch('__builtin__.raw_input', return_value="3"):
            out = StringIO()
            sys.stdout = out
            self.x.show_founds()
            output = out.getvalue()
            expected = u"GC5G5F5 | N 49°47.955, E 009°58.566 | Traditional Cache | D 1.5 | T 4.0 | small   | True  "
            expected += u"| 08 Oct 2016 | Urban Buildering\n\n"
            expected += "\nWas moechtest du als naechstes tun?\n"
            expected += "1: Gefundene Caches auf geocaching.com loggen "
            expected += "(ueber den Upload von drafts / fieldnotes, INTERNET!!!)\n"
            expected += "2: Alle gefundenen Caches loeschen\n"
            expected += "3: zurueck\n"
            self.assertEqual(output, expected)

    def test_delete(self):
        shutil.copy2(r"..\tests\examples\found_not_on_gps\GPX\GC5G5F5.gpx",
                     r"..\tests\examples\temp\GC5G5F5.gpx")  # copy files that are to be removed
        shutil.copy2(r"..\tests\examples\found_not_on_gps\geocache_visits.txt",
                     r"..\tests\examples\temp\geocache_visits.txt")
        shutil.copy2(r"..\tests\examples\found_not_on_gps\geocache_logs.xml", r"..\tests\examples\temp\geocache_logs.xml")

        with mock.patch('__builtin__.raw_input', side_effect=["2", "y"]):
            self.x.show_founds()
            self.assertEqual(len(self.x.geocaches), 5)  # less geocaches
            self.assertFalse(os.path.isfile(r"..\tests\examples\found_not_on_gps\geocache_visits.txt"))  # logfiles deleted
            self.assertFalse(os.path.isfile(r"..\tests\examples\found_not_on_gps\geocache_logs.xml"))

        # move deleted files back
        shutil.move(r"..\tests\examples\temp\GC5G5F5.gpx", r"..\tests\examples\found_not_on_gps\GPX\GC5G5F5.gpx")
        shutil.move(r"..\tests\examples\temp\geocache_visits.txt",
                    r"..\tests\examples\found_not_on_gps\geocache_visits.txt")
        shutil.move(r"..\tests\examples\temp\geocache_logs.xml", r"..\tests\examples\found_not_on_gps\geocache_logs.xml")


class TestDelete(unittest.TestCase):

    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"..\tests\examples\no_logfile")

    def test_not_delete(self):
        cache = geocache.Geocache(r"..\tests\examples\no_logfile\GPX\GC5N23T.gpx")
        with mock.patch('__builtin__.raw_input', return_value="anything_except_for_y"):
            self.x.delete([cache])
            self.assertEqual(len(self.x.geocaches), 6)

    def test_delete_one(self):
        cache = geocache.Geocache(r"..\tests\examples\no_logfile\GPX\GC5N23T.gpx")
        shutil.copy2(r"..\tests\examples\no_logfile\GPX\GC5N23T.gpx",
                     r"..\tests\examples\temp\GC5N23T.gpx")  # copy file that is to be removed
        with mock.patch('__builtin__.raw_input', return_value="y"):
            self.x.delete([cache])
            self.assertEqual(len(self.x.geocaches), 5)
            self.assertFalse(os.path.isfile(r"..\tests\examples\no_logfile\GPX\GC5N23T.gpx"))
        # move deleted file back
        shutil.move(r"..\tests\examples\temp\GC5N23T.gpx", r"..\tests\examples\no_logfile\GPX\GC5N23T.gpx")

    def test_delete_more_than_one(self):
        cache1 = geocache.Geocache(r"..\tests\examples\no_logfile\GPX\GC5N23T.gpx")
        cache2 = geocache.Geocache(r"..\tests\examples\no_logfile\GPX\GC1XRPM.gpx")
        shutil.copy2(r"..\tests\examples\no_logfile\GPX\GC5N23T.gpx",
                     r"..\tests\examples\temp\GC5N23T.gpx")  # copy files that are to be removed
        shutil.copy2(r"..\tests\examples\no_logfile\GPX\GC1XRPM.gpx", r"..\tests\examples\temp\GC1XRPM.gpx")
        with mock.patch('__builtin__.raw_input', return_value="y"):
            self.x.delete([cache1, cache2])
            self.assertEqual(len(self.x.geocaches), 4)
            self.assertFalse(os.path.isfile(r"..\tests\examples\no_logfile\GPX\GC5N23T.gpx"))
            self.assertFalse(os.path.isfile(r"..\tests\examples\no_logfile\GPX\GC1XRPM.gpx"))
        # move deleted files back
        shutil.move(r"..\tests\examples\temp\GC5N23T.gpx", r"..\tests\examples\no_logfile\GPX\GC5N23T.gpx")
        shutil.move(r"..\tests\examples\temp\GC1XRPM.gpx", r"..\tests\examples\no_logfile\GPX\GC1XRPM.gpx")

    def test_bullshit_cachelist_gives_error(self):
        with mock.patch('__builtin__.raw_input', return_value="y"):
            self.assertRaises(AttributeError, self.x.delete, [42, "hallo"])


class TestShowWaypoints(unittest.TestCase):

    def test_no_waypoints(self):
        x = gpscontent.GPSContent(r"..\tests\examples\no_logfile")
        out = StringIO()
        sys.stdout = out
        x.show_waypoints()
        output = out.getvalue()
        expected = "Keine Wegpunkte auf dem Geraet.\n"
        self.assertEqual(output, expected)

    def test_waypoints(self):
        with mock.patch('__builtin__.raw_input', return_value=["n"]):
            x = gpscontent.GPSContent(r"..\tests\examples\no_logfile_waypoints")
            out = StringIO()
            sys.stdout = out
            x.show_waypoints()
            output = out.getvalue()
            expected = u"        | N 49°45.609, E 009°59.454 | BLICK ZUM RANDERSACKERER KÄPPE\n"
            expected += u"        | N 49\xb047.459, E 009\xb055.938 | DOM FINAL (GC1QNWT)\n"
            self.assertEqual(output, expected)


class TestAssignWaypoints(unittest.TestCase):
    # TODO
    pass


class TestCreateMapinfoOne(unittest.TestCase):

    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"..\tests\examples\no_logfile_waypoints")

    def test_cache_with_waypoints(self):
        for g in self.x.geocaches:
            if g.gccode == "GC1XRPM":
                self.x._create_mapinfo_one(g)
        with open("mapinfo.txt","rb") as mapinfo:
            output = mapinfo.read().decode("cp1252")
        os.remove("mapinfo.txt")
        expected = u"49.809317,9.93365 {Im Auftrag ihrer Majestät – Der Märchenstuhl} <default>\r\n"
        expected += u"49.792433,9.932233 {MÄRCHENSTUHL 2} <yellow>\r\n"
        self.assertEqual(output, expected)

    def test_yellowcache_with_waypoints(self):
        gc = geocache.Geocache(r"..\tests\examples\GC78K5W.gpx")
        w = geocache.Waypoint("wpt (GC78K5W)", [49.792433, 9.932233])
        gc.add_waypoint(w)
        self.x._create_mapinfo_one(gc)
        with open("mapinfo.txt","rb") as mapinfo:
            output = mapinfo.read().decode("cp1252")
        os.remove("mapinfo.txt")
        expected = u"49.795567,9.905717 {Cachertreffen Würzburg, die 54ste} <yellow>\r\n"
        expected += u"49.792433,9.932233 {WPT} <grey>\r\n"
        self.assertEqual(output, expected)

    def test_without_waypoints(self):
        gc = geocache.Geocache(r"..\tests\examples\GC78K5W.gpx")
        self.x._create_mapinfo_one(gc)
        with open("mapinfo.txt", "rb") as mapinfo:
            output = mapinfo.read().decode("cp1252")
        os.remove("mapinfo.txt")
        expected = u"49.795567,9.905717 {Cachertreffen Würzburg, die 54ste} <yellow>\r\n"
        self.assertEqual(output, expected)

    # TODO: other colors


def create_testsuite():
    """creates a testsuite with out of all tests in this file"""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestInitNoLogfile))
    suite.addTest(unittest.makeSuite(TestInitWaypoints))
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
    suite.addTest(unittest.makeSuite(TestReadWaypoints))
    suite.addTest(unittest.makeSuite(TestSortAndShowCaches))
    suite.addTest(unittest.makeSuite(TestShowAll))
    suite.addTest(unittest.makeSuite(TestShowAllDist))
    suite.addTest(unittest.makeSuite(TestReadCache))
    suite.addTest(unittest.makeSuite(TestShowOne))
    suite.addTest(unittest.makeSuite(TestShowGCSelection))
    suite.addTest(unittest.makeSuite(TestShowGCSelectionDist))
    suite.addTest(unittest.makeSuite(TestSearch))
    suite.addTest(unittest.makeSuite(TestShowFoundsNoFoundCaches))
    suite.addTest(unittest.makeSuite(TestShowFoundsOnlyFound))
    suite.addTest(unittest.makeSuite(TestShowFoundsOnlyNotFound))
    suite.addTest(unittest.makeSuite(TestShowFoundsNotOnlyFound))
    suite.addTest(unittest.makeSuite(TestShowFoundsFoundNotOnGPS))
    suite.addTest(unittest.makeSuite(TestDelete))
    suite.addTest(unittest.makeSuite(TestShowWaypoints))
    suite.addTest(unittest.makeSuite(TestAssignWaypoints))
    suite.addTest(unittest.makeSuite(TestCreateMapinfoOne))
    return suite


def main(v):
    """runs the testsuite"""
    return test_frame.run(v, create_testsuite, "gpscontent.py")


if __name__ == '__main__':
    if len(sys.argv) > 1:  # if script is run with argument
        verbosity = int(sys.argv[1])
    else:  # if no argument -> verbosity 1
        verbosity = 1
    main(verbosity)
