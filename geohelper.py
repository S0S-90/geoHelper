import sys
import os
import glob
import webbrowser

import geocache     # Geocache-Klasse
import user_io      # Benutzeroberflaeche
import ownfunctions # eigene Datei mit Funktionen

PATH = user_io.ask_for_path()   # Pfad zum GPS-Geraet

class GPS_content(object):
    """
    Ein Objekt dieser Klasse enthält alle relevanten Informationen vom GPS-Geraet (oder einem anderen Speicherort).
    
    
    Attribute:
    ----------
    PATH: string
        Pfadangabe zum GPS-Geraet oder einem anderen Speicherort, der ausgelesen werden soll
        
    geocaches: list
        Liste von allen Geocaches
        
    existing_attributes: list
        Liste aller in den Geocaches vorkommenden Attribute
        
    found_exists: bool
        Information, ob auf dem Geraet Caches als gefunden markiert wurden
    
    found_caches: list
        Liste von gefundenen Geocaches (falls found_exists)
        
    warning: bool
        aktiv, wenn sich neben den gefundenen Caches auch noch andere in der Logdatei befinden (z.B. als nicht gefunden, needs maintainance)
    
    
    Methoden:
    ---------
    __init__(path): Erstellung eines GPS-Content-Objekts aus der Pfadangabe zum Geraet

    """

    
    def __init__(self, path):
        """liest nach Oeffnen des Programms die Geocaches und die Logdatei ein"""
        
        self.PATH = path              # Uebernahme der Pfadangabe aus der user_io
        self.found_exists = False     # Information, ob gefundene Caches auf dem Geraet gespeichert sind
        self.existing_attributes = [] # Liste von Attributen
        
        self.geocaches = []               # alle Caches aus GC*.gpx-Dateien in PATH\GPX auslesen und in Liste geocaches speichern
        GPX_PATH = os.path.join(self.PATH, "GPX")
        for datei in glob.glob(os.path.join(GPX_PATH,"GC*.gpx")):
            self.geocaches.append(geocache.Geocache(datei))
            
        for g in self.geocaches:      # Attribute aus den Geocaches auslesen 
            for a in g.attribute:
                if a not in self.existing_attributes and a != "No attributes specified by the author":
                    self.existing_attributes.append(a)
        self.existing_attributes.sort()
              
        if os.path.isfile(os.path.join(self.PATH, "geocache_visits.txt")):    # alle gefundenen Caches aus Logdatei in found_caches speichern, falls eine solche vorhanden
            [logged_caches, self.found_caches] = self.get_logged_and_found_caches(os.path.join(self.PATH, "geocache_visits.txt"))
            if len(self.found_caches) > 0:
                self.found_exists = True
            if len(self.found_caches) < len(logged_caches): # Warnung, falls weitere Caches in Logdatei, die noch nicht gefunden wurden
                self.warning = True
            else:
                self.warning = False

    def get_logged_and_found_caches(self, visits_file):
        """liest aus visits_file die geloggten und gefundenen Caches aus"""

        logged_caches_raw = []           
        with open(visits_file) as visits:
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
        for lc in logged_caches:
            if lc[-1] == "Found it":
                try:
                    found_caches.append(geocache.Geocache(os.path.join(self.PATH,"GPX",lc[0]+".gpx")))
                except IOError:
                    user_io.general_output("\nWARNUNG! Der Geocache {} befindet sich nicht auf dem Geraet. Er wird daher im Folgenden nicht mehr beruecksichtigt.".format(lc[0])) 
        return [logged_caches, found_caches]

    def sortieren_und_anzeigen(self):
        """sortiert alle Caches auf dem Geraet nach gewuenschtem Kriterium und zeigt sie an"""
        [kriterium, rev] = user_io.sortieren()
        if kriterium == "distance":   # Entfernungsberechnung
            koords = None
            koords_str = user_io.koordinaten_eingabe()
            try:     # Koordinaten im geocaching.com-Format
                koords = ownfunctions.koordinaten_minuten_to_dezimalgrad(koords_str)
            except ValueError:
                try:     # Koordinaten aus google-maps oder geocaching.com/map url
                    koords = ownfunctions.koordinaten_url_to_dezimalgrad(koords_str)  
                except: 
                    user_io.general_output("ERROR: ungueltige Eingabe!")
            
            if koords:             # falls Koordinatenauslesen erfolgreich war
                for g in self.geocaches:
                    g.distance = ownfunctions.calculate_distance(g.koordinaten, koords)
                self.geocaches = sorted(self.geocaches, key = lambda geocache: getattr(geocache, kriterium), reverse = rev)
                user_io.general_output(self.alle_anzeigen_dist())
            
        elif kriterium == "name":    # Kriterien, bei denen die Groß- und Kleinschreibung vernachlaessigt werden soll
            self.geocaches = sorted(self.geocaches, key = lambda geocache: getattr(geocache, kriterium).lower(), reverse = rev)
            user_io.general_output(self.alle_anzeigen())
        else:                    # Kriterien, bei denen Groß- und Kleinschreibung keine Rolle spielt
            self.geocaches = sorted(self.geocaches, key = lambda geocache: getattr(geocache, kriterium), reverse = rev)
            user_io.general_output(self.alle_anzeigen())
        
    def alle_anzeigen(self):
        """gibt einen String zurueck, in dem die Kurzinfos aller Caches auf dem Geraet jeweils in einer Zeile stehen"""
        text = ""
        for c in self.geocaches:
            text = text + c.kurzinfo() + "\n"
        if len(self.geocaches) == 0:
            return "Keine Caches auf dem Geraet."
        return text
        
    def alle_anzeigen_dist(self):
        """gibt einen String zurueck, in dem die Kurzinfos aller Caches auf dem Geraet + die aktuellen Entfernungsangaben jeweils in einer Zeile stehen"""
        text = ""
        for c in self.geocaches:
            newline = u"{:7}km | {}\n".format(round(c.distance,1), c.kurzinfo())
            text = text + newline
        if len(self.geocaches) == 0:
            return "Keine Caches auf dem Geraet."
        return text
        
    def einen_anzeigen(self):
        """zeigt die Langinfo eines Caches an und loescht diesen auf Wunsch"""
        
        gc = user_io.general_input("Gib den GC-Code ein: ")
        cache = None
        for c in self.geocaches:
            if gc == c.gccode:
                cache = c
                break        
        if not cache:
            user_io.general_output("Dieser GC-Code existiert nicht.")
        else:
            user_io.general_output(cache.langinfo())
        
            while True:
                task = user_io.einen_anzeigen()
                if task == "loeschen":
                    self.loeschen([cache])
                    break
                elif task == "gc.com":
                    webbrowser.open_new_tab(cache.url)
                elif task == "gc-map":
                    url = "https://www.geocaching.com/map/#?ll={},{}&z=16".format(cache.koordinaten[0], cache.koordinaten[1])
                    webbrowser.open_new_tab(url)
                elif task == "googlemaps":
                    koords_sec = ownfunctions.koordinaten_minuten_to_sekunden(cache.koordinatenanzeige)
                    url = u"https://www.google.de/maps/place/{}".format(koords_sec)
                    webbrowser.open_new_tab(url)
                else:
                    break
        
    def gc_auswahl_anzeigen(self, cacheliste):
        """gibt einen String zurueck, in dem Kurzinfos aller Caches aus Cacheliste in jeweils einer Zeile stehen"""
        text = ""
        for c in cacheliste:
            text = text + c.kurzinfo() + "\n"
        return text
        
    def suchen(self):
        """durchsucht die Caches nach dem gewuenschten Kriterium und gibt Liste mit den Suchergebnissen zurueck"""
        
        suchergebnisse = []
        kriterium = user_io.suchen()
        if kriterium == "name" or kriterium == "beschreibung":    # Suche nach Name bzw. Beschreibung
            suchbegriff = user_io.input_decode("Suche nach... ")
            for c in self.geocaches:
                if suchbegriff in getattr(c, kriterium):
                    suchergebnisse.append(c)
        elif kriterium == "difficulty" or kriterium == "terrain":  # Suche nach D- bzw. T-Wertung
            eingabe_str = user_io.general_input("Minimaler und maximaler Wert (mit Komma voneinander getrennt): ") 
            eingabe = eingabe_str.split(",")
            if len(eingabe) != 2:
                user_io.general_output("ERROR: ungueltige Eingabe") 
            else:
                try:
                    min = float(eingabe[0])
                    max = float(eingabe[1])
                except ValueError:
                    user_io.general_output("ERROR: ungueltige Eingabe")
                else:
                    if min <= max and min >= 1 and min <=5 and max >=1 and max <=5: # jeweils Werte zwischen 1 und 5 
                        for c in self.geocaches:
                            if getattr(c, kriterium) >= min and getattr(c, kriterium) <= max:
                                suchergebnisse.append(c)
                    else:
                        user_io.general_output("ERROR: ungueltige Eingabe")
        elif kriterium == "size":                                           # Suche nach Cachegroesse
            liste = ["other", "micro", "small", "regular", "large"]
            eingabe_str = user_io.general_input("Minimale und maximale Groesse (mit Komma voneinander getrennt). Moegliche Groessen: other, micro, small, regular, large\n>>")
            eingabe = eingabe_str.split(",")
            if len(eingabe) != 2:
                user_io.general_output("ERROR: ungueltige Eingabe")
            else:
                try:
                    if eingabe[1][0] == " ":
                        max_str = eingabe[1][1:]
                    else:
                        max_str = eingabe[1]
                    min = liste.index(eingabe[0])
                    max = liste.index(max_str)
                except ValueError:
                    user_io.general_output("ERROR: ungueltige Eingabe")
                else:
                    if max < min:
                        user_io.general_output("ERROR: ungueltige Eingabe")
                    else:
                        for c in self.geocaches:
                            if c.size >= min and c.size <= max:
                                suchergebnisse.append(c)
        elif kriterium == "downloaddate":                               # Suche nach Downloaddatum
            eingabe_str = user_io.general_input("Fruehestes und spaetestes Datum (mit Komma voneinander getrennt). Format: DD.MM.YYYY\n>>")
            eingabe = eingabe_str.split(",")
            if len(eingabe) != 2:
                user_io.general_output("ERROR: ungueltige Eingabe")
            else:
                fr = eingabe[0]
                if eingabe[1][0] == " ":
                    sp = eingabe[1][1:]
                else:
                    sp = eingabe[1]
                try:
                    fr_date = ownfunctions.string_to_date(fr)
                    sp_date = ownfunctions.string_to_date(sp)
                except ValueError:
                    user_io.general_output("ERROR: ungueltige Eingabe")
                else:
                    if fr_date > sp_date:
                        user_io.general_output("ERROR: ungueltige Eingabe")
                    else:
                        for c in self.geocaches:
                            if c.downloaddate >= fr_date and c.downloaddate <= sp_date:
                                suchergebnisse.append(c) 
        elif kriterium == "available":                # Suche nach Verfuegbarkeit
            eingabe_str = user_io.general_input("Moechtest du die Caches sehen, die verfuegbar sind, oder die, die nicht verfuegbar sind? (y/n) ")
            if eingabe_str == "n":
                for c in self.geocaches:
                    if c.available == False:
                        suchergebnisse.append(c)
            else:      # falls ungueltige Eingabe: verfuegbare Caches anzeigen
                for c in self.geocaches:
                    if c.available == True:
                        suchergebnisse.append(c)
        elif kriterium == "type":
            eingabe = user_io.search_type()
            if eingabe not in geocache.TYPES_LISTE:
                user_io.general_output("ERROR: ungueltige Eingabe")
            else:
                for c in self.geocaches:
                    if c.type == eingabe:
                        suchergebnisse.append(c)
        elif kriterium == "attribute":
            eingabe = user_io.search_attribute(self.existing_attributes)
            if eingabe not in self.existing_attributes:
                user_io.general_output("ERROR: ungueltige Eingabe")
            else:
                for c in self.geocaches:
                    if eingabe in c.attribute:
                        suchergebnisse.append(c)
        return suchergebnisse
    
    def aktionen_auswahl_suchen(self, suchergebnisse):   
        """fuehrt Aktionen mit den Suchergebnissen aus"""
        if len(suchergebnisse) == 0:                        
            user_io.general_output("keine Geocaches gefunden")
        else:
            user_io.general_output(self.gc_auswahl_anzeigen(suchergebnisse))
            
            while True:
                task = user_io.aktionen_auswahl_suchen()
                if task == "neu_anzeigen":
                    user_io.general_output(self.gc_auswahl_anzeigen(suchergebnisse))
                elif task == "loeschen":
                    self.loeschen(suchergebnisse)
                elif task == "einen_anzeigen":
                    self.einen_anzeigen()
                elif task == "back":
                    break
        
    def gefundene_anzeigen(self):
        """zeigt alle auf dem Geraet als gefunden gespeicherten Caches an und loescht diese auf Wunsch"""
        
        user_io.general_output(self.gc_auswahl_anzeigen(self.found_caches))
        task = user_io.aktionen_auswahl_gefunden()
        if task == "loeschen":
            open_fieldnotes = user_io.open_fieldnotes()
            if open_fieldnotes:
                webbrowser.open_new_tab("https://www.geocaching.com/my/uploadfieldnotes.aspx")
            if self.warning:
                user_io.general_output("WARNUNG! Bei Fortfahren werden auch Log-Informationen ueber Caches geloescht, die nicht gefunden wurden.")
            loeschen = self.loeschen(self.found_caches)
            if loeschen:
                self.found_exists = False
                os.remove(os.path.join(self.PATH,"geocache_visits.txt"))
                os.remove(os.path.join(self.PATH,"geocache_logs.xml"))
           
    def loeschen(self, cacheliste):
        """loescht alle Caches aus cacheliste vom Geraet"""
        loeschen = user_io.loeschbestaetigung()
        if loeschen:
            for c in cacheliste:
                os.remove(c.dateiname_path)
            removelist = []
            for c1 in self.geocaches:
                for c2 in cacheliste:
                    if c1.gccode == c2.gccode:
                        removelist.append(c1)
            self.geocaches = [c for c in self.geocaches if c not in removelist]
        return loeschen
        
            
def show_main_menu(gps):    
    """startet das Hauptmenue"""
    while True:                                         # Hauptmenue
        task = user_io.hauptmenue(gps.found_exists)
        if task == "aktualisieren":
            new = GPS_content(PATH)
            show_main_menu(new)
        elif task == "alle_anzeigen":
            gps.sortieren_und_anzeigen()
        elif task == "einen_anzeigen":
            gps.einen_anzeigen()
        elif task == "suchen":
            results = gps.suchen()
            gps.aktionen_auswahl_suchen(results)
        elif task == "gefundene_anzeigen":
            gps.gefundene_anzeigen()
        elif task == "google-maps":
            webbrowser.open_new_tab("https://www.google.de/maps")
        elif task == "gc-maps":
            webbrowser.open_new_tab("https://www.geocaching.com/map")
        elif task == "exit":
            sys.exit()
          
if __name__ == "__main__":
    if os.path.exists(PATH):
        new = GPS_content(PATH)
        show_main_menu(new)
    else:
        user_io.general_output("\nERROR: GPS-Geraet nicht unter der Pfadangabe '{}' zu finden.".format(PATH))