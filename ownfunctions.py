import math

def zeichen_ersetzen(string):
    """"ersetzt Zeichen, die Probleme bei der Darstellung machen"""    
    string = string.replace(u"\u2013", "-") # u2013 -> Bindestrich
    string = string.replace("<br>", "")     # alle weiteren: html commands
    string = string.replace("<p>", "\n")
    string = string.replace("</p>", "")
    string = string.replace("<br />", "\n")
    return string
    
def koordinaten_dezimalgrad_to_minuten(koordinatenliste):
    """"rechnet Koordinaten in Dezimalgrad (z.B. in gpx-Datei) in Grad und Minuten um (z.B. auf geocaching.com)"""
    nord = koordinatenliste[0]
    ost = koordinatenliste[1]
    nordgrad = int(nord)
    ostgrad = int(ost)
    nordminuten = round(60*(nord - nordgrad), 3)
    ostminuten = round(60*(ost - ostgrad), 3)
    if nordgrad > 0:
        nordsign = "N"
    else:
        nordsign = "S"
        nordgrad = -nordgrad
        nordminuten = -nordminuten
    if ostgrad > 0:
        ostsign = "E"
    else:
        ostsign = "W"
        ostgrad = -ostgrad
        ostminuten = -ostminuten
    return u"{} {:02}°{:6.3f}, {} {:03}°{:6.3f}".format(nordsign, nordgrad, nordminuten, ostsign, ostgrad, ostminuten)
    
def koordinaten_minuten_to_dezimalgrad(koordinatenstring):
    """"rechnet Koordinaten in Grad und Minuten (z.B. auf geocaching.com) in Dezimalgrad (z.B. in gpx-Datei) um"""
    nordgrad = int(koordinatenstring[2:4])
    ostgrad = int(koordinatenstring[15:18])
    nordminuten = float(koordinatenstring[5:11])
    ostminuten = float(koordinatenstring[19:25])
    nord = nordgrad + nordminuten/60
    ost = ostgrad + ostminuten/60
    if koordinatenstring[0] == "S":
        nord = -nord
    if koordinatenstring[13] == "W":
        ost = -ost
    return [nord, ost]
    
def calculate_distance(point1, point2):
        """berechnet Entfernung des Geocaches zu einem bestimmten Punkt, Formel siehe: https://www.kompf.de/gps/distcalc.html)"""

        lat1 = point1[0] * (math.pi / 180)
        lon1 = point1[1] * (math.pi / 180)
        lat2 = point2[0] * (math.pi / 180)
        lon2 = point2[1] * (math.pi / 180)

        cos_g = math.sin(lat1)*math.sin(lat2) + math.cos(lat1)*math.cos(lat2)*math.cos(lon2-lon1)
        g = math.acos(cos_g)*6368000  # Erdradius
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
        return 2