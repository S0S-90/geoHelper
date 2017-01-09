import unittest
import mock
import datetime
import sys
sys.path.append('../src/') # path to source file (user_io.py)
from StringIO import StringIO

import user_io  

saved_stdout = sys.stdout # save standard output
    
class TestGeneralOutput(unittest.TestCase):

    def test_normaltext(self):
        out = StringIO()
        sys.stdout = out                  # capture print output in out
        user_io.general_output("hallo")   # fill out 
        output = out.getvalue().strip()   # save value of out in output
        self.assertEqual(output, "hallo")
        
    def test_textwithcapitalsandnumbers(self):
        out = StringIO()
        sys.stdout = out                  # capture print output in out
        user_io.general_output("hAllo2")  # fill out 
        output = out.getvalue().strip()   # save value of out in output
        self.assertEqual(output, "hAllo2")
        
    def test_umlaute(self):
        out = StringIO()
        sys.stdout = out                                       # capture print output in out
        user_io.general_output(u"m{}rchen".format(u"\u00E4"))  # fill out 
        output = out.getvalue().strip()                        # save value of out in output
        self.assertEqual(output, u"m{}rchen".format(u"\u00E4"))
        
    def test_replacable_signs(self):
        out = StringIO()
        sys.stdout = out                                        # capture print output in out
        user_io.general_output(u"hallo {}".format(u"\u263a"))   # fill out 
        output = out.getvalue().strip()                         # save value of out in output
        self.assertEqual(output, "hallo :-)")
        
    def test_unknown_signs(self):
        out = StringIO()
        sys.stdout = out                                                    # capture print output in out
        user_io.general_output(u"tuerkische Flagge: {}".format(u"\u262a"))  # fill out 
        output = out.getvalue().strip()                                     # save value of out in output
        self.assertEqual(output, u"tuerkische Flagge: {}".format(u"\u001a"))

class TestGeneralInput(unittest.TestCase):   

    def test_normaltext(self):
        with mock.patch('__builtin__.raw_input', return_value="hello"):
            self.assertEqual(user_io.general_input(">> "), 'hello')
        
    def test_textwithcapitalsandnumbers(self):
        with mock.patch('__builtin__.raw_input', return_value="hAllo2"):
            self.assertEqual(user_io.general_input(">> "), 'hAllo2')
        
    def test_replacable_signs(self):
        with mock.patch('__builtin__.raw_input', return_value=u"hallo {}".format(u"\u263a")): 
            self.assertEqual(user_io.general_input(">> "), u"hallo {}".format(u"\u263a"))
        
    def test_umlaute(self):
        with mock.patch('__builtin__.raw_input', return_value=u"m{}rchen".format(u"\u00E4")):
            self.assertEqual(user_io.general_input(">> "), u"m{}rchen".format(u"\u00E4"))
        
    def test_unknown_signs(self):
        with mock.patch('__builtin__.raw_input', return_value=u"tuerkische Flagge: {}".format(u"\u262a")):
            self.assertEqual(user_io.general_input(">> "), u"tuerkische Flagge: {}".format(u"\u262a"))
        
    def test_number(self):
        with mock.patch('__builtin__.raw_input', return_value="42"):
            self.assertEqual(user_io.general_input(">> "), "42")
        
class TestInputDecode(unittest.TestCase):   

    def test_normaltext(self):
        with mock.patch('__builtin__.raw_input', return_value="hello"):
            self.assertEqual(user_io.input_decode(">> "), 'hello')
        
    def test_textwithcapitalsandnumbers(self):
        with mock.patch('__builtin__.raw_input', return_value="hAllo2"):
            self.assertEqual(user_io.input_decode(">> "), 'hAllo2')
        
    def test_replacable_signs(self):
        with mock.patch('__builtin__.raw_input', return_value=u"hallo {}".format(u"\u263a")):
            self.assertRaises(UnicodeEncodeError, user_io.input_decode, ">> ")
        
    def test_umlaute(self):
        with mock.patch('__builtin__.raw_input', return_value='M\xe4rchen'):
            self.assertEqual(user_io.input_decode(">> "), u"Märchen")
        
    def test_unknown_signs(self):
        with mock.patch('__builtin__.raw_input', return_value=u"tuerkische Flagge: {}".format(u"\u262a")):
            self.assertRaises(UnicodeEncodeError, user_io.input_decode, ">> ")
        
    def test_number(self):
        with mock.patch('__builtin__.raw_input', return_value="42"):
            self.assertEqual(user_io.input_decode(">> "), "42")
        
