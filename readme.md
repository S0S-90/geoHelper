This is a program that helps you organize your geocaches on your GPS device. Currently it's only available in a German language version.


#Voraussetzungen
* Python 2.7 (vermutlich auch andere Python 2 Versionen m�glich)
* Module: glob, os, time, xml.etree.ElementTree (alle in Standardbibliothek vorhanden)

* Die Codierung der Konsole, von der aus das Programm gestartet wird, sollte auf Codepage 1252 eingestellt sein. In Windows Eingabeaufforderung erreicht man das durch Eingabe von "chcp 1252".
* Der Pfad zum Ger�t muss "F:\Garmin" lauten. Die Fieldnotes-Datei "geocache_visits.txt" sowie die Logdatei "geocache_logs.xml" sollten direkt dort liegen, die gpx-Dateien in einem Unterordner mit Namen "GPX".
* Die gpx-Dateien m�ssen in dem Format vorliegen, das vom Firefox-Addon "Geocaching.com GPX Downloader" (https://addons.mozilla.org/de/firefox/addon/geocachingcom-gpx-downloader/) verwendet wird.
*[Codierung und Pfad k�nnen ggf. im Quelltext von "user_io.py" ge�ndert werden.]


#Start: 
Aufruf von "geohelper.py" aus der Konsole


#Funktionen
* Anzeigen aller Caches auf dem GPS-Ger�t mit den wichtigsten Informationen (GC-Code, Koordinaten, Cachetyp, D- und T-Wertung, Gr��e, Verf�gbarkeit, Downloaddatum, Name) und Ordnen der Caches nach Eigenschaften (GC-Code und Name)
* Anzeigen der vollst�ndigen Beschreibung eines Caches
* Durchsuchen der Caches (Name und Beschreibung)
* L�schen eines oder mehrerer Caches
* Auslesen der als gefunden markierten Caches und L�schen





