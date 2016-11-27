import math
import datetime
import urllib
from HTMLParser import HTMLParser
import unicodedata


class MyHTMLParser(HTMLParser):
    """Parser, um alle Daten, die in einer Tabelle (Tags <td> bzw. </td>) stehen, auszulesen
    
    Attribute:
    -----------
    read: bool
        legt fest, ob gerade Daten gelesen werden
        
    data: list
        Speicherort fuer Daten, die gelesen werden
        
    
    Methoden:
    ---------    
    define_attributes(): definiert die Attribute read und data

    return data(): gibt Liste data zurueck   
    """

    def define_attributes(self):
        self.read = False
        self.data = []
    
    def handle_starttag(self, tag, attrs):
        if tag == "td":
            self.read = True

    def handle_endtag(self, tag):
        if tag == "td":
            self.read = False

    def handle_data(self, data):
        if self.read == True:
            self.data.append(data)
            
    def return_data(self):
        return self.data
        
        
def find_cp1252():
    """parst Webseite ueber Codepage 1252 und gibt Liste mit den Unicode-Descriptions zurueck"""
    
    x = urllib.urlopen("http://www.cp1252.com/").read() # Webseite auslesen
    
    parser = MyHTMLParser()        # Webseite parsen 
    parser.define_attributes()
    parser.feed(x)  
    cpdata = parser.return_data()  # Inhalt der Tabelle in cpdata
    
    cp1252 = []                    # Unicode-Descriptions fuer Codepage 1252
    for i, d in enumerate(cpdata):
        if i%3 == 1 and i > 6:
            cp1252.append(d)      
    return cp1252
    
ALLOWED_SIGNS = find_cp1252()  # erlaubte Zeichen einmal festlegen

def zeichen_ersetzen(string, allowed_signs):
    """"ersetzt Zeichen, die Probleme bei der Darstellung machen (nicht in allowed_signs vorhanden)"""  

    newstring = ""
    for i,c in enumerate(string):   
        if c == "\n" or c == "\t" or c == "\v":    # Newline, Tab (horizontal oder vertikal)
            newstring = newstring + c   
        elif unicodedata.name(unicode(c)) in allowed_signs: # erlaubte Zeichen
            newstring = newstring + c
        elif unicode(c) == u"\u263a":     # Smiley
            newstring = newstring + ":-)"
        elif unicode(c) == u"\u2211":     # Summenzeichen
            newstring = newstring + "sum"
        elif unicode(c) == u"\u221a":     # Wurzel
            newstring = newstring + "sqrt"
        else:                               # unbekanntes Zeichen
            newstring = newstring + u"\u001a"
    return newstring
    
def koordinaten_dezimalgrad_to_minuten(koordinatenliste):
    """"rechnet Koordinaten in Dezimalgrad (z.B. in gpx-Datei) in Grad und Minuten um (z.B. auf geocaching.com)"""
    if type(koordinatenliste) != list or len(koordinatenliste) != 2:
        raise TypeError("Bad input.")
    nord = koordinatenliste[0]
    ost = koordinatenliste[1]
    if (type(nord) != float or type(ost) != float) and (type(nord) != int or type(ost) != int) and (type(nord) != float or type(ost) != int) and (type(nord) != int or type(ost) != float):
        raise TypeError("One of the coordinates is not a number.")    
    if nord > 90 or ost > 180 or nord < -90 or ost < -180:
        raise ValueError("These coordinates do not exist on earth.")
    nordgrad = int(nord)
    ostgrad = int(ost)
    nordminuten = round(60*(nord - nordgrad), 3)
    ostminuten = round(60*(ost - ostgrad), 3)
    if nordgrad >= 0:
        nordsign = "N"
    else:
        nordsign = "S"
        nordgrad = -nordgrad
        nordminuten = -nordminuten
    if ostgrad >= 0:
        ostsign = "E"
    else:
        ostsign = "W"
        ostgrad = -ostgrad
        ostminuten = -ostminuten
    return u"{} {:02}°{:06.3f}, {} {:03}°{:06.3f}".format(nordsign, nordgrad, nordminuten, ostsign, ostgrad, ostminuten)
    
def koordinaten_minuten_to_dezimalgrad(koordinatenstring):
    """"rechnet Koordinaten in Grad und Minuten (z.B. auf geocaching.com) in Dezimalgrad (z.B. in gpx-Datei) um"""
    if type(koordinatenstring) != unicode and type(koordinatenstring) != str:
        raise TypeError("Wrong input type: {}".format(type(koordinatenstring)))
    if koordinatenstring[4] != u"°" or koordinatenstring[18] != u"°" or len(koordinatenstring) != 25 or koordinatenstring[7] != u"." or koordinatenstring[21] != u".":
        raise ValueError("Bad input.")
    nordgrad = int(koordinatenstring[2:4])
    ostgrad = int(koordinatenstring[15:18])
    nordminuten = float(koordinatenstring[5:11])
    ostminuten = float(koordinatenstring[19:25])
    nord = nordgrad + nordminuten/60
    ost = ostgrad + ostminuten/60
    if nord > 90 or ost > 180:
        raise ValueError("These coordinates do not exist on earth.")
    if koordinatenstring[0] == "S":
        nord = -nord
    elif koordinatenstring[0] != "N":
        raise ValueError("Bad input.")
    if koordinatenstring[13] == "W":
        ost = -ost
    elif koordinatenstring[13] != "E":
        raise ValueError("Bad input.")
    return [nord, ost]
    