class TestHauptmenueAnzeigen(unittest.TestCase):
    
    def test_nofoundexists(self):
        out = StringIO()
        sys.stdout = out                  # capture print output in out
        user_io.hauptmenue_anzeigen(False)   # fill out 
        output = out.getvalue().strip()   # save value of out in output
        expected_output = "Was moechtest du als naechstes tun?\n"
        expected_output = expected_output + "1: Geocaches aktualisieren\n"
        expected_output = expected_output + "2: Alle auf dem Geraet gespeicherten Geocaches sortieren und anzeigen\n"
        expected_output = expected_output + "3: Beschreibung fuer einen bestimmten Cache anzeigen (GC-Code erforderlich)\n"
        expected_output = expected_output + "4: Geocaches durchsuchen\n" 
        expected_output = expected_output + "5: https://www.geocaching.com/map aufrufen\n"
        expected_output = expected_output + "6: https://www.google.de/maps aufrufen\n"
        expected_output = expected_output + "7: Programm verlassen"
        self.assertEqual(output, expected_output)
        
    def test_foundexists(self):
        out = StringIO()
        sys.stdout = out                  # capture print output in out
        user_io.hauptmenue_anzeigen(True)   # fill out 
        output = out.getvalue().strip()   # save value of out in output
        expected_output = "Was moechtest du als naechstes tun?\n"
        expected_output = expected_output + "1: Geocaches aktualisieren\n"
        expected_output = expected_output + "2: Alle auf dem Geraet gespeicherten Geocaches sortieren und anzeigen\n"
        expected_output = expected_output + "3: Beschreibung fuer einen bestimmten Cache anzeigen (GC-Code erforderlich)\n"
        expected_output = expected_output + "4: Geocaches durchsuchen\n" 
        expected_output = expected_output + "5: Alle gefundenen Caches anzeigen\n"
        expected_output = expected_output + "6: https://www.geocaching.com/map aufrufen\n"
        expected_output = expected_output + "7: https://www.google.de/maps aufrufen\n"
        expected_output = expected_output + "8: Programm verlassen"
        self.assertEqual(output, expected_output)
        
class TestHauptmenue(unittest.TestCase):

    def test_1_nofoundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="1"):
            self.assertEqual(user_io.hauptmenue(False), 'aktualisieren')
        
    def test_2_nofoundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="2"):
            self.assertEqual(user_io.hauptmenue(False), 'alle_anzeigen')
        
    def test_3_nofoundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="3"):
            self.assertEqual(user_io.hauptmenue(False), 'einen_anzeigen')
        
    def test_4_nofoundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="4"):
            self.assertEqual(user_io.hauptmenue(False), 'suchen')
        
    def test_5_nofoundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="5"):
            self.assertEqual(user_io.hauptmenue(False), 'gc-maps')
        
    def test_6_nofoundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="6"):
            self.assertEqual(user_io.hauptmenue(False), 'google-maps')
        
    def test_7_nofoundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="7"):
            self.assertEqual(user_io.hauptmenue(False), 'exit')
        
    def test_8_nofoundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="8"):
            self.assertEqual(user_io.hauptmenue(False), None)
        
    def test_1_foundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="1"):
            self.assertEqual(user_io.hauptmenue(True), 'aktualisieren')
        
    def test_2_foundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="2"):
            self.assertEqual(user_io.hauptmenue(True), 'alle_anzeigen')
        
    def test_3_foundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="3"):
            self.assertEqual(user_io.hauptmenue(True), 'einen_anzeigen')
        
    def test_4_foundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="4"):
            self.assertEqual(user_io.hauptmenue(True), 'suchen')
        
    def test_5_foundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="5"):
            self.assertEqual(user_io.hauptmenue(True), 'gefundene_anzeigen')
        
    def test_6_foundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="6"):
            self.assertEqual(user_io.hauptmenue(True), 'gc-maps')
        
    def test_7_foundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="7"):
            self.assertEqual(user_io.hauptmenue(True), 'google-maps')
        
    def test_8_foundexists(self):
        with mock.patch('__builtin__.raw_input', return_value="8"):
            self.assertEqual(user_io.hauptmenue(True), 'exit')
        
