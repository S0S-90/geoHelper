#!/usr/bin/python
# -*- coding: utf-8 -*-

"""tests for gpscontent.py"""

import unittest
from unittest import mock
import sys
import shutil
import os
import platform
import time
from io import StringIO
import xml.etree.ElementTree as ElementTree

import test_frame
import ownfunctions
import geocache
import gpscontent


class TestInitNoLogfile(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"../tests/examples/no_logfile")

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
        self.x = gpscontent.GPSContent(r"../tests/examples/no_logfile_waypoints")

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
        self.x = gpscontent.GPSContent(r"../tests/examples/only_found")

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
        self.x = gpscontent.GPSContent(r"../tests/examples/only_notfound")

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
        self.x = gpscontent.GPSContent(r"../tests/examples/not_only_found")

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


class TestInitNotOnlyFoundNoBOM(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"../tests/examples/not_only_found_no_BOM")

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
        self.x = gpscontent.GPSContent(r"../tests/examples/found_not_on_gps")

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
        self.x = gpscontent.GPSContent(r"../tests/examples/not_found_not_on_gps")

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
        self.x = gpscontent.GPSContent(r"../tests/examples/error_in_gpx")

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
        self.x = gpscontent.GPSContent(r"../tests/examples/only_found")

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
        self.x = gpscontent.GPSContent(r"../tests/examples/not_only_found")

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


class TestGetLoggedAndFoundCachesNotOnlyFoundNoBOM(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"../tests/examples/not_only_found_no_BOM")

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
        self.x = gpscontent.GPSContent(r"../tests/examples/only_notfound")

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
        self.x = gpscontent.GPSContent(r"../tests/examples/found_not_on_gps")

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
        self.x = gpscontent.GPSContent(r"../tests/examples/not_found_not_on_gps")

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
        self.x = gpscontent.GPSContent(r"../tests/examples/no_logfile_waypoints")

    def test_readfile(self):
        wpts = self.x._read_waypoints(r"../tests/examples/no_logfile_waypoints/GPX/Wegpunkte_14-JAN-17.gpx")
        self.assertEqual(len(wpts), 1)  # reads only the waypoint that does not belong to a cache

    def test_broken_wptfile(self):
        exception = False  # has to be that complicated because ParseError unknown
        try:
            self.x._read_waypoints(r"../tests/examples/no_logfile_waypoints/GPX/Wegpunkte_08-OKT-16.gpx")
        except ElementTree.ParseError:
            exception = True
        self.assertTrue(exception)


class TestSortAndShowCaches(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"../tests/examples/no_logfile")

    def test_gccode_up(self):
        with mock.patch('builtins.input', side_effect=['1', '1']):
            expected = ["GC1XRPM", "GC33QGC", "GC5N23T", "GC6K86W", "GC6RNTX", "GCJJ20"]
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            self.assertEqual(sorted_caches, expected)

    def test_gccode_down(self):
        with mock.patch('builtins.input', side_effect=['1', '2']):
            expected = ["GCJJ20", "GC6RNTX", "GC6K86W", "GC5N23T", "GC33QGC", "GC1XRPM"]
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            self.assertEqual(sorted_caches, expected)

    def test_name_up(self):
        with mock.patch('builtins.input', side_effect=['2', '1']):
            expected = ["GC5N23T", "GC6RNTX", "GC1XRPM", "GC6K86W", "GC33QGC", "GCJJ20"]
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            self.assertEqual(sorted_caches, expected)

    def test_name_down(self):
        with mock.patch('builtins.input', side_effect=['2', '2']):
            expected = ["GCJJ20", "GC33QGC", "GC6K86W", "GC1XRPM", "GC6RNTX", "GC5N23T"]
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            self.assertEqual(sorted_caches, expected)

    def test_type_up(self):
        with mock.patch('builtins.input', side_effect=['3', '1']):
            expected = None
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            if platform.system() == "Windows":
                expected = ["GC1XRPM", "GC5N23T", "GC6RNTX", "GC33QGC", "GC6K86W", "GCJJ20"]
            elif platform.system() == "Linux":
                expected = ['GC1XRPM', 'GC5N23T', 'GC6RNTX', 'GC6K86W', 'GC33QGC', 'GCJJ20']
            self.assertEqual(sorted_caches, expected)

    def test_type_down(self):
        with mock.patch('builtins.input', side_effect=['3', '2']):
            expected = None
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            if platform.system() == "Windows":
                expected = ["GCJJ20", "GC33QGC", "GC6K86W", "GC5N23T", "GC6RNTX", "GC1XRPM"]
            elif platform.system() == "Linux":
                expected = ['GCJJ20', 'GC6K86W', 'GC33QGC', 'GC5N23T', 'GC6RNTX', 'GC1XRPM']
            self.assertEqual(sorted_caches, expected)

    def test_difficulty_up(self):
        with mock.patch('builtins.input', side_effect=['4', '1']):
            expected = None
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            if platform.system() == "Windows":
                expected = ["GCJJ20", "GC33QGC", "GC6K86W", "GC6RNTX", "GC1XRPM", "GC5N23T"]
            elif platform.system() == "Linux":
                expected = ['GCJJ20', 'GC6K86W', 'GC6RNTX', 'GC33QGC', 'GC1XRPM', 'GC5N23T']
            self.assertEqual(sorted_caches, expected)

    def test_difficulty_down(self):
        with mock.patch('builtins.input', side_effect=['4', '2']):
            expected = None
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            if platform.system() == "Windows":
                expected = ["GC5N23T", "GC1XRPM", "GC33QGC", "GC6K86W", "GC6RNTX", "GCJJ20"]
            elif platform.system() == "Linux":
                expected = ['GC5N23T', 'GC1XRPM', 'GC6K86W', 'GC6RNTX', 'GC33QGC', 'GCJJ20']
            self.assertEqual(sorted_caches, expected)

    def test_terrain_up(self):
        with mock.patch('builtins.input', side_effect=['5', '1']):
            expected = ["GCJJ20", "GC6RNTX", "GC6K86W", "GC33QGC", "GC1XRPM", "GC5N23T"]
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            self.assertEqual(sorted_caches, expected)

    def test_terrain_down(self):
        with mock.patch('builtins.input', side_effect=['5', '2']):
            expected = ["GC5N23T", "GC1XRPM", "GC33QGC", "GC6K86W", "GC6RNTX", "GCJJ20"]
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            self.assertEqual(sorted_caches, expected)

    def test_size_up(self):
        with mock.patch('builtins.input', side_effect=['6', '1']):
            expected = None
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            if platform.system() == "Windows":
                expected = ["GCJJ20", "GC1XRPM", "GC5N23T", "GC6K86W", "GC6RNTX", "GC33QGC"]
            elif platform.system() == "Linux":
                expected = ['GCJJ20', 'GC1XRPM', 'GC6K86W', 'GC5N23T', 'GC6RNTX', 'GC33QGC']
            self.assertEqual(sorted_caches, expected)

    def test_size_down(self):
        with mock.patch('builtins.input', side_effect=['6', '2']):
            expected = None
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            if platform.system() == "Windows":
                expected = ["GC33QGC", "GC1XRPM", "GC5N23T", "GC6K86W", "GC6RNTX", "GCJJ20"]
            elif platform.system() == "Linux":
                expected = ['GC33QGC', 'GC1XRPM', 'GC6K86W', 'GC5N23T', 'GC6RNTX', 'GCJJ20']
            self.assertEqual(sorted_caches, expected)

    def test_downloaddate_up(self):
        with mock.patch('builtins.input', side_effect=['7', '1']):
            expected = ["GC6K86W", "GC1XRPM", "GC33QGC", "GC6RNTX", "GCJJ20", "GC5N23T"]
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            self.assertEqual(sorted_caches, expected)

    def test_downloaddate_down(self):
        with mock.patch('builtins.input', side_effect=['7', '2']):
            expected = ["GC5N23T", "GCJJ20", "GC6RNTX", "GC33QGC", "GC1XRPM", "GC6K86W"]
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            self.assertEqual(sorted_caches, expected)

    def test_available_up(self):
        with mock.patch('builtins.input', side_effect=['8', '1']):
            expected = None
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            if platform.system() == "Windows":
                expected = ["GC5N23T", "GC1XRPM", "GC33QGC", "GC6K86W", "GC6RNTX", "GCJJ20"]
            elif platform.system() == "Linux":
                expected = ['GC5N23T', 'GC1XRPM', 'GC6K86W', 'GC6RNTX', 'GC33QGC', 'GCJJ20']
            self.assertEqual(sorted_caches, expected)

    def test_available_down(self):
        with mock.patch('builtins.input', side_effect=['8', '2']):
            expected = None
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            if platform.system() == "Windows":
                expected = ["GC1XRPM", "GC33QGC", "GC6K86W", "GC6RNTX", "GCJJ20", "GC5N23T"]
            elif platform.system() == "Linux":
                expected = ['GC1XRPM', 'GC6K86W', 'GC6RNTX', 'GC33QGC', 'GCJJ20', 'GC5N23T']
            self.assertEqual(sorted_caches, expected)

    def test_distance_up(self):
        url = 'https://www.google.de/maps/place/97209+Veitsh%C3%B6chheim/@49.8414697,9.8579699,13z/data=!3m1!4b1!4m5!3m4!'
        url += '1s0x47a2915cbab1bfe3:0xdbe76ec582bb3aa5!8m2!3d49.8312701!4d9.8803666'

        with mock.patch('builtins.input', side_effect=['9', '1', url]):
            expected = ["GC5N23T", "GC1XRPM", "GCJJ20", "GC6RNTX", "GC6K86W", "GC33QGC"]
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            self.assertEqual(sorted_caches, expected)

    def test_distance_down(self):
        url = 'https://www.google.de/maps/place/97209+Veitsh%C3%B6chheim/@49.8414697,9.8579699,13z/data=!3m1!4b1!4m5!'
        url += '3m4!1s0x47a2915cbab1bfe3:0xdbe76ec582bb3aa5!8m2!3d49.8312701!4d9.8803666'

        with mock.patch('builtins.input', side_effect=['9', '2', url]):
            expected = ["GC33QGC", "GC6K86W", "GC6RNTX", "GCJJ20", "GC1XRPM", "GC5N23T"]
            self.x.sort_and_show_caches()
            sorted_caches = []
            for g in self.x.geocaches:
                sorted_caches.append(g.gccode)
            self.assertEqual(sorted_caches, expected)


class TestShowAll(unittest.TestCase):
    def test_show_nothing(self):
        x = gpscontent.GPSContent(r"../tests/examples/empty")
        self.assertEqual(x.show_all(), "Keine Caches auf dem Geraet.")

    def test_show_caches(self):
        x = gpscontent.GPSContent(r"../tests/examples/no_logfile")
        expected = "GC1XRPM | N 49°48.559, E 009°56.019 | Multi-cache       | D 2.5 | T 3.5 | micro   | True  | "
        expected += "06 Sep 2016 | Im Auftrag ihrer Majestät – Der Märchenstuhl\n"
        if platform.system() == "Windows":
            expected += "GC33QGC | S 43°41.726, W 066°27.090 | Traditional Cache | D 2.0 | T 3.0 | small   | "
            expected += "True  | 11 Sep 2016 | Tesoro Ameghino\n"
            expected += "GC5N23T | N 49°48.457, E 009°54.727 | Mystery Cache     | D 3.0 | T 4.0 | micro   | "
            expected += "False | 05 Mar 2017 | 67 - MedTrix - {}\n".format("\u001a" + "\u001a" + "\u001a" +
                                                                           "\u001a" + "\u001a")
        expected += "GC6K86W | N 50°19.133, E 010°11.616 | Traditional Cache | D 2.0 | T 2.0 | micro   | "
        expected += "True  | 04 Aug 2016 | Saaletalblick\n"
        if platform.system() == "Linux":
            expected += "GC5N23T | N 49°48.457, E 009°54.727 | Mystery Cache     | D 3.0 | T 4.0 | micro   | "
            expected += "False | 05 Mar 2017 | 67 - MedTrix - {}\n".format("\u001a" + "\u001a" + "\u001a" +
                                                                           "\u001a" + "\u001a")
        expected += "GC6RNTX | N 49°47.670, E 009°56.456 | Mystery Cache     | D 2.0 | T 1.5 | micro   | "
        expected += "True  | 08 Oct 2016 | Hochschule für Musik 1\n"
        if platform.system() == "Linux":
            expected += "GC33QGC | S 43°41.726, W 066°27.090 | Traditional Cache | D 2.0 | T 3.0 | small   | "
            expected += "True  | 11 Sep 2016 | Tesoro Ameghino\n"
        expected += "GCJJ20  | N 49°47.688, E 009°55.816 | Unknown Type      | D 1.0 | T 1.0 | other   | "
        expected += "True  | 29 Oct 2016 | Wuerzburger webcam\n"
        self.assertEqual(x.show_all(), expected)

    def test_show_caches_with_waypoints(self):
        x = gpscontent.GPSContent(r"../tests/examples/no_logfile_waypoints")
        expected = "GC1XRPM | N 49°48.559, E 009°56.019 | Multi-cache       | D 2.5 | T 3.5 | micro   | True  | "
        expected += "06 Sep 2016 | Im Auftrag ihrer Majestät – Der Märchenstuhl\n"
        expected += "        | N 49°47.546, E 009°55.934 | MÄRCHENSTUHL 2 (1.9km)\n"
        if platform.system() == "Windows":
            expected += "GC33QGC | S 43°41.726, W 066°27.090 | Traditional Cache | D 2.0 | T 3.0 | small   | "
            expected += "True  | 11 Sep 2016 | Tesoro Ameghino\n"
            expected += "GC5N23T | N 49°48.457, E 009°54.727 | Mystery Cache     | D 3.0 | T 4.0 | micro   | "
            expected += "False | 05 Mar 2017 | 67 - MedTrix - {}\n".format("\u001a" + "\u001a" + "\u001a" +
                                                                           "\u001a" + "\u001a")
        expected += "GC6K86W | N 50°19.133, E 010°11.616 | Traditional Cache | D 2.0 | T 2.0 | micro   | "
        expected += "True  | 04 Aug 2016 | Saaletalblick\n"
        if platform.system() == "Linux":
            expected += "GC5N23T | N 49°48.457, E 009°54.727 | Mystery Cache     | D 3.0 | T 4.0 | micro   | "
            expected += "False | 05 Mar 2017 | 67 - MedTrix - {}\n".format("\u001a" + "\u001a" + "\u001a" +
                                                                           "\u001a" + "\u001a")
        expected += "GC6RNTX | N 49°47.670, E 009°56.456 | Mystery Cache     | D 2.0 | T 1.5 | micro   | "
        expected += "True  | 08 Oct 2016 | Hochschule für Musik 1\n"
        if platform.system() == "Linux":
            expected += "GC33QGC | S 43°41.726, W 066°27.090 | Traditional Cache | D 2.0 | T 3.0 | small   | "
            expected += "True  | 11 Sep 2016 | Tesoro Ameghino\n"
        expected += "GCJJ20  | N 49°47.688, E 009°55.816 | Unknown Type      | D 1.0 | T 1.0 | other   | "
        expected += "True  | 29 Oct 2016 | Wuerzburger webcam\n"
        self.assertEqual(x.show_all(), expected)