def koordinaten_minuten_to_sekunden(koordinatenstring):
    """rechnet Koordinaten in Grad und Minuten (z.B. auf geocaching.com) in Grad, Minuten und Sekunden um (z.B. fuer Eingabe in Google-Maps)"""
    if type(koordinatenstring) != unicode and type(koordinatenstring) != str:
        raise TypeError("Wrong input type: {}".format(type(koordinatenstring)))
    if koordinatenstring[4] != u"°" or koordinatenstring[18] != u"°" or len(koordinatenstring) != 25 or koordinatenstring[7] != u"." or koordinatenstring[21] != u".":
        raise ValueError("Bad input.")
    nordsign = koordinatenstring[0]
    ostsign = koordinatenstring[13]
    if (nordsign != "N" and nordsign != "S") or (ostsign != "E" and ostsign != "W"):
        raise ValueError("Bad input.")
    nordgrad = int(koordinatenstring[2:4])
    ostgrad = int(koordinatenstring[15:18])
    if nordgrad > 90 or ostgrad > 180:
        raise ValueError("These coordinates do not exist on earth.")
    nordminuten_dez = float(koordinatenstring[5:11])
    ostminuten_dez = float(koordinatenstring[19:25])
    if (nordgrad == 90 and nordminuten_dez) > 0 or (ostgrad == 180 and ostminuten_dez > 0):
        raise ValueError("These coordinates do not exist on earth.")
    nordminuten = int(nordminuten_dez)
    ostminuten = int(ostminuten_dez)
    nordsekunden = round((nordminuten_dez - nordminuten)*60,1)
    ostsekunden = round((ostminuten_dez - ostminuten)*60,1)
    return u"{}°{}'{}\"{}+{}°{}'{}\"{}".format(nordgrad, nordminuten, nordsekunden, nordsign, ostgrad, ostminuten, ostsekunden, ostsign)
 
def koordinaten_url_to_dezimalgrad(url):
    """"liest die Koordinaten aus einer Google-Maps oder geocaching.com/map url aus und gibt sie im Dezimalgrad-Format zurueck"""
    if type(url) != str and type(url) != unicode:
        raise TypeError("Wrong input type: {}".format(type(koordinatenstring)))
    if url[:31] == "https://www.geocaching.com/map/":    # geocaching.com/map
        indizes = [index for index, char in enumerate(url) if char == "&"]
        end = indizes[-1]
        for i in range(-5,-100,-1):
            if url[i] == "=":
                start = i+1
                break
        koords_list = url[start:end].split(",")
        nord = float(koords_list[0])
        ost = float(koords_list[1])
    elif url[:27] == "https://www.google.de/maps/":                     # Google Maps
        start_nord = 0
        start_ost = 0
        for i,z in enumerate(url):
            if z == "@":
                start_nord = i+1
            elif z == "," and start_nord > 0 and start_ost == 0:
                end_nord = i
                start_ost = i+1
            elif z == "," and start_ost > 0:
                end_ost = i
                break
        nord = float(url[start_nord:end_nord])
        ost = float(url[start_ost:end_ost])
    else:
        raise ValueError("Bad input.")
    return [nord, ost]
    
def koordinaten_string_to_dezimalgrad(koords_str):
    """liest Koordinaten aus einem String (geocaching.com-Format oder url) aus und gibt sie im Dezimalgrad-Format zurueck"""
    try:         # Koordinaten im geocaching.com-Format
        koords = koordinaten_minuten_to_dezimalgrad(koords_str)
    except ValueError:
        try:     # Koordinaten aus google-maps oder geocaching.com/map url
            koords = koordinaten_url_to_dezimalgrad(koords_str)  
        except: 
            return None
    return koords
    
def calculate_distance(point1, point2):
    """berechnet Entfernung des Geocaches zu einem bestimmten Punkt, Formel siehe: https://www.kompf.de/gps/distcalc.html)"""

    lat1 = point1[0] * (math.pi / 180)
    lon1 = point1[1] * (math.pi / 180)
    lat2 = point2[0] * (math.pi / 180)
    lon2 = point2[1] * (math.pi / 180)

    cos_g = math.sin(lat1)*math.sin(lat2) + math.cos(lat1)*math.cos(lat2)*math.cos(lon2-lon1)
    g = math.acos(cos_g)*6368  # Erdradius
    return g
    
def get_month(string):
    """ordnet Monatsnamen einen Zahlenwert zu"""
    if string == "Jan":
        return 1
    elif string == "Feb":
        return 2
    elif string == "Mar":
        return 3
    elif string == "Apr":
        return 4
    elif string == "May":
        return 5
    elif string == "Jun":
        return 6
    elif string == "Jul":
        return 7
    elif string == "Aug":
        return 8
    elif string == "Sep":
        return 9
    elif string == "Oct":
        return 10
    elif string == "Nov":
        return 11
    elif string == "Dez":
        return 12
        
def string_to_date(string):
    """wandelt einen String im Format 'DD.MM.YYYY' in ein datetime.date-Objekt um"""
    day = int(string[0:2])
    month = int(string[3:5])
    year = int(string[6:10])
    return datetime.date(year, month, day)
    
def remove_spaces(string):
    """entfernt ueberfluessige Leerzeichen aus einem String"""
    newstring = ""
    for i,a in enumerate(string):
        if i == 0 and a == " ":     # Leerzeichen zu Beginn
            pass
        elif a == " " and string[i-1] == " ":   # zwei Leerzeichen hintereinander
            pass
        elif a == " " and i == len(string) - 1: # Leerzeichen am Ende
            pass
        else:
            newstring = newstring + a
    return newstring