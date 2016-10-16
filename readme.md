This is a program that helps you organize your geocaches on your GPS device. Currently it's only available in a German language version.


#Voraussetzungen
* Python 2.7 (vermutlich auch andere Python 2 Versionen möglich)
* Module: sys, glob, os, time, datetime, xml.etree.ElementTree, webbrowser (alle in Standardbibliothek vorhanden)

* Die Codierung der Konsole, von der aus das Programm gestartet wird, sollte auf Codepage 1252 eingestellt sein. In Windows Eingabeaufforderung erreicht man das durch Eingabe von "chcp 1252".
* Der Pfad zum Gerät muss "F:\Garmin" lauten. Die Fieldnotes-Datei "geocache_visits.txt" sowie die Logdatei "geocache_logs.xml" sollten direkt dort liegen, die gpx-Dateien in einem Unterordner mit Namen "GPX".
* Die gpx-Dateien müssen in dem Format vorliegen, das vom Firefox-Addon "Geocaching.com GPX Downloader" (https://addons.mozilla.org/de/firefox/addon/geocachingcom-gpx-downloader/) verwendet wird.
* [Codierung und Pfad können ggf. im Quelltext von "user_io.py" geändert werden.]


#Start
* Download aller .py Dateien in einen Ordner
* Öffnen der Konsole in diesem Ordner
* Eingabe von "geohelper.py" in der Konsole 


#Funktionen
* Anzeigen aller Caches auf dem GPS-Gerät mit den wichtigsten Informationen (GC-Code, Koordinaten, Cachetyp, D- und T-Wertung, Größe, Verfügbarkeit, Download-Datum, Name) 
* Sortieren der Caches nach einer bestimmten Eigenschaft (GC-Code, Name, Cachetyp, D- und T-Wertung, Groesse, Download-Datum, Verfügbarkeit)
* Berechnung der Entfernung der Caches zu einer bestimmten Position und Sortieren der Caches nach dieser Entfernung, 
wobei das Einlesen der Position entweder über Eingabe der Koordinaten im auf geocaching.com üblichen Format (Grad und Minuten) oder aus einer Url (Google-Maps oder geocaching.com/map) erfolgt
* Öffnen von https://www.google.de/maps bzw. https://www.geocaching.com/map, um z.B. ein direktes Kopieren der Url für die Abstandsberechnung zu ermöglichen 
* Anzeigen der vollständigen Beschreibung eines Caches sowie Möglichkeit, direkt zur aktuellen Version der Beschreibung im Browser zu wechseln
* Durchsuchen der Caches (Name und Beschreibung)
* Löschen eines oder mehrerer Caches
* Auslesen der als gefunden markierten Caches und Löschen dieser Caches mitsamt der Log-Information