class TestShowAllDist(unittest.TestCase):
    def test_show_nothing(self):
        x = gpscontent.GPSContent(r"../tests/examples/empty")
        self.assertEqual(x.show_all(), "Keine Caches auf dem Geraet.")

    def test_show_caches(self):
        x = gpscontent.GPSContent(r"../tests/examples/no_logfile")
        for gc in x.geocaches:
            gc.distance = ownfunctions.calculate_distance(gc.coordinates, [49.8414697, 9.8579699])
        expected = "    6.5km | GC1XRPM | N 49°48.559, E 009°56.019 | Multi-cache       | D 2.5 | T 3.5 | micro   | "
        expected += "True  | 06 Sep 2016 | Im Auftrag ihrer Majestät – Der Märchenstuhl\n"
        if platform.system() == "Windows":
            expected += "12746.3km | GC33QGC | S 43°41.726, W 066°27.090 | Traditional Cache | D 2.0 | T 3.0 | small   | "
            expected += "True  | 11 Sep 2016 | Tesoro Ameghino\n"
            expected += "    5.4km | GC5N23T | N 49°48.457, E 009°54.727 | Mystery Cache     | D 3.0 | T 4.0 | micro   | "
            expected += "False | 05 Mar 2017 | 67 - MedTrix - {}\n".format("\u001a" + "\u001a" + "\u001a" +
                                                                           "\u001a" + "\u001a")
        expected += "   58.2km | GC6K86W | N 50°19.133, E 010°11.616 | Traditional Cache | D 2.0 | T 2.0 | micro   "
        expected += "| True  | 04 Aug 2016 | Saaletalblick\n"
        if platform.system() == "Linux":
            expected += "    5.4km | GC5N23T | N 49°48.457, E 009°54.727 | Mystery Cache     | D 3.0 | T 4.0 | micro   | "
            expected += "False | 05 Mar 2017 | 67 - MedTrix - {}\n".format("\u001a" + "\u001a" + "\u001a" +
                                                                           "\u001a" + "\u001a")
        expected += "    7.9km | GC6RNTX | N 49°47.670, E 009°56.456 | Mystery Cache     | D 2.0 | T 1.5 | micro   "
        expected += "| True  | 08 Oct 2016 | Hochschule für Musik 1\n"
        if platform.system() == "Linux":
            expected += "12746.3km | GC33QGC | S 43°41.726, W 066°27.090 | Traditional Cache | D 2.0 | T 3.0 | small   | "
            expected += "True  | 11 Sep 2016 | Tesoro Ameghino\n"
        expected += "    7.3km | GCJJ20  | N 49°47.688, E 009°55.816 | Unknown Type      | D 1.0 | T 1.0 | other   "
        expected += "| True  | 29 Oct 2016 | Wuerzburger webcam\n"
        self.assertEqual(x.show_all_dist(), expected)

    def test_show_caches_with_waypoints(self):
        x = gpscontent.GPSContent(r"../tests/examples/no_logfile_waypoints")
        for gc in x.geocaches:
            gc.distance = ownfunctions.calculate_distance(gc.coordinates, [49.8414697, 9.8579699])
        expected = "    6.5km | GC1XRPM | N 49°48.559, E 009°56.019 | Multi-cache       | D 2.5 | T 3.5 | micro   | "
        expected += "True  | 06 Sep 2016 | Im Auftrag ihrer Majestät – Der Märchenstuhl\n"
        expected += "                    | N 49°47.546, E 009°55.934 | MÄRCHENSTUHL 2 (1.9km)\n"
        if platform.system() == "Windows":
            expected += "12746.3km | GC33QGC | S 43°41.726, W 066°27.090 | Traditional Cache | D 2.0 | T 3.0 | small   | "
            expected += "True  | 11 Sep 2016 | Tesoro Ameghino\n"
            expected += "    5.4km | GC5N23T | N 49°48.457, E 009°54.727 | Mystery Cache     | D 3.0 | T 4.0 | micro   | "
            expected += "False | 05 Mar 2017 | 67 - MedTrix - {}\n".format("\u001a" + "\u001a" + "\u001a" +
                                                                           "\u001a" + "\u001a")
        expected += "   58.2km | GC6K86W | N 50°19.133, E 010°11.616 | Traditional Cache | D 2.0 | T 2.0 | micro   "
        expected += "| True  | 04 Aug 2016 | Saaletalblick\n"
        if platform.system() == "Linux":
            expected += "    5.4km | GC5N23T | N 49°48.457, E 009°54.727 | Mystery Cache     | D 3.0 | T 4.0 | micro   | "
            expected += "False | 05 Mar 2017 | 67 - MedTrix - {}\n".format("\u001a" + "\u001a" + "\u001a" +
                                                                           "\u001a" + "\u001a")
        expected += "    7.9km | GC6RNTX | N 49°47.670, E 009°56.456 | Mystery Cache     | D 2.0 | T 1.5 | micro   "
        expected += "| True  | 08 Oct 2016 | Hochschule für Musik 1\n"
        if platform.system() == "Linux":
            expected += "12746.3km | GC33QGC | S 43°41.726, W 066°27.090 | Traditional Cache | D 2.0 | T 3.0 | small   | "
            expected += "True  | 11 Sep 2016 | Tesoro Ameghino\n"
        expected += "    7.3km | GCJJ20  | N 49°47.688, E 009°55.816 | Unknown Type      | D 1.0 | T 1.0 | other   "
        expected += "| True  | 29 Oct 2016 | Wuerzburger webcam\n"
        self.assertEqual(x.show_all_dist(), expected)


class TestReadCache(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"../tests/examples/no_logfile")

    def test_cache(self):
        with mock.patch('builtins.input', return_value="GC5N23T"):
            gc_return = self.x.read_cache()
            gc = geocache.Geocache(r"../tests/examples/no_logfile/GPX/GC5N23T.gpx")
            self.assertEqual(gc_return, gc)

    def test_not_existing_cache(self):
        with mock.patch('builtins.input', return_value="GC12345"):
            out = StringIO()
            sys.stdout = out
            self.x.show_one()
            output = out.getvalue()
            self.assertEqual(output, "Dieser GC-Code existiert nicht.\n")


class TestShowOne(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"../tests/examples/no_logfile_waypoints")

    def test_not_existing_cache(self):
        with mock.patch('builtins.input', return_value="GC12345"):
            out = StringIO()
            sys.stdout = out
            self.x.show_one()
            output = out.getvalue()
            self.assertEqual(output, "Dieser GC-Code existiert nicht.\n")

    def test_delete(self):
        shutil.copy2(r"../tests/examples/no_logfile_waypoints/GPX/GC5N23T.gpx",
                     r"../tests/examples/temp/GC5N23T.gpx")  # copy file that is to be removed
        with mock.patch('builtins.input', side_effect=["GC5N23T", "1", "y"]):
            with mock.patch("webbrowser.open_new_tab"):
                self.x.show_one()
            self.assertEqual(len(self.x.geocaches), 5)
        shutil.move(r"../tests/examples/temp/GC5N23T.gpx",
                    r"../tests/examples/no_logfile_waypoints/GPX/GC5N23T.gpx")  # move deleted file back to GPX folder

    def test_not_delete(self):
        with mock.patch('builtins.input', side_effect=["GC5N23T", "1", "n"]):
            with mock.patch("webbrowser.open_new_tab"):
                self.x.show_one()
            self.assertEqual(len(self.x.geocaches), 6)

    def test_delete_with_wpt(self):
        shutil.copy2(r"../tests/examples/no_logfile_waypoints/GPX/GC1XRPM.gpx",
                     r"../tests/examples/temp/GC1XRPM.gpx")  # copy file that is to be removed
        shutil.copy2(r"../tests/examples/no_logfile_waypoints/GPX/Wegpunkte_14-JAN-17.gpx",
                     r"../tests/examples/temp/Wegpunkte_14-JAN-17.gpx")  # copy waypointfile that is to be changed

        with mock.patch('builtins.input', side_effect=["GC1XRPM", "1", "y"]):
            with mock.patch("webbrowser.open_new_tab"):
                self.x.show_one()
            self.assertEqual(len(self.x.geocaches), 5)
            with open(r"../tests/examples/no_logfile_waypoints/GPX/Wegpunkte_14-JAN-17.gpx") as wptfile:
                wptfile_cont = wptfile.read()
                expected = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix'
                expected += '.com/GPX/1/1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:wptx1'
                expected += '="http://www.garmin.com/xmlschemas/WaypointExtension/v1" xmlns:gpxtpx="http://www.garmin.'
                expected += 'com/xmlschemas/TrackPointExtension/v1" creator="eTrex 10" version="1.1" xmlns:xsi="http:'
                expected += '//www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/'
                expected += '1/1 http://www.topografix.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/Gpx'
                expected += 'Extensions/v3 http://www8.garmin.com/xmlschemas/GpxExtensionsv3.xsd http://www.garmin.'
                expected += 'com/xmlschemas/WaypointExtension/v1 http://www8.garmin.com/xmlschemas/WaypointExtensionv1'
                expected += '.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.com/xml'
                expected += 'schemas/TrackPointExtensionv1.xsd"><metadata><link href="http://www.garmin.com"><text>'
                expected += 'Garmin International</text></link><time>2017-01-14T13:42:12Z</time></metadata><wpt '
                expected += 'lat="49.790983" lon="9.932300"><ele>231.912979</ele><time>2017-01-14T19:02:03Z</time>'
                expected += '<name>DOM FINAL (GC1QNWT)</name><sym>Flag, Blue</sym></wpt></gpx>'
            self.assertEqual(wptfile_cont, expected)

        shutil.move(r"../tests/examples/temp/GC1XRPM.gpx",
                    r"../tests/examples/no_logfile_waypoints/GPX/GC1XRPM.gpx")  # move deleted / modified files
        shutil.move(r"../tests/examples/temp/Wegpunkte_14-JAN-17.gpx",  # back to GPX folder
                    r"../tests/examples/no_logfile_waypoints/GPX/Wegpunkte_14-JAN-17.gpx")


class TestShowGCSelection(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"../tests/examples/no_logfile_waypoints")

    def test_show_nothing(self):
        self.assertEqual(self.x.show_gc_selection([]), "")

    def test_show_selection(self):
        selection = self.x.geocaches[3:5]
        expected = ""
        if platform.system() == "Windows":
            expected = "GC6K86W | N 50°19.133, E 010°11.616 | Traditional Cache | D 2.0 | T 2.0 | micro   | True  | "
            expected += "04 Aug 2016 | Saaletalblick\n"
        expected += "GC6RNTX | N 49°47.670, E 009°56.456 | Mystery Cache     | D 2.0 | T 1.5 | micro   | True  | "
        expected += "08 Oct 2016 | Hochschule für Musik 1\n"
        if platform.system() == "Linux":
            expected += "GC33QGC | S 43°41.726, W 066°27.090 | Traditional Cache | D 2.0 | T 3.0 | small   | "
            expected += "True  | 11 Sep 2016 | Tesoro Ameghino\n"
        self.assertEqual(self.x.show_gc_selection(selection), expected)

    def test_show_selection_waypoint(self):
        selection = self.x.geocaches[:2]
        expected = "GC1XRPM | N 49°48.559, E 009°56.019 | Multi-cache       | D 2.5 | T 3.5 | micro   | "
        expected += "True  | 06 Sep 2016 | Im Auftrag ihrer Majestät – Der Märchenstuhl\n"
        expected += "        | N 49°47.546, E 009°55.934 | MÄRCHENSTUHL 2 (1.9km)\n"
        if platform.system() == "Windows":
            expected += "GC33QGC | S 43°41.726, W 066°27.090 | Traditional Cache | D 2.0 | T 3.0 | small   | "
            expected += "True  | 11 Sep 2016 | Tesoro Ameghino\n"
        elif platform.system() == "Linux":
            expected += "GC6K86W | N 50°19.133, E 010°11.616 | Traditional Cache | D 2.0 | T 2.0 | micro   "
            expected += "| True  | 04 Aug 2016 | Saaletalblick\n"
        self.assertEqual(self.x.show_gc_selection(selection), expected)

    def test_bullshitlist(self):
        selection = ["13", 6]
        self.assertRaises(TypeError, self.x.show_gc_selection, selection)


class TestShowGCSelectionDist(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"../tests/examples/no_logfile_waypoints")
        for gc in self.x.geocaches:
            gc.distance = ownfunctions.calculate_distance(gc.coordinates, [49.8414697, 9.8579699])

    def test_show_nothing(self):
        self.assertEqual(self.x.show_gc_selection_dist([]), "")

    def test_show_selection(self):
        selection = self.x.geocaches[3:5]
        expected = ""
        if platform.system() == "Windows":
            expected = "   58.2km | GC6K86W | N 50°19.133, E 010°11.616 | Traditional Cache | D 2.0 | T 2.0 | micro   | "
            expected += "True  | 04 Aug 2016 | Saaletalblick\n"
        expected += "    7.9km | GC6RNTX | N 49°47.670, E 009°56.456 | Mystery Cache     | D 2.0 | T 1.5 | micro   "
        expected += "| True  | 08 Oct 2016 | Hochschule für Musik 1\n"
        if platform.system() == "Linux":
            expected += "12746.3km | GC33QGC | S 43°41.726, W 066°27.090 | Traditional Cache | D 2.0 | T 3.0 | small   | "
            expected += "True  | 11 Sep 2016 | Tesoro Ameghino\n"
        self.assertEqual(self.x.show_gc_selection_dist(selection), expected)

    def test_show_selection_waypoints(self):
        selection = self.x.geocaches[:2]
        expected = "    6.5km | GC1XRPM | N 49°48.559, E 009°56.019 | Multi-cache       | D 2.5 | T 3.5 | micro   | "
        expected += "True  | 06 Sep 2016 | Im Auftrag ihrer Majestät – Der Märchenstuhl\n"
        expected += "                    | N 49°47.546, E 009°55.934 | MÄRCHENSTUHL 2 (1.9km)\n"
        if platform.system() == "Windows":
            expected += "12746.3km | GC33QGC | S 43°41.726, W 066°27.090 | Traditional Cache | D 2.0 | T 3.0 | small   | "
            expected += "True  | 11 Sep 2016 | Tesoro Ameghino\n"
        elif platform.system() == "Linux":
            expected += "   58.2km | GC6K86W | N 50°19.133, E 010°11.616 | Traditional Cache | D 2.0 | T 2.0 | micro   "
            expected += "| True  | 04 Aug 2016 | Saaletalblick\n"
        self.assertEqual(self.x.show_gc_selection_dist(selection), expected)

    def test_bullshitlist(self):
        selection = ["13", 6]
        self.assertRaises(TypeError, self.x.show_gc_selection_dist, selection)


