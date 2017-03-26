import os
import time
import datetime
import xml.etree.ElementTree as ElementTree

import ownfunctions  

SIZE_LISTE = ["other", "micro", "small", "regular", "large"]
TYPES_LISTE = ["Traditional Cache", "Multi-cache", "EarthCache", "Letterbox Hybrid", "Event Cache", "Wherigo Cache", "Mystery Cache", "Geocaching HQ", "Unknown Type"]

class Geocache(object):

    """
    An object of this class contains all relevant information of the corresponding gpx-file
    
    
    Attributs:
    -----------
    dateiname_path: string
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
        type of the cache (member of TYPES_LISTE)
        used in short description as well as for searching and sorting
        
    longtype: string
        type of the cache (any description possible)
        used in long description
    
    beschreibung: string
        description of the cache
        
    hint: string
        hint for the cache
        
    owner: string
        owner of the cache
        
    url: string
        weblink to the cache on geocaching.com 
        
    koordinaten: list 
        coordinates in decimal degree, first element of the list: latitude, second element: longitude
        
    koordinatenanzeige: string
        coordinates as degree and minutes
        
    attribute: list
        attributes of the cache
        
    logs: list
        last logs before download
        every element of list: list [date, logtype, name of logger]
        
    available: bool 
        availability at the time of download 
        
    downloaddate: datetime.date
        date when the gpx-file was downloaded from geocaching.com
        
    downloaddate_anzeige: string
        date when the gpx-file was downloaded from geocaching.com as string
    
    
    Methods:
    ---------
    __init__(dateiname_path): Create a Geocache-object out of the gpx-file (complete name with path)
    
    kurzinfo(): unicode
        one-line information about the cache 
        
    langinfo(): 
        detailed information about the cache
    """
    
    def __init__(self, dateiname_path):
    
        if type(dateiname_path) != str and type(dateiname_path) != unicode:
            raise TypeError("Bad input.")
        
        self.dateiname_path = dateiname_path
        self.gccode = os.path.splitext(os.path.basename(dateiname_path))[0]  # gc-code
        
        geocache_tree = ElementTree.parse(dateiname_path)    # read .gpx-Datei 
        
        name = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}name").text # read name
        self.name = ownfunctions.zeichen_ersetzen(name) 
        
        difficulty = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}difficulty").text # read difficulty
        self.difficulty = float(difficulty)
        
        terrain = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}terrain").text  # read terrain
        self.terrain = float(terrain)
        
        self.size_string = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}container").text # read size
        if self.size_string not in SIZE_LISTE:
            self.size_string = "other"
        self.size = SIZE_LISTE.index(self.size_string)
        
        self.longtype = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}type").text      # read type
        if self.longtype == "Unknown Cache":
            self.longtype = "Mystery Cache"
        self.type = self._read_type(self.longtype)
        
