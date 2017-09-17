#!/usr/bin/python
# -*- coding: utf-8 -*-

"""tests for user_io.py"""

import unittest
import mock
import sys
# noinspection PyCompatibility
from StringIO import StringIO  # module not existent in python 3
import test_frame
import user_io
import geocache

    
class TestGeneralOutput(unittest.TestCase):

    def test_normaltext(self):
        out = StringIO()
        sys.stdout = out                  # capture print output in out
        user_io.general_output("hello")   # fill out
        output = out.getvalue()   # save value of out in output
        self.assertEqual(output, "hello\n")
        
    def test_textwithcapitalsandnumbers(self):
        out = StringIO()
        sys.stdout = out                  # capture print output in out
        user_io.general_output("hEllo2")  # fill out
        output = out.getvalue()   # save value of out in output
        self.assertEqual(output, "hEllo2\n")
        
    def test_umlauts(self):
        out = StringIO()
        sys.stdout = out                                       # capture print output in out
        user_io.general_output(u"m{}rchen".format(u"\u00E4"))  # fill out
        output = out.getvalue()                        # save value of out in output
        self.assertEqual(output, u"m{}rchen\n".format(u"\u00E4"))
        
    def test_replacable_signs(self):
        out = StringIO()
        sys.stdout = out                                        # capture print output in out
        user_io.general_output(u"hello {}".format(u"\u263a"))   # fill out
        output = out.getvalue()                         # save value of out in output
        self.assertEqual(output, "hello :-)\n")
        
    def test_unknown_signs(self):
        out = StringIO()
        sys.stdout = out                                                    # capture print output in out
        user_io.general_output(u"Flag Turkey: {}".format(u"\u262a"))        # fill out
        output = out.getvalue()                                     # save value of out in output
        self.assertEqual(output, u"Flag Turkey: {}\n".format(u"\u001a"))
  
        
class TestGeneralInput(unittest.TestCase):   

    def test_normaltext(self):
        with mock.patch('__builtin__.raw_input', return_value="hello"):
            self.assertEqual(user_io.general_input(">> "), 'hello')
        
    def test_textwithcapitalsandnumbers(self):
        with mock.patch('__builtin__.raw_input', return_value="hEllo2"):
            self.assertEqual(user_io.general_input(">> "), 'hEllo2')
        
    def test_replacable_signs(self):
        with mock.patch('__builtin__.raw_input', return_value=u"hello {}".format(u"\u263a")): 
            self.assertEqual(user_io.general_input(">> "), u"hello {}".format(u"\u263a"))
        
    def test_umlauts(self):
        with mock.patch('__builtin__.raw_input', return_value=u"m{}rchen".format(u"\u00E4")):
            self.assertEqual(user_io.general_input(">> "), u"m{}rchen".format(u"\u00E4"))
        
    def test_unknown_signs(self):
        with mock.patch('__builtin__.raw_input', return_value=u"Flag Turkey: {}".format(u"\u262a")):
            self.assertEqual(user_io.general_input(">> "), u"Flag Turkey: {}".format(u"\u262a"))
        
    def test_number(self):
        with mock.patch('__builtin__.raw_input', return_value="42"):
            self.assertEqual(user_io.general_input(">> "), "42")
  
        
class TestInputDecode(unittest.TestCase):   

    def test_normaltext(self):
        with mock.patch('__builtin__.raw_input', return_value="hello"):
            self.assertEqual(user_io.input_decode(">> "), 'hello')
        
    def test_textwithcapitalsandnumbers(self):
        with mock.patch('__builtin__.raw_input', return_value="hEllo2"):
            self.assertEqual(user_io.input_decode(">> "), 'hEllo2')
        
    def test_replacable_signs(self):
        with mock.patch('__builtin__.raw_input', return_value=u"hello {}".format(u"\u263a")):
            self.assertRaises(UnicodeEncodeError, user_io.input_decode, ">> ")
        
    def test_umlaute(self):
        with mock.patch('__builtin__.raw_input', return_value='M\xe4rchen'):
            self.assertEqual(user_io.input_decode(">> "), u"Märchen")
        
    def test_unknown_signs(self):
        with mock.patch('__builtin__.raw_input', return_value=u"Flag Turkey: {}".format(u"\u262a")):
            self.assertRaises(UnicodeEncodeError, user_io.input_decode, ">> ")
        
    def test_number(self):
        with mock.patch('__builtin__.raw_input', return_value="42"):
            self.assertEqual(user_io.input_decode(">> "), "42")
 
        
class TestShowMainMenu(unittest.TestCase):
    
    def test_nofoundexists(self):
        out = StringIO()
        sys.stdout = out                  # capture print output in out
        user_io.show_main_menu(False)     # fill out
        output = out.getvalue()   # save value of out in output
        expected = "\nWas moechtest du als naechstes tun?\n"
        expected += "1: Geocaches aktualisieren\n"
        expected += "2: Alle auf dem Geraet gespeicherten Geocaches sortieren und anzeigen\n"
        expected += "3: Wegpunkt-Menue\n"
        expected += "4: Karten-Menue\n"
        expected += "5: Beschreibung fuer einen bestimmten Cache anzeigen (GC-Code erforderlich)\n"
        expected += "6: Geocaches durchsuchen\n"
        expected += "7: Programm verlassen\n"
        self.assertEqual(output, expected)
        
    def test_foundexists(self):
        out = StringIO()
        sys.stdout = out                  # capture print output in out
        user_io.show_main_menu(True)      # fill out
        output = out.getvalue()   # save value of out in output
        expected = "\nWas moechtest du als naechstes tun?\n"
        expected += "1: Geocaches aktualisieren\n"
        expected += "2: Alle auf dem Geraet gespeicherten Geocaches sortieren und anzeigen\n"
        expected += "3: Wegpunkt-Menue\n"
        expected += "4: Karten-Menue\n"
        expected += "5: Beschreibung fuer einen bestimmten Cache anzeigen (GC-Code erforderlich)\n"
        expected += "6: Geocaches durchsuchen\n"
        expected += "7: Alle gefundenen Caches anzeigen\n"
        expected += "8: Programm verlassen\n"
        self.assertEqual(output, expected)
   
        
