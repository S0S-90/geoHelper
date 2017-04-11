import sys
import os
import glob
import webbrowser
import subprocess

import geocache     # Konstanten aus geocache.py (Typen und Groessen)
from geocache import Geocache   # Geocache-Klasse
import user_io      # Benutzeroberflaeche
import ownfunctions # eigene Datei mit Funktionen

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
        self.warning = False          # Warnung, falls Caches in Logdatei, die noch nicht gefunden wurden
        self.existing_attributes = [] # Liste von Attributen
        
        self.geocaches = []               # alle Caches aus GC*.gpx-Dateien in PATH\GPX auslesen und in Liste geocaches speichern
        GPX_PATH = os.path.join(self.PATH, "GPX")
        for datei in glob.glob(os.path.join(GPX_PATH,"GC*.gpx")):
            try:
                self.geocaches.append(Geocache(datei))
            except:
                user_io.general_output("Achtung! Kaputte Datei: {}".format(os.path.basename(datei)))
        user_io.general_output("\n{} Geocaches auf dem Geraet".format(len(self.geocaches)))
            
        for g in self.geocaches:      # Attribute aus den Geocaches auslesen 
            for a in g.attributes:
                if a not in self.existing_attributes and a != "No attributes specified by the author":
                    self.existing_attributes.append(a)
        self.existing_attributes.sort()
              
        if os.path.isfile(os.path.join(self.PATH, "geocache_visits.txt")):    # alle gefundenen Caches aus Logdatei in found_caches speichern, falls eine solche vorhanden
            [logged_caches, self.found_caches] = self.get_logged_and_found_caches()
            if len(self.found_caches) > 0:
                self.found_exists = True
            if len(self.found_caches) < len(logged_caches): # Warnung, falls weitere Caches in Logdatei, die noch nicht gefunden wurden
                self.warning = True
            else:
                self.warning = False

    def get_logged_and_found_caches(self):
        """liest aus visits_file die geloggten und gefundenen Caches aus (nur Caches, die auch auf dem Geraet gespeichert sind)"""

        logged_caches_raw = []           
        with open(os.path.join(self.PATH, "geocache_visits.txt")) as visits:
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
                    found_caches.append(Geocache(os.path.join(self.PATH,"GPX",lc[0]+".gpx")))
                    logged_caches_new.append(lc)
                except IOError:
                    user_io.general_output("\nWARNUNG! Der Geocache {} befindet sich nicht auf dem Geraet. Er wird daher im Folgenden nicht mehr beruecksichtigt.".format(lc[0])) 
            else:
                try:
                    Geocache(os.path.join(self.PATH,"GPX",lc[0]+".gpx"))
                    logged_caches_new.append(lc)
                except IOError:
                    user_io.general_output("\nWARNUNG! Der Geocache {} befindet sich nicht auf dem Geraet. Er wird daher im Folgenden nicht mehr beruecksichtigt.".format(lc[0])) 
        return [logged_caches_new, found_caches]

    def sort_caches_und_anzeigen(self):
        """sortiert alle Caches auf dem Geraet nach gewuenschtem Kriterium und zeigt sie an"""
        [kriterium, rev] = user_io.sort_caches()
        if kriterium == "distance":   # Entfernungsberechnung
            koords_str = user_io.coordinates_input()
            koords = ownfunctions.coords_string_to_decimal(koords_str)
            
            if koords:             # falls Koordinatenauslesen erfolgreich war
                for g in self.geocaches:
                    g.distance = ownfunctions.calculate_distance(g.coordinates, koords)
                self.geocaches = sorted(self.geocaches, key = lambda geocache: getattr(geocache, kriterium), reverse = rev)
                user_io.general_output(self.show_all_dist())
            else:
                user_io.general_output("ERROR: ungueltige Eingabe")
            
        elif kriterium == "name":    # Kriterien, bei denen die Groß- und Kleinschreibung vernachlaessigt werden soll
            self.geocaches = sorted(self.geocaches, key = lambda geocache: getattr(geocache, kriterium).lower(), reverse = rev)
            user_io.general_output(self.show_all())
        else:                    # Kriterien, bei denen Groß- und Kleinschreibung keine Rolle spielt
            self.geocaches = sorted(self.geocaches, key = lambda geocache: getattr(geocache, kriterium), reverse = rev)
            user_io.general_output(self.show_all())
        
    def show_all(self):
        """gibt einen String zurueck, in dem die Kurzinfos aller Caches auf dem Geraet jeweils in einer Zeile stehen"""
        text = ""
        for c in self.geocaches:
            text = text + c.shortinfo() + "\n"
        if len(self.geocaches) == 0:
            return "Keine Caches auf dem Geraet."
        return text
        
    def show_all_dist(self):
        """gibt einen String zurueck, in dem die Kurzinfos aller Caches auf dem Geraet + die aktuellen Entfernungsangaben jeweils in einer Zeile stehen"""
        text = ""
        for c in self.geocaches:
            newline = u"{:7}km | {}\n".format(round(c.distance,1), c.shortinfo())
            text = text + newline
        if len(self.geocaches) == 0:
            return "Keine Caches auf dem Geraet."
        return text
        
    def show_one(self):
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
            user_io.general_output(cache.longinfo())
        
            while True:
                task = user_io.show_one()
                if task == "delete":
                    self.delete([cache])
                    break
                elif task == "gc.com":
                    webbrowser.open_new_tab(cache.url)
                elif task == "dist":
                    koords_str = user_io.coordinates_input()
                    koords = ownfunctions.coords_string_to_decimal(koords_str)
                    if koords:
                        d = ownfunctions.calculate_distance(koords,cache.coordinates)
                        user_io.general_output("Abstand: {} Kilometer".format(round(d,1)))
                elif task == "gc-map":
                    url = "https://www.geocaching.com/map/#?ll={},{}&z=16".format(cache.coordinates[0], cache.coordinates[1])
                    webbrowser.open_new_tab(url)
                elif task == "googlemaps":
                    koords_sec = ownfunctions.coords_minutes_to_seconds(cache.coordinates_string)
                    url = u"https://www.google.de/maps/place/{}".format(koords_sec)
                    webbrowser.open_new_tab(url)
                else:
                    break
        
    def gc_auswahl_anzeigen(self, cacheliste):
        """gibt einen String zurueck, in dem Kurzinfos aller Caches aus Cacheliste in jeweils einer Zeile stehen"""
        text = ""
        for c in cacheliste:
            if type(c) != Geocache:
                raise TypeError("An Element of the selection is not a Geocache!")
            text = text + c.shortinfo() + "\n"
        return text
        
    def gc_auswahl_anzeigen_dist(self, cacheliste):
        """gibt einen String zurueck, in dem Kurzinfos aller Caches aus Cacheliste + die aktuellen Entfernungsangaben jeweils in einer Zeile stehen"""
        text = ""
        for c in cacheliste:
            if type(c) != Geocache:
                raise TypeError("An Element of the selection is not a Geocache!")
            newline = u"{:7}km | {}\n".format(round(c.distance,1), c.shortinfo())
            text = text + newline
        return text
        
    def search(self):
        """durchsucht die Caches nach dem gewuenschten Kriterium und gibt Liste mit den Suchergebnissen zurueck"""
        
        suchergebnisse = []
        kriterium = user_io.search()
        if kriterium == "name" or kriterium == "description":    # Suche nach Name bzw. Beschreibung
            suchbegriff = user_io.input_decode("Suche nach... ")
            for c in self.geocaches:
                if suchbegriff in getattr(c, kriterium):
                    suchergebnisse.append(c)
        elif kriterium == "difficulty" or kriterium == "terrain":  # Suche nach D- bzw. T-Wertung
            input_str = user_io.general_input("Minimaler und maximaler Wert (mit Komma voneinander getrennt): ") 
            input = input_str.split(",")
            if len(input) != 2:
                user_io.general_output("ERROR: ungueltige Eingabe") 
            else:
                try:
                    min = float(input[0])
                    max = float(input[1])
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
            input_str = user_io.general_input("Minimale und maximale Groesse (mit Komma voneinander getrennt). Moegliche Groessen: other, micro, small, regular, large\n>>")
            input = input_str.split(",")
            if len(input) != 2:
                user_io.general_output("ERROR: ungueltige Eingabe")
            else:
                try:
                    if input[1][0] == " ":
                        max_str = input[1][1:]
                    else:
                        max_str = input[1]
                    min = liste.index(input[0])
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
            input_str = user_io.general_input("Fruehestes und spaetestes Datum (mit Komma voneinander getrennt). Format: DD.MM.YYYY\n>>")
            input = input_str.split(",")
            if len(input) != 2:
                user_io.general_output("ERROR: ungueltige Eingabe")
            else:
                fr = input[0]
                if input[1][0] == " ":
                    sp = input[1][1:]
                else:
                    sp = input[1]
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
            input_str = user_io.general_input("Moechtest du die Caches sehen, die verfuegbar sind, oder die, die nicht verfuegbar sind? (y/n) ")
            if input_str == "n":
                for c in self.geocaches:
                    if c.available == False:
                        suchergebnisse.append(c)
            else:      # falls ungueltige Eingabe: verfuegbare Caches anzeigen
                for c in self.geocaches:
                    if c.available == True:
                        suchergebnisse.append(c)
        elif kriterium == "type":
            input = user_io.search_type()
            if input not in geocache.TYPES_LIST:
                user_io.general_output("ERROR: ungueltige Eingabe")
            else:
                for c in self.geocaches:
                    if c.type == input:
                        suchergebnisse.append(c)
        elif kriterium == "attributes":
            input = user_io.search_attributes(self.existing_attributes)
            if input not in self.existing_attributes:
                user_io.general_output("ERROR: ungueltige Eingabe")
            else:
                for c in self.geocaches:
                    if input in c.attributes:
                        suchergebnisse.append(c)
        elif kriterium == "distance":
            koords_str = user_io.coordinates_input()
            koords = ownfunctions.coords_string_to_decimal(koords_str)
            if koords:
                input_str = user_io.general_input("Minimale und maximale Distanz in Kilometern (mit Komma voneinander getrennt): ") 
                input = input_str.split(",")
                if len(input) != 2:
                    user_io.general_output("ERROR: ungueltige Eingabe") 
                else:
                    try:
                        min = float(input[0])
                        max = float(input[1])
                    except ValueError:
                        user_io.general_output("ERROR: ungueltige Eingabe")
                    else:
                        for c in self.geocaches:
                            c.distance = ownfunctions.calculate_distance(koords,c.coordinates)
                            if c.distance >= min and c.distance <= max:
                                suchergebnisse.append(c)
            else:
                user_io.general_output("ERROR: ungueltige Eingabe")
        
        if len(suchergebnisse) == 0:                        # Ausgabe der Suchergebnisse
            user_io.general_output("keine Geocaches gefunden")
        else:
            if kriterium == "distance":
                user_io.general_output(self.gc_auswahl_anzeigen_dist(suchergebnisse))  
            else:
                user_io.general_output(self.gc_auswahl_anzeigen(suchergebnisse))
        return suchergebnisse
    
    def actions_after_search(self, suchergebnisse):   
        """fuehrt Aktionen mit den Suchergebnissen aus"""
        if len(suchergebnisse) != 0:                        
            while True:
                task = user_io.actions_after_search()
                if task == "show_again":
                    user_io.general_output(self.gc_auswahl_anzeigen(suchergebnisse))
                elif task == "delete":
                    self.delete(suchergebnisse)
                elif task == "show_one":
                    self.show_one()
                elif task == "back":
                    break
        
    def show_founds(self):
        """zeigt alle auf dem Geraet als gefunden gespeicherten Caches an und loescht diese auf Wunsch"""
        
        if not self.found_exists:
            raise ValueError("ERROR: no found caches")
        user_io.general_output(self.gc_auswahl_anzeigen(self.found_caches))
        while True:
            task = user_io.actions_with_founds()
            if task == "log":
                webbrowser.open_new_tab("https://www.geocaching.com/my/uploadfieldnotes.aspx")
            elif task == "delete":
                if self.warning:
                    user_io.general_output("WARNUNG! Bei Fortfahren werden auch Log-Informationen ueber Caches geloescht, die nicht gefunden wurden.")
                delete = self.delete(self.found_caches)
                if delete:
                    self.found_exists = False
                    os.remove(os.path.join(self.PATH,"geocache_visits.txt"))
                    os.remove(os.path.join(self.PATH,"geocache_logs.xml"))
                    break
            elif task == "exit":
                break
           
    def delete(self, cacheliste):
        """loescht alle Caches aus cacheliste vom Geraet"""
        delete = user_io.confirm_deletion()
        if delete:
            for c in cacheliste:
                os.remove(c.filename_path)
            removelist = []
            for c1 in self.geocaches:
                for c2 in cacheliste:
                    if c1 == c2:
                        removelist.append(c1)
            self.geocaches = [c for c in self.geocaches if c not in removelist]
        return delete
        
    def show_all_on_map(self):
        editor = user_io.show_all_on_map_start()
        with open("mapinfo.txt","w") as mapinfo:
            for i,g in enumerate(self.geocaches):
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
                mapinfo.write("{},{} {{{}}} <{}>\n".format(g.coordinates[0], g.coordinates[1], g.name.encode("cp1252"), color))
        subprocess.Popen([editor,"mapinfo.txt"]) 
        webbrowser.open_new_tab("https://www.mapcustomizer.com/#bulkEntryModal") 
        user_io.show_all_on_map_end()
        os.remove("mapinfo.txt")        
            
        
            
def show_main_menu(gps):    
    """startet das Hauptmenue"""
    while True:                                         # Hauptmenue
        task = user_io.main_menu(gps.found_exists)
        if task == "update":
            new = GPS_content(PATH)
            show_main_menu(new)
        elif task == "show_all":
            gps.sort_caches_und_anzeigen()
        elif task == "show_all_on_map":
            gps.show_all_on_map()
        elif task == "show_one":
            gps.show_one()
        elif task == "search":
            results = gps.search()
            gps.actions_after_search(results)
        elif task == "show_founds":
            gps.show_founds()
        elif task == "google-maps":
            webbrowser.open_new_tab("https://www.google.de/maps")
        elif task == "gc-maps":
            webbrowser.open_new_tab("https://www.geocaching.com/map")
        elif task == "exit":
            sys.exit()
         
if __name__ == "__main__":
    PATH = user_io.ask_for_path()   # Pfad zum GPS-Geraet
    if os.path.exists(PATH):
        new = GPS_content(PATH)
        show_main_menu(new)
    else:
        user_io.general_output("\nERROR: GPS-Geraet nicht unter der Pfadangabe '{}' zu finden.".format(PATH))