# cleanup until here -> continue with ownfunctions.py
            
        self.beschreibung = self._read_description(geocache_tree)                               # Beschreibung auslesen

        hint = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}encoded_hints").text # Hint auslesen
        self.hint = ownfunctions.zeichen_ersetzen(hint)
        
        owner = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}placed_by").text    # Owner auslesen
        self.owner = ownfunctions.zeichen_ersetzen(owner)
        
        self.url = geocache_tree.find(".//{http://www.topografix.com/GPX/1/0}url").text         # url auslesen
        
        wpt = geocache_tree.find(".//{http://www.topografix.com/GPX/1/0}wpt")                       # Koordinaten auslesen
        self.koordinaten = [float(wpt.get("lat")), float(wpt.get("lon"))]                           # Liste als Dezimalgrad
        self.koordinatenanzeige = ownfunctions.koordinaten_dezimalgrad_to_minuten(self.koordinaten) # String wie auf geocaching.com         
        
        attributes = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}text").text     # Attribute auslesen
        attributes = attributes.split(",")
        self.attribute = []
        for a in attributes:
            self.attribute.append(ownfunctions.remove_spaces(a))
        
        self.logs = self._read_logs(geocache_tree)                                           # Logs auslesen          
           
        cache = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}cache")             # Auslesen, ob verfuegbar oder nicht
        available = cache.get("available")
        if available == "True":
            self.available = True
        elif available == "False":
            self.available = False
        
        downloaddate = time.ctime(os.path.getmtime(dateiname_path))       # Downloaddatum aus Aenderungsdatum der gpx-Datei auslesen
        downloaddate = downloaddate.split(" ")
        self.downloaddate_anzeige = "".join([downloaddate[2]+" ", downloaddate[1]+" ", downloaddate[-1]])
        month = ownfunctions.get_month(downloaddate[1])
        self.downloaddate = datetime.date(int(downloaddate[-1]), month, int(downloaddate[2]))
        
        self.distance = 0     # initialise for later use
        
    def _read_logs(self, geocache_tree):
        """liest die Logs aus der XML-Datei aus, ausgelagerter Teil von __init__"""
    
        log_dates_raw = geocache_tree.findall(".//{http://www.groundspeak.com/cache/1/0}date")
        log_dates = []
        for i,ld in enumerate(log_dates_raw):
            if i > 0:  # Attribute werden auch als Log gespeichert, hier aber nicht beruecksichtigt
                log_dates.append(ld.text[:10])
                
        log_types_raw = geocache_tree.findall(".//{http://www.groundspeak.com/cache/1/0}type")
        log_types = []
        for i,lt in enumerate(log_types_raw):
            if i > 1:  # Index 0 entspricht Cachetyp (Tradi, Mulit,...), Index 1 den Attributen
                log_types.append(lt.text)
        
        finder_raw = geocache_tree.findall(".//{http://www.groundspeak.com/cache/1/0}finder")
        finder = []
        for i,fd in enumerate(finder_raw):
            if i > 0:  # Index 0 entspricht Attributen
                next_fd = ownfunctions.zeichen_ersetzen(fd.text)
                finder.append(next_fd)
          
        logs = [] 
        loganzahl = len(log_dates)        
        if len(log_dates) == len(log_types) == len(finder):
            for i in range(loganzahl):
                logs.append([log_dates[i], log_types[i], finder[i]])
        else:
            print "\nWARNUNG! Fehler in der gpx-Datei. Logs koennen nicht korrekt ausgelesen werden."
        
        return logs
        
    def _read_description(self, geocache_tree):
        """liest die Beschreibung aus der XML-Datei aus, ausgelagerter Teil von __init__"""
        beschreibung_kurz = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}short_description").text 
        if beschreibung_kurz:
            beschreibung_kurz = ownfunctions.zeichen_ersetzen(beschreibung_kurz)
        else:
            beschreibung_kurz = ""
        beschreibung_lang = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}long_description").text
        if beschreibung_lang:
            beschreibung_lang = ownfunctions.zeichen_ersetzen(beschreibung_lang)
        else:
            beschreibung_lang = ""
        return beschreibung_kurz + "\n\n" + beschreibung_lang
        
    def _read_type(self, lt):
        """wandelt Typen aus XML-Datei in solche aus TYPES_LISTE um, ausgelagerter Teil von __init__"""
        if lt in TYPES_LISTE:
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
            
    def kurzinfo(self):                                  
        """ gibt eine einzeilige Kurzinfo zurueck"""
        return u"{} | {} | {} | D {} | T {} | {} | {} | {} | {}".format(self.gccode.ljust(7), self.koordinatenanzeige, self.type.ljust(17), self.difficulty, self.terrain, self.size_string.ljust(7), str(self.available).ljust(5), self.downloaddate_anzeige, self.name)

    def langinfo(self): 
        """gibt eine ausfuehrliche Info zurueck""" 
        z1 = u"\n{} : {}".format(self.gccode,self.name)
        z2 = "\n"
        for i in range(len(z1)):
            z2 = z2 + "-"
        z3 = u"\nSchwierigkeit: {}, Gelaende: {}, Groesse: {}, Typ: {}".format(self.difficulty, self.terrain, self.size_string, self.longtype)
        z4 = u"\nKoordinaten: {}".format(self.koordinatenanzeige)
        z5 = u"\nOwner: {}".format(self.owner)
        z6 = u"\nAttribute: "
        for a in self.attribute:
            z6 = z6 + str(a) + ", "
        z6 = z6[:-2]
        z7 = u"\nCache ist aktiv: {}, Stand: {}".format(self.available, self.downloaddate_anzeige)
        z8 = u"\nLink: {}".format(self.url)
        z9 = u"\n\n{}".format(self.beschreibung)
        z10 = u"\nHinweise: {}".format(self.hint)
        z11 = u"\n\n"
        for l in self.logs:
            z11 = z11 + u"{}: {} by {}\n".format(l[0], l[1], l[2])
        return z1 + z2 + z3 + z4 + z5 + z6 + z7 + z8 + z9 + z10 + z11
        