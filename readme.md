This is a program that helps you organize your geocaches on your GPS device. Currently it's only available in a German language version.


#Voraussetzungen
* Python 2.7 (vermutlich auch andere Python 2 Versionen möglich)
* Module: glob, os, time, xml.etree.ElementTree (alle in Standardbibliothek vorhanden)

* Die Codierung der Konsole, von der aus das Programm gestartet wird, sollte auf Codepage 1252 eingestellt sein. In Windows Eingabeaufforderung erreicht man das durch Eingabe von "chcp 1252".
* Der Pfad zum Gerät muss "F:\Garmin" lauten. Die Fieldnotes-Datei "geocache_visits.txt" sowie die Logdatei "geocache_logs.xml" sollten direkt dort liegen, die gpx-Dateien in einem Unterordner mit Namen "GPX".
*[Codierung und Pfad können ggf. im Quelltext von "user_io.py" geändert werden.]


#Start: 
Aufruf von "geohelper.py" aus der Konsole


#Funktionen:
*...to be continued...*


#Known bugs
Beim Löschen von zwei gefundenen Caches aus "geocache_visits.txt" werden beide Caches gelöscht, aber einer noch angezeigt.


