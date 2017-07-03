#!/usr/bin/python
# -*- coding: utf-8 -*-

"""This file contains the class GPSContent (for everything that is saved on the GPS device)."""

import os
import glob
import webbrowser
import subprocess
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
    
    delete(cachelist): deletes all caches in cachelist from gps-device
    
    show_founds(): shows all caches that are marked as found and performs actions with them if desired
    
    search(): searches caches for desired criterion and returns list of geocaches that match to search
    
    actions_after_search(search_results): performs different actions with search results
    
    show_all_on_map(cachelist): provides the possiblitly to show all caches in cachelist on a map
                                (uses webservice 'www.mapcustomizer.com')

    """

    def __init__(self, path):
        """reads geocaches, waypoints and logfile from gps-device"""
        
        self.path = path              
        self.found_exists = False     
        self.warning = False          
        self.existing_attributes = []
        
        self.geocaches = []               # read all caches from GC*.gpx-files in path\GPX and save in list 'geocaches'
        gpx_path = os.path.join(self.path, "GPX")
        for gpxfile in glob.glob(os.path.join(gpx_path, "GC*.gpx")):
            # noinspection PyBroadException
            # (broad exception necessary because ParseError unknown)
            try:
                self.geocaches.append(Geocache(gpxfile))
            except:
                user_io.general_output("{}: {}".format(user_io.WARNING_BROKEN_FILE, os.path.basename(gpxfile)))

        self.waypoints = []  # read all caches from GC*.gpx-files in path\GPX and save in list 'waypoints'
        for wptfile in glob.glob(os.path.join(gpx_path, "Wegpunkte_*.gpx")):
            # noinspection PyBroadException
            # (broad exception necessary because ParseError unknown)
            try:
                self.waypoints += self._read_waypoints(wptfile)
            except:
                user_io.general_output("{}: {}".format(user_io.WARNING_BROKEN_FILE, os.path.basename(wptfile)))
            
        for g in self.geocaches:      # read existing attributes from geocaches
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

        user_io.general_output("\n{} {} {} {} {}".format(len(self.geocaches), user_io.GEOCACHES, user_io.AND,
                                                         len(self.waypoints), user_io.WAYPOINTS_ON_DEVICE))

    @staticmethod
    def _read_waypoints(wptfile):
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
        if len(namelist) == len(coordlist):
            for i, name in enumerate(namelist):
                w = Waypoint(name, coordlist[i])
                # TODO: see if waypoint belongs to a geocache
                waypoints.append(w)

        return waypoints

    def _get_logged_and_found_caches(self):
        """reads logged and found caches from logfile 'geocache_visits.txt'
        (ignores those that are not saved on device as gpx-files), part of __init__
        
        return: list of two elements which are also lists
            first element: logged caches (not as Geocache-objects but as list [gc-code, date-and-time, logtype])
            second element: list of found caches as Geocache-objects"""

        logged_caches_raw = []           
        with open(os.path.join(self.path, "geocache_visits.txt")) as visits:
            visits = visits.read().decode("utf-16")
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
                try:
                    found_caches.append(Geocache(os.path.join(self.path, "GPX", lc[0]+".gpx")))
                    logged_caches_new.append(lc)
                except IOError:
                    user_io.general_output("\nWARNUNG! Der Geocache {} befindet sich nicht auf dem Geraet. \
                    Er wird daher im Folgenden nicht mehr beruecksichtigt.".format(lc[0]))
            else:
                try:
                    Geocache(os.path.join(self.path, "GPX", lc[0]+".gpx"))
                    logged_caches_new.append(lc)
                except IOError:
                    user_io.general_output("\nWARNUNG! Der Geocache {} befindet sich nicht auf dem Geraet. \
                    Er wird daher im Folgenden nicht mehr beruecksichtigt.".format(lc[0]))
        return [logged_caches_new, found_caches]

    def sort_and_show_caches(self):
        """sorts all caches by criterion that is defined by the user and shows them"""
        
        [criterion, rev] = user_io.sort_caches()
        if criterion == "distance":   # read coordinates from user input
            coords_str = user_io.coordinates_input()
            coords = ownfunctions.coords_string_to_decimal(coords_str)
            
            if coords:             # if reading coordinates successful
                for g in self.geocaches:
                    g.distance = ownfunctions.calculate_distance(g.coordinates, coords)  # calculate distance
                self.geocaches = sorted(self.geocaches, key=lambda geocache: getattr(geocache, criterion), reverse=rev)
                user_io.general_output(self.show_all_dist())
            else:
                user_io.general_output(user_io.INVALID_INPUT)
            
        elif criterion == "name":    # criterions for which capitalization doesn't matter
            self.geocaches = sorted(self.geocaches, key=lambda geocache: getattr(geocache, criterion).lower(), reverse=rev)
            user_io.general_output(self.show_all())
        else:                    # criterions for which capitalization matters
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
            newline = u"{:7}km | {}\n".format(round(c.distance, 1), c.shortinfo())
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
        if cache:
            user_io.general_output(cache.longinfo())
        
            while True:
                task = user_io.show_one()
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
                    url = u"https://www.google.de/maps/place/{}".format(coords_sec)
                    webbrowser.open_new_tab(url)
                else:
                    break

    def show_one_gccom(self):
        """opens one cache on geocaching.com"""

        cache = self.read_cache()
        if cache:
            webbrowser.open_new_tab(cache.url)

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
            newline = u"{:7}km | {}\n".format(round(c.distance, 1), c.shortinfo())
            text += newline
        return text
        
    def search(self):
        """searches caches for desired criterion and returns list of geocaches that match to search"""
        
        search_results = []
        criterion = user_io.search()
        if criterion == "name" or criterion == "description":    # search for name or description
            keyword = user_io.input_decode(user_io.SEARCH_FOR)
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
        elif criterion == "size":                                           # search by size
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
        elif criterion == "downloaddate":                               # search by downloaddate
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
                            if first_date <= c.downloaddate <= last_date:
                                search_results.append(c) 
        elif criterion == "available":                # search by availibility
            input_str = user_io.general_input(user_io.CACHES_AVAILABLE_OR_NOT)
            if input_str == "n":
                for c in self.geocaches:
                    if not c.available:
                        search_results.append(c)
            else:      # if invalid input: show available caches
                for c in self.geocaches:
                    if c.available:
                        search_results.append(c)
        elif criterion == "type":                    # search by cachetype
            inp = user_io.search_type()
            if inp not in TYPE_LIST:
                user_io.general_output(user_io.INVALID_INPUT)
            else:
                for c in self.geocaches:
                    if c.type == inp:
                        search_results.append(c)
        elif criterion == "attribute":              # search by attribute
            inp = user_io.search_attribute(self.existing_attributes)
            if inp not in self.existing_attributes:
                user_io.general_output(user_io.INVALID_INPUT)
            else:
                for c in self.geocaches:
                    if inp in c.attributes:
                        search_results.append(c)
        elif criterion == "distance":                # search by distance to a given point
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
        
        if len(search_results) == 0:                        # print search results
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
                    self.show_all_on_map(search_results)
                elif task == "show_one":
                    self.show_one()
                elif task == "show_one_gc.com":
                    self.show_one_gccom()
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
            for c in cachelist:
                os.remove(c.filename_path)
            removelist = []
            for c1 in self.geocaches:
                for c2 in cachelist:
                    if c1 == c2:
                        removelist.append(c1)
            self.geocaches = [c for c in self.geocaches if c not in removelist]
        return delete
        
    @staticmethod
    def show_all_on_map(cachelist):
        """shows all caches in cachelist on a map (uses webservice 'www.mapcustomizer.com')"""
    
        editor = user_io.show_all_on_map_start()
        with open("mapinfo.txt", "w") as mapinfo:
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
                else:                        # cache of unknown type
                    color = "pink"
                mapinfo.write("{},{} {{{}}} <{}>\n".
                              format(g.coordinates[0], g.coordinates[1], g.name.encode(user_io.CODING), color))
        subprocess.Popen([editor, "mapinfo.txt"])
        webbrowser.open_new_tab("https://www.mapcustomizer.com/#bulkEntryModal") 
        user_io.show_all_on_map_end()
        os.remove("mapinfo.txt")
