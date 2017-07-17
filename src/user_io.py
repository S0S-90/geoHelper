#!/usr/bin/python
# -*- coding: utf-8 -*-

"""This file contains the user interface."""

from __future__ import print_function
import ownfunctions

PATH = r"F:\Garmin"    # path to GPS-device (standard)
CODING = "cp1252"   # coding of cmd (cp1252 recommended)
EDITORNAME = "notepad.exe"  # name (+ path) of standard text editor


def general_output(string):
    """prints string on cmd"""
    string = ownfunctions.replace_signs(string)
    print(string)


# noinspection PyCompatibility
def general_input(string):
    """asks for user input (by the use of string) and returns it (as string)"""
    return raw_input(string)  # in python 3 input is raw_input by standard


# noinspection PyCompatibility
def input_decode(string):
    """asks for user input (by the help of string), decodes it and returns it as string
    string must not contain characters that are not included in CODING"""
    return raw_input(string).decode(CODING)  # in python 3 input is raw_input by standard


def show_main_menu(found_exists):
    """prints main menu"""

    print ("\nWas moechtest du als naechstes tun?")
    print ("1: Geocaches aktualisieren")
    print ("2: Alle auf dem Geraet gespeicherten Geocaches sortieren und anzeigen")
    print ("3: Alle Wegpunkte anzeigen und zu Geocaches zuordnen")
    print ("4: Alle auf dem Geraet gespeicherten Geocaches auf Karte zeigen (INTERNET!!!)")
    print ("5: Beschreibung fuer einen bestimmten Cache anzeigen (GC-Code erforderlich)")
    print ("6: Einen bestimmten Cache auf geocaching.com oeffnen (INTERNET!!!)")
    print ("7: Geocaches durchsuchen")
    if found_exists:
        print ("8: Alle gefundenen Caches anzeigen")
        print ("9: https://www.geocaching.com/map aufrufen (INTERNET!!!)")
        print ("10: https://www.google.de/maps aufrufen (INTERNET!!!)")
        print ("11: Programm verlassen")
    else:
        print ("8: https://www.geocaching.com/map aufrufen (INTERNET!!!)")
        print ("9: https://www.google.de/maps aufrufen (INTERNET!!!)")
        print ("10: Programm verlassen")


def main_menu(found_exists):
    """prints main menu and asks for user input
    returns task that is chosen by user input"""
    
    show_main_menu(found_exists)
    # noinspection PyCompatibility
    inp = raw_input(">> ")  # in python 3 input is raw_input by standard
    
    if inp == "1":
        return "update"
    elif inp == "2":
        return "show_all"
    elif inp == "3":
        return "show_waypoints"
    elif inp == "4":
        return "show_on_map"
    elif inp == "5":
        return "show_one"
    elif inp == "6":
        return "show_one_gc.com"
    elif inp == "7":
        return "search"
    elif inp == "8" and found_exists:
        return "show_founds"
    elif inp == "9" and found_exists:
        return "gc-maps"
    elif inp == "10" and found_exists:
        return "google-maps"
    elif inp == "11" and found_exists:
        return "exit"
    elif inp == "8" and not found_exists:
        return "gc-maps"
    elif inp == "9" and not found_exists:
        return "google-maps"
    elif inp == "10" and not found_exists:
        return "exit"
    else:
        print ("Ungueltige Eingabe!")


