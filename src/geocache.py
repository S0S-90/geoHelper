#!/usr/bin/python
# -*- coding: utf-8 -*-

"""This file contains the classes Geocache (for a single geocache) and
Waypoint (for a waypoint, consisting only of name and coordinates."""

import os
import time
import datetime
import xml.etree.ElementTree as ElementTree

import ownfunctions  

SIZE_LIST = ["other", "micro", "small", "regular", "large"]
TYPE_LIST = ["Traditional Cache", "Multi-cache", "EarthCache", "Letterbox Hybrid", "Event Cache", "Wherigo Cache",
             "Mystery Cache", "Geocaching HQ", "Unknown Type"]


# stringcollection for German language
STR_D = "Schwierigkeit"
STR_T = "Gelaende"
STR_SIZE = "Groesse"
STR_TYPE = "Typ"
STR_COORDS = "Koordinaten"
STR_OWNER = "Owner"
STR_ATTR = "Attribute"
STR_ACT = "Cache ist aktiv"
STR_DATE = "Stand"
STR_LINK = "Link"
STR_HINT = "Hinweis"
STR_WAYPOINTS = "Wegpunkte"


class Geocache(object):

    """
    An object of this class contains all relevant information of the corresponding gpx-file
    
    
    Attributes:
    -----------
    filename_path: string
        filename (including path)

    source: string
        'downloader' if gpx-file is created by geocaching.com gpx-downloader
        'geocaching.com' if gpx-file is created by geocaching.com itself
        
    gccode: string
        gc-code - used for overloaded operators == and != and is printed by "print"
        
    name: string
        name of the geocache
    
    difficulty: float
        difficulty value of the cache
        
    terrain: float
        terrain value of the cache
        
    size: int
        size of the cache as number (other = 0, then increasing by size)
        
    size_string: string
        size of the cache as word
        
    type: string
        type of the cache (member of TYPE_LIST)
        used in short description as well as for searching and sorting
        
    longtype: string
        type of the cache (any description possible)
        used in long description
    
    description: string
        description of the cache
        
    hint: string
        hint for the cache
        
    owner: string
        owner of the cache
        
    url: string
        weblink to the cache on geocaching.com 
        
    coordinates: list 
        coordinates in decimal degree, first element of the list: latitude, second element: longitude
        
    coordinates_string: string
        coordinates as degree and minutes
        
    attributes: list
        attributes of the cache
        
    logs: list
        last logs before download
        every element of list: list [date, logtype, name of logger (, logtext)]
                               last element only if gpx-file is created directly from geocaching.com
        
    available: bool 
        availability at the time of download 
        
    downloaddate: datetime.date
        date when the gpx-file was downloaded from geocaching.com
        
    downloaddate_string: string
        date when the gpx-file was downloaded from geocaching.com as string

    waypoints: list
        list of waypoints that belong to cache (empty if no waypoints)
    
    
    Methods:
    ---------
    __init__(filename_path): Create a Geocache-object out of the gpx-file (complete name with path)

    add_waypoint(self, waypoint): adds a waypoint to the cache
    
    shortinfo(space=0): string
        one-line information about the cache and the waypoints
        set space to 12 if cache is shown with distance
        
    longinfo(): 
        detailed information about the cache
    """
    
    def __init__(self, filename_path):
        """constructor: reads all attributes from gpx-file that has to be given by 'filename_path'"""
    
        if type(filename_path) != str:
            raise TypeError("Bad input.")

        self.filename_path = filename_path
        self.gccode = os.path.splitext(os.path.basename(self.filename_path))[0]  # gc-code

        downloaddate = time.ctime(os.path.getmtime(self.filename_path))  # read downloaddate (= change of gpx-file)
        downloaddate = ownfunctions.remove_spaces(downloaddate).split(" ")
        self.downloaddate_string = "{:02} {} {}".format(int(downloaddate[2]), downloaddate[1], downloaddate[-1])
        month = ownfunctions.get_month_number(downloaddate[1])
        self.downloaddate = datetime.date(int(downloaddate[-1]), month, int(downloaddate[2]))

        self.name = ""       # initialize attributes for geocache
        self.difficulty = 0
        self.terrain = 0
        self.size_string = ""
        self.size = ""
        self.longtype = ""
        self.type = ""
        self.description = ""
        self.hint = ""
        self.owner = ""
        self.url = ""
        self.coordinates = []
        self.coordinates_string = ""
        self.attributes = []
        self.logs = []
        self.available = False

        geocache_tree = ElementTree.parse(self.filename_path)  # read .gpx-Datei and find source
        source = geocache_tree.find(".//{http://www.topografix.com/GPX/1/0}name").text

        if source == "Cache Listing Generated from Geocaching.com":  # get attributes from gpx-file
            self.source = "geocaching.com"
            self._read_from_geocachingcom_gpxfile(geocache_tree)
        else:
            self.source = "downloader"
            self._read_from_gpx_downloader(geocache_tree)
        
        self.distance = 0     # initialize attributes for waypoints
        self.waypoints = []

    def _read_from_gpx_downloader(self, geocache_tree):
        """reads attributes from a gpx-file that is created by the firefox plugin 'Geocaching.com GPX Downloader'
        (part of __init__)"""

        name = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}name").text  # read name
        self.name = ownfunctions.replace_signs(name)

        difficulty = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}difficulty").text  # read difficulty
        self.difficulty = float(difficulty)

        terrain = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}terrain").text  # read terrain
        self.terrain = float(terrain)

        self.size_string = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}container").text  # read size
        if self.size_string not in SIZE_LIST:
            self.size_string = "other"
        self.size = SIZE_LIST.index(self.size_string)

        self.longtype = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}type").text  # read type
        if self.longtype == "Unknown Cache":
            self.longtype = "Mystery Cache"
        self.type = self._read_type(self.longtype)

        self.description = self._read_description(geocache_tree)  # read description

        hint = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}encoded_hints").text  # read hint
        self.hint = ownfunctions.replace_signs(hint)

        owner = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}placed_by").text  # read owner
        self.owner = ownfunctions.replace_signs(owner)

        self.url = geocache_tree.find(".//{http://www.topografix.com/GPX/1/0}url").text  # read url

        wpt = geocache_tree.find(".//{http://www.topografix.com/GPX/1/0}wpt")  # read coordinates
        self.coordinates = [float(wpt.get("lat")), float(wpt.get("lon"))]  # list of floats [lat, lon]
        coord_str = ownfunctions.coords_decimal_to_minutes(self.coordinates)
        self.coordinates_string = coord_str  # string 'X XX°XX.XXX, X XXX°XX.XXX'

        attributes = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}text").text  # read attributes
        attributes = attributes.split(",")
        for a in attributes:
            self.attributes.append(ownfunctions.remove_spaces(a))

        self.logs = self._read_logs(geocache_tree)  # read logs

        cache = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}cache")  # read if available or not
        available = cache.get("available")
        if available == "True":
            self.available = True
        elif available == "False":
            self.available = False

    def _read_from_geocachingcom_gpxfile(self, geocache_tree):
        """reads attributes from a gpx-file that is created by geocaching.com (part of __init__)"""

        name = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0/1}name").text  # read name
        self.name = ownfunctions.replace_signs(name)

        difficulty = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0/1}difficulty").text  # read difficulty
        self.difficulty = float(difficulty)

        terrain = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0/1}terrain").text  # read terrain
        self.terrain = float(terrain)

        self.size_string = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0/1}container").text.lower()  # size
        if self.size_string not in SIZE_LIST:
            self.size_string = "other"
        self.size = SIZE_LIST.index(self.size_string)

        self.longtype = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0/1}type").text  # read type
        if self.longtype == "Unknown Cache":
            self.longtype = "Mystery Cache"
        self.type = self._read_type(self.longtype)

        self.description = self._read_description(geocache_tree)  # read description

        hint = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0/1}encoded_hints").text  # read hint
        self.hint = ownfunctions.replace_signs(hint)

        owner = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0/1}placed_by").text  # read owner
        self.owner = ownfunctions.replace_signs(owner)

        url_raw = geocache_tree.findall(".//{http://www.topografix.com/GPX/1/0}url")  # read url
        self.url = url_raw[1].text  # because index 0 is only http://www.geocaching.com

        wpt = geocache_tree.find(".//{http://www.topografix.com/GPX/1/0}wpt")  # read coordinates
        self.coordinates = [float(wpt.get("lat")), float(wpt.get("lon"))]  # list of floats [lat, lon]
        coord_str = ownfunctions.coords_decimal_to_minutes(self.coordinates)
        self.coordinates_string = coord_str  # string 'X XX°XX.XXX, X XXX°XX.XXX'

        attributes = geocache_tree.findall(".//{http://www.groundspeak.com/cache/1/0/1}attribute")  # read attributes
        for a in attributes:
            self.attributes.append(ownfunctions.remove_spaces(a.text))

        self.logs = self._read_logs(geocache_tree)  # read logs

        cache = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0/1}cache")  # read if available or not
        available = cache.get("available")
        if available == "True":
            self.available = True
        elif available == "False":
            self.available = False

    def _read_logs(self, geocache_tree):
        """reads logs from xml-file, part of __init__"""

        log_dates_raw = []
        if self.source == "downloader":
            log_dates_raw = geocache_tree.findall(".//{http://www.groundspeak.com/cache/1/0}date")
        elif self.source == "geocaching.com":
            log_dates_raw = geocache_tree.findall(".//{http://www.groundspeak.com/cache/1/0/1}date")
        log_dates = []
        for i, ld in enumerate(log_dates_raw):
            if i == 0 and self.source == "geocaching.com":
                log_dates.append(ld.text[:10])
            elif i > 0:  # in gpx-file from the gpx-downloader the attributes are also saved as logs
                log_dates.append(ld.text[:10])                     # but not taken into account here

        log_types_raw = []
        if self.source == "downloader":
            log_types_raw = geocache_tree.findall(".//{http://www.groundspeak.com/cache/1/0}type")
        elif self.source == "geocaching.com":
            log_types_raw = geocache_tree.findall(".//{http://www.groundspeak.com/cache/1/0/1}type")
        log_types = []
        for i, lt in enumerate(log_types_raw):
            if i == 0 and self.source == "geocaching.com":
                log_types.append(lt.text)
            elif i > 1:  # in gpx-file from the gpx-downloader index 0 corresponds to cachetyp (Tradi, Multi,...),
                log_types.append(lt.text)                                           # index 1 to the attributes...

        finder_raw = []
        if self.source == "downloader":
            finder_raw = geocache_tree.findall(".//{http://www.groundspeak.com/cache/1/0}finder")
        elif self.source == "geocaching.com":
            finder_raw = geocache_tree.findall(".//{http://www.groundspeak.com/cache/1/0/1}finder")
        finder = []
        for i, fd in enumerate(finder_raw):
            if i == 0 and self.source == "geocaching.com":
                next_fd = ownfunctions.replace_signs(fd.text)
                finder.append(next_fd)
            if i > 0:  # in gpx-file from the gpx-downloader index 0 corresponding to attributes
                next_fd = ownfunctions.replace_signs(fd.text)
                finder.append(next_fd)

        log_texts = []
        if self.source == "geocaching.com":  # logtext is only saved in gpx-files from geocaching.com
            text_raw = geocache_tree.findall(".//{http://www.groundspeak.com/cache/1/0/1}text")
            for i, tx in enumerate(text_raw):
                next_tx = ownfunctions.replace_signs(tx.text)
                log_texts.append(next_tx)

        logs = []
        log_number = len(log_dates)
        if len(log_dates) == len(log_types) == len(finder):
            for i in range(log_number):
                new_log = [log_dates[i], log_types[i], finder[i]]
                if self.source == "geocaching.com":
                    new_log.append(log_texts[i])
                logs.append(new_log)
        else:
            print("\nWARNING! Error in gpx-file. Reading logs correctly not possible.")

        return logs

    def _read_description(self, geocache_tree):
        """reads description from xml-file, part of __init__
        source: is the xml-file created by geocaching.com gpx-downloader or by geocaching.com itself?"""

        description_short = ""
        if self.source == "downloader":
            description_short = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}short_description").text
        elif self.source == "geocaching.com":
            description_short = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0/1}short_description").text
        if description_short:
            description_short = ownfunctions.replace_signs(description_short)
        else:
            description_short = ""

        description_long = ""
        if self.source == "downloader":
            description_long = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}long_description").text
        elif self.source == "geocaching.com":
            description_long = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0/1}long_description").text
        if description_long:
            description_long = ownfunctions.replace_signs(description_long)
        else:
            description_long = ""

        return description_short + "\n\n" + description_long

    @staticmethod
    def _read_type(lt):
        """converts cachetypes from xml-file to those from TYPE_LIST, part of __init__"""
        if lt in TYPE_LIST:
            cachetype = lt
        elif lt == "Cache In Trash Out Event" or lt == "Mega-Event Cache" or lt == "Giga-Event Cache":
            cachetype = "Event Cache"
        else:
            cachetype = "Unknown Type"
        return cachetype
        
    def __str__(self):
        return self.gccode
        
    def __eq__(self, other):
        return self.gccode == other
        
    def __ne__(self, other):
        return self.gccode != other

    def add_waypoint(self, waypoint):
        """adds a waypoint to the cache"""

        if type(waypoint) == Waypoint:
            waypoint.find_shown_name_and_distance(self)
            self.waypoints.append(waypoint)
        else:
            raise TypeError("Waypoint can't be added because it is not of waypoint type")
            
    def shortinfo(self, space=0):
        """returns one-line information about the cache
        space = number of spaces before waypoint lines
        (space = 0 if cache is shown without distance, space = 12 if it's shown with distance)"""

        a = self.gccode.ljust(7)
        b = self.coordinates_string
        c = self.type.ljust(17)
        d = self.difficulty
        e = self.terrain
        f = self.size_string.ljust(7)
        g = str(self.available).ljust(5)
        h = self.downloaddate_string
        i = self.name
        result = "{} | {} | {} | D {} | T {} | {} | {} | {} | {}".format(a, b, c, d, e, f, g, h, i)
        for w in self.waypoints:
            result += "\n" + space*" " + w.info()
        return result

    def longinfo(self): 
        """returns detailed information about the cache""" 
        
        z1 = "\n{} : {}".format(self.gccode, self.name)
        z2 = "\n"
        for i in range(len(z1)):
            z2 += "-"
        d = self.difficulty
        t = self.terrain
        sizestr = self.size_string
        lt = self.longtype
        z3 = "\n{}: {}, {}: {}, {}: {}, {}: {}".format(STR_D, d, STR_T, t, STR_SIZE, sizestr, STR_TYPE, lt)
        z4 = "\n{}: {}".format(STR_COORDS, self.coordinates_string)
        if self.waypoints:
            z4 += ", {}: ".format(STR_WAYPOINTS)
            for w in self.waypoints:
                z4 += "{} ({}), ".format(w.shown_name, w.coordinates_string)
            z4 = z4[:-2]
        z5 = "\n{}: {}".format(STR_OWNER, self.owner)
        z6 = "\n{}: ".format(STR_ATTR)
        for a in self.attributes:
            z6 = z6 + str(a) + ", "
        z6 = z6[:-2]
        z7 = "\n{}: {}, {}: {}".format(STR_ACT, self.available, STR_DATE, self.downloaddate_string)
        z8 = "\n{}: {}".format(STR_LINK, self.url)
        z9 = "\n\n{}".format(self.description)
        z10 = "\n{}: {}".format(STR_HINT, self.hint)
        z11 = "\n\n"
        for l in self.logs:
            z11 += "{}: {} by {}\n".format(l[0], l[1], l[2])
        return z1 + z2 + z3 + z4 + z5 + z6 + z7 + z8 + z9 + z10 + z11