class TestMainMenu(unittest.TestCase):

    def test_1_nofoundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="1"):
            self.assertEqual(user_io.main_menu(False), 'update')
        
    def test_2_nofoundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="2"):
            self.assertEqual(user_io.main_menu(False), 'show_all')
        
    def test_3_nofoundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="3"):
            self.assertEqual(user_io.main_menu(False), 'show_waypoints')

    def test_4_nofoundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="4"):
            self.assertEqual(user_io.main_menu(False), 'map-menu')
            
    def test_5_nofoundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="5"):
            self.assertEqual(user_io.main_menu(False), 'show_one')
        
    def test_6_nofoundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="6"):
            self.assertEqual(user_io.main_menu(False), 'search')
        
    def test_7_nofoundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="7"):
            self.assertEqual(user_io.main_menu(False), 'exit')
        
    def test_11_nofoundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="11"):
            self.assertEqual(user_io.main_menu(False), None)
        
    def test_1_foundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="1"):
            self.assertEqual(user_io.main_menu(True), 'update')
        
    def test_2_foundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="2"):
            self.assertEqual(user_io.main_menu(True), 'show_all')

    def test_3_foundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="3"):
            self.assertEqual(user_io.main_menu(False), 'show_waypoints')
        
    def test_4_foundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="4"):
            self.assertEqual(user_io.main_menu(True), 'map-menu')
            
    def test_5_foundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="5"):
            self.assertEqual(user_io.main_menu(True), 'show_one')
        
    def test_6_foundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="6"):
            self.assertEqual(user_io.main_menu(True), 'search')
        
    def test_7_foundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="7"):
            self.assertEqual(user_io.main_menu(True), 'show_founds')
        
    def test_8_foundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="8"):
            self.assertEqual(user_io.main_menu(True), 'exit')


class TestMapMenu(unittest.TestCase):

    def test_output(self):
        with mock.patch('__builtin__.raw_input', return_value="any bullshit"):
            out = StringIO()
            sys.stdout = out                  # capture print output in out
            user_io.map_menu()     # fill out
            output = out.getvalue()   # save value of out in output
            expected = "\nWas moechtest du als naechstes tun?\n"
            expected += "1: Alle auf dem Geraet gespeicherten Geocaches auf Karte zeigen (INTERNET!!!)\n"
            expected += "2: https://www.geocaching.com/map aufrufen (INTERNET!!!)\n"
            expected += "3: https://www.google.de/maps aufrufen (INTERNET!!!)\n"
            self.assertEqual(output, expected)

    def test_1(self):
        with mock.patch('__builtin__.raw_input', return_value="1"):
            self.assertEqual(user_io.map_menu(), 'show_on_map')

    def test_2(self):
        with mock.patch('__builtin__.raw_input', return_value="2"):
            self.assertEqual(user_io.map_menu(), 'gc-maps')

    def test_3(self):
        with mock.patch('__builtin__.raw_input', return_value="3"):
            self.assertEqual(user_io.map_menu(), 'google-maps')

    def test_bullshit(self):
        with mock.patch('__builtin__.raw_input', return_value="blub"):
            self.assertIsNone(user_io.map_menu())


class TestSortCaches(unittest.TestCase):

    def test_gccode(self):
        with mock.patch('__builtin__.raw_input', side_effect=['1', '1']):  
            self.assertEqual(user_io.sort_caches(), ["gccode", False])
        
    def test_name(self):
        with mock.patch('__builtin__.raw_input', side_effect=['2', '1']): 
            self.assertEqual(user_io.sort_caches(), ["name", False])

    def test_type(self):
        with mock.patch('__builtin__.raw_input', side_effect=['3', '1']): 
            self.assertEqual(user_io.sort_caches(), ["type", False])
        
    def test_difficulty(self):
        with mock.patch('__builtin__.raw_input', side_effect=['4', '1']): 
            self.assertEqual(user_io.sort_caches(), ["difficulty", False])
        
    def test_terrain(self):
        with mock.patch('__builtin__.raw_input', side_effect=['5', '1']): 
            self.assertEqual(user_io.sort_caches(), ["terrain", False])
        
    def test_size(self):
        with mock.patch('__builtin__.raw_input', side_effect=['6', '1']): 
            self.assertEqual(user_io.sort_caches(), ["size", False])
        
    def test_downloaddate(self):
        with mock.patch('__builtin__.raw_input', side_effect=['7', '1']): 
            self.assertEqual(user_io.sort_caches(), ["downloaddate", False])
        
    def test_available(self):
        with mock.patch('__builtin__.raw_input', side_effect=['8', '1']): 
            self.assertEqual(user_io.sort_caches(), ["available", False])
        
    def test_distance(self):
        with mock.patch('__builtin__.raw_input', side_effect=['9', '1']): 
            self.assertEqual(user_io.sort_caches(), ["distance", False])
            
    def test_gccode_backwards(self):
        with mock.patch('__builtin__.raw_input', side_effect=['1', '2']):  
            self.assertEqual(user_io.sort_caches(), ["gccode", True])
        
    def test_name_backwards(self):
        with mock.patch('__builtin__.raw_input', side_effect=['2', '2']): 
            self.assertEqual(user_io.sort_caches(), ["name", True])

    def test_type_backwards(self):
        with mock.patch('__builtin__.raw_input', side_effect=['3', '2']): 
            self.assertEqual(user_io.sort_caches(), ["type", True])
        
    def test_difficulty_backwards(self):
        with mock.patch('__builtin__.raw_input', side_effect=['4', '2']): 
            self.assertEqual(user_io.sort_caches(), ["difficulty", True])
        
    def test_terrain_backwards(self):
        with mock.patch('__builtin__.raw_input', side_effect=['5', '2']): 
            self.assertEqual(user_io.sort_caches(), ["terrain", True])
        
    def test_size_backwards(self):
        with mock.patch('__builtin__.raw_input', side_effect=['6', '2']): 
            self.assertEqual(user_io.sort_caches(), ["size", True])
        
    def test_downloaddate_backwards(self):
        with mock.patch('__builtin__.raw_input', side_effect=['7', '2']): 
            self.assertEqual(user_io.sort_caches(), ["downloaddate", True])
        
    def test_available_backwards(self):
        with mock.patch('__builtin__.raw_input', side_effect=['8', '2']): 
            self.assertEqual(user_io.sort_caches(), ["available", True])
        
    def test_distance_backwards(self):
        with mock.patch('__builtin__.raw_input', side_effect=['9', '2']): 
            self.assertEqual(user_io.sort_caches(), ["distance", True])
            
    def test_criterion0(self):
        with mock.patch('__builtin__.raw_input', side_effect=['0', '2']): 
            self.assertEqual(user_io.sort_caches(), ["gccode", True])
            
    def test_criterion_invalid(self):
        with mock.patch('__builtin__.raw_input', side_effect=['bla', '1']): 
            self.assertEqual(user_io.sort_caches(), ["gccode", False])
            
    def test_revert_invalid(self):
        with mock.patch('__builtin__.raw_input', side_effect=['1', '0']): 
            self.assertEqual(user_io.sort_caches(), ["gccode", False])
            
    def test_output_normal(self):
        with mock.patch('__builtin__.raw_input', side_effect=['3', '2']):
            out = StringIO()
            sys.stdout = out                   
            user_io.sort_caches()
            output = out.getvalue()
            expected = "\nWonach sollen die Geocaches sortiert werden?\n"
            expected += "1: GC-Code\n"
            expected += "2: Name\n"
            expected += "3: Cache-Typ\n"
            expected += "4: D-Wertung\n"
            expected += "5: T-Wertung\n"
            expected += "6: Groesse\n"
            expected += "7: Download-Datum\n"
            expected += "8: Verfuegbarkeit\n"
            expected += "9: Abstand von einer bestimmten Position (Koordinaten erforderlich)\n"   
            expected += "In welche Richtung sollen die Caches sortiert werden?\n"
            expected += "1: aufsteigend\n"
            expected += "2: absteigend\n"
            self.assertEqual(output, expected)
            
    def test_output_criterion_invalid(self):
        with mock.patch('__builtin__.raw_input', side_effect=['0', '2']):
            out = StringIO()
            sys.stdout = out                   
            user_io.sort_caches()
            output = out.getvalue()
            expected = "\nWonach sollen die Geocaches sortiert werden?\n"
            expected += "1: GC-Code\n"
            expected += "2: Name\n"
            expected += "3: Cache-Typ\n"
            expected += "4: D-Wertung\n"
            expected += "5: T-Wertung\n"
            expected += "6: Groesse\n"
            expected += "7: Download-Datum\n"
            expected += "8: Verfuegbarkeit\n"
            expected += "9: Abstand von einer bestimmten Position (Koordinaten erforderlich)\n"   
            expected += "Ungueltige Eingabe: Sortierung erfolgt nach GC-Code\n" 
            expected += "In welche Richtung sollen die Caches sortiert werden?\n"
            expected += "1: aufsteigend\n"
            expected += "2: absteigend\n"
            self.assertEqual(output, expected)
 
                  