class TestSearch(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"../tests/examples/no_logfile")

    def test_name(self):
        with mock.patch('builtins.input', side_effect=["1", "A"]):
            expected = None
            if platform.system() == "Windows":
                expected = [self.x.geocaches[0], self.x.geocaches[1]]
            elif platform.system() == "Linux":
                expected = [self.x.geocaches[0], self.x.geocaches[4]]
            self.assertEqual(self.x.search(), expected)

    def test_description(self):
        with mock.patch('builtins.input', side_effect=["2", "ist"]):
            expected = None
            if platform.system() == "Windows":
                expected = [self.x.geocaches[0], self.x.geocaches[1], self.x.geocaches[2], self.x.geocaches[5]]
            elif platform.system() == "Linux":
                expected = [self.x.geocaches[0], self.x.geocaches[4], self.x.geocaches[2], self.x.geocaches[5]]
            self.assertEqual(self.x.search(), expected)

    def test_cachetype(self):
        with mock.patch('builtins.input', side_effect=["3", "Mystery Cache"]):
            expected = None
            if platform.system() == "Windows":
                expected = [self.x.geocaches[2], self.x.geocaches[4]]
            elif platform.system() == "Linux":
                expected = [self.x.geocaches[2], self.x.geocaches[3]]
            self.assertEqual(self.x.search(), expected)

    def test_cachetype_invalid(self):
        with mock.patch('builtins.input', side_effect=["3", "Mystery"]):
            self.assertEqual(self.x.search(), [])

    def test_difficulty(self):
        with mock.patch('builtins.input', side_effect=["4", "2, 2.5"]):
            expected = [self.x.geocaches[0], self.x.geocaches[1], self.x.geocaches[3], self.x.geocaches[4]]
            self.assertEqual(self.x.search(), expected)

    def test_difficulty_without_space(self):
        with mock.patch('builtins.input', side_effect=["4", "2,2.5"]):
            expected = [self.x.geocaches[0], self.x.geocaches[1], self.x.geocaches[3], self.x.geocaches[4]]
            self.assertEqual(self.x.search(), expected)

    def test_difficulty_error(self):
        with mock.patch('builtins.input', side_effect=["4", "2.5,2"]):
            self.assertEqual(self.x.search(), [])

    def test_difficulty_error2(self):
        with mock.patch('builtins.input', side_effect=["4", "2.5,7"]):
            self.assertEqual(self.x.search(), [])

    def test_terrain(self):
        with mock.patch('builtins.input', side_effect=["5", "1.5, 2"]):
            expected = None
            if platform.system() == "Windows":
                expected = [self.x.geocaches[3], self.x.geocaches[4]]
            elif platform.system() == "Linux":
                expected = [self.x.geocaches[1], self.x.geocaches[3]]
            self.assertEqual(self.x.search(), expected)

    def test_size(self):
        with mock.patch('builtins.input', side_effect=["6", "micro, small"]):
            expected = [self.x.geocaches[0], self.x.geocaches[1], self.x.geocaches[2], self.x.geocaches[3],
                        self.x.geocaches[4]]
            self.assertEqual(self.x.search(), expected)

    def test_size_without_space(self):
        with mock.patch('builtins.input', side_effect=["6", "micro,small"]):
            expected = [self.x.geocaches[0], self.x.geocaches[1], self.x.geocaches[2], self.x.geocaches[3],
                        self.x.geocaches[4]]
            self.assertEqual(self.x.search(), expected)

    def test_size_error(self):
        with mock.patch('builtins.input', side_effect=["6", "small, micro"]):
            self.assertEqual(self.x.search(), [])

    def test_downloaddate(self):
        with mock.patch('builtins.input', side_effect=["7", "01.10.2016, 31.10.2016"]):
            expected = None
            if platform.system() == "Windows":
                expected = [self.x.geocaches[4], self.x.geocaches[5]]
            elif platform.system() == "Linux":
                expected = [self.x.geocaches[3], self.x.geocaches[5]]
            self.assertEqual(self.x.search(), expected)

    def test_downloaddate_without_space(self):
        with mock.patch('builtins.input', side_effect=["7", "01.10.2016,31.10.2016"]):
            expected = None
            if platform.system() == "Windows":
                expected = [self.x.geocaches[4], self.x.geocaches[5]]
            elif platform.system() == "Linux":
                expected = [self.x.geocaches[3], self.x.geocaches[5]]
            self.assertEqual(self.x.search(), expected)

    def test_downloaddate_error(self):
        with mock.patch('builtins.input', side_effect=["7", "1.10.2016, 31.10.2016"]):
            self.assertEqual(self.x.search(), [])

    def test_downloaddate_error2(self):
        with mock.patch('builtins.input', side_effect=["7", "31.10.2016, 01.10.2016"]):
            self.assertEqual(self.x.search(), [])

    def test_not_available(self):
        with mock.patch('builtins.input', side_effect=["8", "n"]):
            expected = [self.x.geocaches[2]]
            self.assertEqual(self.x.search(), expected)

    def test_available(self):
        with mock.patch('builtins.input', side_effect=["8", "y"]):
            expected = [self.x.geocaches[0], self.x.geocaches[1], self.x.geocaches[3], self.x.geocaches[4],
                        self.x.geocaches[5]]
            self.assertEqual(self.x.search(), expected)

    def test_available_by_bullshit(self):
        with mock.patch('builtins.input', side_effect=["8", "dfghj"]):
            expected = [self.x.geocaches[0], self.x.geocaches[1], self.x.geocaches[3], self.x.geocaches[4],
                        self.x.geocaches[5]]
            self.assertEqual(self.x.search(), expected)

    def test_attributes(self):
        with mock.patch('builtins.input', side_effect=["9", "available 24-7"]):
            expected = None
            if platform.system() == "Windows":
                expected = [self.x.geocaches[2], self.x.geocaches[4], self.x.geocaches[5]]
            elif platform.system() == "Linux":
                expected = [self.x.geocaches[2], self.x.geocaches[3], self.x.geocaches[5]]
            self.assertEqual(self.x.search(), expected)

    def test_attributes_that_doesnt_exist(self):
        with mock.patch('builtins.input', side_effect=["9", "No attributes specified by the author"]):
            self.assertEqual(self.x.search(), [])

    def test_distance(self):
        url = "https://www.google.de/maps/place/97209+Veitsh%C3%B6chheim/@49.8414697,9.8579699,13z/data=!3m1!4b1!4m5!3m4"
        url += "!1s0x47a2915cbab1bfe3:0xdbe76ec582bb3aa5!8m2!3d49.8312701!4d9.8803666"

        with mock.patch('builtins.input', side_effect=["10", url, "6.4, 7.4"]):
            expected = [self.x.geocaches[0], self.x.geocaches[5]]
            self.assertEqual(self.x.search(), expected)

    def test_distance_without_space(self):
        url = "https://www.google.de/maps/place/97209+Veitsh%C3%B6chheim/@49.8414697,9.8579699,13z/data=!3m1!4b1!4m5!3m4"
        url += "!1s0x47a2915cbab1bfe3:0xdbe76ec582bb3aa5!8m2!3d49.8312701!4d9.8803666"

        with mock.patch('builtins.input', side_effect=["10", url, "6.4,7.4"]):
            expected = [self.x.geocaches[0], self.x.geocaches[5]]
            self.assertEqual(self.x.search(), expected)

    def test_distance_error(self):
        url = "https://www.gooe/maps/place/97209+Veitsh%C3%B6chheim/@49.8414697,9.8579699,13z/data=!3m1!4b1!4m5!3m4!"
        url += "1s0x47a2915cbab1bfe3:0xdbe76ec582bb3aa5!8m2!3d49.8312701!4d9.8803666"

        with mock.patch('builtins.input', side_effect=["10", url, "6.4,7.4"]):
            self.assertEqual(self.x.search(), [])

    def test_distance_error2(self):
        url = "https://www.google.de/maps/place/97209+Veitsh%C3%B6chheim/@49.8414697,9.8579699,13z/data=!3m1!4b1!4m5!"
        url += "3m4!1s0x47a2915cbab1bfe3:0xdbe76ec582bb3aa5!8m2!3d49.8312701!4d9.8803666"

        with mock.patch('builtins.input', side_effect=["10", url, "hh, 7.4"]):
            self.assertEqual(self.x.search(), [])

    def test_distance_error3(self):
        url = "https://www.google.de/maps/place/97209+Veitsh%C3%B6chheim/@49.8414697,9.8579699,13z/data=!3m1!4b1!4m5!"
        url += "3m4!1s0x47a2915cbab1bfe3:0xdbe76ec582bb3aa5!8m2!3d49.8312701!4d9.8803666"

        with mock.patch('builtins.input', side_effect=["10", url, "10.3, 7.4"]):
            self.assertEqual(self.x.search(), [])


class TestShowFoundsNoFoundCaches(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"../tests/examples/no_logfile")

    def test_gives_error(self):
        self.assertRaises(ValueError, self.x.show_founds)


class TestShowFoundsOnlyFound(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"../tests/examples/only_found")

    def test_show_caches(self):
        with mock.patch('builtins.input', return_value="3"):
            out = StringIO()
            sys.stdout = out
            self.x.show_founds()
            output = out.getvalue()
            expected = "GC1XRPM | N 49°48.559, E 009°56.019 | Multi-cache       | D 2.5 | T 3.5 | micro   | True  "
            expected += "| 06 Sep 2016 | Im Auftrag ihrer Majestät – Der Märchenstuhl\n"
            expected += "GC5G5F5 | N 49°47.955, E 009°58.566 | Traditional Cache | D 1.5 | T 4.0 | small   | True  "
            expected += "| 08 Oct 2016 | Urban Buildering\n\n"
            expected += "\nWas moechtest du als naechstes tun?\n"
            expected += "1: Gefundene Caches auf geocaching.com loggen "
            expected += "(ueber den Upload von drafts / fieldnotes, INTERNET!!!)\n"
            expected += "2: Alle gefundenen Caches loeschen\n"
            expected += "3: zurueck\n"
            self.assertEqual(output, expected)

    def test_delete(self):
        shutil.copy2(r"../tests/examples/only_found/GPX/GC1XRPM.gpx",
                     r"../tests/examples/temp/GC1XRPM.gpx")  # copy files that are to be removed
        shutil.copy2(r"../tests/examples/only_found/GPX/GC5G5F5.gpx", r"../tests/examples/temp/GC5G5F5.gpx")
        shutil.copy2(r"../tests/examples/only_found/geocache_visits.txt", r"../tests/examples/temp/geocache_visits.txt")
        shutil.copy2(r"../tests/examples/only_found/geocache_logs.xml", r"../tests/examples/temp/geocache_logs.xml")

        with mock.patch('builtins.input', side_effect=["2", "y"]):
            self.x.show_founds()
            self.assertEqual(len(self.x.geocaches), 5)  # less geocaches
            self.assertFalse(os.path.isfile(r"../tests/examples/only_found/geocache_visits.txt"))  # logfiles deleted
            self.assertFalse(os.path.isfile(r"../tests/examples/only_found/geocache_logs.xml"))

        # move deleted files back
        shutil.move(r"../tests/examples/temp/GC1XRPM.gpx", r"../tests/examples/only_found/GPX/GC1XRPM.gpx")
        shutil.move(r"../tests/examples/temp/GC5G5F5.gpx", r"../tests/examples/only_found/GPX/GC5G5F5.gpx")
        shutil.move(r"../tests/examples/temp/geocache_visits.txt", r"../tests/examples/only_found/geocache_visits.txt")
        shutil.move(r"../tests/examples/temp/geocache_logs.xml", r"../tests/examples/only_found/geocache_logs.xml")


class TestShowFoundsOnlyNotFound(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"../tests/examples/only_notfound")

    def test_gives_error(self):
        self.assertRaises(ValueError, self.x.show_founds)


class TestShowFoundsNotOnlyFound(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"../tests/examples/not_only_found")

    def test_show_caches(self):
        with mock.patch('builtins.input', return_value="3"):
            out = StringIO()
            sys.stdout = out
            self.x.show_founds()
            output = out.getvalue()
            expected = "GC1XRPM | N 49°48.559, E 009°56.019 | Multi-cache       | D 2.5 | T 3.5 | micro   | True  "
            expected += "| 06 Sep 2016 | Im Auftrag ihrer Majestät – Der Märchenstuhl\n"
            expected += "GC5N23T | N 49°48.457, E 009°54.727 | Mystery Cache     | D 3.0 | T 4.0 | micro   | True  "
            expected += "| 09 Jan 2017 | 67 - MedTrix - \u001a\u001a\u001a\u001a\u001a\n\n"
            expected += "\nWas moechtest du als naechstes tun?\n"
            expected += "1: Gefundene Caches auf geocaching.com loggen "
            expected += "(ueber den Upload von drafts / fieldnotes, INTERNET!!!)\n"
            expected += "2: Alle gefundenen Caches loeschen\n"
            expected += "3: zurueck\n"
            self.assertEqual(output, expected)

    def test_delete(self):
        shutil.copy2(r"../tests/examples/not_only_found/GPX/GC1XRPM.gpx",
                     r"../tests/examples/temp/GC1XRPM.gpx")  # copy files that are to be removed
        shutil.copy2(r"../tests/examples/not_only_found/GPX/GC5N23T.gpx", r"../tests/examples/temp/GC5N23T.gpx")
        shutil.copy2(r"../tests/examples/not_only_found/geocache_visits.txt",
                     r"../tests/examples/temp/geocache_visits.txt")
        shutil.copy2(r"../tests/examples/not_only_found/geocache_logs.xml", r"../tests/examples/temp/geocache_logs.xml")

        with mock.patch('builtins.input', side_effect=["2", "y"]):
            self.x.show_founds()
            self.assertEqual(len(self.x.geocaches), 5)  # less geocaches
            self.assertFalse(os.path.isfile(r"../tests/examples/not_only_found/geocache_visits.txt"))  # logfiles deleted
            self.assertFalse(os.path.isfile(r"../tests/examples/not_only_found/geocache_logs.xml"))

        # move deleted files back
        shutil.move(r"../tests/examples/temp/GC1XRPM.gpx", r"../tests/examples/not_only_found/GPX/GC1XRPM.gpx")
        shutil.move(r"../tests/examples/temp/GC5N23T.gpx", r"../tests/examples/not_only_found/GPX/GC5N23T.gpx")
        shutil.move(r"../tests/examples/temp/geocache_visits.txt", r"../tests/examples/not_only_found/geocache_visits.txt")
        shutil.move(r"../tests/examples/temp/geocache_logs.xml", r"../tests/examples/not_only_found/geocache_logs.xml")


class TestShowFoundsOnlyFoundWaypoints(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"../tests/examples/only_found_waypoints")

    def test_show_caches(self):
        with mock.patch('builtins.input', return_value="3"):
            out = StringIO()
            sys.stdout = out
            self.x.show_founds()
            output = out.getvalue()
            expected = "GC1XRPM | N 49°48.559, E 009°56.019 | Multi-cache       | D 2.5 | T 3.5 | micro   | True  "
            expected += "| 06 Sep 2016 | Im Auftrag ihrer Majestät – Der Märchenstuhl\n"
            expected += "        | N 49°47.546, E 009°55.934 | MÄRCHENSTUHL 2 (1.9km)\n"
            expected += "GC5G5F5 | N 49°47.955, E 009°58.566 | Traditional Cache | D 1.5 | T 4.0 | small   | True  "
            expected += "| 08 Oct 2016 | Urban Buildering\n\n"
            expected += "\nWas moechtest du als naechstes tun?\n"
            expected += "1: Gefundene Caches auf geocaching.com loggen "
            expected += "(ueber den Upload von drafts / fieldnotes, INTERNET!!!)\n"
            expected += "2: Alle gefundenen Caches loeschen\n"
            expected += "3: zurueck\n"
            self.assertEqual(output, expected)

    def test_delete(self):
        shutil.copy2(r"../tests/examples/only_found_waypoints/GPX/GC1XRPM.gpx",
                     r"../tests/examples/temp/GC1XRPM.gpx")  # copy files that are to be removed
        shutil.copy2(r"../tests/examples/only_found_waypoints/GPX/GC5G5F5.gpx", r"../tests/examples/temp/GC5G5F5.gpx")
        shutil.copy2(r"../tests/examples/only_found_waypoints/GPX/Wegpunkte_14-JAN-17.gpx",
                     r"../tests/examples/temp/Wegpunkte_14-JAN-17.gpx")
        shutil.copy2(r"../tests/examples/only_found_waypoints/geocache_visits.txt",
                     r"../tests/examples/temp/geocache_visits.txt")
        shutil.copy2(r"../tests/examples/only_found_waypoints/geocache_logs.xml",
                     r"../tests/examples/temp/geocache_logs.xml")

        with mock.patch('builtins.input', side_effect=["2", "y"]):
            self.x.show_founds()
            self.assertEqual(len(self.x.geocaches), 5)  # less geocaches, logfiles and waypointfile are deleted
            self.assertFalse(os.path.isfile(r"../tests/examples/only_found_waypoints/geocache_visits.txt"))
            self.assertFalse(os.path.isfile(r"../tests/examples/only_found_waypoints/geocache_logs.xml"))
            self.assertFalse(os.path.isfile(r"../tests/examples/only_found_waypoints/GPX/Wegpunkte_14-JAN-17.gpx"))

        # move deleted files back
        shutil.move(r"../tests/examples/temp/GC1XRPM.gpx", r"../tests/examples/only_found_waypoints/GPX/GC1XRPM.gpx")
        shutil.move(r"../tests/examples/temp/GC5G5F5.gpx", r"../tests/examples/only_found_waypoints/GPX/GC5G5F5.gpx")
        shutil.move(r"../tests/examples/temp/Wegpunkte_14-JAN-17.gpx",
                    r"../tests/examples/only_found_waypoints/GPX/Wegpunkte_14-JAN-17.gpx")
        shutil.move(r"../tests/examples/temp/geocache_visits.txt",
                    r"../tests/examples/only_found_waypoints/geocache_visits.txt")
        shutil.move(r"../tests/examples/temp/geocache_logs.xml",
                    r"../tests/examples/only_found_waypoints/geocache_logs.xml")


