#!/usr/bin/python
# -*- coding: utf-8 -*-

"""This file contains the class GPSContent (for everything that is saved on the GPS device)."""

import os
import glob
import webbrowser
import subprocess
import time
import xml.etree.ElementTree as ElementTree

from geocache import TYPE_LIST, SIZE_LIST
from geocache import Geocache, Waypoint
import user_io
import ownfunctions


class GPSContent(object):
    """
    An object of this class contains all relevant information from the gps-device (or from another user-defined place)
    
    
    Attributes:
    ----------
    path: string
        path to gps-device (or other place where the information should be read from)
        
    geocaches: list
        list with all geocaches

    waypoints: list
        list with all waypoints that do not belong to a geocache
        
    existing_attributes: list
        list with all attributes existing in the geocaches
        
    found_exists: bool
        is True, if caches are marked as found on gps-device
    
    found_caches: list
        list of all geocaches marked as found (if found_exists)
        
    warning: bool
        is True, if there are other caches beside the found ones in logfile (e.g. as not found, needs maintainance, ...)
    
    
    Methods:
    ---------
    __init__(path): creates a GPS_content-object from path to gps-device
    
    show_all(): returns a string with most important infos for each cache, each cache in one line
    
    show_all_dist(): returns a string with most important infos (+ distances) for each cache, each cache in one line
    
    show_gc_selection(cachelist): returns a string with most important information of all caches in cachelist,
                                  each cache in one line
    
    show_gc_selection_dist(cachelist): returns a string with most important information (+ distances) of all caches in
                                       cachelist, each cache in one line
    
    sort_and_show_caches(): sorts all caches by criterion that is defined by the user and shows them"
    
    show_one(): shows detailed information about one cache and performs another actions with it if desired

    show_waypoints(): shows all free waypoints and lets the user choose what to do next
    
    delete(cachelist): deletes all caches in cachelist from gps-device
    
    show_founds(): shows all caches that are marked as found and performs actions with them if desired
    
    search(): searches caches for desired criterion and returns list of geocaches that match to search
    
    actions_after_search(search_results): performs different actions with search results
    
    show_on_map(cachelist, one=False): provides the possiblitly to show all caches in cachelist on a map
                                (uses webservice 'www.mapcustomizer.com')

    find_suggestions(waypoint): finds suggestions to which cache the given waypoint should be assigned
                                (based on name similarity)

    assign_waypoints(): lets the user choose for every waypoint if the waypoint should be assigned to a geocache
                        (and to which) or if it should be deleted

    delete_waypoint_from_files(waypointfiles, waypoint): deletes waypoint from waypointfiles (list of strings
                                                         where each string is the content of one waypointfile)

    create_waypointfilestrings(self): creates two lists (one with names and one with contents) out of waypointfiles

    rewrite_waypointfiles(wptfile_names, wpt_files): overwrite waypoint files on GPS-device by new content

    show_map_menu(): calls the map menu
    """

    def __init__(self, path):
        """reads geocaches, waypoints and logfile from gps-device"""

        self.path = path
        self.found_exists = False
        self.warning = False
        self.existing_attributes = []

        self.geocaches = []  # read all caches from GC*.gpx-files in path\GPX and save in list 'geocaches'
        gpx_path = os.path.join(self.path, "GPX")
        for gpxfile in glob.glob(os.path.join(gpx_path, "GC*.gpx")):
            try:
                self.geocaches.append(Geocache(gpxfile))
            except ElementTree.ParseError:
                user_io.general_output("{}: {}".format(user_io.WARNING_BROKEN_FILE, os.path.basename(gpxfile)))
            except AttributeError:
                user_io.general_output("{}: {}".format(user_io.WARNING_BROKEN_FILE, os.path.basename(gpxfile)))

        self.waypoints = []  # read all caches from Waypoints*.gpx-files in path\GPX and save in list 'waypoints'
        for wptfile in (glob.glob(os.path.join(gpx_path, "Wegpunkte_*.gpx")) +
                        glob.glob(os.path.join(gpx_path, "Waypoints_*.gpx"))):
            try:
                self.waypoints += self._read_waypoints(wptfile)
            except ElementTree.ParseError:
                user_io.general_output("{}: {}".format(user_io.WARNING_BROKEN_FILE, os.path.basename(wptfile)))

        for g in self.geocaches:  # read existing attributes from geocaches
            for a in g.attributes:
                if a not in self.existing_attributes and a != "No attributes specified by the author":
                    self.existing_attributes.append(a)
        self.existing_attributes.sort()

        # save all found caches from logfile in found_caches (if logfile is present)
        if os.path.isfile(os.path.join(self.path, "geocache_visits.txt")):
            [logged_caches, self.found_caches] = self._get_logged_and_found_caches()
            if len(self.found_caches) > 0:
                self.found_exists = True
            if len(self.found_caches) < len(logged_caches):
                self.warning = True  # warning, if caches in logfile that are marked as something different (not found)
            else:
                self.warning = False

        if self.waypoints:
            user_io.general_output("\n{} {} {} {} {} {}".format(len(self.geocaches), user_io.GEOCACHES, user_io.AND,
                                                                len(self.waypoints), user_io.WAYPOINTS, user_io.ON_DEVICE))
        else:
            user_io.general_output("\n{} {} {}".format(len(self.geocaches), user_io.GEOCACHES, user_io.ON_DEVICE))

    def _read_waypoints(self, wptfile):
        """read waypoints from waypoint-gpx-file and return list of waypoints, part of __init__"""

        wpt_tree = ElementTree.parse(wptfile)  # read .gpx-Datei

        names_raw = wpt_tree.findall(".//{http://www.topografix.com/GPX/1/1}name")  # find name of every waypoint
        namelist = []
        for n in names_raw:
            namelist.append(n.text)

        coords_raw = wpt_tree.findall(".//{http://www.topografix.com/GPX/1/1}wpt")  # find coordinates for every waypoint
        coordlist = []
        for c in coords_raw:
            coords = [float(c.get("lat")), float(c.get("lon"))]
            coordlist.append(coords)

        waypoints = []
        if len(namelist) == len(coordlist):  # as many names as coordinates (else file is broken)
            for i, name in enumerate(namelist):  # for every waypoint (defined by name)
                w = Waypoint(name, coordlist[i])  # create waypoint out of name and coordinates
                last_word = w.name.split()[-1]
                belongs_to_cache = False
                if last_word.startswith("(GC") and last_word.endswith(")"):  # decide if waypoint belongs to cache
                    gc = last_word[1:-1]
                    for c in self.geocaches:
                        if gc == c.gccode:
                            belongs_to_cache = True
                            c.add_waypoint(w)  # if yes add waypoint to cache
                            break
                if not belongs_to_cache:
                    waypoints.append(w)  # if not add waypoint to gps
        else:
            user_io.general_output(user_io.WARNING_BROKEN_FILE)

        return waypoints

    def _get_logged_and_found_caches(self):
        """reads logged and found caches from logfile 'geocache_visits.txt'
        (ignores those that are not saved on device as gpx-files), part of __init__
        
        return: list of two elements which are also lists
            first element: logged caches (not as Geocache-objects but as list [gc-code, date-and-time, logtype])
            second element: list of found caches as Geocache-objects"""

        logged_caches_raw = []
        with open(os.path.join(self.path, "geocache_visits.txt"), encoding="utf-16") as visits:
            try:
                visits = visits.read()  # file has BOM
            except UnicodeError:
                with open(os.path.join(self.path, "geocache_visits.txt"), encoding="utf-16-le") as visits2:
                    visits = visits2.read()   # file has no BOM
            visits_lines = visits.split("\n")
            for line in visits_lines:
                logged_caches_raw.append(line)
        logged_caches = []
        for lcr in logged_caches_raw:
            lcr = lcr.split(",")
            lcr.remove(lcr[-1])
            if len(lcr) > 0:
                logged_caches.append(lcr)
        found_caches = []
        logged_caches_new = []
        for lc in logged_caches:
            if lc[-1] == "Found it":
                on_gpx = False
                for gc in self.geocaches:
                    if gc.gccode == lc[0]:
                        found_caches.append(gc)
                        on_gpx = True
                        break
                if on_gpx:
                    logged_caches_new.append(lc)
                else:
                    user_io.general_output("\nWARNUNG! Der Geocache {} befindet sich nicht auf dem Geraet. \
                    Er wird daher im Folgenden nicht mehr beruecksichtigt.".format(lc[0]))
            else:
                try:
                    Geocache(os.path.join(self.path, "GPX", lc[0] + ".gpx"))
                    logged_caches_new.append(lc)
                except IOError:
                    user_io.general_output("\nWARNUNG! Der Geocache {} befindet sich nicht auf dem Geraet. \
                    Er wird daher im Folgenden nicht mehr beruecksichtigt.".format(lc[0]))
        return [logged_caches_new, found_caches]

    def sort_and_show_caches(self):
        """sorts all caches by criterion that is defined by the user and shows them"""

        [criterion, rev] = user_io.sort_caches()
        if criterion == "distance":  # read coordinates from user input
            coords_str = user_io.coordinates_input()
            coords = ownfunctions.coords_string_to_decimal(coords_str)

            if coords:  # if reading coordinates successful
                for g in self.geocaches:
                    g.distance = ownfunctions.calculate_distance(g.coordinates, coords)  # calculate distance
                self.geocaches = sorted(self.geocaches, key=lambda geocache: getattr(geocache, criterion), reverse=rev)
                user_io.general_output(self.show_all_dist())
            else:
                user_io.general_output(user_io.INVALID_INPUT)

        elif criterion == "name":  # criterions for which capitalization doesn't matter
            self.geocaches = sorted(self.geocaches, key=lambda geocache: getattr(geocache, criterion).lower(), reverse=rev)
            user_io.general_output(self.show_all())
        else:  # criterions for which capitalization matters
            self.geocaches = sorted(self.geocaches, key=lambda geocache: getattr(geocache, criterion), reverse=rev)
            user_io.general_output(self.show_all())

    def show_all(self):
        """returns a string with most important infos for each cache, each cache in one line"""
        text = ""
        for c in self.geocaches:
            text = text + c.shortinfo() + "\n"
        if len(self.geocaches) == 0:
            return user_io.NO_CACHES_ON_DEVICE
        return text

    def show_all_dist(self):
        """returns a string with most important infos (+ distances) for each cache, each cache in one line"""
        text = ""
        for c in self.geocaches:
            newline = "{:7}km | {}\n".format(round(c.distance, 1), c.shortinfo(12))
            text += newline
        if len(self.geocaches) == 0:
            return user_io.NO_CACHES_ON_DEVICE
        return text

    def read_cache(self):
        """asks the user for the gc-code and returns the cache if existent on gps,
        otherwise returns None"""
        gc = user_io.general_input(user_io.INPUT_GCCODE)
        cache = None
        for c in self.geocaches:
            if gc == c.gccode:
                cache = c
                break
        if not cache:
            user_io.general_output(user_io.GC_DOES_NOT_EXIST)
        else:
            return cache

    def show_one(self):
        """shows detailed information about one cache and performs another actions with it if desired"""

        cache = self.read_cache()
        if cache:    # if reading successful
            user_io.general_output(cache.longinfo())  # show information

            if ownfunctions.connected(cache.url):   # if internetconnection
                webbrowser.open_new_tab(cache.url)  # open description of cache on geocaching.com

            while True:                             # further actions
                wpt = False  # no waypoints exist
                if cache.waypoints:
                    wpt = True  # waypoints exist
                task = user_io.show_one(wpt)
                if task == "delete":
                    self.delete([cache])
                    break
                elif task == "gc.com":
                    webbrowser.open_new_tab(cache.url)
                elif task == "dist":
                    coords_str = user_io.coordinates_input()
                    coords = ownfunctions.coords_string_to_decimal(coords_str)
                    if coords:
                        d = ownfunctions.calculate_distance(coords, cache.coordinates)
                        user_io.general_output("Abstand: {} Kilometer".format(round(d, 1)))
                elif task == "gc-map":
                    latitude = cache.coordinates[0]
                    longitude = cache.coordinates[1]
                    url = "https://www.geocaching.com/map/#?ll={},{}&z=16".format(latitude, longitude)
                    webbrowser.open_new_tab(url)
                elif task == "googlemaps":
                    coords_sec = ownfunctions.coords_minutes_to_seconds(cache.coordinates_string)
                    url = "https://www.google.de/maps/place/{}".format(coords_sec)
                    webbrowser.open_new_tab(url)
                elif task == "mapcustomizer":
                    self.show_on_map(cache)
                else:
                    break

    @staticmethod
    def show_gc_selection(cachelist):
        """returns a string with most important information of all caches in cachelist, each cache in one line
        
        input: list of caches (as Geocache-objects) that are found on gps-device
        return: string with informations about these caches"""

        text = ""
        for c in cachelist:
            if type(c) != Geocache:
                raise TypeError("An Element of the selection is not a Geocache!")
            text = text + c.shortinfo() + "\n"
        return text

    @staticmethod
    def show_gc_selection_dist(cachelist):
        """returns a string with most important information (+ distances) of all caches in cachelist,
        each cache in one line
        
        input: list of caches (as Geocache-objects) that are found on gps-device
        return: string with informations about these caches"""

        text = ""
        for c in cachelist:
            if type(c) != Geocache:
                raise TypeError("An Element of the selection is not a Geocache!")
            newline = "{:7}km | {}\n".format(round(c.distance, 1), c.shortinfo(12))
            text += newline
        return text

    def search(self):
        """searches caches for desired criterion and returns list of geocaches that match to search"""

        search_results = []
        criterion = user_io.search()
        if criterion == "name" or criterion == "description":  # search for name or description
            keyword = user_io.general_input(user_io.SEARCH_FOR)
            for c in self.geocaches:
                if keyword in getattr(c, criterion):
                    search_results.append(c)
        elif criterion == "difficulty" or criterion == "terrain":  # search for difficulty or terrain value
            input_str = user_io.general_input("{}: ".format(user_io.MIN_MAX_SEPERATED_BY_KOMMA))
            inp = input_str.split(",")
            if len(inp) != 2:
                user_io.general_output(user_io.INVALID_INPUT)
            else:
                try:
                    mini = float(inp[0])
                    maxi = float(inp[1])
                except ValueError:
                    user_io.general_output(user_io.INVALID_INPUT)
                else:
                    if maxi >= mini >= 1.0 and mini <= 5.0 and 1.0 <= maxi <= 5.0:  # all values between 1 and 5
                        for c in self.geocaches:
                            if mini <= getattr(c, criterion) <= maxi:
                                search_results.append(c)
                    else:
                        user_io.general_output(user_io.INVALID_INPUT)
        elif criterion == "size":  # search by size
            input_str = user_io.general_input("{}. {}: other, micro, small, regular, large\n>>".
                                              format(user_io.MIN_MAX_SEPERATED_BY_KOMMA, user_io.POSSIBLE_SIZES))
            inp = input_str.split(",")
            if len(inp) != 2:
                user_io.general_output(user_io.INVALID_INPUT)
            else:
                try:
                    if inp[1][0] == " ":
                        max_str = inp[1][1:]
                    else:
                        max_str = inp[1]
                    mini = SIZE_LIST.index(inp[0])
                    maxi = SIZE_LIST.index(max_str)
                except ValueError:
                    user_io.general_output(user_io.INVALID_INPUT)
                else:
                    if maxi < mini:
                        user_io.general_output(user_io.INVALID_INPUT)
                    else:
                        for c in self.geocaches:
                            if mini <= c.size <= maxi:
                                search_results.append(c)
        elif criterion == "date":  # search by downloaddate
            input_str = user_io.general_input("{}\n>>".format(user_io.DATE_SEPERATED_BY_KOMMA))
            inp = input_str.split(",")
            if len(inp) != 2:
                user_io.general_output(user_io.INVALID_INPUT)
            else:
                first = inp[0]
                if inp[1][0] == " ":
                    last = inp[1][1:]
                else:
                    last = inp[1]
                try:
                    first_date = ownfunctions.string_to_date(first)
                    last_date = ownfunctions.string_to_date(last)
                except ValueError:
                    user_io.general_output(user_io.INVALID_INPUT)
                else:
                    if first_date > last_date:
                        user_io.general_output(user_io.INVALID_INPUT)
                    else:
                        for c in self.geocaches:
                            if first_date <= c.date <= last_date:
                                search_results.append(c)
        elif criterion == "available":  # search by availibility
            input_str = user_io.general_input(user_io.CACHES_AVAILABLE_OR_NOT)
            if input_str == "n":
                for c in self.geocaches:
                    if not c.available:
                        search_results.append(c)
            else:  # if invalid input: show available caches
                for c in self.geocaches:
                    if c.available:
                        search_results.append(c)
        elif criterion == "type":  # search by cachetype
            inp = user_io.search_type()
            if inp not in TYPE_LIST:
                user_io.general_output(user_io.INVALID_INPUT)
            else:
                for c in self.geocaches:
                    if c.type == inp:
                        search_results.append(c)
        elif criterion == "attribute":  # search by attribute
            inp = user_io.search_attribute(self.existing_attributes)
            if inp not in self.existing_attributes:
                user_io.general_output(user_io.INVALID_INPUT)
            else:
                for c in self.geocaches:
                    if inp in c.attributes:
                        search_results.append(c)
        elif criterion == "distance":  # search by distance to a given point
            coords_str = user_io.coordinates_input()
            coords = ownfunctions.coords_string_to_decimal(coords_str)
            if coords:
                input_str = user_io.general_input(user_io.DIST_SEPERATED_BY_KOMMA)
                inp = input_str.split(",")
                if len(inp) != 2:
                    user_io.general_output(user_io.INVALID_INPUT)
                else:
                    try:
                        mini = float(inp[0])
                        maxi = float(inp[1])
                    except ValueError:
                        user_io.general_output(user_io.INVALID_INPUT)
                    else:
                        for c in self.geocaches:
                            c.distance = ownfunctions.calculate_distance(coords, c.coordinates)
                            if mini <= c.distance <= maxi:
                                search_results.append(c)
            else:
                user_io.general_output(user_io.INVALID_INPUT)

        if len(search_results) == 0:  # print search results
            user_io.general_output(user_io.NO_CACHES_FOUND)
        else:
            if criterion == "distance":
                user_io.general_output(self.show_gc_selection_dist(search_results))
            else:
                user_io.general_output(self.show_gc_selection(search_results))
        return search_results

    def actions_after_search(self, search_results):
        """performs different actions with search results
        input: output from function search()"""

        if len(search_results) != 0:
            while True:
                task = user_io.actions_after_search()
                if task == "show_again":
                    user_io.general_output(self.show_gc_selection(search_results))
                elif task == "delete":
                    self.delete(search_results)
                elif task == "show_on_map":
                    self.show_on_map(search_results)
                elif task == "show_one":
                    self.show_one()
                elif task == "back":
                    break

    def show_founds(self):
        """shows all caches that are marked as found and performs actions with them if desired"""

        if not self.found_exists:
            raise ValueError("ERROR: no found caches")
        user_io.general_output(self.show_gc_selection(self.found_caches))
        while True:
            task = user_io.actions_with_founds()
            if task == "log":
                webbrowser.open_new_tab("https://www.geocaching.com/my/uploadfieldnotes.aspx")
            elif task == "delete":
                if self.warning:
                    user_io.general_output(user_io.WARNING_LOG_INFO)
                delete = self.delete(self.found_caches)
                if delete:
                    self.found_exists = False
                    os.remove(os.path.join(self.path, "geocache_visits.txt"))
                    os.remove(os.path.join(self.path, "geocache_logs.xml"))
                    break
            elif task == "exit":
                break

    def delete(self, cachelist):
        """deletes all caches in cachelist from gps-device
        
        input: list of caches that are to be deleted
        return: bool that is True if caches are deleted and False if not"""

        delete = user_io.confirm_deletion()
        if delete:
            wptfile_names, wptfile_strings = self.create_waypointfilestrings()
            for c in cachelist:
                os.remove(c.filename_path)  # delete cache from gps-device
                for w in c.waypoints:  # also delete waypoints from gps-device
                    wptfile_strings = self.delete_waypoint_from_files(wptfile_strings, w)
            removelist = []
            for c1 in self.geocaches:
                for c2 in cachelist:
                    if c1 == c2:
                        removelist.append(c1)

            self.geocaches = [c for c in self.geocaches if c not in removelist]  # geocaches without deleted
            self.rewrite_waypointfiles(wptfile_names, wptfile_strings)  # waypoints without deleted
        return delete

    def _create_mapinfo_several(self, cachelist, show_waypoints, free_waypoints):
        """creates a textfile from a list of caches that is used to configure the map on 'www.mapcustomizer.com'
        part of show_on_map
        input:
        cachelist: list of caches that are to be shown
        show_waypoints: determines if waypoints are shown on map, too
        free_waypoints: show also waypoints that don't belong to a cache (normally set to true if cachelist contains all
        caches on gpx-device and waypoints should be shown)"""

        with open("mapinfo.txt", "w", encoding=user_io.CODING) as mapinfo:
            for i, g in enumerate(cachelist):
                if g.type == "Traditional Cache":
                    color = "green"
                elif g.type == "Multi-cache":
                    color = "default"
                elif g.type == "EarthCache":
                    color = "tan"
                elif g.type == "Letterbox Hybrid" or g.type == "Geocaching HQ":
                    color = "gray"
                elif g.type == "Event Cache" or g.type == "Wherigo Cache":
                    color = "yellow"
                elif g.type == "Mystery Cache":
                    color = "blue"
                else:  # cache of unknown type
                    color = "pink"
                name = g.name
                if g.waypoints and show_waypoints:  # if waypoints: add gccode to name
                    name = "{} ({})".format(name, g.gccode)
                mapinfo.write("{},{} {{{}}} <{}>\n".format(g.coordinates[0], g.coordinates[1], name, color))
                if show_waypoints:  # waypoints belonging to cache
                    for w in g.waypoints:
                        mapinfo.write("{},{} {{{}}} <{}>\n".format(w.coordinates[0], w.coordinates[1], w.name, color))

            if free_waypoints:  # free waypoints
                for w in self.waypoints:
                    mapinfo.write("{},{} {{{}}} <{}>\n".format(w.coordinates[0], w.coordinates[1], w.name, "yellow"))

    @staticmethod
    def _create_mapinfo_one(cache):
        """creates a textfile from a cache with waypoints that is used to configure the map on 'www.mapcustomizer.com'
        part of show_on_map"""

        with open("mapinfo.txt", "w", encoding=user_io.CODING) as mapinfo:
            if cache.type == "Traditional Cache":  # cache itself
                color = "green"
            elif cache.type == "Multi-cache":
                color = "default"
            elif cache.type == "EarthCache":
                color = "tan"
            elif cache.type == "Letterbox Hybrid" or cache.type == "Geocaching HQ":
                color = "gray"
            elif cache.type == "Event Cache" or cache.type == "Wherigo Cache":
                color = "yellow"
            elif cache.type == "Mystery Cache":
                color = "blue"
            else:  # cache of unknown type
                color = "pink"

            mapinfo.write("{},{} {{{}}} <{}>\n".format(cache.coordinates[0], cache.coordinates[1], cache.name, color))

            for w in cache.waypoints:  # waypoints
                if color == "yellow":
                    color_w = "grey"
                else:
                    color_w = "yellow"
                mapinfo.write("{},{} {{{}}} <{}>\n".format(w.coordinates[0], w.coordinates[1], w.shown_name, color_w))

    def show_on_map(self, cachelist, all_caches=False):
        """shows all caches in cachelist on a map (uses webservice 'www.mapcustomizer.com')"""

        one = True
        if type(cachelist) == list:  # one is True if one cache, False if several caches
            one = False
        show_waypoints = False  # determines if waypoints are shown
        if not one:
            show_waypoints = user_io.ask_for_waypoints()
        free_waypoints = False
        if show_waypoints and all_caches:  # free waypoints are shown (only for all caches, not a selection)
            free_waypoints = True
        editor = user_io.show_on_map_start(one, free_waypoints)
        if one:
            self._create_mapinfo_one(cachelist)
        else:
            self._create_mapinfo_several(cachelist, show_waypoints, free_waypoints)
        subprocess.Popen([editor, "mapinfo.txt"])
        webbrowser.open_new_tab("https://www.mapcustomizer.com/#bulkEntryModal")
        user_io.show_on_map_end()
        os.remove("mapinfo.txt")

    def show_waypoints(self):
        """shows all free waypoints and lets the user choose what to do next"""

        if not self.waypoints:
            user_io.general_output(user_io.NO_WAYPOINTS_ON_DEVICE)
            inp = user_io.waypoint_menu(False)
            if inp == "add":
                self.add_waypoints()
        else:
            for w in self.waypoints:  # show waypoints
                user_io.general_output(w.info())
            inp = user_io.waypoint_menu(True)  # assign waypoints
            if inp == "assign":
                self.assign_waypoints()
            elif inp == "add":
                self.add_waypoints()

    @staticmethod
    def _try_creating_waypoint(name, coords):
        """try if a waypoint can be created from name and coords
        return waypoint if yes
        (part of add_waypoints) """

        try:
            ownfunctions.validate_coordinates(coords)
        except TypeError or ValueError:
            user_io.general_output(user_io.COORDINATES_WRONG + " " + user_io.NO_WAYPOINT_CREATED)
        else:
            if len(name) > 30:
                user_io.general_output(user_io.NAME_TO_LONG + " " + user_io.NO_WAYPOINT_CREATED)
            else:
                try:
                    w = Waypoint(name, coords)
                except TypeError:
                    user_io.general_output(user_io.NOT_ALLOWED_SIGNS + " " + user_io.NO_WAYPOINT_CREATED)
                else:
                    return w

    def _add_waypoint_to_files(self, waypoint):
        """adds waypoint to waypoint files on gps-device
        part of add_waypoints()"""

        now = time.localtime()
        month = ownfunctions.get_month(now.tm_mon).upper()
        year = ownfunctions.get_year_without_century(now.tm_year)
        filename = "Waypoints_{:02}-{}-{:02}.gpx".format(now.tm_mday, month, year)
        wptfile_path = os.path.join(self.path, "GPX", filename)
        filename_ger = "Wegpunkte_{:02}-{}-{:02}.gpx".format(now.tm_mday, month, year)
        wptfile_path_ger = os.path.join(self.path, "GPX", filename_ger)
        timestring = "{}-{:02}-{:02}T{:02}:{:02}:{:02}Z".format(now.tm_year, now.tm_mon, now.tm_mday,
                                                                now.tm_hour, now.tm_min, now.tm_sec)
        if os.path.isfile(wptfile_path):   # file Waypoints_XX-XX-XX.gpx exists
            wptstring = '<wpt lat="{}" lon="{}"><time>{}</time><name>{}</name><sym>Flag, Blue</sym></wpt>'.format(
                waypoint.coordinates[0], waypoint.coordinates[1], timestring, waypoint.name)
            with open(wptfile_path, encoding="utf-8") as wptfile:
                content = wptfile.read()
            newstring = content[:-6] + wptstring + "</gpx>"
            with open(wptfile_path, "w", encoding="utf-8") as wptfile_new:
                wptfile_new.write(newstring)
        elif os.path.isfile(wptfile_path_ger):   # file Wegpunkte_XX-XX-XX.gpx exists
            wptstring = '<wpt lat="{}" lon="{}"><time>{}</time><name>{}</name><sym>Flag, Blue</sym></wpt>'.format(
                waypoint.coordinates[0], waypoint.coordinates[1], timestring, waypoint.name)
            with open(wptfile_path_ger, encoding="utf-8") as wptfile:
                content = wptfile.read()
            newstring = content[:-6] + wptstring + "</gpx>"
            with open(wptfile_path_ger, "w", encoding="utf-8") as wptfile_new:
                wptfile_new.write(newstring)

        else:   # if no waypointfile from today exists -> create the file
            string = '<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com/GPX'
            string += '/1/1" xmlns:gpxx="http://www.garmin.com/xmlschemas/GpxExtensions/v3" xmlns:wptx1="http://www.'
            string += 'garmin.com/xmlschemas/WaypointExtension/v1" xmlns:gpxtpx="http://www.garmin.com/xmlschemas/'
            string += 'TrackPointExtension/v1" creator="eTrex 10" version="1.1" xmlns:xsi="http://www.w3.org/2001/'
            string += 'XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.'
            string += 'topografix.com/GPX/1/1/gpx.xsd http://www.garmin.com/xmlschemas/GpxExtensions/v3 http://www8.'
            string += 'garmin.com/xmlschemas/GpxExtensionsv3.xsd http://www.garmin.com/xmlschemas/WaypointExtension/v1 '
            string += 'http://www8.garmin.com/xmlschemas/WaypointExtensionv1.xsd http://www.garmin.com/xmlschemas/'
            string += 'TrackPointExtension/v1 http://www.garmin.com/xmlschemas/TrackPointExtensionv1.xsd"><metadata>'
            string += '<link href="http://www.garmin.com"><text>Garmin International</text></link><time>{}</time>'\
                .format(timestring)
            string += '</metadata><wpt lat="{}" lon="{}"><time>{}</time><name>{}</name><sym>Flag, Blue</sym></wpt></gpx>'\
                .format(waypoint.coordinates[0], waypoint.coordinates[1], timestring, waypoint.name)
            with open(wptfile_path, "w", encoding="utf-8") as wptfile:
                wptfile.write(string)

    def add_waypoints(self):
        """adds waypoints"""

        name, coordstr = user_io.wpt_ask_for_name_and_coords()
        coords = ownfunctions.coords_string_to_decimal(coordstr)
        wpt = self._try_creating_waypoint(name, coords)
        if wpt:
            inp = user_io.general_input("{} (y/n) ".format(user_io.ASSIGN_WAYPOINT_TO_CACHE))
            if inp == "y":
                suggestions = self.find_suggestions(wpt)
                cache = user_io.choose_cache(suggestions, False)
                if type(cache) == Geocache:  # assign waypoint accordning to suggestion
                    wpt.name = u"{} ({})".format(wpt.name, cache.gccode)
                    cache.add_waypoint(wpt)
                    self._add_waypoint_to_files(wpt)
                elif cache == "other":  # assign waypoint to other geocache
                    inp_gccode = user_io.general_input(user_io.INPUT_GCCODE).upper()
                    adding = False
                    for g in self.geocaches:
                        if g.gccode == inp_gccode:  # successfull assigning waypoint to cache
                            wpt.name = u"{} ({})".format(wpt.name, inp_gccode)
                            g.add_waypoint(wpt)
                            self._add_waypoint_to_files(wpt)
                            adding = True
                            break
                    if not adding:  # not successfull assigning waypoint to cache
                        self.waypoints.append(wpt)
                        self._add_waypoint_to_files(wpt)
                        user_io.general_output(user_io.GC_DOES_NOT_EXIST)
                else:
                    self.waypoints.append(wpt)
                    self._add_waypoint_to_files(wpt)
            else:
                self.waypoints.append(wpt)
                self._add_waypoint_to_files(wpt)
        inp = user_io.general_input("{} (y/n) ".format(user_io.ADD_WAYPOINT))
        if inp == "y":
            self.add_waypoints()

    def find_suggestions(self, waypoint):
        """finds suggestions to which cache the given waypoint should be assigned"""

        suggestions = []
        namelist = waypoint.name.split(" ")
        if namelist[-1] == "FINAL" or ownfunctions.string_is_int(namelist[-1]):
            namelist = namelist[:-1]  # if last word is "FINAL" oder a number: discard
        for g in self.geocaches:
            for word in namelist:     # suggest cache if one of the word in waypoint name also is in geocachename
                if word in g.name.upper():
                    suggestions.append(g)
                    break
        return suggestions

    @staticmethod
    def _replace_waypoint_name(waypointfiles, waypoint):
        """replaces the name of the waypoint in waypointfiles by the name + gccode of assigned geocache
        (part of assign_waypoints)

        input:
        waypointfiles: list of strings where each string is the content of one waypointfile
        waypoint: waypoint whose name should be changed

        returns new list of waypointfile strings"""

        wptfiles_new = []
        for cont in waypointfiles:
            old = "<name>{}</name>".format(waypoint.shown_name)
            new = "<name>{}</name>".format(waypoint.name)
            new_cont = cont.replace(old, new)
            wptfiles_new.append(new_cont)
        return wptfiles_new

    @staticmethod
    def delete_waypoint_from_files(waypointfiles, waypoint):
        """deletes waypoint from waypointfiles

        input:
        waypointfiles: list of strings where each string is the content of one waypointfile
        waypoint: waypoint who is to be deleted
        returns new list of waypointfile strings"""

        wptfiles_new = []
        for cont in waypointfiles:
            new_cont = ""
            cont_list = cont.split("</wpt><wpt ")  # split in single waypoints
            for i, wpt_cont in enumerate(cont_list):
                if len(cont_list) == 1:  # only one waypoint in file
                    x = wpt_cont.find("<name>{}</name>".format(waypoint.name))
                    if x != -1:  # waypoint present in current string
                        new_cont = ""  # delete everything
                    else:  # waypoint not present in current string
                        new_cont += wpt_cont
                elif i == 0:  # first waypoint in file
                    x = wpt_cont.find("<name>{}</name>".format(waypoint.name))
                    if x != -1:  # waypoint present in current string
                        new_cont += wpt_cont[:948]
                    else:  # waypoint not present in current string
                        new_cont += wpt_cont + "</wpt>"
                elif i == len(cont_list) - 1:  # last cache in file
                    x = wpt_cont.find(u"<name>{}</name>".format(waypoint.name))
                    if x != -1:  # waypoint present in current string
                        new_cont += "</gpx>"
                    else:  # waypoint not present in current string
                        new_cont += "<wpt " + wpt_cont
                else:  # neither first nor last cache in file with 3 or more caches
                    x = wpt_cont.find("<name>{}</name>".format(waypoint.name))
                    if x != -1:  # waypoint present in current string
                        new_cont += ""
                    else:  # waypoint not present in current string
                        new_cont += "<wpt " + wpt_cont + "</wpt>"
            wptfiles_new.append(new_cont)
        return wptfiles_new

    def create_waypointfilestrings(self):
        """creates two lists:
        wptfile_names: list of all names of waypointfiles on gps device
        wpt_files: list of strings, every string is the content of one waypointfile"""

        gpx_path = os.path.join(self.path, "GPX")
        wpt_files = []
        wptfile_names = glob.glob(os.path.join(gpx_path, "Wegpunkte_*.gpx"))
        wptfile_names += glob.glob(os.path.join(gpx_path, "Waypoints_*.gpx"))
        for wptfile_name in wptfile_names:
            with open(wptfile_name, encoding="utf-8") as wptfile:
                wpt_files.append(wptfile.read())
        return [wptfile_names, wpt_files]

    @staticmethod
    def rewrite_waypointfiles(wptfile_names, waypointfiles):
        """overwrite waypoint files on GPS-device by new content
        (used to assign or delete waypoints)

        input:
        wptfile_names: list of all names of waypointfiles (with path) on gps device
        wpt_files: list of strings, every string is the content of one waypointfile"""

        if len(wptfile_names) != len(waypointfiles):
            raise IOError("Invalid Input")

        for i, wptfile_cont in enumerate(waypointfiles):
            if not os.path.isfile(wptfile_names[i]):
                raise TypeError("{} is not an existing file".format(wptfile_names[i]))

            if wptfile_cont == "":  # if filestring is empty: delete file
                os.remove(wptfile_names[i])
            else:  # else write new content
                with open(wptfile_names[i], "w", encoding="utf-8") as wpt_file:
                    wpt_file.write(wptfile_cont)

    def assign_waypoints(self):
        """lets the user choose for every waypoint if the waypoint should be assigned to a geocache (and to which)
        or if it should be deleted"""

        wptfile_names, wpt_files = self.create_waypointfilestrings()

        waypoints_new = []
        for w in self.waypoints:
            user_io.general_output("\n{}: {}".format(user_io.CURRENT_WAYPOINT, w.name))
            suggestions = self.find_suggestions(w)
            inp = user_io.choose_cache(suggestions, True)
            if type(inp) == Geocache:  # assign waypoint accordning to suggestion
                w.name = "{} ({})".format(w.name, inp.gccode)
                inp.add_waypoint(w)
                wpt_files = self._replace_waypoint_name(wpt_files, w)
            elif inp == "other":  # assign waypoint to other geocache
                inp = user_io.general_input(user_io.INPUT_GCCODE).upper()
                adding = False
                for g in self.geocaches:
                    if g.gccode == inp:  # successfull assigning waypoint to cache
                        w.name = "{} ({})".format(w.name, inp)
                        g.add_waypoint(w)
                        adding = True
                        wpt_files = self._replace_waypoint_name(wpt_files, w)
                        break
                if not adding:  # not successfull assigning waypoint to cache
                    waypoints_new.append(w)
                    user_io.general_output("{} {}".format(user_io.GC_DOES_NOT_EXIST, user_io.WAYPOINT_LEFT_OUT))
            elif inp == "delete":  # delete waypoint
                if user_io.confirm_deletion_wpt():
                    wpt_files = self.delete_waypoint_from_files(wpt_files, w)
                else:
                    waypoints_new.append(w)
            else:
                waypoints_new.append(w)

        self.rewrite_waypointfiles(wptfile_names, wpt_files)  # write new files
        self.waypoints = waypoints_new  # save changes in programme

    def show_map_menu(self):
        """calls the map menu"""
        task = user_io.map_menu()
        if task == "show_on_map":
            self.show_on_map(self.geocaches, True)
        elif task == "google-maps":
            webbrowser.open_new_tab("https://www.google.de/maps")
        elif task == "gc-maps":
            webbrowser.open_new_tab("https://www.geocaching.com/map")