class TestSearch(unittest.TestCase):

    def test_name(self):
        with mock.patch('__builtin__.raw_input', return_value="1"):  
            self.assertEqual(user_io.search(), "name")
            
    def test_description(self):
        with mock.patch('__builtin__.raw_input', return_value="2"):  
            self.assertEqual(user_io.search(), "description")
            
    def test_type(self):
        with mock.patch('__builtin__.raw_input', return_value="3"):  
            self.assertEqual(user_io.search(), "type")
            
    def test_difficulty(self):
        with mock.patch('__builtin__.raw_input', return_value="4"):  
            self.assertEqual(user_io.search(), "difficulty")
            
    def test_terrain(self):
        with mock.patch('__builtin__.raw_input', return_value="5"):  
            self.assertEqual(user_io.search(), "terrain")
            
    def test_size(self):
        with mock.patch('__builtin__.raw_input', return_value="6"):  
            self.assertEqual(user_io.search(), "size")
            
    def test_downloaddate(self):
        with mock.patch('__builtin__.raw_input', return_value="7"):  
            self.assertEqual(user_io.search(), "downloaddate")
            
    def test_available(self):
        with mock.patch('__builtin__.raw_input', return_value="8"):  
            self.assertEqual(user_io.search(), "available")
            
    def test_attribute(self):
        with mock.patch('__builtin__.raw_input', return_value="9"):  
            self.assertEqual(user_io.search(), "attribute")
            
    def test_distance(self):
        with mock.patch('__builtin__.raw_input', return_value="10"):  
            self.assertEqual(user_io.search(), "distance")
            
    def test_0(self):
        with mock.patch('__builtin__.raw_input', return_value="0"): 
            self.assertEqual(user_io.search(), None)
            
    def test_invalid(self):
        with mock.patch('__builtin__.raw_input', return_value="bla"): 
            self.assertEqual(user_io.search(), None)
            
    def test_output_normal(self):
        with mock.patch('__builtin__.raw_input', return_value="2"):
            out = StringIO()
            sys.stdout = out                   
            user_io.search()
            output = out.getvalue()
            expected = "\nWonach willst du suchen?\n"
            expected += "1: Name\n"
            expected += "2: Beschreibung\n"
            expected += "3: Cache-Typ\n"
            expected += "4: D-Wertung\n"
            expected += "5: T-Wertung\n"
            expected += "6: Groesse\n"
            expected += "7: Download-Datum\n"
            expected += "8: Verfuegbarkeit\n"
            expected += "9: Attribut\n"
            expected += "10: Abstand von einer bestimmten Position (Koordinaten erforderlich)\n"
            self.assertEqual(output, expected)
            
    def test_output_invalid(self):
        with mock.patch('__builtin__.raw_input', return_value="bla"):
            out = StringIO()
            sys.stdout = out                   
            user_io.search()
            output = out.getvalue()
            expected = "\nWonach willst du suchen?\n"
            expected += "1: Name\n"
            expected += "2: Beschreibung\n"
            expected += "3: Cache-Typ\n"
            expected += "4: D-Wertung\n"
            expected += "5: T-Wertung\n"
            expected += "6: Groesse\n"
            expected += "7: Download-Datum\n"
            expected += "8: Verfuegbarkeit\n"
            expected += "9: Attribut\n"
            expected += "10: Abstand von einer bestimmten Position (Koordinaten erforderlich)\n"  
            expected += "Ungueltige Eingabe\n"
            self.assertEqual(output, expected)
      
            
class TestSearchType(unittest.TestCase):
    
    def test_return(self):
        with mock.patch('__builtin__.raw_input', return_value="Traditional Cache"): 
            self.assertEqual(user_io.search_type(), "Traditional Cache")
            
    def test_output(self):
        with mock.patch('__builtin__.raw_input', return_value="any_nonsense"):
            out = StringIO()
            sys.stdout = out                 
            user_io.search_type()
            output = out.getvalue()
            expected = "Gib den Cachetyp ein, nach dem du suchen willst.\n"
            expected += "Moegliche Typen: Traditional Cache, Multi-cache, Mystery Cache, EarthCache, "
            expected += "Letterbox Hybrid, Event Cache, Wherigo Cache, Geocaching HQ, Unknown Type\n"
            expected += "Achtung! Gross- und Kleinschreibung beachten!\n"
            self.assertEqual(output, expected)
            
            