class TestSortieren(unittest.TestCase):

    def test_gccode(self):
        with mock.patch('__builtin__.raw_input', side_effect=['1', '1']):  
            self.assertEqual(user_io.sortieren(), ["gccode", False])
        
    def test_name(self):
        with mock.patch('__builtin__.raw_input', side_effect=['2', '1']): 
            self.assertEqual(user_io.sortieren(), ["name", False])

    def test_type(self):
        with mock.patch('__builtin__.raw_input', side_effect=['3', '1']): 
            self.assertEqual(user_io.sortieren(), ["type", False])
        
    def test_difficulty(self):
        with mock.patch('__builtin__.raw_input', side_effect=['4', '1']): 
            self.assertEqual(user_io.sortieren(), ["difficulty", False])
        
    def test_terrain(self):
        with mock.patch('__builtin__.raw_input', side_effect=['5', '1']): 
            self.assertEqual(user_io.sortieren(), ["terrain", False])
        
    def test_size(self):
        with mock.patch('__builtin__.raw_input', side_effect=['6', '1']): 
            self.assertEqual(user_io.sortieren(), ["size", False])
        
    def test_downloaddate(self):
        with mock.patch('__builtin__.raw_input', side_effect=['7', '1']): 
            self.assertEqual(user_io.sortieren(), ["downloaddate", False])
        
    def test_available(self):
        with mock.patch('__builtin__.raw_input', side_effect=['8', '1']): 
            self.assertEqual(user_io.sortieren(), ["available", False])
        
    def test_distance(self):
        with mock.patch('__builtin__.raw_input', side_effect=['9', '1']): 
            self.assertEqual(user_io.sortieren(), ["distance", False])
            
    def test_gccode_revert(self):
        with mock.patch('__builtin__.raw_input', side_effect=['1', '2']):  
            self.assertEqual(user_io.sortieren(), ["gccode", True])
        
    def test_name_revert(self):
        with mock.patch('__builtin__.raw_input', side_effect=['2', '2']): 
            self.assertEqual(user_io.sortieren(), ["name", True])

    def test_type_revert(self):
        with mock.patch('__builtin__.raw_input', side_effect=['3', '2']): 
            self.assertEqual(user_io.sortieren(), ["type", True])
        
    def test_difficulty_revert(self):
        with mock.patch('__builtin__.raw_input', side_effect=['4', '2']): 
            self.assertEqual(user_io.sortieren(), ["difficulty", True])
        
    def test_terrain_revert(self):
        with mock.patch('__builtin__.raw_input', side_effect=['5', '2']): 
            self.assertEqual(user_io.sortieren(), ["terrain", True])
        
    def test_size_revert(self):
        with mock.patch('__builtin__.raw_input', side_effect=['6', '2']): 
            self.assertEqual(user_io.sortieren(), ["size", True])
        
    def test_downloaddate_revert(self):
        with mock.patch('__builtin__.raw_input', side_effect=['7', '2']): 
            self.assertEqual(user_io.sortieren(), ["downloaddate", True])
        
    def test_available_revert(self):
        with mock.patch('__builtin__.raw_input', side_effect=['8', '2']): 
            self.assertEqual(user_io.sortieren(), ["available", True])
        
    def test_distance_revert(self):
        with mock.patch('__builtin__.raw_input', side_effect=['9', '2']): 
            self.assertEqual(user_io.sortieren(), ["distance", True])
            
    def test_criterion0(self):
        with mock.patch('__builtin__.raw_input', side_effect=['0', '2']): 
            self.assertEqual(user_io.sortieren(), ["gccode", True])
            
    def test_criterion_invalid(self):
        with mock.patch('__builtin__.raw_input', side_effect=['bla', '1']): 
            self.assertEqual(user_io.sortieren(), ["gccode", False])
            
    def test_revert_invalid(self):
        with mock.patch('__builtin__.raw_input', side_effect=['1', '0']): 
            self.assertEqual(user_io.sortieren(), ["gccode", False])
            
    def test_output_normal(self):
        with mock.patch('__builtin__.raw_input', side_effect=['3', '2']):
            out = StringIO()
            sys.stdout = out                   
            user_io.sortieren()    
            output = out.getvalue().strip() 
            expected_output = "Wonach sollen die Geocaches sortiert werden?\n"
            expected_output = expected_output + "1: GC-Code\n"
            expected_output = expected_output + "2: Name\n"
            expected_output = expected_output + "3: Cache-Typ\n"
            expected_output = expected_output + "4: D-Wertung\n"
            expected_output = expected_output + "5: T-Wertung\n"
            expected_output = expected_output + "6: Groesse\n"
            expected_output = expected_output + "7: Download-Datum\n"
            expected_output = expected_output + "8: Verfuegbarkeit\n"
            expected_output = expected_output + "9: Abstand von einer bestimmten Position (Koordinaten erforderlich)\n"   
            expected_output = expected_output + "In welche Richtung sollen die Caches sortiert werden?\n"
            expected_output = expected_output + "1: aufsteigend\n"
            expected_output = expected_output + "2: absteigend"            
            self.assertEqual(output, expected_output)
            
    def test_output_criterion_invalid(self):
        with mock.patch('__builtin__.raw_input', side_effect=['0', '2']):
            out = StringIO()
            sys.stdout = out                   
            user_io.sortieren()    
            output = out.getvalue().strip() 
            expected_output = "Wonach sollen die Geocaches sortiert werden?\n"
            expected_output = expected_output + "1: GC-Code\n"
            expected_output = expected_output + "2: Name\n"
            expected_output = expected_output + "3: Cache-Typ\n"
            expected_output = expected_output + "4: D-Wertung\n"
            expected_output = expected_output + "5: T-Wertung\n"
            expected_output = expected_output + "6: Groesse\n"
            expected_output = expected_output + "7: Download-Datum\n"
            expected_output = expected_output + "8: Verfuegbarkeit\n"
            expected_output = expected_output + "9: Abstand von einer bestimmten Position (Koordinaten erforderlich)\n"   
            expected_output = expected_output + "Ungueltige Eingabe: Sortierung erfolgt nach GC-Code\n" 
            expected_output = expected_output + "In welche Richtung sollen die Caches sortiert werden?\n"
            expected_output = expected_output + "1: aufsteigend\n"
            expected_output = expected_output + "2: absteigend"             
            self.assertEqual(output, expected_output)
                  
