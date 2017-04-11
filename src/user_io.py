PATH = r"F:\Garmin"    # path to GPS-device (standard)
CODING = "cp1252"   # coding of cmd (cp1252 recommended)
EDITORNAME = "notepad.exe" # name (+ path) of standard text editor

import ownfunctions

def general_output(string):
    """prints string on cmd"""
    string = ownfunctions.replace_signs(string)
    print string
    
def general_input(string):
    """asks for user input (by the use of string) and returns it (as string)"""
    return raw_input(string)
 
def input_decode(string):
    """asks for user input (by the help of string), decodes it and returns it as string
    string must not contain characters that are not included in CODING"""
    return raw_input(string).decode(CODING)
    
def show_main_menu(found_exists):
    """prints main menu"""
    
    print "\nWas moechtest du als naechstes tun?"
    print "1: Geocaches update"
    print "2: Alle auf dem Geraet gespeicherten Geocaches sort_caches und anzeigen"
    print "3: Alle auf dem Geraet gespeicherten Geocaches auf Karte zeigen"
    print "4: Beschreibung fuer einen bestimmten Cache anzeigen (GC-Code erforderlich)"
    print "5: Geocaches durchsearch"
    if found_exists:
        print "6: Alle gefundenen Caches anzeigen"
        print "7: https://www.geocaching.com/map aufrufen"
        print "8: https://www.google.de/maps aufrufen"
        print "9: Programm verlassen"
    else:
        print "6: https://www.geocaching.com/map aufrufen"
        print "7: https://www.google.de/maps aufrufen"
        print "8: Programm verlassen"
    
def main_menu(found_exists):
    """prints main menu and asks for user input
    returns task that is chosen by user input"""
    
    show_main_menu(found_exists)
    input = raw_input(">> ")
    
    if input == "1":
        return "update"
    elif input == "2":
        return "show_all"
    elif input == "3":
        return "show_all_on_map"
    elif input == "4":
        return "show_one"
    elif input == "5":
        return "search"
    elif input == "6" and found_exists:
        return "show_founds"
    elif input == "7" and found_exists:
        return "gc-maps"
    elif input == "8" and found_exists:
        return "google-maps"
    elif input == "9" and found_exists:
        return "exit"
    elif input == "6" and not found_exists:
        return "gc-maps"
    elif input == "7" and not found_exists:
        return "google-maps"
    elif input == "8" and not found_exists:
        return "exit"
    else:
        print "Ungueltige Eingabe!"  

def sort_caches():
    """asks for criterion and if the caches should be sorted forwards or backwards
    
    returns list with two elements
    first element: string that corresponds to criterion
    second element: True (sorting backwards) or False (sorting forwards)"""
    
    criterions = ["gccode", "name", "type", "difficulty", "terrain", "size", "downloaddate", "available", "distance"]
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
    input_criterion = raw_input(">> ")
    if input_criterion == "0":
        print "Ungueltige Eingabe: Sortierung erfolgt nach GC-Code"
        criterion = "gccode"
    else:
        try:
            criterion = criterions[int(input_criterion)-1]
        except IndexError:
            print "Ungueltige Eingabe: Sortierung erfolgt nach GC-Code"
            criterion = "gccode"
        except ValueError:
            print "Ungueltige Eingabe: Sortierung erfolgt nach GC-Code"
            criterion = "gccode"
        
    print "In welche Richtung sollen die Caches sortiert werden?"
    print "1: aufsteigend"
    print "2: absteigend"
    input_direction = raw_input(">> ")
    if input_direction == "2":
        backward = True
    else:
        backward = False 
        
    return [criterion, backward]
    
def search():
    """asks for criterion by which search should be performed and returns it (as string)"""
    
    criterions = ["name", "description", "type", "difficulty", "terrain", "size", "downloaddate", "available", "attributes", "distance"]
    print "\nWonach willst du search?"
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
    input = raw_input(">> ")
    if input == "0":
        print "Ungueltige Eingabe"
    else:
        try:
            return criterions[int(input)-1]
        except IndexError:
            print "Ungueltige Eingabe"
        except ValueError:
            print "Ungueltige Eingabe"
        