def sort_caches():
    """asks for criterion and if the caches should be sorted forwards or backwards
    
    returns list with two elements
    first element: string that corresponds to criterion
    second element: True (sorting backwards) or False (sorting forwards)"""
    
    criterions = ["gccode", "name", "type", "difficulty", "terrain", "size", "downloaddate", "available", "distance"]
    print ("\nWonach sollen die Geocaches sortiert werden?")
    print ("1: GC-Code")
    print ("2: Name")
    print ("3: Cache-Typ")
    print ("4: D-Wertung")
    print ("5: T-Wertung")
    print ("6: Groesse")
    print ("7: Download-Datum")
    print ("8: Verfuegbarkeit")
    print ("9: Abstand von einer bestimmten Position (Koordinaten erforderlich)")
    # noinspection PyCompatibility
    input_criterion = raw_input(">> ")  # in python 3 input is raw_input by standard
    if input_criterion == "0":
        print ("Ungueltige Eingabe: Sortierung erfolgt nach GC-Code")
        criterion = "gccode"
    else:
        try:
            criterion = criterions[int(input_criterion)-1]
        except IndexError:
            print ("Ungueltige Eingabe: Sortierung erfolgt nach GC-Code")
            criterion = "gccode"
        except ValueError:
            print ("Ungueltige Eingabe: Sortierung erfolgt nach GC-Code")
            criterion = "gccode"
        
    print ("In welche Richtung sollen die Caches sortiert werden?")
    print ("1: aufsteigend")
    print ("2: absteigend")
    # noinspection PyCompatibility
    input_direction = raw_input(">> ")  # in python 3 input is raw_input by standard
    if input_direction == "2":
        backward = True
    else:
        backward = False 
        
    return [criterion, backward]


def search():
    """asks for criterion by which search should be performed and returns it (as string)"""
    
    criterions = ["name", "description", "type", "difficulty", "terrain",
                  "size", "downloaddate", "available", "attribute", "distance"]
    print ("\nWonach willst du suchen?")
    print ("1: Name")
    print ("2: Beschreibung")
    print ("3: Cache-Typ")
    print ("4: D-Wertung")
    print ("5: T-Wertung")
    print ("6: Groesse")
    print ("7: Download-Datum")
    print ("8: Verfuegbarkeit")
    print ("9: Attribut")
    print ("10: Abstand von einer bestimmten Position (Koordinaten erforderlich)")
    # noinspection PyCompatibility
    inp = raw_input(">> ")  # in python 3 input is raw_input by standard
    if inp == "0":
        print ("Ungueltige Eingabe")
    else:
        try:
            return criterions[int(inp)-1]
        except IndexError:
            print ("Ungueltige Eingabe")
        except ValueError:
            print ("Ungueltige Eingabe")


def search_type():
    """asks for cachetype which should be searched and returns it (as string)"""
    
    print ("Gib den Cachetyp ein, nach dem du suchen willst.")
    print ("Moegliche Typen: Traditional Cache, Multi-cache, Mystery Cache, EarthCache, Letterbox Hybrid, Event Cache, "
           "Wherigo Cache, Geocaching HQ, Unknown Type")
    print ("Achtung! Gross- und Kleinschreibung beachten!")
    # noinspection PyCompatibility
    inp = raw_input(">> ")  # in python 3 input is raw_input by standard
    return inp


def search_attribute(existing_attributes):
    """asks for attribute which should be searched and returns it (as string)"""

    print ("Gib das Attribut ein, nach dem du suchen willst.")
    attr_string = ", ".join(existing_attributes)
    print ("Moegliche Attribute: {}".format(attr_string))
    # noinspection PyCompatibility
    inp = raw_input(">> ")  # in python 3 input is raw_input by standard
    return inp


def actions_after_search():
    """asks for next action after a search, returns this action as a string"""
    
    print ("\nWas moechtest du als naechstes tun?")
    print ("1: Alle Suchergebnisse erneut anzeigen (bei evtl. Loeschen nicht aktualisiert)")
    print ("2: Alle Suchergebnisse loeschen")
    print ("3: Alle Suchergebnisse auf Karte zeigen (INTERNET!!!)")
    print ("4: Beschreibung fuer eines der Suchergebnisse anzeigen")
    print ("5: Einen bestimmten Cache auf geocaching.com oeffnen (INTERNET!!!)")
    print ("6: zurueck")
    # noinspection PyCompatibility
    inp = raw_input(">> ")  # in python 3 input is raw_input by standard
    
    if inp == "1":
        return "show_again"
    elif inp == "2":
        return "delete"
    elif inp == "3":
        return "show_on_map"
    elif inp == "4":
        return "show_one"
    elif inp == "5":
        return "show_one_gc.com"
    elif inp == "6":
        return "back"
    else:
        print ("Ungueltige Eingabe")