class TestSuchen(unittest.TestCase):

    def test_name(self):
        with mock.patch('__builtin__.raw_input', return_value= "1"):  
            self.assertEqual(user_io.suchen(), "name")
            
    def test_beschreibung(self):
        with mock.patch('__builtin__.raw_input', return_value= "2"):  
            self.assertEqual(user_io.suchen(), "beschreibung")
            
    def test_type(self):
        with mock.patch('__builtin__.raw_input', return_value= "3"):  
            self.assertEqual(user_io.suchen(), "type")
            
    def test_difficulty(self):
        with mock.patch('__builtin__.raw_input', return_value= "4"):  
            self.assertEqual(user_io.suchen(), "difficulty")
            
    def test_terrain(self):
        with mock.patch('__builtin__.raw_input', return_value= "5"):  
            self.assertEqual(user_io.suchen(), "terrain")
            
    def test_size(self):
        with mock.patch('__builtin__.raw_input', return_value= "6"):  
            self.assertEqual(user_io.suchen(), "size")
            
    def test_downloaddate(self):
        with mock.patch('__builtin__.raw_input', return_value= "7"):  
            self.assertEqual(user_io.suchen(), "downloaddate")
            
    def test_available(self):
        with mock.patch('__builtin__.raw_input', return_value= "8"):  
            self.assertEqual(user_io.suchen(), "available")
            
    def test_attribute(self):
        with mock.patch('__builtin__.raw_input', return_value= "9"):  
            self.assertEqual(user_io.suchen(), "attribute")
            
    def test_distance(self):
        with mock.patch('__builtin__.raw_input', return_value= "10"):  
            self.assertEqual(user_io.suchen(), "distance")
            
    def test_0(self):
        with mock.patch('__builtin__.raw_input', return_value= "0"): 
            self.assertEqual(user_io.suchen(), None)
            
    def test_invalid(self):
        with mock.patch('__builtin__.raw_input', return_value= "bla"): 
            self.assertEqual(user_io.suchen(), None)
            
    def test_output_normal(self):
        with mock.patch('__builtin__.raw_input', return_value="2"):
            out = StringIO()
            sys.stdout = out                   
            user_io.suchen()    
            output = out.getvalue().strip() 
            expected_output = "Wonach willst du suchen?\n"
            expected_output = expected_output + "1: Name\n"
            expected_output = expected_output + "2: Beschreibung\n"
            expected_output = expected_output + "3: Cache-Typ\n"
            expected_output = expected_output + "4: D-Wertung\n"
            expected_output = expected_output + "5: T-Wertung\n"
            expected_output = expected_output + "6: Groesse\n"
            expected_output = expected_output + "7: Download-Datum\n"
            expected_output = expected_output + "8: Verfuegbarkeit\n"
            expected_output = expected_output + "9: Attribut\n"
            expected_output = expected_output + "10: Abstand von einer bestimmten Position (Koordinaten erforderlich)"                       
            self.assertEqual(output, expected_output)
            
    def test_output_invalid(self):
        with mock.patch('__builtin__.raw_input', return_value="bla"):
            out = StringIO()
            sys.stdout = out                   
            user_io.suchen()    
            output = out.getvalue().strip() 
            expected_output = "Wonach willst du suchen?\n"
            expected_output = expected_output + "1: Name\n"
            expected_output = expected_output + "2: Beschreibung\n"
            expected_output = expected_output + "3: Cache-Typ\n"
            expected_output = expected_output + "4: D-Wertung\n"
            expected_output = expected_output + "5: T-Wertung\n"
            expected_output = expected_output + "6: Groesse\n"
            expected_output = expected_output + "7: Download-Datum\n"
            expected_output = expected_output + "8: Verfuegbarkeit\n"
            expected_output = expected_output + "9: Attribut\n"
            expected_output = expected_output + "10: Abstand von einer bestimmten Position (Koordinaten erforderlich)\n"  
            expected_output = expected_output + "Ungueltige Eingabe"            
            self.assertEqual(output, expected_output)
            