def search_type():
    """asks for cachetype which should be searched and returns it (as string)"""
    
    print "Gib den Cachetyp ein, nach dem du search willst."
    print "Moegliche Typen: Traditional Cache, Multi-cache, Mystery Cache, EarthCache, Letterbox Hybrid, Event Cache, Wherigo Cache, Geocaching HQ, Unknown Type"
    print "Achtung! Gross- und Kleinschreibung beachten!"
    input = raw_input(">> ")
    return input
    
def search_attribute(existing_attributes):
    """asks for attribute which should be searched and returns it (as string)"""

    print "Gib das Attribut ein, nach dem du search willst."
    attr_string = ", ".join(existing_attributes)
    print "Moegliche Attribute: {}".format(attr_string)
    input = raw_input(">> ")
    return input
        
def actions_after_search():
    """asks for next action after a search, returns this action as a string"""
    
    print "\nWas moechtest du als naechstes tun?"
    print "1: Alle Suchergebnisse erneut anzeigen (bei evtl. Loeschen nicht aktualisiert)"
    print "2: Alle Suchergebnisse delete"
    print "3: Beschreibung fuer eines der Suchergebnisse anzeigen"
    print "4: zurueck"
    input = raw_input(">> ")
    
    if input == "1":
        return "show_again"
    elif input == "2":
        return "delete"
    elif input == "3":
        return "show_one"
    elif input == "4":
        return "back"
    else:
        print "Ungueltige Eingabe"
        
def actions_with_founds():
    """asks after showing the found caches what to do next
    returns the next action as a string"""
    
    print "\nWas moechtest du als naechstes tun?"
    print "1: Gefundene Caches auf geocaching.com log (by uploading drafts / fieldnotes)"
    print "2: Alle gefundenen Caches delete"
    print "3: zurueck"
    input = raw_input(">> ")
    if input == "1":
        return "log"
    elif input == "2":
        return "delete"
    elif input == "3":
        return "exit"    
      
def confirm_deletion():
    """asks before deleting caches if they should really be deleted
    returns True for yes and False for no"""
    
    input = raw_input("\nWillst du den / die ausgewaehlten Cache(s) wirklich delete? (y/n) ")
    if input == "y":
        return True
    else:
        return False
        
def show_one():
    """asks after showing one cache what to do next
    returns the next action as a string"""
    
    print "\nWas moechtest du als naechstes tun?"
    print "1: diesen Cache delete"
    print "2: diesen Cache auf geocaching.com oeffnen"
    print "3: Abstand dieses Caches zu einer bestimmten Position berechnen"
    print "4: Position des Caches auf der Karte https://www.geocaching.com/map anzeigen"
    print "5: Position des Caches auf der Karte https://www.google.de/maps anzeigen"
    print "6: zurueck"
    input = raw_input(">> ")
    if input == "1":
        return "delete"
    elif input == "2":
        return "gc.com"
    elif input == "3":
        return "dist"
    elif input == "4":
        return "gc-map"
    elif input == "5":
        return "googlemaps"
        
def coordinates_input():
    """asks for coordinates, returns input as a string"""
    
    print u"Gib die Koordinaten ein (Format: X XX°XX.XXX, X XXX°XX.XXX oder URL (google maps oder geocaching.com/map)"
    koords = raw_input(">> ")
    return koords
        
def ask_for_path():
    """asks for the path to the GPS-device and returns it
    if no path is specified: returns the standard PATH"""

    print "\nGib den Pfad zum GPS-Geraet ein (NICHT zum Unterordner 'GPX')."
    print "Falls Standardpfad '{}' uebernommen werden soll: keine Eingabe".format(PATH)
    input = raw_input(">> ")
    if input == "":
        return PATH
    else:
        return input
        
def show_all_on_map_start():
    """explains how the task 'show_all_on_map' works and asks for path to texteditor
    returns path to texteditor or - if no path is specified - the standard EDITORNAME"""

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
    input = raw_input(">> ")
    if input == "":
        return EDITORNAME
    else:
        return input
    
def show_all_on_map_end():
    """asks for another input before leaving task 'show_all_on_map'"""
    
    print "Schliesse den Editor und druecke Enter."
    raw_input(">> ")
        