def actions_with_founds():
    """asks after showing the found caches what to do next
    returns the next action as a string"""
    
    print ("\nWas moechtest du als naechstes tun?")
    print ("1: Gefundene Caches auf geocaching.com loggen (ueber den Upload von drafts / fieldnotes, INTERNET!!!)")
    print ("2: Alle gefundenen Caches loeschen")
    print ("3: zurueck")
    # noinspection PyCompatibility
    inp = raw_input(">> ")  # in python 3 input is raw_input by standard
    if inp == "1":
        return "log"
    elif inp == "2":
        return "delete"
    elif inp == "3":
        return "exit"    


def confirm_deletion():
    """asks before deleting caches if they should really be deleted
    returns True for yes and False for no"""

    # noinspection PyCompatibility
    inp = raw_input("\nWillst du den / die ausgewaehlten Cache(s) wirklich loeschen? (y/n) ")  # in python 3 only raw_input
    if inp == "y":
        return True
    else:
        return False


def assign_waypoints():
    """asks if waypoints should be assigned"""

    # noinspection PyCompatibility
    inp = raw_input("\nWillst die Wegpunkte zu Geocaches zuordnen? (y/n) ")  # in python 3 only raw_input
    if inp == "y":
        return True
    else:
        return False


def show_one(waypoints):
    """asks after showing one cache what to do next
    waypoints = True, if shown cache has waypoints, False if not

    returns the next action as a string"""
    
    print ("\nWas moechtest du als naechstes tun?")
    print ("1: diesen Cache loeschen")
    print ("2: diesen Cache auf geocaching.com oeffnen (INTERNET!!!)")
    print ("3: Abstand dieses Caches zu einer bestimmten Position berechnen")
    print ("4: Position des Caches auf der Karte https://www.geocaching.com/map anzeigen (INTERNET!!!)")
    print ("5: Position des Caches auf der Karte https://www.google.de/maps anzeigen (INTERNET!!!)")
    if waypoints:
        print ("6: diesen Cache mit allen Wegpunkten auf Karte zeigen (INTERNET!!!)")
        print ("7: zurueck")
    else:
        print ("6: zurueck")
    # noinspection PyCompatibility
    inp = raw_input(">> ")  # in python 3 input is raw_input by standard
    if inp == "1":
        return "delete"
    elif inp == "2":
        return "gc.com"
    elif inp == "3":
        return "dist"
    elif inp == "4":
        return "gc-map"
    elif inp == "5":
        return "googlemaps"
    elif inp == "6" and waypoints:
        return "mapcustomizer"


def coordinates_input():
    """asks for coordinates, returns input as a string"""
    
    print (u"Gib die Koordinaten ein (Format: X XX°XX.XXX, X XXX°XX.XXX oder URL (google maps oder geocaching.com/map))")
    # noinspection PyCompatibility
    coords = raw_input(">> ").decode(CODING)  # in python 3 input is raw_input by standard
    return coords


def ask_for_path():
    """asks for the path to the GPS-device and returns it
    if no path is specified: returns the standard PATH"""

    print ("\nGib den Pfad zum GPS-Geraet ein (NICHT zum Unterordner 'GPX').")
    print ("Falls Standardpfad '{}' uebernommen werden soll: keine Eingabe".format(PATH))
    # noinspection PyCompatibility
    inp = raw_input(">> ")  # in python 3 input is raw_input by standard
    if inp == "":
        return PATH
    else:
        return inp


