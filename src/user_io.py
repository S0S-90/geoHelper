PATH = r"F:\Garmin"    # Pfad zu dem Geraet (Standardwert)
CODIERUNG = "cp1252"   # Codierung der Kosole (cp1252 empfohlen)
EDITORNAME = "notepad.exe" # Name (+Pfad) des Standardeditors

import ownfunctions

def general_output(string):
    """gibt einen String auf der Konsole aus"""
    string = ownfunctions.zeichen_ersetzen(string)
    print string
    
def general_input(string):
    """fragt mit Hilfe von string nach einer Benutzereingabe und gibt diese zurueck"""
    return raw_input(string)
 
def input_decode(string):
    """fragt mit Hilfe von string nach einer Benutzereingabe, dekodiert diese und gibt sie zurueck
    string darf keine Charakters enthalten, die nicht in der CODIERUNG vorhanden sind"""
    return raw_input(string).decode(CODIERUNG)
    
def hauptmenue_anzeigen(found_exists):
    """gibt das Hauptmenue aus"""
    print "\nWas moechtest du als naechstes tun?"
    print "1: Geocaches aktualisieren"
    print "2: Alle auf dem Geraet gespeicherten Geocaches sortieren und anzeigen"
    print "3: Alle auf dem Geraet gespeicherten Geocaches auf Karte zeigen"
    print "4: Beschreibung fuer einen bestimmten Cache anzeigen (GC-Code erforderlich)"
    print "5: Geocaches durchsuchen"
    if found_exists:
        print "6: Alle gefundenen Caches anzeigen"
        print "7: https://www.geocaching.com/map aufrufen"
        print "8: https://www.google.de/maps aufrufen"
        print "9: Programm verlassen"
    else:
        print "6: https://www.geocaching.com/map aufrufen"
        print "7: https://www.google.de/maps aufrufen"
        print "8: Programm verlassen"
    
def hauptmenue(found_exists):
    """"gibt das Hauptmenue aus und je nach Benutzereingabe die Aufgabe zurueck, die als naechstes ausgefuehrt werden soll"""
    
    hauptmenue_anzeigen(found_exists)
    eingabe = raw_input(">> ")
    
    if eingabe == "1":
        return "aktualisieren"
    elif eingabe == "2":
        return "alle_anzeigen"
    elif eingabe == "3":
        return "show_all_on_map"
    elif eingabe == "4":
        return "einen_anzeigen"
    elif eingabe == "5":
        return "suchen"
    elif eingabe == "6" and found_exists:
        return "gefundene_anzeigen"
    elif eingabe == "7" and found_exists:
        return "gc-maps"
    elif eingabe == "8" and found_exists:
        return "google-maps"
    elif eingabe == "9" and found_exists:
        return "exit"
    elif eingabe == "6" and not found_exists:
        return "gc-maps"
    elif eingabe == "7" and not found_exists:
        return "google-maps"
    elif eingabe == "8" and not found_exists:
        return "exit"
    else:
        print "Ungueltige Eingabe!"  

def sortieren():
    """fragt nach dem Kriterium und der Reihenfolge fuer die Suche
    gibt eine Liste zurueck, in der das erste Element das Kriterium und 
    das zweite je nachdem, ob die Reihenfolge umgekehrt werden soll, True oder False ist"""
    
    kriterien = ["gccode", "name", "type", "difficulty", "terrain", "size", "downloaddate", "available", "distance"]
    print "\nWonach sollen die Geocaches sortiert werden?"
    print "1: GC-Code"
    print "2: Name"
    print "3: Cache-Typ"
    print "4: D-Wertung"
    print "5: T-Wertung"
    print "6: Groesse"
    print "7: Download-Datum"
    print "8: Verfuegbarkeit"
    print "9: Abstand von einer bestimmten Position (Koordinaten erforderlich)"
    eingabe_kriterium = raw_input(">> ")
    if eingabe_kriterium == "0":
        print "Ungueltige Eingabe: Sortierung erfolgt nach GC-Code"
        kriterium = "gccode"
    else:
        try:
            kriterium = kriterien[int(eingabe_kriterium)-1]
        except IndexError:
            print "Ungueltige Eingabe: Sortierung erfolgt nach GC-Code"
            kriterium = "gccode"
        except ValueError:
            print "Ungueltige Eingabe: Sortierung erfolgt nach GC-Code"
            kriterium = "gccode"
        
    print "In welche Richtung sollen die Caches sortiert werden?"
    print "1: aufsteigend"
    print "2: absteigend"
    eingabe_richtung = raw_input(">> ")
    if eingabe_richtung == "2":
        richtung_umkehren = True
    else:
        richtung_umkehren = False 
        
    return [kriterium, richtung_umkehren]
    
def suchen():
    """fragt nach dem Kriterium, wonach gesucht werden soll, und gibt dieses zurueck"""
    
    kriterien = ["name", "beschreibung", "type", "difficulty", "terrain", "size", "downloaddate", "available", "attribute", "distance"]
    print "\nWonach willst du suchen?"
    print "1: Name"
    print "2: Beschreibung"
    print "3: Cache-Typ"
    print "4: D-Wertung"
    print "5: T-Wertung"
    print "6: Groesse"
    print "7: Download-Datum"
    print "8: Verfuegbarkeit"
    print "9: Attribut"
    print "10: Abstand von einer bestimmten Position (Koordinaten erforderlich)"
    eingabe = raw_input(">> ")
    if eingabe == "0":
        print "Ungueltige Eingabe"
    else:
        try:
            return kriterien[int(eingabe)-1]
        except IndexError:
            print "Ungueltige Eingabe"
        except ValueError:
            print "Ungueltige Eingabe"
        