class TestShowFoundsFoundNotOnGPS(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"../tests/examples/found_not_on_gps")

    def test_show_caches(self):
        with mock.patch('builtins.input', return_value="3"):
            out = StringIO()
            sys.stdout = out
            self.x.show_founds()
            output = out.getvalue()
            expected = "GC5G5F5 | N 49°47.955, E 009°58.566 | Traditional Cache | D 1.5 | T 4.0 | small   | True  "
            expected += "| 08 Oct 2016 | Urban Buildering\n\n"
            expected += "\nWas moechtest du als naechstes tun?\n"
            expected += "1: Gefundene Caches auf geocaching.com loggen "
            expected += "(ueber den Upload von drafts / fieldnotes, INTERNET!!!)\n"
            expected += "2: Alle gefundenen Caches loeschen\n"
            expected += "3: zurueck\n"
            self.assertEqual(output, expected)

    def test_delete(self):
        shutil.copy2(r"../tests/examples/found_not_on_gps/GPX/GC5G5F5.gpx",
                     r"../tests/examples/temp/GC5G5F5.gpx")  # copy files that are to be removed
        shutil.copy2(r"../tests/examples/found_not_on_gps/geocache_visits.txt",
                     r"../tests/examples/temp/geocache_visits.txt")
        shutil.copy2(r"../tests/examples/found_not_on_gps/geocache_logs.xml", r"../tests/examples/temp/geocache_logs.xml")

        with mock.patch('builtins.input', side_effect=["2", "y"]):
            self.x.show_founds()
            self.assertEqual(len(self.x.geocaches), 5)  # less geocaches
            self.assertFalse(os.path.isfile(r"../tests/examples/found_not_on_gps/geocache_visits.txt"))  # logfiles deleted
            self.assertFalse(os.path.isfile(r"../tests/examples/found_not_on_gps/geocache_logs.xml"))

        # move deleted files back
        shutil.move(r"../tests/examples/temp/GC5G5F5.gpx", r"../tests/examples/found_not_on_gps/GPX/GC5G5F5.gpx")
        shutil.move(r"../tests/examples/temp/geocache_visits.txt",
                    r"../tests/examples/found_not_on_gps/geocache_visits.txt")
        shutil.move(r"../tests/examples/temp/geocache_logs.xml", r"../tests/examples/found_not_on_gps/geocache_logs.xml")


class TestDelete(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"../tests/examples/no_logfile_waypoints")

    def test_not_delete(self):
        cache = geocache.Geocache(r"../tests/examples/no_logfile_waypoints/GPX/GC5N23T.gpx")
        with mock.patch('builtins.input', return_value="anything_except_for_y"):
            self.x.delete([cache])
            self.assertEqual(len(self.x.geocaches), 6)

    def test_delete_one(self):
        cache = geocache.Geocache(r"../tests/examples/no_logfile_waypoints/GPX/GC5N23T.gpx")
        shutil.copy2(r"../tests/examples/no_logfile/GPX/GC5N23T.gpx",
                     r"../tests/examples/temp/GC5N23T.gpx")  # copy file that is to be removed
        with mock.patch('builtins.input', return_value="y"):
            self.x.delete([cache])
            self.assertEqual(len(self.x.geocaches), 5)
            self.assertFalse(os.path.isfile(r"../tests/examples/no_logfile_waypoints/GPX/GC5N23T.gpx"))
        # move deleted file back
        shutil.move(r"../tests/examples/temp/GC5N23T.gpx", r"../tests/examples/no_logfile_waypoints/GPX/GC5N23T.gpx")

    def test_delete_more_than_one(self):
        cache1 = geocache.Geocache(r"../tests/examples/no_logfile_waypoints/GPX/GC5N23T.gpx")
        cache2 = geocache.Geocache(r"../tests/examples/no_logfile_waypoints/GPX/GC6K86W.gpx")
        shutil.copy2(r"../tests/examples/no_logfile_waypoints/GPX/GC5N23T.gpx",
                     r"../tests/examples/temp/GC5N23T.gpx")  # copy files that are to be removed
        shutil.copy2(r"../tests/examples/no_logfile_waypoints/GPX/GC6K86W.gpx", r"../tests/examples/temp/GC6K86W.gpx")
        with mock.patch('builtins.input', return_value="y"):
            self.x.delete([cache1, cache2])
            self.assertEqual(len(self.x.geocaches), 4)
            self.assertFalse(os.path.isfile(r"../tests/examples/no_logfile_waypoints/GPX/GC5N23T.gpx"))
            self.assertFalse(os.path.isfile(r"../tests/examples/no_logfile_waypoints/GPX/GC6K86W.gpx"))
        # move deleted files back
        shutil.move(r"../tests/examples/temp/GC5N23T.gpx", r"../tests/examples/no_logfile_waypoints/GPX/GC5N23T.gpx")
        shutil.move(r"../tests/examples/temp/GC6K86W.gpx", r"../tests/examples/no_logfile_waypoints/GPX/GC6K86W.gpx")

    def test_delete_with_waypoint(self):
        cache1 = self.x.geocaches[0]  # geocaches have to be created like this because by creating them directly
        cache2 = self.x.geocaches[2]  # there are no waypoints assigned
        shutil.copy2(r"../tests/examples/no_logfile_waypoints/GPX/GC5N23T.gpx",
                     r"../tests/examples/temp/GC5N23T.gpx")  # copy files that are to be removed or modified
        shutil.copy2(r"../tests/examples/no_logfile_waypoints/GPX/GC1XRPM.gpx", r"../tests/examples/temp/GC1XRPM.gpx")
        shutil.copy2(r"../tests/examples/no_logfile_waypoints/GPX/Wegpunkte_14-JAN-17.gpx",
                     r"../tests/examples/temp/Wegpunkte_14-JAN-17.gpx")  # copy waypointfile that is to be changed
        with mock.patch('builtins.input', return_value="y"):
            self.x.delete([cache1, cache2])
            self.assertEqual(len(self.x.geocaches), 4)
            self.assertFalse(os.path.isfile(r"../tests/examples/no_logfile_waypoints/GPX/GC5N23T.gpx"))
            self.assertFalse(os.path.isfile(r"../tests/examples/no_logfile_waypoints/GPX/GC1XRPM.gpx"))
            with open(r"../tests/examples/no_logfile_waypoints/GPX/Wegpunkte_14-JAN-17.gpx") as wptfile:
                wptfile_cont = wptfile.read()
                expected = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix'
                expected += '.com/GPX/1/1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:wptx1'
                expected += '="http://www.garmin.com/xmlschemas/WaypointExtension/v1" xmlns:gpxtpx="http://www.garmin.'
                expected += 'com/xmlschemas/TrackPointExtension/v1" creator="eTrex 10" version="1.1" xmlns:xsi="http:'
                expected += '//www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/'
                expected += '1/1 http://www.topografix.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/Gpx'
                expected += 'Extensions/v3 http://www8.garmin.com/xmlschemas/GpxExtensionsv3.xsd http://www.garmin.'
                expected += 'com/xmlschemas/WaypointExtension/v1 http://www8.garmin.com/xmlschemas/WaypointExtensionv1'
                expected += '.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.com/xml'
                expected += 'schemas/TrackPointExtensionv1.xsd"><metadata><link href="http://www.garmin.com"><text>'
                expected += 'Garmin International</text></link><time>2017-01-14T13:42:12Z</time></metadata><wpt '
                expected += 'lat="49.790983" lon="9.932300"><ele>231.912979</ele><time>2017-01-14T19:02:03Z</time>'
                expected += '<name>DOM FINAL (GC1QNWT)</name><sym>Flag, Blue</sym></wpt></gpx>'
            self.assertEqual(wptfile_cont, expected)
        # move files back
        shutil.move(r"../tests/examples/temp/GC5N23T.gpx", r"../tests/examples/no_logfile_waypoints/GPX/GC5N23T.gpx")
        shutil.move(r"../tests/examples/temp/GC1XRPM.gpx", r"../tests/examples/no_logfile_waypoints/GPX/GC1XRPM.gpx")
        shutil.move(r"../tests/examples/temp/Wegpunkte_14-JAN-17.gpx",
                    r"../tests/examples/no_logfile_waypoints/GPX/Wegpunkte_14-JAN-17.gpx")

    def test_bullshit_cachelist_gives_error(self):
        with mock.patch('builtins.input', return_value="y"):
            self.assertRaises(AttributeError, self.x.delete, [42, "hallo"])


class TestShowWaypoints(unittest.TestCase):
    def test_no_waypoints(self):
        with mock.patch('builtins.input', return_value=["2"]):
            x = gpscontent.GPSContent(r"../tests/examples/no_logfile")
            out = StringIO()
            sys.stdout = out
            x.show_waypoints()
            output = out.getvalue()
            expected = "Keine Wegpunkte auf dem Geraet.\n"
            expected += "\nWas moechtest du als naechstes tun?\n"
            expected += "1: Wegpunkte hinzufuegen\n"
            expected += "2: nichts\n"
            self.assertEqual(output, expected)

    def test_waypoints(self):
        with mock.patch('builtins.input', return_value=["3"]):
            x = gpscontent.GPSContent(r"../tests/examples/no_logfile_waypoints")
            out = StringIO()
            sys.stdout = out
            x.show_waypoints()
            output = out.getvalue()
            expected = "        | N 49\xb047.459, E 009\xb055.938 | DOM FINAL (GC1QNWT)\n"
            expected += "        | N 49°45.609, E 009°59.454 | BLICK ZUM RANDERSACKERER KÄPPE\n"
            expected += "\nWas moechtest du als naechstes tun?\n"
            expected += "1: Wegpunkte hinzufuegen\n"
            expected += "2: Wegpunkte zu Geocaches zuordnen oder loeschen\n"
            expected += "3: nichts\n"
            self.assertEqual(output, expected)


class TestReplaceWaypointName(unittest.TestCase):
    def setUp(self):
        """is not used but a gpscontent has to exist in order to use class functions"""
        self.x = gpscontent.GPSContent(r"../tests/examples/no_logfile")

    def test_all_well(self):
        gc = geocache.Geocache(r"../tests/examples/GC78K5W.gpx")
        wpt = geocache.Waypoint("testwpt (GC78K5W)", [49.792433, 9.932233])
        gc.add_waypoint(wpt)

        filestring1 = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com'
        filestring1 += '/GPX/1/1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:wptx1="http://'
        filestring1 += 'www.garmin.com/xmlschemas/WaypointExtension/v1" xmlns:gpxtpx="http://www.garmin.com/xmlschemas'
        filestring1 += '/TrackPointExtension/v1" creator="eTrex 10" version="1.1" xmlns:xsi="http://www.w3.org/2001/'
        filestring1 += 'XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix'
        filestring1 += '.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www8.garmin.com/'
        filestring1 += 'xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/WaypointExtension/v1 http://'
        filestring1 += 'www8.garmin.com/xmlschemas/WaypointExtensionv1.xsd http://www.garmin.com/xmlschemas/TrackPoint'
        filestring1 += 'Extension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd"><metadata><link '
        filestring1 += 'href="http://www.garmin.com"><text>Garmin International</text></link><time>2016-10-08T13:'
        filestring1 += '26:03Z</time></metadata><wpt lat="49.794800" lon="9.941167"><time>2016-10-08T13:27:25Z</time>'
        filestring1 += '<name>TESTWPT</name><sym>Flag, Blue</sym></wpt><wpt lat="49.794800" lon="9.941167"><time>2016'
        filestring1 += '-10-08T13:27:25Z</time><name>TESTWPT FINAL</name><sym>Flag, Blue</sym></wpt></gpx>'

        filestring2 = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com'
        filestring2 += '/GPX/1/1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:wptx1="http://'
        filestring2 += 'www.garmin.com/xmlschemas/WaypointExtension/v1" xmlns:gpxtpx="http://www.garmin.com/xmlschemas'
        filestring2 += '/TrackPointExtension/v1" creator="eTrex 10" version="1.1" xmlns:xsi="http://www.w3.org/2001/'
        filestring2 += 'XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix'
        filestring2 += '.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www8.garmin.com/'
        filestring2 += 'xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/WaypointExtension/v1 http://'
        filestring2 += 'www8.garmin.com/xmlschemas/WaypointExtensionv1.xsd http://www.garmin.com/xmlschemas/TrackPoint'
        filestring2 += 'Extension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd"><metadata><link '
        filestring2 += 'href="http://www.garmin.com"><text>Garmin International</text></link><time>2016-10-08T13:'
        filestring2 += '26:03Z</time></metadata><wpt lat="49.794800" lon="9.941167"><time>2016-10-08T13:27:25Z</time>'
        filestring2 += '<name>QUACK</name><sym>Flag, Blue</sym></wpt></gpx>'

        wptfiles = [filestring1, filestring2]
        new_wptfls = self.x._replace_waypoint_name(wptfiles, wpt)

        filestring1 = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com'
        filestring1 += '/GPX/1/1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:wptx1="http://'
        filestring1 += 'www.garmin.com/xmlschemas/WaypointExtension/v1" xmlns:gpxtpx="http://www.garmin.com/xmlschemas'
        filestring1 += '/TrackPointExtension/v1" creator="eTrex 10" version="1.1" xmlns:xsi="http://www.w3.org/2001/'
        filestring1 += 'XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix'
        filestring1 += '.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www8.garmin.com/'
        filestring1 += 'xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/WaypointExtension/v1 http://'
        filestring1 += 'www8.garmin.com/xmlschemas/WaypointExtensionv1.xsd http://www.garmin.com/xmlschemas/TrackPoint'
        filestring1 += 'Extension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd"><metadata><link '
        filestring1 += 'href="http://www.garmin.com"><text>Garmin International</text></link><time>2016-10-08T13:'
        filestring1 += '26:03Z</time></metadata><wpt lat="49.794800" lon="9.941167"><time>2016-10-08T13:27:25Z</time>'
        filestring1 += '<name>TESTWPT (GC78K5W)</name><sym>Flag, Blue</sym></wpt><wpt lat="49.794800" lon="9.941167">'
        filestring1 += '<time>2016-10-08T13:27:25Z</time><name>TESTWPT FINAL</name><sym>Flag, Blue</sym></wpt></gpx>'

        expected = [filestring1, filestring2]

        self.assertEqual(new_wptfls, expected)


class TestTryCreatingWaypoints(unittest.TestCase):
    def setUp(self):
        """is not used but a gpscontent has to exist in order to use class functions"""
        self.x = gpscontent.GPSContent(r"../tests/examples/no_logfile")

    def test_all_well(self):
        wpt = self.x._try_creating_waypoint("wpt", [49.792433, 9.932233])
        self.assertEqual(wpt.name, "WPT")
        self.assertEqual(wpt.coordinates, [49.792433, 9.932233])

    def test_invalid_coordinates(self):
        out = StringIO()
        sys.stdout = out
        w = self.x._try_creating_waypoint("wpt", "blub")
        output = out.getvalue()
        self.assertIsNone(w)
        self.assertEqual(output, "Koordinaten fehlerhaft. Kein Wegpunkt wurde erstellt.\n")

    def test_name_too_long(self):
        out = StringIO()
        sys.stdout = out
        w = self.x._try_creating_waypoint("wptqwertzuiopülkjhgfdsxcvbnmrwq8tho4ghfbwqufib32fboaes", [49.792433, 9.932233])
        output = out.getvalue()
        self.assertIsNone(w)
        self.assertEqual(output, "Name zu lang. Kein Wegpunkt wurde erstellt.\n")

    def test_sign_not_allowed(self):
        out = StringIO()
        sys.stdout = out
        w = self.x._try_creating_waypoint("s°s", [49.792433, 9.932233])
        output = out.getvalue()
        self.assertIsNone(w)
        self.assertEqual(output, "Name enthaelt ungueltige Zeichen. Kein Wegpunkt wurde erstellt.\n")