class TestSearchAttribute(unittest.TestCase):
    
    def test_return(self):
        with mock.patch('__builtin__.raw_input', return_value="does not need to be an attr"): 
            self.assertEqual(user_io.search_attribute(["attr1", "attr2"]), "does not need to be an attr")
            
    def test_output(self):
        with mock.patch('__builtin__.raw_input', return_value="any_nonsense"):
            out = StringIO()
            sys.stdout = out                 
            user_io.search_attribute(["attr1", "attr2"])
            output = out.getvalue()
            expected = "Gib das Attribut ein, nach dem du suchen willst.\n"
            expected += "Moegliche Attribute: attr1, attr2\n"
            self.assertEqual(output, expected)
 
            
class TestActionsAfterSearch(unittest.TestCase):

    def test_1(self):
        with mock.patch('__builtin__.raw_input', return_value="1"):
            self.assertEqual(user_io.actions_after_search(), "show_again")
            
    def test_2(self):
        with mock.patch('__builtin__.raw_input', return_value="2"):
            self.assertEqual(user_io.actions_after_search(), "delete")
            
    def test_3(self):
        with mock.patch('__builtin__.raw_input', return_value="3"):
            self.assertEqual(user_io.actions_after_search(), "show_on_map")
            
    def test_4(self):
        with mock.patch('__builtin__.raw_input', return_value="4"):
            self.assertEqual(user_io.actions_after_search(), "show_one")
            
    def test_5(self):
        with mock.patch('__builtin__.raw_input', return_value="5"):
            self.assertEqual(user_io.actions_after_search(), "show_one_gc.com")

    def test_6(self):
        with mock.patch('__builtin__.raw_input', return_value="6"):
            self.assertEqual(user_io.actions_after_search(), "back")
            
    def test_other(self):
        with mock.patch('__builtin__.raw_input', return_value="0"):
            self.assertEqual(user_io.actions_after_search(), None)
            
    def test_output(self):
        with mock.patch('__builtin__.raw_input', return_value="1"):
            out = StringIO()
            sys.stdout = out                 
            user_io.actions_after_search()
            output = out.getvalue()
            expected = "\nWas moechtest du als naechstes tun?\n"
            expected += "1: Alle Suchergebnisse erneut anzeigen (bei evtl. Loeschen nicht aktualisiert)\n" 
            expected += "2: Alle Suchergebnisse loeschen\n"
            expected += "3: Alle Suchergebnisse auf Karte zeigen (INTERNET!!!)\n"
            expected += "4: Beschreibung fuer eines der Suchergebnisse anzeigen\n"
            expected += "5: Einen bestimmten Cache auf geocaching.com oeffnen (INTERNET!!!)\n"
            expected += "6: zurueck\n"
            self.assertEqual(output, expected)
            
    def test_output_invalid_input(self):
        with mock.patch('__builtin__.raw_input', return_value="bla"):
            out = StringIO()
            sys.stdout = out                 
            user_io.actions_after_search()
            output = out.getvalue()
            expected = "\nWas moechtest du als naechstes tun?\n"
            expected += "1: Alle Suchergebnisse erneut anzeigen (bei evtl. Loeschen nicht aktualisiert)\n" 
            expected += "2: Alle Suchergebnisse loeschen\n"
            expected += "3: Alle Suchergebnisse auf Karte zeigen (INTERNET!!!)\n"
            expected += "4: Beschreibung fuer eines der Suchergebnisse anzeigen\n"
            expected += "5: Einen bestimmten Cache auf geocaching.com oeffnen (INTERNET!!!)\n"
            expected += "6: zurueck\n"
            expected += "Ungueltige Eingabe\n"
            self.assertEqual(output, expected)
       
            
class TestActionsWithFounds(unittest.TestCase):

    def test_1(self):
        with mock.patch('__builtin__.raw_input', return_value="1"):
            self.assertEqual(user_io.actions_with_founds(), "log")
            
    def test_2(self):
        with mock.patch('__builtin__.raw_input', return_value="2"):
            self.assertEqual(user_io.actions_with_founds(), "delete")
            
    def test_3(self):
        with mock.patch('__builtin__.raw_input', return_value="3"):
            self.assertEqual(user_io.actions_with_founds(), "exit")
            
    def test_other(self):
        with mock.patch('__builtin__.raw_input', return_value="0"):
            self.assertEqual(user_io.actions_after_search(), None)
            
    def test_output(self):
        with mock.patch('__builtin__.raw_input', return_value="3"):
            out = StringIO()
            sys.stdout = out                 
            user_io.actions_with_founds()
            output = out.getvalue()
            expected = "\nWas moechtest du als naechstes tun?\n"
            expected += "1: Gefundene Caches auf geocaching.com loggen "
            expected += "(ueber den Upload von drafts / fieldnotes, INTERNET!!!)\n"
            expected += "2: Alle gefundenen Caches loeschen\n"
            expected += "3: zurueck\n"
            self.assertEqual(output, expected)
            
            
class TestConfirmDeletion(unittest.TestCase):

    def test_yes(self):
        with mock.patch('__builtin__.raw_input', return_value="y"):
            self.assertEqual(user_io.confirm_deletion(), True)
            
    def test_no(self):
        with mock.patch('__builtin__.raw_input', return_value="n"):
            self.assertEqual(user_io.confirm_deletion(), False)
            
    def test_nonsense(self):
        with mock.patch('__builtin__.raw_input', return_value="any_nonsense"):
            self.assertEqual(user_io.confirm_deletion(), False)


