import os
import time
import xml.etree.ElementTree as ElementTree

import ownfunctions  # eigene Datei mit Funktionen

class Geocache(object):

    """
    Klasse Geocache
    
    Methoden:
    __init__(dateiname_path): Erstellung eines Geocache-Objekt aus dem vollstaendigen Dateinamen der zugehoerigen GPX-Datei
    
    kurzinfo(): einzeilige Information ueber den Cache (Typ: unicode)
    langinfo(): ausfuehrliche Information ueber den Cache (Typ: unicode)
    
    Attribute:
    dateiname_path: vollstaendiger Dateiname (mit Pfadangabe)
    gccode: GC-Code (Typ: string)
    name: Name des Geocaches (Typ: string)
    difficulty: Schwierigkeitsgrad (Typ: float)
    terrain: Gelaendewertung (Typ: float)
    size: Groesse des Caches (Typ: string)
    type: Art des Caches (Typ: string)
    beschreibung: Cachebeschreibung (Typ: string)
    hint: Hinweis (Typ: string)
    owner: Besitzer des Caches (Typ: string)
    url: Link zur Cacheseite auf geocaching.com (Typ: string)
    koordinaten: Koordinaten als Dezimalgrad (Typ: list [Breitengrad, Längengrad])
    koordinatenanzeige: Koordinaten als Grad und Minuten (Typ: string)
    attribute: Attribute des Caches (Typ: list)
    logs: letzte Logs vor dem Download (Typ: list of lists, jede enthält [Datum, Logtyp, Finder])
    available: Verfuegbarkeit zum Zeitpunkt des Downloads (Typ: bool)
    downloaddate: Datum des Downloads der gpx-Datei (Typ: string)
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
        
        self.size = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}container").text # Groesse auslesen
        self.type = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}type").text      # Typ auslesen

        self.beschreibung = self._beschreibung_auslesen(geocache_tree)                               # Beschreibung auslesen

        hint = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}encoded_hints").text # Hint auslesen
        self.hint = ownfunctions.zeichen_ersetzen(hint)
        
        owner = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}placed_by").text    # Owner auslesen
        self.owner = ownfunctions.zeichen_ersetzen(owner)
        
        self.url = geocache_tree.find(".//{http://www.topografix.com/GPX/1/0}url").text         # url auslesen
        
        wpt = geocache_tree.find(".//{http://www.topografix.com/GPX/1/0}wpt")                    # Koordinaten auslesen
        self.koordinaten = [wpt.get("lat"), wpt.get("lon")]     # Liste als Dezimalgrad
        self.koordinatenanzeige = ownfunctions.koordinaten_dezimalgrad_to_minuten(self.koordinaten) # String wie auf geocaching.com        
        
        attribute = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}text").text     # Attribute auslesen
        self.attribute = attribute.split(",")
        
        self.logs = self._logs_auslesen(geocache_tree)                                           # Logs auslesen          
           
        cache = geocache_tree.find(".//{http://www.groundspeak.com/cache/1/0}cache")             # Auslesen, ob verfuegbar oder nicht
        self.available = cache.get("available")
        
        downloaddate = time.ctime(os.path.getmtime(dateiname_path))       # Downloaddatum aus Aenderungsdatum der gpx-Datei auslesen
        downloaddate = downloaddate.split(" ")
        self.downloaddate = "".join([downloaddate[2]+" ", downloaddate[1]+" ", downloaddate[-1]])
        
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

    def kurzinfo(self):                                  
        """ gibt eine einzeilige Kurzinfo zurueck"""
        return u"{} | {} | {} | D {} | T {} | {} | {} | {} | {}".format(self.gccode.ljust(7), self.koordinatenanzeige, self.type.ljust(17), self.difficulty, self.terrain, self.size.ljust(7), self.available.ljust(5), self.downloaddate, self.name)

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
        