class TestDeleteWaypointFromFiles(unittest.TestCase):
    def setUp(self):
        """is not used but a gpscontent has to exist in order to use class functions"""
        self.x = gpscontent.GPSContent(r"../tests/examples/no_logfile")

    def test_only_one_wpt_in_file(self):
        wpt = geocache.Waypoint("testwpt", [49.792433, 9.932233])

        filestring1 = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com'
        filestring1 += '/GPX/1/1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:wptx1="http://'
        filestring1 += 'www.garmin.com/xmlschemas/WaypointExtension/v1" xmlns:gpxtpx="http://www.garmin.com/xmlschemas'
        filestring1 += '/TrackPointExtension/v1" creator="eTrex 10" version="1.1" xmlns:xsi="http://www.w3.org/2001/'
        filestring1 += 'XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix'
        filestring1 += '.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www8.garmin.com/'
        filestring1 += 'xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/WaypointExtension/v1 http://'
        filestring1 += 'www8.garmin.com/xmlschemas/WaypointExtensionv1.xsd http://www.garmin.com/xmlschemas/TrackPoint'
        filestring1 += 'Extension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd"><metadata><link '
        filestring1 += 'href="http://www.garmin.com"><text>Garmin International</text></link><time>2016-10-08T13:'
        filestring1 += '26:03Z</time></metadata><wpt lat="49.794800" lon="9.941167"><time>2016-10-08T13:27:25Z</time>'
        filestring1 += '<name>BLA</name><sym>Flag, Blue</sym></wpt><wpt lat="49.794800" lon="9.941167"><time>2016'
        filestring1 += '-10-08T13:27:25Z</time><name>TESTWPT FINAL</name><sym>Flag, Blue</sym></wpt></gpx>'

        filestring2 = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com'
        filestring2 += '/GPX/1/1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:wptx1="http://'
        filestring2 += 'www.garmin.com/xmlschemas/WaypointExtension/v1" xmlns:gpxtpx="http://www.garmin.com/xmlschemas'
        filestring2 += '/TrackPointExtension/v1" creator="eTrex 10" version="1.1" xmlns:xsi="http://www.w3.org/2001/'
        filestring2 += 'XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix'
        filestring2 += '.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www8.garmin.com/'
        filestring2 += 'xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/WaypointExtension/v1 http://'
        filestring2 += 'www8.garmin.com/xmlschemas/WaypointExtensionv1.xsd http://www.garmin.com/xmlschemas/TrackPoint'
        filestring2 += 'Extension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd"><metadata><link '
        filestring2 += 'href="http://www.garmin.com"><text>Garmin International</text></link><time>2016-10-08T13:'
        filestring2 += '26:03Z</time></metadata><wpt lat="49.794800" lon="9.941167"><time>2016-10-08T13:27:25Z</time>'
        filestring2 += '<name>TESTWPT</name><sym>Flag, Blue</sym></wpt></gpx>'

        wptfiles = [filestring1, filestring2]
        new_wptfiles = self.x.delete_waypoint_from_files(wptfiles, wpt)
        self.assertEqual(new_wptfiles, [filestring1, ""])

    def test_first_wpt_in_file(self):
        wpt = geocache.Waypoint("testwpt", [49.792433, 9.932233])

        filestring1 = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com'
        filestring1 += '/GPX/1/1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:wptx1="http://'
        filestring1 += 'www.garmin.com/xmlschemas/WaypointExtension/v1" xmlns:gpxtpx="http://www.garmin.com/xmlschemas'
        filestring1 += '/TrackPointExtension/v1" creator="eTrex 10" version="1.1" xmlns:xsi="http://www.w3.org/2001/'
        filestring1 += 'XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix'
        filestring1 += '.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www8.garmin.com/'
        filestring1 += 'xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/WaypointExtension/v1 http://'
        filestring1 += 'www8.garmin.com/xmlschemas/WaypointExtensionv1.xsd http://www.garmin.com/xmlschemas/TrackPoint'
        filestring1 += 'Extension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd"><metadata><link '
        filestring1 += 'href="http://www.garmin.com"><text>Garmin International</text></link><time>2016-10-08T13:'
        filestring1 += '26:03Z</time></metadata><wpt lat="49.794800" lon="9.941167"><time>2016-10-08T13:27:25Z</time>'
        filestring1 += '<name>TESTWPT</name><sym>Flag, Blue</sym></wpt><wpt lat="49.794800" lon="9.941167"><time>2016'
        filestring1 += '-10-08T13:27:25Z</time><name>TESTWPT FINAL</name><sym>Flag, Blue</sym></wpt></gpx>'

        filestring2 = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com'
        filestring2 += '/GPX/1/1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:wptx1="http://'
        filestring2 += 'www.garmin.com/xmlschemas/WaypointExtension/v1" xmlns:gpxtpx="http://www.garmin.com/xmlschemas'
        filestring2 += '/TrackPointExtension/v1" creator="eTrex 10" version="1.1" xmlns:xsi="http://www.w3.org/2001/'
        filestring2 += 'XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix'
        filestring2 += '.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www8.garmin.com/'
        filestring2 += 'xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/WaypointExtension/v1 http://'
        filestring2 += 'www8.garmin.com/xmlschemas/WaypointExtensionv1.xsd http://www.garmin.com/xmlschemas/TrackPoint'
        filestring2 += 'Extension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd"><metadata><link '
        filestring2 += 'href="http://www.garmin.com"><text>Garmin International</text></link><time>2016-10-08T13:'
        filestring2 += '26:03Z</time></metadata><wpt lat="49.794800" lon="9.941167"><time>2016-10-08T13:27:25Z</time>'
        filestring2 += '<name>QUAK</name><sym>Flag, Blue</sym></wpt></gpx>'

        wptfiles = [filestring1, filestring2]
        new_wptfiles = self.x.delete_waypoint_from_files(wptfiles, wpt)

        filestring1 = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com'
        filestring1 += '/GPX/1/1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:wptx1="http://'
        filestring1 += 'www.garmin.com/xmlschemas/WaypointExtension/v1" xmlns:gpxtpx="http://www.garmin.com/xmlschemas'
        filestring1 += '/TrackPointExtension/v1" creator="eTrex 10" version="1.1" xmlns:xsi="http://www.w3.org/2001/'
        filestring1 += 'XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix'
        filestring1 += '.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www8.garmin.com/'
        filestring1 += 'xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/WaypointExtension/v1 http://'
        filestring1 += 'www8.garmin.com/xmlschemas/WaypointExtensionv1.xsd http://www.garmin.com/xmlschemas/TrackPoint'
        filestring1 += 'Extension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd"><metadata><link '
        filestring1 += 'href="http://www.garmin.com"><text>Garmin International</text></link><time>2016-10-08T13:'
        filestring1 += '26:03Z</time></metadata><wpt lat="49.794800" lon="9.941167"><time>2016'
        filestring1 += '-10-08T13:27:25Z</time><name>TESTWPT FINAL</name><sym>Flag, Blue</sym></wpt></gpx>'

        self.assertEqual(new_wptfiles, [filestring1, filestring2])

    def test_last_wpt_in_file(self):
        wpt = geocache.Waypoint("testwpt", [49.792433, 9.932233])

        filestring1 = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com'
        filestring1 += '/GPX/1/1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:wptx1="http://'
        filestring1 += 'www.garmin.com/xmlschemas/WaypointExtension/v1" xmlns:gpxtpx="http://www.garmin.com/xmlschemas'
        filestring1 += '/TrackPointExtension/v1" creator="eTrex 10" version="1.1" xmlns:xsi="http://www.w3.org/2001/'
        filestring1 += 'XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix'
        filestring1 += '.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www8.garmin.com/'
        filestring1 += 'xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/WaypointExtension/v1 http://'
        filestring1 += 'www8.garmin.com/xmlschemas/WaypointExtensionv1.xsd http://www.garmin.com/xmlschemas/TrackPoint'
        filestring1 += 'Extension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd"><metadata><link '
        filestring1 += 'href="http://www.garmin.com"><text>Garmin International</text></link><time>2016-10-08T13:'
        filestring1 += '26:03Z</time></metadata><wpt lat="49.794800" lon="9.941167"><time>2016-10-08T13:27:25Z</time>'
        filestring1 += '<name>TESTWPT START</name><sym>Flag, Blue</sym></wpt><wpt lat="49.794800" lon="9.941167"><time>'
        filestring1 += '2016-10-08T13:27:25Z</time><name>TESTWPT</name><sym>Flag, Blue</sym></wpt></gpx>'

        filestring2 = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com'
        filestring2 += '/GPX/1/1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:wptx1="http://'
        filestring2 += 'www.garmin.com/xmlschemas/WaypointExtension/v1" xmlns:gpxtpx="http://www.garmin.com/xmlschemas'
        filestring2 += '/TrackPointExtension/v1" creator="eTrex 10" version="1.1" xmlns:xsi="http://www.w3.org/2001/'
        filestring2 += 'XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix'
        filestring2 += '.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www8.garmin.com/'
        filestring2 += 'xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/WaypointExtension/v1 http://'
        filestring2 += 'www8.garmin.com/xmlschemas/WaypointExtensionv1.xsd http://www.garmin.com/xmlschemas/TrackPoint'
        filestring2 += 'Extension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd"><metadata><link '
        filestring2 += 'href="http://www.garmin.com"><text>Garmin International</text></link><time>2016-10-08T13:'
        filestring2 += '26:03Z</time></metadata><wpt lat="49.794800" lon="9.941167"><time>2016-10-08T13:27:25Z</time>'
        filestring2 += '<name>QUAK</name><sym>Flag, Blue</sym></wpt></gpx>'

        wptfiles = [filestring1, filestring2]
        new_wptfiles = self.x.delete_waypoint_from_files(wptfiles, wpt)

        filestring1 = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com'
        filestring1 += '/GPX/1/1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:wptx1="http://'
        filestring1 += 'www.garmin.com/xmlschemas/WaypointExtension/v1" xmlns:gpxtpx="http://www.garmin.com/xmlschemas'
        filestring1 += '/TrackPointExtension/v1" creator="eTrex 10" version="1.1" xmlns:xsi="http://www.w3.org/2001/'
        filestring1 += 'XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix'
        filestring1 += '.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www8.garmin.com/'
        filestring1 += 'xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/WaypointExtension/v1 http://'
        filestring1 += 'www8.garmin.com/xmlschemas/WaypointExtensionv1.xsd http://www.garmin.com/xmlschemas/TrackPoint'
        filestring1 += 'Extension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd"><metadata><link '
        filestring1 += 'href="http://www.garmin.com"><text>Garmin International</text></link><time>2016-10-08T13:'
        filestring1 += '26:03Z</time></metadata><wpt lat="49.794800" lon="9.941167"><time>2016-10-08T13:27:25Z</time>'
        filestring1 += '<name>TESTWPT START</name><sym>Flag, Blue</sym></wpt></gpx>'

        self.assertEqual(new_wptfiles, [filestring1, filestring2])

    def test_wpt_in_middle_of_file(self):
        wpt = geocache.Waypoint("testwpt", [49.792433, 9.932233])

        filestring1 = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com'
        filestring1 += '/GPX/1/1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:wptx1="http://'
        filestring1 += 'www.garmin.com/xmlschemas/WaypointExtension/v1" xmlns:gpxtpx="http://www.garmin.com/xmlschemas'
        filestring1 += '/TrackPointExtension/v1" creator="eTrex 10" version="1.1" xmlns:xsi="http://www.w3.org/2001/'
        filestring1 += 'XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix'
        filestring1 += '.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www8.garmin.com/'
        filestring1 += 'xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/WaypointExtension/v1 http://'
        filestring1 += 'www8.garmin.com/xmlschemas/WaypointExtensionv1.xsd http://www.garmin.com/xmlschemas/TrackPoint'
        filestring1 += 'Extension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd"><metadata><link '
        filestring1 += 'href="http://www.garmin.com"><text>Garmin International</text></link><time>2016-10-08T13:'
        filestring1 += '26:03Z</time></metadata><wpt lat="49.794800" lon="9.941167"><time>2016-10-08T13:27:25Z</time>'
        filestring1 += '<name>TESTWPT START</name><sym>Flag, Blue</sym></wpt><wpt lat="49.794800" lon="9.941167"><time>'
        filestring1 += '2016-10-08T13:27:25Z</time><name>TESTWPT</name><sym>Flag, Blue</sym></wpt><wpt lat="49.794800"'
        filestring1 += ' lon="9.941167"><time>2016-10-08T13:27:25Z</time><name>TESTWPT FINAL</name><sym>Flag, Blue'
        filestring1 += '</sym></wpt></gpx>'

        filestring2 = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com'
        filestring2 += '/GPX/1/1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:wptx1="http://'
        filestring2 += 'www.garmin.com/xmlschemas/WaypointExtension/v1" xmlns:gpxtpx="http://www.garmin.com/xmlschemas'
        filestring2 += '/TrackPointExtension/v1" creator="eTrex 10" version="1.1" xmlns:xsi="http://www.w3.org/2001/'
        filestring2 += 'XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix'
        filestring2 += '.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www8.garmin.com/'
        filestring2 += 'xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/WaypointExtension/v1 http://'
        filestring2 += 'www8.garmin.com/xmlschemas/WaypointExtensionv1.xsd http://www.garmin.com/xmlschemas/TrackPoint'
        filestring2 += 'Extension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd"><metadata><link '
        filestring2 += 'href="http://www.garmin.com"><text>Garmin International</text></link><time>2016-10-08T13:'
        filestring2 += '26:03Z</time></metadata><wpt lat="49.794800" lon="9.941167"><time>2016-10-08T13:27:25Z</time>'
        filestring2 += '<name>QUAK</name><sym>Flag, Blue</sym></wpt></gpx>'

        wptfiles = [filestring1, filestring2]
        new_wptfiles = self.x.delete_waypoint_from_files(wptfiles, wpt)

        filestring1 = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com'
        filestring1 += '/GPX/1/1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:wptx1="http://'
        filestring1 += 'www.garmin.com/xmlschemas/WaypointExtension/v1" xmlns:gpxtpx="http://www.garmin.com/xmlschemas'
        filestring1 += '/TrackPointExtension/v1" creator="eTrex 10" version="1.1" xmlns:xsi="http://www.w3.org/2001/'
        filestring1 += 'XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix'
        filestring1 += '.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www8.garmin.com/'
        filestring1 += 'xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/WaypointExtension/v1 http://'
        filestring1 += 'www8.garmin.com/xmlschemas/WaypointExtensionv1.xsd http://www.garmin.com/xmlschemas/TrackPoint'
        filestring1 += 'Extension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd"><metadata><link '
        filestring1 += 'href="http://www.garmin.com"><text>Garmin International</text></link><time>2016-10-08T13:'
        filestring1 += '26:03Z</time></metadata><wpt lat="49.794800" lon="9.941167"><time>2016-10-08T13:27:25Z</time>'
        filestring1 += '<name>TESTWPT START</name><sym>Flag, Blue</sym></wpt><wpt lat="49.794800"'
        filestring1 += ' lon="9.941167"><time>2016-10-08T13:27:25Z</time><name>TESTWPT FINAL</name><sym>Flag, Blue'
        filestring1 += '</sym></wpt></gpx>'

        self.assertEqual(new_wptfiles, [filestring1, filestring2])

    def test_wpt_not_in_file(self):
        wpt = geocache.Waypoint("testwpt", [49.792433, 9.932233])

        filestring1 = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com'
        filestring1 += '/GPX/1/1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:wptx1="http://'
        filestring1 += 'www.garmin.com/xmlschemas/WaypointExtension/v1" xmlns:gpxtpx="http://www.garmin.com/xmlschemas'
        filestring1 += '/TrackPointExtension/v1" creator="eTrex 10" version="1.1" xmlns:xsi="http://www.w3.org/2001/'
        filestring1 += 'XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix'
        filestring1 += '.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www8.garmin.com/'
        filestring1 += 'xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/WaypointExtension/v1 http://'
        filestring1 += 'www8.garmin.com/xmlschemas/WaypointExtensionv1.xsd http://www.garmin.com/xmlschemas/TrackPoint'
        filestring1 += 'Extension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd"><metadata><link '
        filestring1 += 'href="http://www.garmin.com"><text>Garmin International</text></link><time>2016-10-08T13:'
        filestring1 += '26:03Z</time></metadata><wpt lat="49.794800" lon="9.941167"><time>2016-10-08T13:27:25Z</time>'
        filestring1 += '<name>BLA</name><sym>Flag, Blue</sym></wpt><wpt lat="49.794800" lon="9.941167"><time>2016'
        filestring1 += '-10-08T13:27:25Z</time><name>TESTWPT FINAL</name><sym>Flag, Blue</sym></wpt></gpx>'

        filestring2 = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com'
        filestring2 += '/GPX/1/1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:wptx1="http://'
        filestring2 += 'www.garmin.com/xmlschemas/WaypointExtension/v1" xmlns:gpxtpx="http://www.garmin.com/xmlschemas'
        filestring2 += '/TrackPointExtension/v1" creator="eTrex 10" version="1.1" xmlns:xsi="http://www.w3.org/2001/'
        filestring2 += 'XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix'
        filestring2 += '.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www8.garmin.com/'
        filestring2 += 'xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/WaypointExtension/v1 http://'
        filestring2 += 'www8.garmin.com/xmlschemas/WaypointExtensionv1.xsd http://www.garmin.com/xmlschemas/TrackPoint'
        filestring2 += 'Extension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd"><metadata><link '
        filestring2 += 'href="http://www.garmin.com"><text>Garmin International</text></link><time>2016-10-08T13:'
        filestring2 += '26:03Z</time></metadata><wpt lat="49.794800" lon="9.941167"><time>2016-10-08T13:27:25Z</time>'
        filestring2 += '<name>QUAK</name><sym>Flag, Blue</sym></wpt></gpx>'

        wptfiles = [filestring1, filestring2]
        new_wptfiles = self.x.delete_waypoint_from_files(wptfiles, wpt)
        self.assertEqual(new_wptfiles, [filestring1, filestring2])