class TestWaypointMenu(unittest.TestCase):

    def test_output_no_waypoints(self):
        with mock.patch('__builtin__.raw_input', return_value="any bullshit"):
            out = StringIO()
            sys.stdout = out  # capture print output in out
            user_io.waypoint_menu(False)  # fill out
            output = out.getvalue()  # save value of out in output
            expected = "\nWas moechtest du als naechstes tun?\n"
            expected += "1: Wegpunkte hinzufuegen\n"
            expected += "2: nichts\n"
            self.assertEqual(output, expected)

    def test_output_waypoints(self):
        with mock.patch('__builtin__.raw_input', return_value="any bullshit"):
            out = StringIO()
            sys.stdout = out  # capture print output in out
            user_io.waypoint_menu(True)  # fill out
            output = out.getvalue()  # save value of out in output
            expected = "\nWas moechtest du als naechstes tun?\n"
            expected += "1: Wegpunkte hinzufuegen\n"
            expected += "2: Wegpunkte zu Geocaches zuordnen oder loeschen\n"
            expected += "3: nichts\n"
            self.assertEqual(output, expected)

    def test_no_waypoints_1(self):
        with mock.patch('__builtin__.raw_input', return_value="1"):
            self.assertEqual(user_io.waypoint_menu(False), 'add')

    def test_no_waypoints_2(self):
        with mock.patch('__builtin__.raw_input', return_value="2"):
            self.assertEqual(user_io.waypoint_menu(False), 'continue')

    def test_no_waypoints_shit(self):
        with mock.patch('__builtin__.raw_input', return_value="shit"):
            self.assertEqual(user_io.waypoint_menu(False), 'continue')

    def test_waypoints_1(self):
        with mock.patch('__builtin__.raw_input', return_value="1"):
            self.assertEqual(user_io.waypoint_menu(True), 'add')

    def test_waypoints_2(self):
        with mock.patch('__builtin__.raw_input', return_value="2"):
            self.assertEqual(user_io.waypoint_menu(True), 'assign')

    def test_no_waypoints_3(self):
        with mock.patch('__builtin__.raw_input', return_value="3"):
            self.assertEqual(user_io.waypoint_menu(True), 'continue')


