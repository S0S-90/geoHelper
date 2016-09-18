PATH = r"F:\Garmin"    # Pfad zu dem Geraet
CODIERUNG = "cp1252"   # Codierung der Kosole (cp1252 empfohlen)

def general_output(string):
    """gibt einen String auf der Konsole aus"""
    print string
    
def general_input(string):
    """fragt mit Hilfe von string nach einer Benutzereingabe und gibt diese zurueck"""
    return raw_input(string)
 
def input_decode(string):
    """fragt mit Hilfe von string nach einer Benutzereingabe, dekodiert diese und gibt sie zurueck"""
    return raw_input(string).decode(CODIERUNG)
    
def hauptmenue(found_exists):
    """"gibt das Hauptmenue aus und je nach Benutzereingabe die Aufgabe zurueck, die als naechstes ausgefuehrt werden soll"""
    
    print "\nWas moechtest du als naechstes tun?"
    print "1: Alle auf dem Geraet gespeicherten Geocaches sortieren und anzeigen"
    print "2: Beschreibung fuer einen bestimmten Cache anzeigen (GC-Code erforderlich)"
    print "3: Geocaches durchsuchen"
    if found_exists:
        print "4: Alle gefundenen Caches anzeigen"
        print "5: Programm verlassen"
    else:
        print "4: Programm verlassen"
    eingabe = raw_input(">> ")
    
    if eingabe == "1":
        return "alle_anzeigen"
    elif eingabe == "2":
        return "einen_anzeigen"
    elif eingabe == "3":
        return "suchen"
    elif eingabe == "4" and found_exists:
        return "gefundene_anzeigen"
    elif eingabe == "4" and not found_exists:
        return "exit"
    elif eingabe == "5" and found_exists:
        return "exit"
    else:
        print "Ungueltige Eingabe!"  

def sortieren():
    """fragt nach dem Kriterium und der Reihenfolge fuer die Suche
    gibt eine Liste zurueck, in der das erste Element das Kriterium und 
    das zweite je nachdem, ob die Reihenfolge umgekehrt werden soll, True oder False ist"""
    
    kriterien = ["gccode", "name"]
    print "\nWonach sollen die Geocaches sortiert werden?"
    print "1: GC-Code"
    print "2: Name"
    eingabe_kriterium = raw_input(">> ")
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
    
    kriterien = ["name", "beschreibung"]
    print "\nWonach willst du suchen?"
    print "1: Name"
    print "2: Beschreibung"
    eingabe = raw_input(">> ")
    try:
        return kriterien[int(eingabe)-1]
    except IndexError:
        print "Ungueltige Eingabe"
    except ValueError:
        print "Ungueltige Eingabe"
        
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
    print "1: Alle gefundenen Caches loeschen"
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
    
    print "\nWas moechstest du als naechstes tun?"
    print "1: diesen Cache loeschen"
    print "2: zurueck"
    eingabe = raw_input(">> ")
    if eingabe == "1":
        return "loeschen"
     


        