class TestRewriteWaypointfiles(unittest.TestCase):
    def setUp(self):
        """is not used but a gpscontent has to exist in order to use class functions"""
        self.x = gpscontent.GPSContent(r"../tests/examples/no_logfile_waypoints")

    def test_files_do_not_exist(self):
        names = [r"../tests/examples/temp/one.gpx", r"../tests/examples/temp/two.gpx", r"../tests/examples/temp/three.gpx"]
        conts = ["bli", "bla", "blub"]
        self.assertRaises(TypeError, self.x.rewrite_waypointfiles, names, conts)

    def test_overwrite_files(self):
        with open(r"../tests/examples/temp/one.gpx", "w") as file1:
            file1.write("one")
        with open(r"../tests/examples/temp/two.gpx", "w") as file1:
            file1.write("two")
        with open(r"../tests/examples/temp/three.gpx", "w") as file1:
            file1.write("three")

        names = [r"../tests/examples/temp/one.gpx", r"../tests/examples/temp/two.gpx", r"../tests/examples/temp/three.gpx"]
        conts = ["bli", "bla", "blub"]
        self.x.rewrite_waypointfiles(names, conts)

        for i, n in enumerate(names):  # for every file
            with open(n) as f:
                cont = f.read()
                self.assertEqual(cont, conts[i])  # look if right content
            os.remove(n)  # delete created file

    def test_delete_a_file(self):
        with open(r"../tests/examples/temp/one.gpx", "w") as file1:
            file1.write("one")
        with open(r"../tests/examples/temp/two.gpx", "w") as file1:
            file1.write("two")
        with open(r"../tests/examples/temp/three.gpx", "w") as file1:
            file1.write("three")

        names = [r"../tests/examples/temp/one.gpx", r"../tests/examples/temp/two.gpx", r"../tests/examples/temp/three.gpx"]
        conts = ["bli", "", "blub"]
        self.x.rewrite_waypointfiles(names, conts)

        self.assertRaises(IOError, open, r"../tests/examples/temp/two.gpx")  # file does not exist amymore

        os.remove(r"../tests/examples/temp/one.gpx")  # delete created files
        os.remove(r"../tests/examples/temp/three.gpx")

    def test_wrong_length(self):
        with open(r"../tests/examples/temp/one.gpx", "w") as file1:
            file1.write("one")
        with open(r"../tests/examples/temp/two.gpx", "w") as file1:
            file1.write("two")
        with open(r"../tests/examples/temp/three.gpx", "w") as file1:
            file1.write("three")

        names = [r"../tests/examples/temp/one.gpx", r"../tests/examples/temp/two.gpx", r"../tests/examples/temp/three.gpx"]
        conts = ["bli", "blub"]
        self.assertRaises(IOError, self.x.rewrite_waypointfiles, names, conts)

        os.remove(r"../tests/examples/temp/one.gpx")  # delete created files
        os.remove(r"../tests/examples/temp/two.gpx")
        os.remove(r"../tests/examples/temp/three.gpx")

    def test_wrong_type_in_cont(self):
        with open(r"../tests/examples/temp/one.gpx", "w") as file1:
            file1.write("one")
        with open(r"../tests/examples/temp/two.gpx", "w") as file1:
            file1.write("two")
        with open(r"../tests/examples/temp/three.gpx", "w") as file1:
            file1.write("three")

        names = [r"../tests/examples/temp/one.gpx", r"../tests/examples/temp/two.gpx", r"../tests/examples/temp/three.gpx"]
        conts = ["bli", "bla", 42]
        self.assertRaises(TypeError, self.x.rewrite_waypointfiles, names, conts)

        os.remove(r"../tests/examples/temp/one.gpx")  # delete created files
        os.remove(r"../tests/examples/temp/two.gpx")
        os.remove(r"../tests/examples/temp/three.gpx")

    def test_wrong_type_in_names(self):
        with open(r"../tests/examples/temp/one.gpx", "w") as file1:
            file1.write("one")
        with open(r"../tests/examples/temp/two.gpx", "w") as file1:
            file1.write("two")
        with open(r"../tests/examples/temp/three.gpx", "w") as file1:
            file1.write("three")

        names = [42, r"../tests/examples/temp/two.gpx", r"../tests/examples/temp/three.gpx"]
        conts = ["bli", "bla", "blub"]
        self.assertRaises(TypeError, self.x.rewrite_waypointfiles, names, conts)

        os.remove(r"../tests/examples/temp/one.gpx")  # delete created files
        os.remove(r"../tests/examples/temp/two.gpx")
        os.remove(r"../tests/examples/temp/three.gpx")


class TestFindSuggestions(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"../tests/examples/no_logfile")

    def test_normal(self):
        wpt = geocache.Waypoint("FÜR", [49.80761666666667, 9.912116666666666])
        sug = self.x.find_suggestions(wpt)
        g = geocache.Geocache(r"../tests/examples/no_logfile/GPX/GC6RNTX.gpx")
        self.assertEqual(sug, [g])

    def test_number_at_the_end_only_part_of_word(self):
        wpt = geocache.Waypoint("Märchen 1", [49.80761666666667, 9.912116666666666])
        sug = self.x.find_suggestions(wpt)
        g = geocache.Geocache(r"../tests/examples/no_logfile/GPX/GC1XRPM.gpx")
        self.assertEqual(sug, [g])

    def test_number_not_at_the_end_more_than_one_suggestion(self):
        wpt = geocache.Waypoint("Märchen 1 2", [49.80761666666667, 9.912116666666666])
        sug = self.x.find_suggestions(wpt)
        g1 = geocache.Geocache(r"../tests/examples/no_logfile/GPX/GC1XRPM.gpx")
        g2 = geocache.Geocache(r"../tests/examples/no_logfile/GPX/GC6RNTX.gpx")
        self.assertEqual(sug, [g1, g2])

    def test_musikhochschule(self):
        wpt = geocache.Waypoint("Musikhochschule", [49.80761666666667, 9.912116666666666])
        sug = self.x.find_suggestions(wpt)
        self.assertEqual(sug, [])


class TestAssignWaypoints(unittest.TestCase):

    def setUp(self):
        """stuff that has to be done before tests start"""

        # create gpscontent object
        self.x = gpscontent.GPSContent(r"../tests/examples/no_logfile_waypoints2")

        # copy files that will be changed
        shutil.copy2(r"../tests/examples/no_logfile_waypoints2/GPX/Wegpunkte_05-SEP-17.gpx",
                     r"../tests/examples/temp/Wegpunkte_05-SEP-17.gpx")
        shutil.copy2(r"../tests/examples/no_logfile_waypoints2/GPX/Waypoints_11-MAR-17.gpx",
                     r"../tests/examples/temp/Waypoints_11-MAR-17.gpx")

        # run function assign_waypoint()
        with mock.patch('builtins.input',
                        side_effect=['2', '2', "y", "2", "n", "3", "blub", "1", "bla", "1", "GC6K86W"]):
            self.x.assign_waypoints()

            # this is what happens when running the function:
            # 2: 'MÄRCHEN 1 2' is assigned to suggestion 2 (GC6RNTX)
            # 2, y: 'DELETE' is deleted
            # 2, n: "NOT DELETE" is nearly deleted but in the end not
            # 3: 'DO NOTHING' remains unchanged
            # blub: some bullshit input is given for 'BULLSHIT' so it also remains unchanged
            # 1, bla: 'DOM FINAL' is tried to be assigned to geocache 'bla' which doesn't exists so it remains unchanged
            # 1, GC6K86W: 'BLICK ZUM RANDERSACKERER KÄPPE' is assigned to geocache GC6K86W

    def test_assign_maerchen(self):
        for gc in self.x.geocaches:
            if gc.gccode == "GC6RNTX":
                self.assertEqual(len(gc.waypoints), 1)

        maerchen = False
        for wpt in self.x.waypoints:
            if wpt.name == "MÄRCHEN 1 2":
                maerchen = True
        self.assertFalse(maerchen)  # waypoint not in gps.waypoints any more

    def test_delete(self):
        delete = False
        for wpt in self.x.waypoints:
            if wpt.name == "DELETE":
                delete = True
        self.assertFalse(delete)

    def test_file_05sep17(self):
        expected = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com/GPX/1/' \
                   '1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:wptx1="http://www.garmin.' \
                   'com/xmlschemas/WaypointExtension/v1" xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPoint' \
                   'Extension/v1" creator="eTrex 10" version="1.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance' \
                   '" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd ' \
                   'http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www8.garmin.com/xmlschemas/GpxExtensionsv3' \
                   '.xsd http://www.garmin.com/xmlschemas/WaypointExtension/v1 http://www8.garmin.com/xmlschemas/' \
                   'WaypointExtensionv1.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.' \
                   'com/xmlschemas/TrackPointExtensionv1.xsd"><metadata><link href="http://www.garmin.com"><text>Garmin' \
                   ' International</text></link><time>2017-01-14T13:42:12Z</time></metadata><wpt lat="49.792433" lon="' \
                   '9.932233"><time>2017-01-14T13:43:14Z</time><name>MÄRCHEN 1 2 (GC6RNTX)</name><sym>Flag, Blue</sym>' \
                   '</wpt><wpt lat="49.790983" lon="9.932300"><ele>231.912979</ele><time>2017-01-14T19:02:03Z</time>' \
                   '<name>NOT DELETE</name><sym>Flag, Blue</sym></wpt><wpt lat="49.790983" lon="9.932300"><ele>231.' \
                   '912979</ele><time>2017-01-14T19:02:03Z</time><name>DO NOTHING</name><sym>Flag, Blue</sym></wpt>' \
                   '<wpt lat="49.790983" lon="9.932300"><ele>231.912979</ele><time>2017-01-14T19:02:03Z</time><name>' \
                   'BULLSHIT</name><sym>Flag, Blue</sym></wpt></gpx>'
        with open(r"../tests/examples/no_logfile_waypoints2/GPX/Wegpunkte_05-SEP-17.gpx", encoding="utf-8") as wptfile:
            output = wptfile.read()
        self.assertEqual(output, expected)

    def test_not_delete(self):
        not_delete = False
        for wpt in self.x.waypoints:
            if wpt.name == "NOT DELETE":
                not_delete = True
        self.assertTrue(not_delete)

    def test_do_nothing(self):
        do_nothing = False
        for wpt in self.x.waypoints:
            if wpt.name == "DO NOTHING":
                do_nothing = True
        self.assertTrue(do_nothing)

    def test_bullshit_input(self):
        bullshit = False
        for wpt in self.x.waypoints:
            if wpt.name == "BULLSHIT":
                bullshit = True
        self.assertTrue(bullshit)

    def test_assigning_fails(self):
        dom_final = False
        for wpt in self.x.waypoints:
            if wpt.name == "DOM FINAL":
                dom_final = True
        self.assertTrue(dom_final)

    def test_assign_randersackerer_kaeppe(self):
        for gc in self.x.geocaches:
            if gc.gccode == "GC6K86W":
                self.assertEqual(len(gc.waypoints), 1)

        kaeppe = False
        for wpt in self.x.waypoints:
            if wpt.name == "BLICK ZUM RANDERSACKERER KÄPPE":
                kaeppe = True
        self.assertFalse(kaeppe)  # waypoint not in gps.waypoints any more

    def test_file_11mar17(self):
        expected = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com/GPX/1' \
                   '/1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:wptx1="http://www.garmin.' \
                   'com/xmlschemas/WaypointExtension/v1" xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPoint' \
                   'Extension/v1" creator="eTrex 10" version="1.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"' \
                   ' xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd ' \
                   'http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www8.garmin.com/xmlschemas/GpxExtensionsv3.' \
                   'xsd http://www.garmin.com/xmlschemas/WaypointExtension/v1 http://www8.garmin.com/xmlschemas/Waypoint' \
                   'Extensionv1.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.com/' \
                   'xmlschemas/TrackPointExtensionv1.xsd"><metadata><link href="http://www.garmin.com"><text>Garmin' \
                   ' International</text></link><time>2017-03-11T13:42:47Z</time></metadata><wpt lat="49.760150" ' \
                   'lon="9.990900"><ele>216.568268</ele><time>2017-03-11T13:44:53Z</time><name>BLICK ZUM RANDERSACKERER' \
                   ' KÄPPE (GC6K86W)</name><sym>Flag, Blue</sym></wpt></gpx>'
        with open(r"../tests/examples/no_logfile_waypoints2/GPX/Waypoints_11-MAR-17.gpx", encoding="utf-8") as wptfile:
            output = wptfile.read()
        self.assertEqual(output, expected)

    def test_file_14jan17_no_changes(self):
        expected = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com/GPX/1/1' \
                   '" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:wptx1="http://www.garmin.com/' \
                   'xmlschemas/WaypointExtension/v1" xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPointExtension' \
                   '/v1" creator="eTrex 10" version="1.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:' \
                   'schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd http:/' \
                   '/www.garmin.com/xmlschemas/GpxExtensions/v3 http://www8.garmin.com/xmlschemas/GpxExtensionsv3.xsd ' \
                   'http://www.garmin.com/xmlschemas/WaypointExtension/v1 http://www8.garmin.com/xmlschemas/Waypoint' \
                   'Extensionv1.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.com/xml' \
                   'schemas/TrackPointExtensionv1.xsd"><metadata><link href="http://www.garmin.com"><text>Garmin ' \
                   'International</text></link><time>2017-01-14T13:42:12Z</time></metadata><wpt lat="49.792433" ' \
                   'lon="9.932233"><time>2017-01-14T13:43:14Z</time><name>MÄRCHENSTUHL 2 (GC1XRPM)</name><sym>Flag, ' \
                   'Blue</sym></wpt><wpt lat="49.790983" lon="9.932300"><ele>231.912979</ele><time>2017-01-14T19:02:03Z' \
                   '</time><name>DOM FINAL</name><sym>Flag, Blue</sym></wpt></gpx>'
        with open(r"../tests/examples/no_logfile_waypoints2/GPX/Wegpunkte_14-JAN-17.gpx", encoding="utf-8") as wptfile:
            output = wptfile.read()
        self.assertEqual(output, expected)

    def tearDown(self):
        """move files back after tests are done"""
        shutil.move(r"../tests/examples/temp/Wegpunkte_05-SEP-17.gpx",
                    r"../tests/examples/no_logfile_waypoints2/GPX/Wegpunkte_05-SEP-17.gpx")
        shutil.move(r"../tests/examples/temp/Waypoints_11-MAR-17.gpx",
                    r"../tests/examples/no_logfile_waypoints2/GPX/Waypoints_11-MAR-17.gpx")