class TestSearchType(unittest.TestCase):
    
    def test_return(self):
        with mock.patch('__builtin__.raw_input', return_value= "Traditional Cache"): 
            self.assertEqual(user_io.search_type(), "Traditional Cache")
            
    def test_output(self):
        with mock.patch('__builtin__.raw_input', return_value= "any_nonsense"):
            out = StringIO()
            sys.stdout = out                 
            user_io.search_type()  
            output = out.getvalue().strip()  
            expected_output = "Gib den Cachetyp ein, nach dem du suchen willst.\n"
            expected_output = expected_output + "Moegliche Typen: Traditional Cache, Multi-cache, Mystery Cache, EarthCache, Letterbox Hybrid, Event Cache, Wherigo Cache, Geocaching HQ, Unknown Type\n"
            expected_output = expected_output + "Achtung! Gross- und Kleinschreibung beachten!"
            self.assertEqual(output, expected_output)
            
class TestSearchAttribute(unittest.TestCase):
    
    def test_return(self):
        with mock.patch('__builtin__.raw_input', return_value= "does not need to be an attr"): 
            self.assertEqual(user_io.search_attribute(["attr1", "attr2"]), "does not need to be an attr")
            
    def test_output(self):
        with mock.patch('__builtin__.raw_input', return_value= "any_nonsense"):
            out = StringIO()
            sys.stdout = out                 
            user_io.search_attribute(["attr1", "attr2"])  
            output = out.getvalue().strip()  
            expected_output = "Gib das Attribut ein, nach dem du suchen willst.\n"
            expected_output = expected_output + "Moegliche Attribute: attr1, attr2" 
            self.assertEqual(output, expected_output)
            