class TestChooseCache(unittest.TestCase):

    def test_bullshit_suggestions_give_error(self):
        self.assertRaises(TypeError, user_io.choose_cache, "bla", False)

    def test_no_suggestions_no_more_options_output(self):
        with mock.patch('__builtin__.raw_input', return_value="any bullshit"):
            out = StringIO()
            sys.stdout = out  # capture print output in out
            user_io.choose_cache([], False)  # fill out
            output = out.getvalue()  # save value of out in output
            expected = "Keine Vorschlaege vorhanden. Was nun?\n"
            expected += "1: zu anderem Geocache zuordnen (GC-Code erforderlich)\n"
            expected += "2: Wegpunkt doch nicht zuordnen\n"
            self.assertEqual(output, expected)

    def test_no_suggestions_more_options_output(self):
        with mock.patch('__builtin__.raw_input', return_value="any bullshit"):
            out = StringIO()
            sys.stdout = out  # capture print output in out
            user_io.choose_cache([], True)  # fill out
            output = out.getvalue()  # save value of out in output
            expected = "Keine Vorschlaege vorhanden. Was nun?\n"
            expected += "1: zu anderem Geocache zuordnen (GC-Code erforderlich)\n"
            expected += "2: Wegpunkt loeschen\n"
            expected += "3: nichts tun\n"
            self.assertEqual(output, expected)

    def test_no_suggestions_no_more_options_1(self):
        with mock.patch('__builtin__.raw_input', return_value="1"):
            self.assertEqual(user_io.choose_cache([], False), 'other')

    def test_no_suggestions_no_more_options_2(self):
        with mock.patch('__builtin__.raw_input', return_value="2"):
            self.assertEqual(user_io.choose_cache([], False), 'continue')

    def test_no_suggestions_no_more_options_3(self):
        with mock.patch('__builtin__.raw_input', return_value="3"):
            self.assertEqual(user_io.choose_cache([], False), 'continue')

    def test_no_suggestions_more_options_1(self):
        with mock.patch('__builtin__.raw_input', return_value="1"):
            self.assertEqual(user_io.choose_cache([], True), 'other')

    def test_no_suggestions_more_options_2(self):
        with mock.patch('__builtin__.raw_input', return_value="2"):
            self.assertEqual(user_io.choose_cache([], True), 'delete')

    def test_no_suggestions_more_options_3(self):
        with mock.patch('__builtin__.raw_input', return_value="3"):
            self.assertEqual(user_io.choose_cache([], True), 'continue')

    def test_suggestions_no_more_options_output(self):
        gc1 = geocache.Geocache(r"../tests/examples/GC78K5W.gpx")
        gc2 = geocache.Geocache(r"../tests/examples/GC6K86W.gpx")
        gc3 = geocache.Geocache(r"../tests/examples/GC6RNTX.gpx")
        with mock.patch('__builtin__.raw_input', return_value="any bullshit"):
            out = StringIO()
            sys.stdout = out  # capture print output in out
            user_io.choose_cache([gc1, gc2, gc3], False)  # fill out
            output = out.getvalue()  # save value of out in output
            expected = u"Zu welchem der folgenden Caches moechtest du den Wegpunkt zuordnen?\n"
            expected += u"1: Cachertreffen Würzburg, die 54ste (GC78K5W)\n"
            expected += u"2: Saaletalblick (GC6K86W)\n"
            expected += u"3: Hochschule für Musik 1 (GC6RNTX)\n"
            expected += u"4: zu anderem Geocache zuordnen (GC-Code erforderlich)\n"
            expected += u"5: Wegpunkt doch nicht zuordnen\n"
            self.assertEqual(output, expected)

    def test_suggestions_more_options_output(self):
        gc1 = geocache.Geocache(r"../tests/examples/GC78K5W.gpx")
        gc2 = geocache.Geocache(r"../tests/examples/GC6K86W.gpx")
        gc3 = geocache.Geocache(r"../tests/examples/GC6RNTX.gpx")
        with mock.patch('__builtin__.raw_input', return_value="any bullshit"):
            out = StringIO()
            sys.stdout = out  # capture print output in out
            user_io.choose_cache([gc1, gc2, gc3], True)  # fill out
            output = out.getvalue()  # save value of out in output
            expected = u"Zu welchem der folgenden Caches moechtest du den Wegpunkt zuordnen?\n"
            expected += u"1: Cachertreffen Würzburg, die 54ste (GC78K5W)\n"
            expected += u"2: Saaletalblick (GC6K86W)\n"
            expected += u"3: Hochschule für Musik 1 (GC6RNTX)\n"
            expected += u"4: zu anderem Geocache zuordnen (GC-Code erforderlich)\n"
            expected += u"5: Wegpunkt loeschen\n"
            expected += u"6: nichts tun\n"
            self.assertEqual(output, expected)

    def test_suggestions_no_more_options_1(self):
        gc1 = geocache.Geocache(r"../tests/examples/GC78K5W.gpx")
        gc2 = geocache.Geocache(r"../tests/examples/GC6K86W.gpx")
        gc3 = geocache.Geocache(r"../tests/examples/GC6RNTX.gpx")
        with mock.patch('__builtin__.raw_input', return_value="1"):
            self.assertEqual(user_io.choose_cache([gc1, gc2, gc3], False), gc1)

    def test_suggestions_no_more_options_2(self):
        gc1 = geocache.Geocache(r"../tests/examples/GC78K5W.gpx")
        gc2 = geocache.Geocache(r"../tests/examples/GC6K86W.gpx")
        gc3 = geocache.Geocache(r"../tests/examples/GC6RNTX.gpx")
        with mock.patch('__builtin__.raw_input', return_value="2"):
            self.assertEqual(user_io.choose_cache([gc1, gc2, gc3], False), gc2)

    def test_suggestions_no_more_options_3(self):
        gc1 = geocache.Geocache(r"../tests/examples/GC78K5W.gpx")
        gc2 = geocache.Geocache(r"../tests/examples/GC6K86W.gpx")
        gc3 = geocache.Geocache(r"../tests/examples/GC6RNTX.gpx")
        with mock.patch('__builtin__.raw_input', return_value="3"):
            self.assertEqual(user_io.choose_cache([gc1, gc2, gc3], False), gc3)

    def test_suggestions_no_more_options_4(self):
        gc1 = geocache.Geocache(r"../tests/examples/GC78K5W.gpx")
        gc2 = geocache.Geocache(r"../tests/examples/GC6K86W.gpx")
        gc3 = geocache.Geocache(r"../tests/examples/GC6RNTX.gpx")
        with mock.patch('__builtin__.raw_input', return_value="4"):
            self.assertEqual(user_io.choose_cache([gc1, gc2, gc3], False), "other")

    def test_suggestions_no_more_options_5(self):
        gc1 = geocache.Geocache(r"../tests/examples/GC78K5W.gpx")
        gc2 = geocache.Geocache(r"../tests/examples/GC6K86W.gpx")
        gc3 = geocache.Geocache(r"../tests/examples/GC6RNTX.gpx")
        with mock.patch('__builtin__.raw_input', return_value="5"):
            self.assertEqual(user_io.choose_cache([gc1, gc2, gc3], False), "continue")

    def test_suggestions_no_more_options_6(self):
        gc1 = geocache.Geocache(r"../tests/examples/GC78K5W.gpx")
        gc2 = geocache.Geocache(r"../tests/examples/GC6K86W.gpx")
        gc3 = geocache.Geocache(r"../tests/examples/GC6RNTX.gpx")
        with mock.patch('__builtin__.raw_input', return_value="6"):
            self.assertEqual(user_io.choose_cache([gc1, gc2, gc3], False), "continue")

    def test_suggestions_more_options_1(self):
        gc1 = geocache.Geocache(r"../tests/examples/GC78K5W.gpx")
        gc2 = geocache.Geocache(r"../tests/examples/GC6K86W.gpx")
        gc3 = geocache.Geocache(r"../tests/examples/GC6RNTX.gpx")
        with mock.patch('__builtin__.raw_input', return_value="1"):
            self.assertEqual(user_io.choose_cache([gc1, gc2, gc3], True), gc1)

    def test_suggestions_more_options_2(self):
        gc1 = geocache.Geocache(r"../tests/examples/GC78K5W.gpx")
        gc2 = geocache.Geocache(r"../tests/examples/GC6K86W.gpx")
        gc3 = geocache.Geocache(r"../tests/examples/GC6RNTX.gpx")
        with mock.patch('__builtin__.raw_input', return_value="2"):
            self.assertEqual(user_io.choose_cache([gc1, gc2, gc3], True), gc2)

    def test_suggestions_more_options_3(self):
        gc1 = geocache.Geocache(r"../tests/examples/GC78K5W.gpx")
        gc2 = geocache.Geocache(r"../tests/examples/GC6K86W.gpx")
        gc3 = geocache.Geocache(r"../tests/examples/GC6RNTX.gpx")
        with mock.patch('__builtin__.raw_input', return_value="3"):
            self.assertEqual(user_io.choose_cache([gc1, gc2, gc3], True), gc3)

    def test_suggestions_more_options_4(self):
        gc1 = geocache.Geocache(r"../tests/examples/GC78K5W.gpx")
        gc2 = geocache.Geocache(r"../tests/examples/GC6K86W.gpx")
        gc3 = geocache.Geocache(r"../tests/examples/GC6RNTX.gpx")
        with mock.patch('__builtin__.raw_input', return_value="4"):
            self.assertEqual(user_io.choose_cache([gc1, gc2, gc3], True), "other")

    def test_suggestions_more_options_5(self):
        gc1 = geocache.Geocache(r"../tests/examples/GC78K5W.gpx")
        gc2 = geocache.Geocache(r"../tests/examples/GC6K86W.gpx")
        gc3 = geocache.Geocache(r"../tests/examples/GC6RNTX.gpx")
        with mock.patch('__builtin__.raw_input', return_value="5"):
            self.assertEqual(user_io.choose_cache([gc1, gc2, gc3], True), "delete")

    def test_suggestions_more_options_6(self):
        gc1 = geocache.Geocache(r"../tests/examples/GC78K5W.gpx")
        gc2 = geocache.Geocache(r"../tests/examples/GC6K86W.gpx")
        gc3 = geocache.Geocache(r"../tests/examples/GC6RNTX.gpx")
        with mock.patch('__builtin__.raw_input', return_value="6"):
            self.assertEqual(user_io.choose_cache([gc1, gc2, gc3], True), "continue")