class TestCreateMapinfoOne(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"../tests/examples/no_logfile_waypoints")

    def test_cache_with_waypoints(self):
        for g in self.x.geocaches:
            if g.gccode == "GC1XRPM":
                self.x._create_mapinfo_one(g)
        with open("mapinfo.txt", "rb") as mapinfo:
            output = mapinfo.read().decode("cp1252")
        os.remove("mapinfo.txt")
        expected = "49.809317,9.93365 {Im Auftrag ihrer Majestät – Der Märchenstuhl} <default>\r\n"
        expected += "49.792433,9.932233 {MÄRCHENSTUHL 2} <yellow>\r\n"
        self.assertEqual(output, expected)

    def test_yellowcache_with_waypoints(self):
        gc = geocache.Geocache(r"../tests/examples/GC78K5W.gpx")
        w = geocache.Waypoint("wpt (GC78K5W)", [49.792433, 9.932233])
        gc.add_waypoint(w)
        self.x._create_mapinfo_one(gc)
        with open("mapinfo.txt", "rb") as mapinfo:
            output = mapinfo.read().decode("cp1252")
        os.remove("mapinfo.txt")
        expected = "49.795567,9.905717 {Cachertreffen Würzburg, die 54ste} <yellow>\r\n"
        expected += "49.792433,9.932233 {WPT} <grey>\r\n"
        self.assertEqual(output, expected)

    def test_without_waypoints(self):
        gc = geocache.Geocache(r"../tests/examples/GC78K5W.gpx")
        self.x._create_mapinfo_one(gc)
        with open("mapinfo.txt", "rb") as mapinfo:
            output = mapinfo.read().decode("cp1252")
        os.remove("mapinfo.txt")
        expected = "49.795567,9.905717 {Cachertreffen Würzburg, die 54ste} <yellow>\r\n"
        self.assertEqual(output, expected)


class TestCreateMapinfoSeveral(unittest.TestCase):
    def setUp(self):
        """creates a gpscontent object and a cachelist for the tests"""
        self.x = gpscontent.GPSContent(r"../tests/examples/no_logfile_waypoints")
        self.cachelist = []
        for gc in self.x.geocaches:
            if gc.gccode == "GC1XRPM" or gc.gccode == "GC5N23T":
                self.cachelist.append(gc)

    def test_without_waypoints(self):
        self.x._create_mapinfo_several(self.cachelist, False, False)
        with open("mapinfo.txt", "rb") as mapinfo:
            output = mapinfo.read().decode("cp1252")
        os.remove("mapinfo.txt")
        expected = "49.809317,9.93365 {Im Auftrag ihrer Majestät – Der Märchenstuhl} <default>\r\n"
        expected += "49.80761666666667,9.912116666666666 {67 - MedTrix - \u001a\u001a\u001a\u001a\u001a} <blue>\r\n"
        self.assertEqual(output, expected)

    def test_with_waypoints(self):
        self.x._create_mapinfo_several(self.cachelist, True, False)
        with open("mapinfo.txt", "rb") as mapinfo:
            output = mapinfo.read().decode("cp1252")
        os.remove("mapinfo.txt")
        expected = "49.809317,9.93365 {Im Auftrag ihrer Majestät – Der Märchenstuhl (GC1XRPM)} <default>\r\n"
        expected += "49.792433,9.932233 {MÄRCHENSTUHL 2 (GC1XRPM)} <default>\r\n"
        expected += "49.80761666666667,9.912116666666666 {67 - MedTrix - \u001a\u001a\u001a\u001a\u001a} <blue>\r\n"
        self.assertEqual(output, expected)

    def test_with_all_waypoints(self):
        self.x._create_mapinfo_several(self.cachelist, True, True)
        with open("mapinfo.txt", "rb") as mapinfo:
            output = mapinfo.read().decode("cp1252")
        os.remove("mapinfo.txt")
        expected = "49.809317,9.93365 {Im Auftrag ihrer Majestät – Der Märchenstuhl (GC1XRPM)} <default>\r\n"
        expected += "49.792433,9.932233 {MÄRCHENSTUHL 2 (GC1XRPM)} <default>\r\n"
        expected += "49.80761666666667,9.912116666666666 {67 - MedTrix - \u001a\u001a\u001a\u001a\u001a} <blue>\r\n"
        expected += "49.790983,9.9323 {DOM FINAL (GC1QNWT)} <yellow>\r\n"
        expected += "49.76015,9.9909 {BLICK ZUM RANDERSACKERER KÄPPE} <yellow>\r\n"
        self.assertEqual(output, expected)

    def test_only_free_waypoints(self):  # normally should not happen
        self.maxDiff = None
        self.x._create_mapinfo_several(self.cachelist, False, True)
        with open("mapinfo.txt", "rb") as mapinfo:
            output = mapinfo.read().decode("cp1252")
        os.remove("mapinfo.txt")
        expected = "49.809317,9.93365 {Im Auftrag ihrer Majestät – Der Märchenstuhl} <default>\r\n"
        expected += "49.80761666666667,9.912116666666666 {67 - MedTrix - \u001a\u001a\u001a\u001a\u001a} <blue>\r\n"
        expected += "49.790983,9.9323 {DOM FINAL (GC1QNWT)} <yellow>\r\n"
        expected += "49.76015,9.9909 {BLICK ZUM RANDERSACKERER KÄPPE} <yellow>\r\n"
        self.assertEqual(output, expected)


class TestCreateWaypointfilestrings(unittest.TestCase):
    def test_all_well(self):
        x = gpscontent.GPSContent(r"../tests/examples/no_logfile_waypoints")
        y = x.create_waypointfilestrings()

        namelist = [os.path.join(r"../tests/examples/no_logfile_waypoints", "GPX", r"Wegpunkte_08-OKT-16.gpx"),
                    os.path.join(r"../tests/examples/no_logfile_waypoints", "GPX", r"Wegpunkte_14-JAN-17.gpx"),
                    os.path.join(r"../tests/examples/no_logfile_waypoints", "GPX", r"Waypoints_11-MAR-17.gpx")]

        cont1 = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com/GPX/1/1"'
        cont1 += ' xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:wptx1="http://www.garmin.com/'
        cont1 += 'xmlschemas/WaypointExtension/v1" xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPointExtension/'
        cont1 += 'v1" creator="eTrex 10" version="1.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:sche'
        cont1 += 'maLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd http://www.'
        cont1 += 'garmin.com/xmlschemas/GpxExtensions/v3 http://www8.garmin.com/xmlschemas/GpxExtensionsv3.xsd http:/'
        cont1 += '/www.garmin.com/xmlschemas/WaypointExtension/v1 http://www8.garmin.com/xmlschemas/WaypointExtension'
        cont1 += 'v1.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.com/xmlschemas/Trac'
        cont1 += 'kPointExtensionv1.xsd"><metadata><link href="http://www.garmin.com"><text>Garmin International</te'
        cont1 += 'xt></link><time>2016-10-08T13:26:03Z</time></metadata><wpt lat="49.794800" lon="9.941167"><time>2016'
        cont1 += '-10-08T13:27:25Z</time><name>MUSIKHOCHSCHULE</name><sym>Flag, Blue</sym></wt></gpx>'

        cont2 = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com/GPX/1/1"'
        cont2 += ' xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:wptx1="http://www.garmin.com/'
        cont2 += 'xmlschemas/WaypointExtension/v1" xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPointExtension/'
        cont2 += 'v1" creator="eTrex 10" version="1.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:sche'
        cont2 += 'maLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd http://www.'
        cont2 += 'garmin.com/xmlschemas/GpxExtensions/v3 http://www8.garmin.com/xmlschemas/GpxExtensionsv3.xsd http://'
        cont2 += 'www.garmin.com/xmlschemas/WaypointExtension/v1 http://www8.garmin.com/xmlschemas/WaypointExtensionv1'
        cont2 += '.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.com/xmlschemas/Track'
        cont2 += 'PointExtensionv1.xsd"><metadata><link href="http://www.garmin.com"><text>Garmin International</text>'
        cont2 += '</link><time>2017-01-14T13:42:12Z</time></metadata><wpt lat="49.792433" lon="9.932233"><time>2017-01'
        cont2 += '-14T13:43:14Z</time><name>MÄRCHENSTUHL 2 (GC1XRPM)</name><sym>Flag, Blue</sym></wpt><wpt lat="49.'
        cont2 += '790983" lon="9.932300"><ele>231.912979</ele><time>2017-01-14T19:02:03Z</time><name>DOM FINAL '
        cont2 += '(GC1QNWT)</name><sym>Flag, Blue</sym></wpt></gpx>'

        cont3 = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com/GPX/1/1"'
        cont3 += ' xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:wptx1="http://www.garmin.com/'
        cont3 += 'xmlschemas/WaypointExtension/v1" xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPointExtension'
        cont3 += '/v1" creator="eTrex 10" version="1.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:sch'
        cont3 += 'emaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd http://www'
        cont3 += '.garmin.com/xmlschemas/GpxExtensions/v3 http://www8.garmin.com/xmlschemas/GpxExtensionsv3.xsd http:/'
        cont3 += '/www.garmin.com/xmlschemas/WaypointExtension/v1 http://www8.garmin.com/xmlschemas/WaypointExtensionv1'
        cont3 += '.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.com/xmlschemas/Track'
        cont3 += 'PointExtensionv1.xsd"><metadata><link href="http://www.garmin.com"><text>Garmin International</text>'
        cont3 += '</link><time>2017-03-11T13:42:47Z</time></metadata><wpt lat="49.760150" lon="9.990900"><ele>216.568'
        cont3 += '268</ele><time>2017-03-11T13:44:53Z</time><name>BLICK ZUM RANDERSACKERER KÄPPE</name><sym>Flag, '
        cont3 += 'Blue</sym></wpt></gpx>'

        contlist = [str(cont1), str(cont2), str(cont3)]

        self.assertEqual(y, [namelist, contlist])


class TestShowOnMap(unittest.TestCase):

    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"../tests/examples/no_logfile_waypoints")

    def test_one_always_with_waypoints(self):
        with mock.patch('builtins.input', return_value=""):
            with mock.patch("webbrowser.open_new_tab"):
                with mock.patch("subprocess.Popen"):
                    with mock.patch("user_io.show_on_map_end"):
                        with mock.patch("os.remove"):
                            for g in self.x.geocaches:
                                if g.gccode == "GC1XRPM":
                                    self.x.show_on_map(g)
        expected = "49.809317,9.93365 {Im Auftrag ihrer Majestät – Der Märchenstuhl} <default>\r\n"
        expected += "49.792433,9.932233 {MÄRCHENSTUHL 2} <yellow>\r\n"
        with open("mapinfo.txt", "rb") as mapinfo:
            result = mapinfo.read().decode("cp1252")
        self.assertEqual(expected, result)

    def test_several_without_waypoints(self):
        self.cachelist = []           # create cachelist
        for gc in self.x.geocaches:
            if gc.gccode == "GC1XRPM" or gc.gccode == "GC5N23T":
                self.cachelist.append(gc)
        with mock.patch('builtins.input', side_effect=["n", ""]):   # test
            with mock.patch("webbrowser.open_new_tab"):
                with mock.patch("subprocess.Popen"):
                    with mock.patch("user_io.show_on_map_end"):
                        with mock.patch("os.remove"):
                            self.x.show_on_map(self.cachelist)
        expected = "49.809317,9.93365 {Im Auftrag ihrer Majestät – Der Märchenstuhl} <default>\r\n"
        expected += "49.80761666666667,9.912116666666666 {67 - MedTrix - \u001a\u001a\u001a\u001a\u001a} <blue>\r\n"
        with open("mapinfo.txt", "rb") as mapinfo:
            result = mapinfo.read().decode("cp1252")
        self.assertEqual(expected, result)

    def test_several_with_waypoints(self):
        self.cachelist = []           # create cachelist
        for gc in self.x.geocaches:
            if gc.gccode == "GC1XRPM" or gc.gccode == "GC5N23T":
                self.cachelist.append(gc)
        with mock.patch('builtins.input', side_effect=["y", ""]):   # test
            with mock.patch("webbrowser.open_new_tab"):
                with mock.patch("subprocess.Popen"):
                    with mock.patch("user_io.show_on_map_end"):
                        with mock.patch("os.remove"):
                            self.x.show_on_map(self.cachelist)
        expected = "49.809317,9.93365 {Im Auftrag ihrer Majestät – Der Märchenstuhl (GC1XRPM)} <default>\r\n"
        expected += "49.792433,9.932233 {MÄRCHENSTUHL 2 (GC1XRPM)} <default>\r\n"
        expected += "49.80761666666667,9.912116666666666 {67 - MedTrix - \u001a\u001a\u001a\u001a\u001a} <blue>\r\n"
        with open("mapinfo.txt", "rb") as mapinfo:
            result = mapinfo.read().decode("cp1252")
        self.assertEqual(expected, result)

    def test_all_without_waypoints(self):
        with mock.patch('builtins.input', side_effect=["n", ""]):
            with mock.patch("webbrowser.open_new_tab"):
                with mock.patch("subprocess.Popen"):
                    with mock.patch("user_io.show_on_map_end"):
                        with mock.patch("os.remove"):
                            self.x.show_on_map(self.x.geocaches, True)
        expected = "49.809317,9.93365 {Im Auftrag ihrer Majestät – Der Märchenstuhl} <default>\r\n"
        expected += "-43.695433,-66.4515 {Tesoro Ameghino} <green>\r\n"
        expected += "49.80761666666667,9.912116666666666 {67 - MedTrix - \u001a\u001a\u001a\u001a\u001a} <blue>\r\n"
        expected += "50.318883,10.1936 {Saaletalblick} <green>\r\n"
        expected += "49.794497,9.94094 {Hochschule für Musik 1} <blue>\r\n"
        expected += "49.7948,9.930267 {Wuerzburger webcam} <pink>\r\n"
        with open("mapinfo.txt", "rb") as mapinfo:
            result = mapinfo.read().decode("cp1252")
        self.assertEqual(expected, result)

    def test_all_with_waypoints(self):
        with mock.patch('builtins.input', side_effect=["y", ""]):
            with mock.patch("webbrowser.open_new_tab"):
                with mock.patch("subprocess.Popen"):
                    with mock.patch("user_io.show_on_map_end"):
                        with mock.patch("os.remove"):
                            self.x.show_on_map(self.x.geocaches, True)
        expected = "49.809317,9.93365 {Im Auftrag ihrer Majestät – Der Märchenstuhl (GC1XRPM)} <default>\r\n"
        expected += "49.792433,9.932233 {MÄRCHENSTUHL 2 (GC1XRPM)} <default>\r\n"
        expected += "-43.695433,-66.4515 {Tesoro Ameghino} <green>\r\n"
        expected += "49.80761666666667,9.912116666666666 {67 - MedTrix - \u001a\u001a\u001a\u001a\u001a} <blue>\r\n"
        expected += "50.318883,10.1936 {Saaletalblick} <green>\r\n"
        expected += "49.794497,9.94094 {Hochschule für Musik 1} <blue>\r\n"
        expected += "49.7948,9.930267 {Wuerzburger webcam} <pink>\r\n"
        expected += "49.790983,9.9323 {DOM FINAL (GC1QNWT)} <yellow>\r\n"            # free waypoints
        expected += "49.76015,9.9909 {BLICK ZUM RANDERSACKERER K\xc4PPE} <yellow>\r\n"
        with open("mapinfo.txt", "rb") as mapinfo:
            result = mapinfo.read().decode("cp1252")
        self.assertEqual(expected, result)

    def tearDown(self):
        """delete mapinfo.txt file"""
        os.remove("mapinfo.txt")