class TestAktionenAuswahlSuchen(unittest.TestCase):

    def test_1(self):
        with mock.patch('__builtin__.raw_input', return_value= "1"):
            self.assertEqual(user_io.aktionen_auswahl_suchen(), "neu_anzeigen")
            
    def test_2(self):
        with mock.patch('__builtin__.raw_input', return_value= "2"):
            self.assertEqual(user_io.aktionen_auswahl_suchen(), "loeschen")
            
    def test_3(self):
        with mock.patch('__builtin__.raw_input', return_value= "3"):
            self.assertEqual(user_io.aktionen_auswahl_suchen(), "einen_anzeigen")
            
    def test_4(self):
        with mock.patch('__builtin__.raw_input', return_value= "4"):
            self.assertEqual(user_io.aktionen_auswahl_suchen(), "back")
            
    def test_other(self):
        with mock.patch('__builtin__.raw_input', return_value= "0"):
            self.assertEqual(user_io.aktionen_auswahl_suchen(), None)
            
    def test_output(self):
        with mock.patch('__builtin__.raw_input', return_value= "1"):
            out = StringIO()
            sys.stdout = out                 
            user_io.aktionen_auswahl_suchen()
            output = out.getvalue().strip()  
            expected_output = "Was moechtest du als naechstes tun?\n"
            expected_output = expected_output + "1: Alle Suchergebnisse erneut anzeigen (bei evtl. Loeschen nicht aktualisiert)\n" 
            expected_output = expected_output + "2: Alle Suchergebnisse loeschen\n"
            expected_output = expected_output + "3: Beschreibung fuer eines der Suchergebnisse anzeigen\n"
            expected_output = expected_output + "4: zurueck"
            self.assertEqual(output, expected_output)
            
    def test_output_invalid_input(self):
        with mock.patch('__builtin__.raw_input', return_value= "bla"):
            out = StringIO()
            sys.stdout = out                 
            user_io.aktionen_auswahl_suchen()
            output = out.getvalue().strip()  
            expected_output = "Was moechtest du als naechstes tun?\n"
            expected_output = expected_output + "1: Alle Suchergebnisse erneut anzeigen (bei evtl. Loeschen nicht aktualisiert)\n" 
            expected_output = expected_output + "2: Alle Suchergebnisse loeschen\n"
            expected_output = expected_output + "3: Beschreibung fuer eines der Suchergebnisse anzeigen\n"
            expected_output = expected_output + "4: zurueck\n"
            expected_output = expected_output + "Ungueltige Eingabe"
            self.assertEqual(output, expected_output)
            
class TestLoeschbestaetigung(unittest.TestCase):

    def test_yes(self):
        with mock.patch('__builtin__.raw_input', return_value= "y"):
            self.assertEqual(user_io.loeschbestaetigung(), True)
            
    def test_no(self):
        with mock.patch('__builtin__.raw_input', return_value= "n"):
            self.assertEqual(user_io.loeschbestaetigung(), False)
            
    def test_nonsense(self):
        with mock.patch('__builtin__.raw_input', return_value= "any_nonsense"):
            self.assertEqual(user_io.loeschbestaetigung(), False)
            
