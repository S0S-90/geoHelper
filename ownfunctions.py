﻿def zeichen_ersetzen(string):
    """"ersetzt Zeichen, die Probleme bei der Darstellung machen"""    
    string = string.replace(u"\u2013", "-") # u2013 -> Bindestrich
    string = string.replace("<br>", "")     # alle weiteren: html commands
    string = string.replace("<p>", "\n")
    string = string.replace("</p>", "")
    string = string.replace("<br />", "\n")
    return string
    
def koordinaten_dezimalgrad_to_minuten(koordinatenliste):
    """"rechnet Koordinaten in Dezimalgrad (z.B. in gpx-Datei) in Grad und Minuten um (z.B. auf geocaching.com)"""
    nord = float(koordinatenliste[0])
    ost = float(koordinatenliste[1])
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
    
def get_month(string):
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