class Waypoint(object):
    """
    An object of this class contains all information about a waypoint


    Attributes:
    -----------
    name: string
        name of the waypoint

    shown_name: string
        name of the waypoint that is shown
        i.e. without the gccode of the cache if waypoint belongs to a geocache

    coordinates: list
        coordinates in decimal degree, first element of the list: latitude, second element: longitude

    coordinates_string: string
        coordinates as degree and minutes

    distance: float
        distance of the coordinates of the cache if waypoint belongs to a cache
        else None


    Methods:
    ---------
    __init__(name, coordinates): creates the object out of name and coordinates as list [lat, lon]

    find_shown_name_and_distance(geocache): is performed if waypoint belongs to a geocache,
                                            calculates shown_name and distance

    info(): returns information about the waypoint
    """

    ALLOWED_SIGNS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                     "U", "V", "W", "X", "Y", "Z", u"Ä", u"Ö", u"Ü", u"ß", "!", "#", "$", '"', "?", "*", "/", "(", ")",
                     "-", "+", "&", "'", ";", ":", ",", ".", "=", "@", "%", "<", ">", "0", "1", "2", "3", "4", "5", "6",
                     "7", "8", "9", " "]

    def __init__(self, name, coordinates):
        """creates the object out of name and coordinates as list [lat, lon]"""

        if type(name) != str:
            raise TypeError("waypoint name is of wrong type")
        self.name = name.upper()
        for c in self.name:
            if c not in self.ALLOWED_SIGNS:
                raise TypeError("GARMIN does not allow '{}' in a waypoint name.".format(c))
        self.shown_name = self.name  # for waypoints not belonging to a geocache

        ownfunctions.validate_coordinates(coordinates)  # throws an error if coordinates not valid
        self.coordinates = coordinates
        coord_str = ownfunctions.coords_decimal_to_minutes(self.coordinates)
        self.coordinates_string = coord_str  # string 'X XX°XX.XXX, X XXX°XX.XXX'
        self.distance = None  # initialize for later use

    def find_shown_name_and_distance(self, geocache):
        """calculates the shown name and the distance to the 'main coordinates'
        if waypoint belongs to a geocache"""

        namelist = self.name.split()
        if not (namelist[-1].startswith("(GC") and namelist[-1].endswith(")")) or namelist[-1][1:-1] != geocache.gccode:
            raise TypeError("This waypoint does not belong to the geocache.")
        self.shown_name = " ".join(namelist[:-1])
        self.distance = ownfunctions.calculate_distance(self.coordinates, geocache.coordinates)

    def info(self):
        """returns information about the waypoint"""
        result = "        | {} | {}".format(self.coordinates_string, self.shown_name)
        if self.distance:
            result += " ({}km)".format(round(self.distance, 1))
        return result
