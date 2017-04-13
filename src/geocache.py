import os
import time
import datetime
import xml.etree.ElementTree as ElementTree

import ownfunctions  

SIZE_LIST = ["other", "micro", "small", "regular", "large"]
TYPE_LIST = ["Traditional Cache", "Multi-cache", "EarthCache", "Letterbox Hybrid", "Event Cache", "Wherigo Cache", "Mystery Cache", "Geocaching HQ", "Unknown Type"]


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


class Geocache(object):

    """
    An object of this class contains all relevant information of the corresponding gpx-file
    
    
    Attributes:
    -----------
    filename_path: string
        filename (including path)
        
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
        every element of list: list [date, logtype, name of logger]
        
    available: bool 
        availability at the time of download 
        
    downloaddate: datetime.date
        date when the gpx-file was downloaded from geocaching.com
        
    downloaddate_string: string
        date when the gpx-file was downloaded from geocaching.com as string
    
    
    Methods:
    ---------
    __init__(filename_path): Create a Geocache-object out of the gpx-file (complete name with path)
    
    shortinfo(): unicode
        one-line information about the cache 
        
    longinfo(): 
        detailed information about the cache
    """
    
    def __init__(self, filename_path):
    
        if type(filename_path) != str and type(filename_path) != unicode:
            raise TypeError("Bad input.")
        
        self.filename_path = filename_path
        self.gccode = os.path.splitext(os.path.basename(filename_path))[0]  # gc-code
        
        geocache_tree = ElementTree.parse(filename_path)    # read .gpx-Datei 
        
        name = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}name").text # read name
        self.name = ownfunctions.replace_signs(name) 
        
        difficulty = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}difficulty").text # read difficulty
        self.difficulty = float(difficulty)
        
        terrain = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}terrain").text  # read terrain
        self.terrain = float(terrain)
        
        self.size_string = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}container").text # read size
        if self.size_string not in SIZE_LIST:
            self.size_string = "other"
        self.size = SIZE_LIST.index(self.size_string)
        
        self.longtype = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}type").text      # read type
        if self.longtype == "Unknown Cache":
            self.longtype = "Mystery Cache"
        self.type = self._read_type(self.longtype)
            
        self.description = self._read_description(geocache_tree)                               # read description

        hint = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}encoded_hints").text # read hint
        self.hint = ownfunctions.replace_signs(hint)
        
        owner = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}placed_by").text    # read owner
        self.owner = ownfunctions.replace_signs(owner)
        
        self.url = geocache_tree.find(".//{http://www.topografix.com/GPX/1/0}url").text         # read url
        
        wpt = geocache_tree.find(".//{http://www.topografix.com/GPX/1/0}wpt")                       # read coordinates
        self.coordinates = [float(wpt.get("lat")), float(wpt.get("lon"))]                           # list of floats [lat, lon]
        self.coordinates_string = ownfunctions.coords_decimal_to_minutes(self.coordinates)          # string 'X XX°XX.XXX, X XXX°XX.XXX'       
        
        attributes = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}text").text     # read attributes
        attributes = attributes.split(",")
        self.attributes = []
        for a in attributes:
            self.attributes.append(ownfunctions.remove_spaces(a))
        
        self.logs = self._read_logs(geocache_tree)                                           # read logs        
           
        cache = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}cache")             # read if available or not
        available = cache.get("available")
        if available == "True":
            self.available = True
        elif available == "False":
            self.available = False
        
        downloaddate = time.ctime(os.path.getmtime(filename_path))       # read downloaddate (= change of gpx-file)
        downloaddate = downloaddate.split(" ")
        self.downloaddate_string = "".join([downloaddate[2]+" ", downloaddate[1]+" ", downloaddate[-1]])
        month = ownfunctions.get_month(downloaddate[1])
        self.downloaddate = datetime.date(int(downloaddate[-1]), month, int(downloaddate[2]))
        
        self.distance = 0     # initialise for later use
        
    def _read_logs(self, geocache_tree):
        """reads logs from xml-file, part of __init__"""
    
        log_dates_raw = geocache_tree.findall(".//{http://www.groundspeak.com/cache/1/0}date")
        log_dates = []
        for i,ld in enumerate(log_dates_raw):
            if i > 0:  # attributes are also saved as logs but not taken into account here
                log_dates.append(ld.text[:10])
                
        log_types_raw = geocache_tree.findall(".//{http://www.groundspeak.com/cache/1/0}type")
        log_types = []
        for i,lt in enumerate(log_types_raw):
            if i > 1:  # index 0 corresponds to cachetyp (Tradi, Multi,...), index 1 to the attributes
                log_types.append(lt.text)
        
        finder_raw = geocache_tree.findall(".//{http://www.groundspeak.com/cache/1/0}finder")
        finder = []
        for i,fd in enumerate(finder_raw):
            if i > 0:  # index 0 corresponding to attributes
                next_fd = ownfunctions.replace_signs(fd.text)
                finder.append(next_fd)
          
        logs = [] 
        log_number = len(log_dates)        
        if len(log_dates) == len(log_types) == len(finder):
            for i in range(log_number):
                logs.append([log_dates[i], log_types[i], finder[i]])
        else:
            print "\nWARNING! Error in gpx-file. Reading logs correctly not possible."
        
        return logs
        
    def _read_description(self, geocache_tree):
        """reads description from xml-file, part of __init__"""
        
        description_short = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}short_description").text 
        if description_short:
            description_short = ownfunctions.replace_signs(description_short)
        else:
            description_short = ""
        description_long = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}long_description").text
        if description_long:
            description_long = ownfunctions.replace_signs(description_long)
        else:
            description_long = ""
        return description_short + "\n\n" + description_long
        
    def _read_type(self, lt):
        """converts cachetypes from xml-file to those from TYPE_LIST, part of __init__"""
        if lt in TYPE_LIST:
            type = lt
        elif lt == "Cache In Trash Out Event" or lt == "Mega-Event Cache" or lt == "Giga-Event Cache":
            type = "Event Cache"
        else:
            type = "Unknown Type"
        return type
        
    def __str__(self):
        return self.gccode
        
    def __eq__(self, other):
        return self.gccode == other
        
    def __ne__(self, other):
        return self.gccode != other
            
    def shortinfo(self):                                  
        """returns one-line information about the cache"""
        return u"{} | {} | {} | D {} | T {} | {} | {} | {} | {}".format(self.gccode.ljust(7), self.coordinates_string, self.type.ljust(17), self.difficulty, self.terrain, self.size_string.ljust(7), str(self.available).ljust(5), self.downloaddate_string, self.name)

    def longinfo(self): 
        """returns detailed information about the cache""" 
        
        z1 = u"\n{} : {}".format(self.gccode,self.name)
        z2 = "\n"
        for i in range(len(z1)):
            z2 = z2 + "-"
        z3 = u"\n{}: {}, {}: {}, {}: {}, {}: {}".format(STR_D, self.difficulty, STR_T, self.terrain, STR_SIZE, self.size_string, STR_TYPE, self.longtype)
        z4 = u"\n{}: {}".format(STR_COORDS, self.coordinates_string)
        z5 = u"\n{}: {}".format(STR_OWNER, self.owner)
        z6 = u"\n{}: ".format(STR_ATTR)
        for a in self.attributes:
            z6 = z6 + str(a) + ", "
        z6 = z6[:-2]
        z7 = u"\n{}: {}, {}: {}".format(STR_ACT, self.available, STR_DATE, self.downloaddate_string)
        z8 = u"\n{}: {}".format(STR_LINK, self.url)
        z9 = u"\n\n{}".format(self.description)
        z10 = u"\n{}: {}".format(STR_HINT, self.hint)
        z11 = u"\n\n"
        for l in self.logs:
            z11 = z11 + u"{}: {} by {}\n".format(l[0], l[1], l[2])
        return z1 + z2 + z3 + z4 + z5 + z6 + z7 + z8 + z9 + z10 + z11
        