def ask_for_waypoints():
    """asks if waypoints should be shown on map"""

    # noinspection PyCompatibility
    inp = raw_input("\nSollen auch Wegpunkte auf der Karte angezeigt werden? (y/n) ")  # in python 3 only raw_input
    if inp == "y":
        return True
    else:
        return False


def show_on_map_start(one, free_waypoints):
    """explains how the task 'show_on_map' works and asks for path to texteditor
    returns path to texteditor or - if no path is specified - the standard EDITORNAME

    one = True if only one geocache (with waypoints), False if several geocaches
    free_waypoints = True if free waypoints are shown (i.e. waypoints that don't belong to a cache)
                     only if all caches are shown and waypoints should be shown
    """

    print ("\nNach dem Klicken werden sich mehrere Fenster oeffnen. "
           "Eines davon ist der Editor, das andere die Seite mapcustomizer.com in deinem Browser.")
    print ("Um den Cache / die Caches auf der Karte anzuzeigen, kopiere den vollstaendigen Inhalt der Textdatei "
           "aus deinem Editor in das Feld 'Bulk Entry' im Browser.")
    if not one:        # if more than one geocache
        print ("Die Caches werden in folgenden Farben angezeigt:")
        print ("Gruen: Traditional Cache")
        print ("Rot: Multi-cache")
        print ("Blau: Mystery Cache")
        print ("Braun: EarthCache")
        print ("Grau: Letterbox, Geocaching HQ")
        z = "Gelb: Event Cache, Wherigo Cache"
        if free_waypoints:
            z += ", Wegpunkte"
        print (z)
        print ("Pink: unbekannter Typ")
    print ("Gib nun den Pfad zu deinem Editor an: (bei Benutzung von Windows sollte das unnoetig sein)")
    # noinspection PyCompatibility
    inp = raw_input(">> ")  # in python 3 input is raw_input by standard
    if inp == "":
        return EDITORNAME
    else:
        return inp


def show_on_map_end():
    """asks for another input before leaving task 'show_on_map'"""
    
    print ("Schliesse den Editor und druecke Enter.")
    # noinspection PyCompatibility
    raw_input(">> ")  # in python 3 input is raw_input by standard
 
 
# string for main.py
GPS_NOT_FOUND = "GPS-Geraet nicht unter folgender Pfadangabe zu finden"

# string collection for gps_content.py
INVALID_INPUT = "Achtung! Ungueltige Eingabe."
WARNING_BROKEN_FILE = "Achtung! Kaputte Datei"
GEOCACHES = "Geocaches"
WAYPOINTS = "Wegpunkte"
AND = "und"
ON_DEVICE = "auf dem Geraet."
NO_WAYPOINTS_ON_DEVICE = "Keine Wegpunkte auf dem Geraet."
NO_CACHES_ON_DEVICE = "Keine Caches auf dem Geraet."
INPUT_GCCODE = "Gib den GC-Code ein: "
GC_DOES_NOT_EXIST = "Dieser GC-Code existiert nicht."
SEARCH_FOR = "Suche nach... "
MIN_MAX_SEPERATED_BY_KOMMA = "Minimaler und maximaler Wert (mit Komma voneinander getrennt)"
POSSIBLE_SIZES = "Moegliche Groessen"
DATE_SEPERATED_BY_KOMMA = "Fruehestes und spaetestes Datum (mit Komma voneinander getrennt). Format: DD.MM.YYYY"
CACHES_AVAILABLE_OR_NOT = "Moechtest du die Caches sehen, die verfuegbar sind, oder die, die nicht verfuegbar sind? (y/n) "
DIST_SEPERATED_BY_KOMMA = "Minimale und maximale Distanz in Kilometern (mit Komma voneinander getrennt): "
NO_CACHES_FOUND = "keine Geocaches gefunden"
WARNING_LOG_INFO = "WARNUNG! Bei Fortfahren werden auch Log-Informationen ueber Caches geloescht,  \
                   die nicht gefunden wurden."