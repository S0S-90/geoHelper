This is a program that helps you organize your geocaches on your GPS device. Currently it's only available in a German language version.


#Voraussetzungen
* Python 2.7 (vermutlich auch andere Python 2 Versionen m�glich)
* Module: glob, os, time, xml.etree.ElementTree (alle in Standardbibliothek vorhanden)

* Die Codierung der Konsole, von der aus das Programm gestartet wird, sollte auf Codepage 1252 eingestellt sein. In Windows Eingabeaufforderung erreicht man das durch Eingabe von "chcp 1252".
* Der Pfad zum Ger�t muss "F:\Garmin" lauten. Die Fieldnotes-Datei "geocache_visits.txt" sowie die Logdatei "geocache_logs.xml" sollten direkt dort liegen, die gpx-Dateien in einem Unterordner mit Namen "GPX".
*[Codierung und Pfad k�nnen ggf. im Quelltext von "user_io.py" ge�ndert werden.]


#Start: 
Aufruf von "geohelper.py" aus der Konsole


#Funktionen:
*...to be continued...*


#Known bugs
Beim L�schen von zwei gefundenen Caches aus "geocache_visits.txt" werden beide Caches gel�scht, aber einer noch angezeigt.