class TestShowOne(unittest.TestCase):

    def test_1_no_waypoints(self):
        with mock.patch('__builtin__.raw_input', return_value="1"):
            self.assertEqual(user_io.show_one(False), "delete")
            
    def test_2_no_waypoints(self):
        with mock.patch('__builtin__.raw_input', return_value="2"):
            self.assertEqual(user_io.show_one(False), "gc.com")
            
    def test_3_no_waypoints(self):
        with mock.patch('__builtin__.raw_input', return_value="3"):
            self.assertEqual(user_io.show_one(False), "dist")
            
    def test_4_no_waypoints(self):
        with mock.patch('__builtin__.raw_input', return_value="4"):
            self.assertEqual(user_io.show_one(False), "gc-map")
            
    def test_5_no_waypoints(self):
        with mock.patch('__builtin__.raw_input', return_value="5"):
            self.assertEqual(user_io.show_one(False), "googlemaps")
            
    def test_6_no_waypoints(self):
        with mock.patch('__builtin__.raw_input', return_value="6"):
            self.assertEqual(user_io.show_one(False), None)
            
    def test_other_no_waypoints(self):
        with mock.patch('__builtin__.raw_input', return_value="0"):
            self.assertEqual(user_io.show_one(False), None)
            
    def test_output_no_waypoints(self):
        with mock.patch('__builtin__.raw_input', return_value="bla"):
            out = StringIO()
            sys.stdout = out                 
            user_io.show_one(False)
            output = out.getvalue()
            expected = "\nWas moechtest du als naechstes tun?\n"
            expected += "1: diesen Cache loeschen\n" 
            expected += "2: diesen Cache auf geocaching.com oeffnen (INTERNET!!!)\n"
            expected += "3: Abstand dieses Caches zu einer bestimmten Position berechnen\n"
            expected += "4: Position des Caches auf der Karte "
            expected += "https://www.geocaching.com/map anzeigen (INTERNET!!!)\n"
            expected += "5: Position des Caches auf der Karte https://www.google.de/maps anzeigen (INTERNET!!!)\n"
            expected += "6: zurueck\n"
            self.assertEqual(output, expected)

    def test_1_waypoints(self):
        with mock.patch('__builtin__.raw_input', return_value="1"):
            self.assertEqual(user_io.show_one(True), "delete")

    def test_2_waypoints(self):
        with mock.patch('__builtin__.raw_input', return_value="2"):
            self.assertEqual(user_io.show_one(True), "gc.com")

    def test_3_waypoints(self):
        with mock.patch('__builtin__.raw_input', return_value="3"):
            self.assertEqual(user_io.show_one(True), "dist")

    def test_4_waypoints(self):
        with mock.patch('__builtin__.raw_input', return_value="4"):
            self.assertEqual(user_io.show_one(True), "gc-map")

    def test_5_waypoints(self):
        with mock.patch('__builtin__.raw_input', return_value="5"):
            self.assertEqual(user_io.show_one(True), "googlemaps")

    def test_6_waypoints(self):
        with mock.patch('__builtin__.raw_input', return_value="6"):
            self.assertEqual(user_io.show_one(True), "mapcustomizer")

    def test_7_waypoints(self):
        with mock.patch('__builtin__.raw_input', return_value="7"):
            self.assertEqual(user_io.show_one(True), None)

    def test_other_waypoints(self):
        with mock.patch('__builtin__.raw_input', return_value="0"):
            self.assertEqual(user_io.show_one(True), None)

    def test_output_waypoints(self):
        with mock.patch('__builtin__.raw_input', return_value="bla"):
            out = StringIO()
            sys.stdout = out
            user_io.show_one(True)
            output = out.getvalue()
            expected = "\nWas moechtest du als naechstes tun?\n"
            expected += "1: diesen Cache loeschen\n"
            expected += "2: diesen Cache auf geocaching.com oeffnen (INTERNET!!!)\n"
            expected += "3: Abstand dieses Caches zu einer bestimmten Position berechnen\n"
            expected += "4: Position des Caches auf der Karte "
            expected += "https://www.geocaching.com/map anzeigen (INTERNET!!!)\n"
            expected += "5: Position des Caches auf der Karte https://www.google.de/maps anzeigen (INTERNET!!!)\n"
            expected += "6: diesen Cache mit allen Wegpunkten auf Karte zeigen (INTERNET!!!)\n"
            expected += "7: zurueck\n"
            self.assertEqual(output, expected)


class TestCoordinatesInput(unittest.TestCase):
    
    def test_return(self):
        with mock.patch('__builtin__.raw_input', return_value="X XX\xb0XX.XXX, X XXX\xb0XX.XXX"): 
            self.assertEqual(user_io.coordinates_input(), u"X XX°XX.XXX, X XXX°XX.XXX")
            
    def test_output(self):
        with mock.patch('__builtin__.raw_input', return_value="any_nonsense"):
            out = StringIO()
            sys.stdout = out                 
            user_io.coordinates_input()
            output = out.getvalue()
            expected = u"Gib die Koordinaten ein "
            expected += u"(Format: X XX°XX.XXX, X XXX°XX.XXX oder URL (google maps oder geocaching.com/map))\n"
            self.assertEqual(output, expected)     


class TestAskForPath(unittest.TestCase): 

    def test_output(self):
        with mock.patch('__builtin__.raw_input', return_value="any_nonsense"):
            out = StringIO()
            sys.stdout = out                 
            user_io.ask_for_path()
            output = out.getvalue()
            expected = "\nGib den Pfad zum GPS-Geraet ein (NICHT zum Unterordner 'GPX').\n"
            expected += "Falls Standardpfad uebernommen werden soll: keine Eingabe\n"
            self.assertEqual(output, expected) 

    def test_return(self):
        with mock.patch('__builtin__.raw_input', return_value="any_path"): 
            self.assertEqual(user_io.ask_for_path(), "any_path")

    def test_default_return(self):
        with mock.patch('__builtin__.raw_input', return_value=""): 
            self.assertEqual(user_io.ask_for_path(), "default")


class TestAskForWaypoints(unittest.TestCase):

    def test_yes(self):
        with mock.patch('__builtin__.raw_input', return_value="y"):
            self.assertEqual(user_io.ask_for_waypoints(), True)

    def test_no(self):
        with mock.patch('__builtin__.raw_input', return_value="n"):
            self.assertEqual(user_io.ask_for_waypoints(), False)

    def test_nonsense(self):
        with mock.patch('__builtin__.raw_input', return_value="any_nonsense"):
            self.assertEqual(user_io.ask_for_waypoints(), False)


