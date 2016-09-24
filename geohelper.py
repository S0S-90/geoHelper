import os
import glob

import geocache  # Geocache-Klasse
import user_io   # Benutzeroberflaeche

class Programinstanz(object):

    def __init__(self):
        """list nach Oeffnen des Programms die Geocaches ein und leitet zu weiteren Tasks des Hauptmenues weiter"""
        
        self.PATH = user_io.PATH     # Uebernahme der Pfadangabe aus der user_io
        self.found_exists = False    # Information, ob gefundene Caches auf dem Geraet gespeichert sind
        
        self.geocaches = []               # alle Caches aus GC*.gpx-Dateien in PATH\GPX auslesen und in Liste geocaches speichern
        GPX_PATH = os.path.join(self.PATH, "GPX")
        for datei in glob.glob(os.path.join(GPX_PATH,"GC*.gpx")):
            self.geocaches.append(geocache.Geocache(datei))
              
        if os.path.isfile(os.path.join(self.PATH, "geocache_visits.txt")):    # alle gefundenen Caches aus Logdatei in found_caches speichern, falls eine solche vorhanden
            [logged_caches, self.found_caches] = self.get_logged_and_found_caches(os.path.join(self.PATH, "geocache_visits.txt"))
            if len(self.found_caches) > 0:
                self.found_exists = True
            if len(self.found_caches) < len(logged_caches): # Warnung, falls weitere Caches in Logdatei, die noch nicht gefunden wurden
                self.warning = True
            else:
                self.warning = False
                
        while True:                                         # Hauptmenue
            task = user_io.hauptmenue(self.found_exists)
            if task == "alle_anzeigen":
                self.sortieren_und_anzeigen()
            elif task == "einen_anzeigen":
                self.einen_anzeigen()
            elif task == "suchen":
                self.suchen()
            elif task == "gefundene_anzeigen":
                self.gefundene_anzeigen()
            elif task == "exit":
                break

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
        self.geocaches = sorted(self.geocaches, key = lambda geocache: getattr(geocache, kriterium).lower(), reverse = rev)
        user_io.general_output(self.alle_anzeigen())
        
    def alle_anzeigen(self):
        """gibt einen String zurueck, in dem die Kurzinfos aller Caches auf dem Geraet jeweils in einer Zeile stehen"""
        text = ""
        for c in self.geocaches:
            text = text + c.kurzinfo() + "\n"
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
        
            task = user_io.einen_anzeigen()
            if task == "loeschen":
                self.loeschen([cache])
        
    def gc_auswahl_anzeigen(self, cacheliste):
        """gibt einen String zurueck, in dem Kurzinfos aller Caches aus Cacheliste in jeweils einer Zeile stehen"""
        text = ""
        for c in cacheliste:
            text = text + c.kurzinfo() + "\n"
        return text
        
    def suchen(self):
        """durchsucht die Caches nach dem gewuenschten Kriterium und leitet ggf. zu weiteren Aufgaben weiter"""
        
        suchergebnisse = []
        kriterium = user_io.suchen()
        if kriterium == "name" or kriterium == "beschreibung":
            suchbegriff = user_io.input_decode("Suche nach... ")
            for c in self.geocaches:
                if suchbegriff in getattr(c, kriterium):
                    suchergebnisse.append(c)
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
            user_io.general_output("Achtung! Du solltest die Caches vor dem Loeschen auf geocaching.com loggen.")
            if self.warning:
                user_io.general_output("Warnung! Bei Fortfahren werden auch Log-Informationen ueber Caches geloescht, die nicht gefunden wurden.")
            self.loeschen(self.found_caches)
            self.found_exists = False
            os.remove(os.path.join(self.PATH,"geocache_visits.txt"))
            os.remove(os.path.join(self.PATH,"geocache_logs.xml"))
           
    def loeschen(self, cacheliste):
        """loescht alle Caches aus cacheliste vom Geraet"""
        if user_io.loeschbestaetigung():
            for c in cacheliste:
                os.remove(c.dateiname_path)
                self.geocaches = [c for c in self.geocaches if c not in cacheliste]
          
if __name__ == "__main__":
    newProgram = Programinstanz()
  