class TestAddWaypointToFiles(unittest.TestCase):

    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"../tests/examples/no_logfile_waypoints")

    def test_add_new_file(self):
        struct_time = time.strptime("30 Nov 00 20 17 05", "%d %b %y %H %M %S")
        wpt = geocache.Waypoint("NEW", [49.792433, 9.932233])
        with mock.patch("time.localtime", return_value=struct_time):
            self.x._add_waypoint_to_files(wpt)

        string = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com/GPX'
        string += '/1/1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:wptx1="http://www.'
        string += 'garmin.com/xmlschemas/WaypointExtension/v1" xmlns:gpxtpx="http://www.garmin.com/xmlschemas/'
        string += 'TrackPointExtension/v1" creator="eTrex 10" version="1.1" xmlns:xsi="http://www.w3.org/2001/'
        string += 'XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.'
        string += 'topografix.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www8.'
        string += 'garmin.com/xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/WaypointExtension/v1 '
        string += 'http://www8.garmin.com/xmlschemas/WaypointExtensionv1.xsd http://www.garmin.com/xmlschemas/'
        string += 'TrackPointExtension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd"><metadata>'
        string += '<link href="http://www.garmin.com"><text>Garmin International</text></link>'
        string += '<time>2000-11-30T20:17:05Z</time></metadata><wpt lat="49.792433" '
        string += 'lon="9.932233"><time>2000-11-30T20:17:05Z</time><name>NEW</name><sym>Flag, Blue</sym></wpt></gpx>'
        with open(r"../tests/examples/no_logfile_waypoints/GPX/Waypoints_30-NOV-00.gpx") as wptfile:
            content = wptfile.read()

        self.assertEqual(string, content)
        os.remove(r"../tests/examples/no_logfile_waypoints/GPX/Waypoints_30-NOV-00.gpx")

    def test_add_wpt_to_existing_file_ger(self):
        shutil.copy2(r"../tests/examples/no_logfile_waypoints/GPX/Wegpunkte_14-JAN-17.gpx",
                     r"../tests/examples/temp/Wegpunkte_14-JAN-17.gpx")  # copy file that is to be changed

        struct_time = time.strptime("14 Jan 17 13 07 25", "%d %b %y %H %M %S")
        wpt = geocache.Waypoint("NEW", [49.792433, 9.932233])
        with mock.patch("time.localtime", return_value=struct_time):
            self.x._add_waypoint_to_files(wpt)

        expected = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com/GPX/1/' \
                   '1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:wptx1="http://www.garmin.' \
                   'com/xmlschemas/WaypointExtension/v1" xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPoint' \
                   'Extension/v1" creator="eTrex 10" version="1.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance' \
                   '" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd ' \
                   'http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www8.garmin.com/xmlschemas/GpxExtensions' \
                   'v3.xsd http://www.garmin.com/xmlschemas/WaypointExtension/v1 http://www8.garmin.com/xmlschemas/' \
                   'WaypointExtensionv1.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.' \
                   'com/xmlschemas/TrackPointExtensionv1.xsd"><metadata><link href="http://www.garmin.com"><text>Garmin' \
                   ' International</text></link><time>2017-01-14T13:42:12Z</time></metadata><wpt lat="49.792433" ' \
                   'lon="9.932233"><time>2017-01-14T13:43:14Z</time><name>MÄRCHENSTUHL 2 (GC1XRPM)</name><sym>Flag, ' \
                   'Blue</sym></wpt><wpt lat="49.790983" lon="9.932300"><ele>231.912979</ele><time>2017-01-14T19:02:03Z' \
                   '</time><name>DOM FINAL (GC1QNWT)</name><sym>Flag, Blue</sym></wpt><wpt lat="49.792433" ' \
                   'lon="9.932233"><time>2017-01-14T13:07:25Z</time><name>NEW</name><sym>Flag, Blue</sym></wpt></gpx>'

        with open(r"../tests/examples/no_logfile_waypoints/GPX/Wegpunkte_14-JAN-17.gpx", encoding="utf-8") as wptfile:
            content = wptfile.read()

        self.assertEqual(content, expected)

        shutil.move(r"../tests/examples/temp/Wegpunkte_14-JAN-17.gpx",
                    r"../tests/examples/no_logfile_waypoints/GPX/Wegpunkte_14-JAN-17.gpx")  # move file back

    def test_add_wpt_to_existing_file_eng(self):

        shutil.copy2(r"../tests/examples/no_logfile_waypoints/GPX/Waypoints_11-MAR-17.gpx",
                     r"../tests/examples/temp/Waypoints_11-MAR-17.gpx")  # copy file that is to be changed

        struct_time = time.strptime("11 Mar 17 13 07 25", "%d %b %y %H %M %S")
        wpt = geocache.Waypoint("NEW", [49.792433, 9.932233])
        with mock.patch("time.localtime", return_value=struct_time):
            self.x._add_waypoint_to_files(wpt)

        expected = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com/GPX/1/' \
                   '1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:wptx1="http://www.garmin.' \
                   'com/xmlschemas/WaypointExtension/v1" xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPoint' \
                   'Extension/v1" creator="eTrex 10" version="1.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance' \
                   '" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd ' \
                   'http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www8.garmin.com/xmlschemas/GpxExtensionsv3' \
                   '.xsd http://www.garmin.com/xmlschemas/WaypointExtension/v1 http://www8.garmin.com/xmlschemas/' \
                   'WaypointExtensionv1.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.' \
                   'com/xmlschemas/TrackPointExtensionv1.xsd"><metadata><link href="http://www.garmin.com"><text>Garmin' \
                   ' International</text></link><time>2017-03-11T13:42:47Z</time></metadata><wpt lat="49.760150" ' \
                   'lon="9.990900"><ele>216.568268</ele><time>2017-03-11T13:44:53Z</time><name>BLICK ZUM RANDERSACKERER' \
                   ' KÄPPE</name><sym>Flag, Blue</sym></wpt><wpt lat="49.792433" ' \
                   'lon="9.932233"><time>2017-03-11T13:07:25Z</time><name>NEW</name><sym>Flag, Blue</sym></wpt></gpx>'

        with open(r"../tests/examples/no_logfile_waypoints/GPX/Waypoints_11-MAR-17.gpx", encoding="utf-8") as wptfile:
            content = wptfile.read()

        self.assertEqual(content, expected)

        shutil.move(r"../tests/examples/temp/Waypoints_11-MAR-17.gpx",
                    r"../tests/examples/no_logfile_waypoints/GPX/Waypoints_11-MAR-17.gpx")  # move file back


class TestAddWaypoints(unittest.TestCase):

    def setUp(self):
        """creates a gpscontent object for the tests"""
        self.x = gpscontent.GPSContent(r"../tests/examples/no_logfile_waypoints")

    def test_add_one_wpt_without_assigning(self):

        struct_time = time.strptime("02 Oct 17 20 17 05", "%d %b %y %H %M %S")
        with mock.patch('builtins.input', side_effect=["NEW", "N 49\xb057.340, E 009\xb034.222", "n", "n"]):
            with mock.patch("time.localtime", return_value=struct_time):
                self.x.add_waypoints()
        self.assertEqual(len(self.x.waypoints), 3)  # before: 2
        file_exists = os.path.isfile(r"../tests/examples/no_logfile_waypoints/GPX/Waypoints_02-OCT-17.gpx")
        self.assertTrue(file_exists)

        os.remove(r"../tests/examples/no_logfile_waypoints/GPX/Waypoints_02-OCT-17.gpx")

    def test_add_several_wpts_without_assigning(self):

        struct_time = time.strptime("02 Oct 17 20 17 05", "%d %b %y %H %M %S")
        with mock.patch('builtins.input', side_effect=["NEW", "N 49\xb057.340, E 009\xb034.222", "n", "y", "TWO",
                                                              "N 39\xb057.340, E 010\xb034.222", "n", "n"]):
            with mock.patch("time.localtime", return_value=struct_time):
                self.x.add_waypoints()
        self.assertEqual(len(self.x.waypoints), 4)  # before: 2

        expected = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com/GPX/1/' \
                   '1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:wptx1="http://www.garmin.' \
                   'com/xmlschemas/WaypointExtension/v1" xmlns:gpxtpx="http://www.garmin.com/xmlschemas/TrackPoint' \
                   'Extension/v1" creator="eTrex 10" version="1.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance' \
                   '" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd ' \
                   'http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www8.garmin.com/xmlschemas/GpxExtensionsv3' \
                   '.xsd http://www.garmin.com/xmlschemas/WaypointExtension/v1 http://www8.garmin.com/xmlschemas/' \
                   'WaypointExtensionv1.xsd http://www.garmin.com/xmlschemas/TrackPointExtension/v1 http://www.garmin.' \
                   'com/xmlschemas/TrackPointExtensionv1.xsd"><metadata><link href="http://www.garmin.com"><text>Garmin' \
                   ' International</text></link><time>2017-10-02T20:17:05Z</time></metadata>' \
                   '<wpt lat="49.955666666666666" lon="9.570366666666667">' \
                   '<time>2017-10-02T20:17:05Z</time><name>NEW</name><sym>Flag, Blue</sym>' \
                   '</wpt><wpt lat="39.955666666666666" lon="10.570366666666667"' \
                   '><time>2017-10-02T20:17:05Z</time><name>TWO</name><sym>Flag, Blue</sym></wpt></gpx>'
        with open(r"../tests/examples/no_logfile_waypoints/GPX/Waypoints_02-OCT-17.gpx") as wptfile:
            content = wptfile.read()
        self.assertEqual(content, expected)

        os.remove(r"../tests/examples/no_logfile_waypoints/GPX/Waypoints_02-OCT-17.gpx")

    def test_add_one_with_assigning_to_suggestion(self):

        shutil.copy2(r"../tests/examples/no_logfile_waypoints/GPX/GC6K86W.gpx",
                     r"../tests/examples/temp/GC6K86W.gpx")

        struct_time = time.strptime("02 Oct 17 20 17 05", "%d %b %y %H %M %S")
        with mock.patch('builtins.input', side_effect=["SAALE", "N 49\xb057.340, E 009\xb034.222", "y", "1", "n"]):
            with mock.patch("time.localtime", return_value=struct_time):
                self.x.add_waypoints()

        self.assertEqual(len(self.x.waypoints), 2)  # still two because waypoints belongs to cache
        file_exists = os.path.isfile(r"../tests/examples/no_logfile_waypoints/GPX/Waypoints_02-OCT-17.gpx")
        self.assertTrue(file_exists)

        for gc in self.x.geocaches:
            if gc.gccode == "GC6K86W":
                self.assertEqual(len(gc.waypoints), 1)

        os.remove(r"../tests/examples/no_logfile_waypoints/GPX/Waypoints_02-OCT-17.gpx")
        shutil.move(r"../tests/examples/temp/GC6K86W.gpx",
                    r"../tests/examples/no_logfile_waypoints/GPX/GC6K86W.gpx")

    def test_add_one_with_assigning_to_other(self):

        shutil.copy2(r"../tests/examples/no_logfile_waypoints/GPX/GC1XRPM.gpx",
                     r"../tests/examples/temp/GC1XRPM.gpx")

        struct_time = time.strptime("02 Oct 17 20 17 05", "%d %b %y %H %M %S")
        with mock.patch('builtins.input', side_effect=["SAALE", "N 49\xb057.340, E 009\xb034.222", "y", "2",
                                                       "GC1XRPM", "n"]):
            with mock.patch("time.localtime", return_value=struct_time):
                self.x.add_waypoints()

        self.assertEqual(len(self.x.waypoints), 2)  # still two because waypoints belongs to cache
        file_exists = os.path.isfile(r"../tests/examples/no_logfile_waypoints/GPX/Waypoints_02-OCT-17.gpx")
        self.assertTrue(file_exists)

        for gc in self.x.geocaches:
            if gc.gccode == "GC1XRPM":
                self.assertEqual(len(gc.waypoints), 2)

        os.remove(r"../tests/examples/no_logfile_waypoints/GPX/Waypoints_02-OCT-17.gpx")
        shutil.move(r"../tests/examples/temp/GC1XRPM.gpx",
                    r"../tests/examples/no_logfile_waypoints/GPX/GC1XRPM.gpx")

    def test_add_one_with_assigning_to_other_not_successfull(self):

        struct_time = time.strptime("02 Oct 17 20 17 05", "%d %b %y %H %M %S")
        with mock.patch('builtins.input', side_effect=["SAALE", "N 49\xb057.340, E 009\xb034.222", "y", "2",
                                                       "fewufeiwf", "n"]):
            with mock.patch("time.localtime", return_value=struct_time):
                self.x.add_waypoints()

        self.assertEqual(len(self.x.waypoints), 3)  # new waypoint is in here
        file_exists = os.path.isfile(r"../tests/examples/no_logfile_waypoints/GPX/Waypoints_02-OCT-17.gpx")
        self.assertTrue(file_exists)

        os.remove(r"../tests/examples/no_logfile_waypoints/GPX/Waypoints_02-OCT-17.gpx")


def create_testsuite():
    """creates a testsuite with out of all tests in this file"""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestInitNoLogfile))
    suite.addTest(unittest.makeSuite(TestInitWaypoints))
    suite.addTest(unittest.makeSuite(TestInitOnlyFound))
    suite.addTest(unittest.makeSuite(TestInitOnlyNotFound))
    suite.addTest(unittest.makeSuite(TestInitNotOnlyFound))
    suite.addTest(unittest.makeSuite(TestInitNotOnlyFoundNoBOM))
    suite.addTest(unittest.makeSuite(TestInitFoundNotOnGPS))
    suite.addTest(unittest.makeSuite(TestInitNotFoundNotOnGPS))
    suite.addTest(unittest.makeSuite(TestInitErrorInGPX))
    suite.addTest(unittest.makeSuite(TestGetLoggedAndFoundCachesOnlyFound))
    suite.addTest(unittest.makeSuite(TestGetLoggedAndFoundCachesNotOnlyFound))
    suite.addTest(unittest.makeSuite(TestGetLoggedAndFoundCachesNotOnlyFoundNoBOM))
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
    suite.addTest(unittest.makeSuite(TestShowFoundsOnlyFoundWaypoints))
    suite.addTest(unittest.makeSuite(TestShowFoundsNotOnlyFound))
    suite.addTest(unittest.makeSuite(TestShowFoundsFoundNotOnGPS))
    suite.addTest(unittest.makeSuite(TestDelete))
    suite.addTest(unittest.makeSuite(TestShowWaypoints))
    suite.addTest(unittest.makeSuite(TestReplaceWaypointName))
    suite.addTest(unittest.makeSuite(TestTryCreatingWaypoints))
    suite.addTest(unittest.makeSuite(TestDeleteWaypointFromFiles))
    suite.addTest(unittest.makeSuite(TestRewriteWaypointfiles))
    suite.addTest(unittest.makeSuite(TestFindSuggestions))
    suite.addTest(unittest.makeSuite(TestAssignWaypoints))
    suite.addTest(unittest.makeSuite(TestCreateMapinfoOne))
    suite.addTest(unittest.makeSuite(TestCreateMapinfoSeveral))
    suite.addTest(unittest.makeSuite(TestCreateWaypointfilestrings))
    suite.addTest(unittest.makeSuite(TestShowOnMap))
    suite.addTest(unittest.makeSuite(TestAddWaypointToFiles))
    suite.addTest(unittest.makeSuite(TestAddWaypoints))
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