class TestShowOnMapStart(unittest.TestCase):

    def test_output_no_waypoints(self):
        with mock.patch('__builtin__.raw_input', return_value="any_nonsense"):
            out = StringIO()
            sys.stdout = out
            user_io.show_on_map_start(False, False)
            output = out.getvalue()
            expected = "\nNach dem Klicken werden sich mehrere Fenster oeffnen. Eines davon ist der Editor, "
            expected += "das andere die Seite mapcustomizer.com in deinem Browser.\n"
            expected += "Um den Cache / die Caches auf der Karte anzuzeigen, " \
                        "kopiere den vollstaendigen Inhalt der Textdatei "
            expected += "aus deinem Editor in das Feld 'Bulk Entry' im Browser.\n"
            expected += "Die Caches werden in folgenden Farben angezeigt:\n"
            expected += "Gruen: Traditional Cache\n"
            expected += "Rot: Multi-cache\n"
            expected += "Blau: Mystery Cache\n"
            expected += "Braun: EarthCache\n"
            expected += "Grau: Letterbox, Geocaching HQ\n"
            expected += "Gelb: Event Cache, Wherigo Cache\n"
            expected += "Pink: unbekannter Typ\n"
            expected += "Gib nun den Pfad zu deinem Editor an: (bei Benutzung von Windows sollte das unnoetig sein)\n"
            self.assertEqual(output, expected)

    def test_output_all_waypoints(self):
        with mock.patch('__builtin__.raw_input', return_value="any_nonsense"):
            out = StringIO()
            sys.stdout = out
            user_io.show_on_map_start(False, True)
            output = out.getvalue()
            expected = "\nNach dem Klicken werden sich mehrere Fenster oeffnen. Eines davon ist der Editor, "
            expected += "das andere die Seite mapcustomizer.com in deinem Browser.\n"
            expected += "Um den Cache / die Caches auf der Karte anzuzeigen, kopiere den vollstaendigen Inhalt "
            expected += "der Textdatei aus deinem Editor in das Feld 'Bulk Entry' im Browser.\n"
            expected += "Die Caches werden in folgenden Farben angezeigt:\n"
            expected += "Gruen: Traditional Cache\n"
            expected += "Rot: Multi-cache\n"
            expected += "Blau: Mystery Cache\n"
            expected += "Braun: EarthCache\n"
            expected += "Grau: Letterbox, Geocaching HQ\n"
            expected += "Gelb: Event Cache, Wherigo Cache, Wegpunkte\n"
            expected += "Pink: unbekannter Typ\n"
            expected += "Gib nun den Pfad zu deinem Editor an: (bei Benutzung von Windows sollte das unnoetig sein)\n"
            self.assertEqual(output, expected)

    def test_output_one_waypoints(self):
        with mock.patch('__builtin__.raw_input', return_value="any_nonsense"):
            out = StringIO()
            sys.stdout = out
            user_io.show_on_map_start(True, True)
            output = out.getvalue()
            expected = "\nNach dem Klicken werden sich mehrere Fenster oeffnen. Eines davon ist der Editor, "
            expected += "das andere die Seite mapcustomizer.com in deinem Browser.\n"
            expected += "Um den Cache / die Caches auf der Karte anzuzeigen, kopiere den vollstaendigen Inhalt "
            expected += "der Textdatei aus deinem Editor in das Feld 'Bulk Entry' im Browser.\n"
            expected += "Gib nun den Pfad zu deinem Editor an: (bei Benutzung von Windows sollte das unnoetig sein)\n"
            self.assertEqual(output, expected)

    def test_output_one_no_waypoints(self):      # makes no difference because it is nonsense
        with mock.patch('__builtin__.raw_input', return_value="any_nonsense"):
            out = StringIO()
            sys.stdout = out
            user_io.show_on_map_start(True, False)
            output = out.getvalue()
            expected = "\nNach dem Klicken werden sich mehrere Fenster oeffnen. Eines davon ist der Editor, "
            expected += "das andere die Seite mapcustomizer.com in deinem Browser.\n"
            expected += "Um den Cache / die Caches auf der Karte anzuzeigen, kopiere den vollstaendigen Inhalt "
            expected += "der Textdatei aus deinem Editor in das Feld 'Bulk Entry' im Browser.\n"
            expected += "Gib nun den Pfad zu deinem Editor an: (bei Benutzung von Windows sollte das unnoetig sein)\n"
            self.assertEqual(output, expected)
            
    def test_return(self):
        with mock.patch('__builtin__.raw_input', return_value="any_editor"): 
            self.assertEqual(user_io.show_on_map_start(False, True), "any_editor")
            
    def test_default_return(self):
        with mock.patch('__builtin__.raw_input', return_value=""): 
            self.assertEqual(user_io.show_on_map_start(True, False), "notepad.exe")


class TestShowOnMapEnd(unittest.TestCase):

    def test_output(self):
        with mock.patch('__builtin__.raw_input', return_value="any_nonsense"):
            out = StringIO()
            sys.stdout = out
            user_io.show_on_map_end()
            output = out.getvalue()
            expected = "Schliesse den Editor und druecke Enter.\n"
            self.assertEqual(output, expected) 


def create_testsuite():
    """creates a testsuite with out of all tests in this file"""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGeneralOutput))
    suite.addTest(unittest.makeSuite(TestGeneralInput))
    suite.addTest(unittest.makeSuite(TestInputDecode))
    suite.addTest(unittest.makeSuite(TestShowMainMenu))
    suite.addTest(unittest.makeSuite(TestMainMenu))
    suite.addTest(unittest.makeSuite(TestMapMenu))
    suite.addTest(unittest.makeSuite(TestSortCaches))
    suite.addTest(unittest.makeSuite(TestSearch))
    suite.addTest(unittest.makeSuite(TestSearchType))
    suite.addTest(unittest.makeSuite(TestSearchAttribute))
    suite.addTest(unittest.makeSuite(TestActionsAfterSearch))
    suite.addTest(unittest.makeSuite(TestActionsWithFounds))
    suite.addTest(unittest.makeSuite(TestConfirmDeletion))
    suite.addTest(unittest.makeSuite(TestWaypointMenu))
    suite.addTest(unittest.makeSuite(TestChooseCache))
    suite.addTest(unittest.makeSuite(TestShowOne))
    suite.addTest(unittest.makeSuite(TestCoordinatesInput))
    suite.addTest(unittest.makeSuite(TestAskForPath))
    suite.addTest(unittest.makeSuite(TestAskForWaypoints))
    suite.addTest(unittest.makeSuite(TestShowOnMapStart))
    suite.addTest(unittest.makeSuite(TestShowOnMapEnd))
    return suite


def main(v):
    """runs the testsuite"""
    return test_frame.run(v, create_testsuite, "user_io.py")

if __name__ == '__main__':
    if len(sys.argv) > 1:  # if script is run with argument
        verbosity = int(sys.argv[1])
    else:  # if no argument -> verbosity 1
        verbosity = 1
    main(verbosity)