def search_type():
    print "Gib den Cachetyp ein, nach dem du suchen willst."
    print "Moegliche Typen: Traditional Cache, Multi-cache, Mystery Cache, EarthCache, Letterbox Hybrid, Event Cache, Wherigo Cache, Geocaching HQ, Unknown Type"
    print "Achtung! Gross- und Kleinschreibung beachten!"
    eingabe = raw_input(">> ")
    return eingabe
    
def search_attribute(existing_attributes):
    print "Gib das Attribut ein, nach dem du suchen willst."
    attr_string = ", ".join(existing_attributes)
    print "Moegliche Attribute: {}".format(attr_string)
    eingabe = raw_input(">> ")
    return eingabe
        
def aktionen_auswahl_suchen():
    """fragt nach einer Suche nach der naechsten Aktion"""
    
    print "\nWas moechtest du als naechstes tun?"
    print "1: Alle Suchergebnisse erneut anzeigen (bei evtl. Loeschen nicht aktualisiert)"
    print "2: Alle Suchergebnisse loeschen"
    print "3: Beschreibung fuer eines der Suchergebnisse anzeigen"
    print "4: zurueck"
    eingabe = raw_input(">> ")
    
    if eingabe == "1":
        return "neu_anzeigen"
    elif eingabe == "2":
        return "loeschen"
    elif eingabe == "3":
        return "einen_anzeigen"
    elif eingabe == "4":
        return "back"
    else:
        print "Ungueltige Eingabe"
        
def aktionen_auswahl_gefunden():
    """fragt, nachdem die gefundenen Caches angezeigt wurden, ob sie nun geloescht werden sollen"""
    
    print "\nWas moechtest du als naechstes tun?"
    print "1: Alle gefundenen Caches loeschen (vorher Loggen auf geocaching.com moeglich)"
    print "2: zurueck"
    eingabe = raw_input(">> ")
    if eingabe == "1":
        return "loeschen"
      
def loeschbestaetigung():
    """fragt vor dem Loeschen von Caches nach, ob tatsaechlich geloescht werden soll"""
    
    eingabe = raw_input("\nWillst du den / die ausgewaehlten Cache(s) wirklich loeschen? (y/n) ")
    if eingabe == "y":
        return True
    else:
        return False
        
def einen_anzeigen():
    """fragt nach dem Anzeigen eines Caches, ob dieser geloescht werden soll"""
    
    print "\nWas moechtest du als naechstes tun?"
    print "1: diesen Cache loeschen"
    print "2: diesen Cache auf geocaching.com oeffnen"
    print "3: Abstand dieses Caches zu einer bestimmten Position berechnen"
    print "4: Position des Caches auf der Karte https://www.geocaching.com/map anzeigen"
    print "5: Position des Caches auf der Karte https://www.google.de/maps anzeigen"
    print "6: zurueck"
    eingabe = raw_input(">> ")
    if eingabe == "1":
        return "loeschen"
    elif eingabe == "2":
        return "gc.com"
    elif eingabe == "3":
        return "dist"
    elif eingabe == "4":
        return "gc-map"
    elif eingabe == "5":
        return "googlemaps"
        
def koordinaten_eingabe():
    print u"Gib die Koordinaten ein (Format: X XX°XX.XXX, X XXX°XX.XXX oder URL (google maps oder geocaching.com/map)"
    koords = raw_input(">> ")
    return koords

def open_fieldnotes():
    print "Achtung! Du solltest die Caches vor dem Loeschen auf geocaching.com loggen."
    eingabe = raw_input("Moechtest du deine Fieldnotes auf geocaching.com hochladen? (y/n) ")
    if eingabe == "y":
        return True
    else:
        return False
        
def ask_for_path():
    print "\nGib den Pfad zum GPS-Geraet ein (NICHT zum Unterordner 'GPX')."
    print "Falls Standardpfad '{}' uebernommen werden soll: keine Eingabe".format(PATH)
    eingabe = raw_input(">> ")
    if eingabe == "":
        return PATH
    else:
        return eingabe
        
def show_all_on_map_start():
    print "\nNach dem Klicken werden sich mehrere Fenster oeffnen. Eines davon ist der Editor, das andere die Seite mapcustomizer.com in deinem Browser."
    print "Um die Caches auf der Karte anzuzeigen, kopiere den vollstaendigen Inhalt der Textdatei aus deinem Editor in das Feld 'Bulk Entry' im Browser."
    print "Die Caches werden in folgenden Farben angezeigt:"
    print "Gruen: Traditional Cache"
    print "Rot: Multi-cache"
    print "Blau: Mystery Cache"
    print "Braun: EarthCache"
    print "Grau: Letterbox, Geocaching HQ"
    print "Gelb: Event Cache, Wherigo Cache"
    print "Pink: unbekannter Typ"
    print "Gib nun den Pfad zu deinem Editor an: (bei Benutzung von Windows sollte das unnoetig sein)"
    eingabe = raw_input(">> ")
    if eingabe == "":
        return EDITORNAME
    else:
        return eingabe
    
def show_all_on_map_end():
    print "Schliesse den Editor und druecke Enter."
    raw_input(">> ")


        