class TestEinenAnzeigen(unittest.TestCase):

    def test_1(self):
        with mock.patch('__builtin__.raw_input', return_value= "1"):
            self.assertEqual(user_io.einen_anzeigen(), "loeschen")
            
    def test_2(self):
        with mock.patch('__builtin__.raw_input', return_value= "2"):
            self.assertEqual(user_io.einen_anzeigen(), "gc.com")
            
    def test_3(self):
        with mock.patch('__builtin__.raw_input', return_value= "3"):
            self.assertEqual(user_io.einen_anzeigen(), "dist")
            
    def test_4(self):
        with mock.patch('__builtin__.raw_input', return_value= "4"):
            self.assertEqual(user_io.einen_anzeigen(), "gc-map")
            
    def test_5(self):
        with mock.patch('__builtin__.raw_input', return_value= "5"):
            self.assertEqual(user_io.einen_anzeigen(), "googlemaps")
            
    def test_6(self):
        with mock.patch('__builtin__.raw_input', return_value= "6"):
            self.assertEqual(user_io.einen_anzeigen(), None)
            
    def test_other(self):
        with mock.patch('__builtin__.raw_input', return_value= "0"):
            self.assertEqual(user_io.einen_anzeigen(), None)
            
    def test_output(self):
        with mock.patch('__builtin__.raw_input', return_value= "bla"):
            out = StringIO()
            sys.stdout = out                 
            user_io.einen_anzeigen()
            output = out.getvalue().strip()  
            expected_output = "Was moechtest du als naechstes tun?\n"
            expected_output = expected_output + "1: diesen Cache loeschen\n" 
            expected_output = expected_output + "2: diesen Cache auf geocaching.com oeffnen\n"
            expected_output = expected_output + "3: Abstand dieses Caches zu einer bestimmten Position berechnen\n"
            expected_output = expected_output + "4: Position des Caches auf der Karte https://www.geocaching.com/map anzeigen\n"
            expected_output = expected_output + "5: Position des Caches auf der Karte https://www.google.de/maps anzeigen\n"
            expected_output = expected_output + "6: zurueck"
            self.assertEqual(output, expected_output)

class TestKoordinatenEingabe(unittest.TestCase):
    
    def test_return(self):
        with mock.patch('__builtin__.raw_input', return_value= "X XX°XX.XXX, X XXX°XX.XXX"): 
            self.assertEqual(user_io.koordinaten_eingabe(), "X XX°XX.XXX, X XXX°XX.XXX")
            
    def test_output(self):
        with mock.patch('__builtin__.raw_input', return_value= "any_nonsense"):
            out = StringIO()
            sys.stdout = out                 
            user_io.koordinaten_eingabe()  
            output = out.getvalue().strip()  
            expected_output = u"Gib die Koordinaten ein (Format: X XX°XX.XXX, X XXX°XX.XXX oder URL (google maps oder geocaching.com/map)"
            self.assertEqual(output, expected_output)     

# weiter mit openfieldnotes            
        
def create_testsuite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGeneralOutput))
    suite.addTest(unittest.makeSuite(TestGeneralInput))
    suite.addTest(unittest.makeSuite(TestInputDecode))
    suite.addTest(unittest.makeSuite(TestHauptmenueAnzeigen))
    suite.addTest(unittest.makeSuite(TestHauptmenue))
    suite.addTest(unittest.makeSuite(TestSortieren))
    suite.addTest(unittest.makeSuite(TestSuchen))
    suite.addTest(unittest.makeSuite(TestSearchType))
    suite.addTest(unittest.makeSuite(TestSearchAttribute))
    suite.addTest(unittest.makeSuite(TestAktionenAuswahlSuchen))
    suite.addTest(unittest.makeSuite(TestLoeschbestaetigung))
    suite.addTest(unittest.makeSuite(TestEinenAnzeigen))
    suite.addTest(unittest.makeSuite(TestKoordinatenEingabe))
    return suite

def main(v):
    sys.stdout = saved_stdout  # print output to display
    print "\nTesting user_io.py"
    testsuite = create_testsuite()
    unittest.TextTestRunner(verbosity=v).run(testsuite)  

if __name__ == '__main__':
    main(2)
