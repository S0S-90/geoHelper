import os
import time
import datetime
import xml.etree.ElementTree as ElementTree

import ownfunctions  # eigene Datei mit Funktionen

class Geocache(object):

    """
    Ein Objekt dieser Klasse enthält alle relevanten Informationen aus der entsprechenden GPX-Datei.
    
    
    Attribute:
    -----------
    dateiname_path: string
        vollstaendiger Dateiname (mit Pfadangabe) 
        
    gccode: string
        CG-Code
        
    name: string
        Name des Geocaches 
    
    difficulty: float
        Schwierigkeitsgrad
        
    terrain: float
        Gelaendewertung
        
    size: int
        Groesse des Caches (other = 0, dann mit der Groesse aufsteigend)
        
    size_anzeige: string
        Groesse des Caches
        
    type: string
        Art des Caches
    
    beschreibung: string
        Cachebeschreibung
        
    hint: string
        Hinweis
        
    owner: string
        Besitzer des Caches
        
    url: string
        Link zur Cacheseite auf geocaching.com 
        
    koordinaten: list 
        Koordinaten als Dezimalgrad, erstes Element der Liste: Breitengrad, zweites Element: Laengengrad
        
    koordinatenanzeige: string
        Koordinaten als Grad und Minuten
        
    attribute: list
        Attribute des Caches 
        
    logs: list
        letzte Logs vor dem Download
        jedes Element der Liste: Liste vom Typ [Datum, Logtyp, Finder]
        
    available: bool
        Verfuegbarkeit zum Zeitpunkt des Downloads 
        
    downloaddate: datetime.date
        Datum des Downloads der gpx-Datei
        
    downloaddate_anzeige: string
        Datum des Downloads der gpx-Datei wie in der Anzeige
    
    
    Methoden:
    ---------
    __init__(dateiname_path): Erstellung eines Geocache-Objekt aus dem vollstaendigen Dateinamen der zugehoerigen GPX-Datei
    
    kurzinfo(): unicode
        einzeilige Information ueber den Cache 
        
    langinfo(): 
        ausfuehrliche Information ueber den Cache 
    """

    def __init__(self, dateiname_path):
        self.dateiname_path = dateiname_path
        self.gccode = os.path.splitext(os.path.basename(dateiname_path))[0]  # GC-Code
        
        geocache_tree = ElementTree.parse(dateiname_path)    # .gpx-Datei einlesen 
        
        name = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}name").text # Name auslesen
        self.name = ownfunctions.zeichen_ersetzen(name) 
        
        difficulty = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}difficulty").text # Schwierigkeitsgrad auslesen
        self.difficulty = float(difficulty)
        
        terrain = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}terrain").text  # Terrainwertung auslesen
        self.terrain = float(terrain)
        
        self.size_anzeige = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}container").text # Groesse auslesen
        self.size = self._get_size(self.size_anzeige)
        
        self.type = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}type").text              # Typ auslesen

        self.beschreibung = self._beschreibung_auslesen(geocache_tree)                               # Beschreibung auslesen

        hint = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}encoded_hints").text # Hint auslesen
        self.hint = ownfunctions.zeichen_ersetzen(hint)
        
        owner = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}placed_by").text    # Owner auslesen
        self.owner = ownfunctions.zeichen_ersetzen(owner)
        
        self.url = geocache_tree.find(".//{http://www.topografix.com/GPX/1/0}url").text         # url auslesen
        
        wpt = geocache_tree.find(".//{http://www.topografix.com/GPX/1/0}wpt")                       # Koordinaten auslesen
        self.koordinaten = [float(wpt.get("lat")), float(wpt.get("lon"))]                           # Liste als Dezimalgrad
        self.koordinatenanzeige = ownfunctions.koordinaten_dezimalgrad_to_minuten(self.koordinaten) # String wie auf geocaching.com         
        
        attribute = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}text").text     # Attribute auslesen
        self.attribute = attribute.split(",")
        
        self.logs = self._logs_auslesen(geocache_tree)                                           # Logs auslesen          
           
        cache = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}cache")             # Auslesen, ob verfuegbar oder nicht
        self.available = cache.get("available")
        
        downloaddate = time.ctime(os.path.getmtime(dateiname_path))       # Downloaddatum aus Aenderungsdatum der gpx-Datei auslesen
        downloaddate = downloaddate.split(" ")
        self.downloaddate_anzeige = "".join([downloaddate[2]+" ", downloaddate[1]+" ", downloaddate[-1]])
        month = ownfunctions.get_month(downloaddate[1])
        self.downloaddate = datetime.date(int(downloaddate[-1]), month, int(downloaddate[2]))
        
        self.distance = 0     # initialise for later use
        
    def _logs_auslesen(self, geocache_tree):
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
                finder.append(fd.text)
          
        logs = [] 
        loganzahl = len(log_dates)        
        if len(log_dates) == len(log_types) == len(finder):
            for i in range(loganzahl):
                logs.append([log_dates[i], log_types[i], finder[i]])
        else:
            print "\nWARNUNG! Fehler in der gpx-Datei. Logs koennen nicht korrekt ausgelesen werden."
        
        return logs
        
    def _beschreibung_auslesen(self, geocache_tree):
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
        
    def _get_size(self, size):
        """ordnet die Groessenbezeichnungen einem Zahlenwert zu (zum Sortieren)"""
        if size == "other":
            return 0
        elif size == "micro":
            return 2
        elif size == "small":
            return 3
        elif size == "regular":
            return 4
        elif size == "large":
            return 5
            
    def kurzinfo(self):                                  
        """ gibt eine einzeilige Kurzinfo zurueck"""
        return u"{} | {} | {} | D {} | T {} | {} | {} | {} | {}".format(self.gccode.ljust(7), self.koordinatenanzeige, self.type.ljust(17), self.difficulty, self.terrain, self.size_anzeige.ljust(7), self.available.ljust(5), self.downloaddate_anzeige, self.name)

    def langinfo(self): 
        """gibt eine ausfuehrliche Info zurueck""" 
        z1 = u"\n{} : {}".format(self.gccode,self.name)
        z2 = "\n"
        for i in range(len(z1)):
            z2 = z2 + "-"
        z3 = u"\nSchwierigkeit: {}, Gelaende: {}, Groesse: {}, Typ: {}".format(self.difficulty, self.terrain, self.size, self.type)
        z4 = u"\nKoordinaten: {}".format(self.koordinatenanzeige)
        z5 = u"\nOwner: {}".format(self.owner)
        z6 = u"\nAttribute: "
        for a in self.attribute:
            z6 = z6 + str(a) + ", "
        z6 = z6[:-2]
        z7 = u"\nCache ist aktiv: {}, Stand: {}".format(self.available, self. downloaddate)
        z8 = u"\nLink: {}".format(self.url)
        z9 = u"\n\n{}".format(self.beschreibung)
        z10 = u"\nHinweise: {}".format(self.hint)
        z11 = u"\n\n"
        for l in self.logs:
            z11 = z11 + u"{}: {} by {}\n".format(l[0], l[1], l[2])
        return z1 + z2 + z3 + z4 + z5 + z6 + z7 + z8 + z9 + z10 + z11
        