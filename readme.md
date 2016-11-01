This is a program that helps you organize your geocaches on your GPS device. Currently it's only available in a German language version.


#Voraussetzungen
* Python 2.7 (vermutlich auch andere Python 2 Versionen möglich) - Download unter https://www.python.org/downloads/
* Module: sys, glob, os, time, datetime, xml.etree.ElementTree, webbrowser (alle in Standardbibliothek vorhanden)

* Die Fieldnotes-Datei "geocache_visits.txt" sowie die Logdatei "geocache_logs.xml" müssen direkt im angegebenen Ordner für das GPS-Gerät liegen, 
die gpx-Dateien in einem Unterordner mit Namen "GPX".
* Die gpx-Dateien müssen in dem Format vorliegen, das vom Firefox-Addon "Geocaching.com GPX Downloader" (https://addons.mozilla.org/de/firefox/addon/geocachingcom-gpx-downloader/) 
verwendet wird.


#Start
* Download aller .py Dateien und "winstarter.bat" in einen Ordner
* Doppelklick auf "winstarter.bat"
* [Alternativ kann das Programm "geohelper.py" auch direkt (aus der Konsole) geöffnet werden. Dazu muss jedoch vorher die Codierung der Konsole auf Codepage 1252 eingestellt werden.
So sollte das Programm auch auf Nicht-Windows-Rechnern laufen, was allerdings nicht getestet wurde.]


#Funktionen
* Anzeigen aller Caches auf dem GPS-Gerät mit den wichtigsten Informationen (GC-Code, Koordinaten, Cachetyp, D- und T-Wertung, Größe, Verfügbarkeit, Download-Datum, Name) 
* Sortieren der Caches nach einer bestimmten Eigenschaft (GC-Code, Name, Cachetyp, D- und T-Wertung, Groesse, Download-Datum, Verfügbarkeit)
* Berechnung der Entfernung der Caches zu einer bestimmten Position und Sortieren der Caches nach dieser Entfernung, wobei das Einlesen der Position entweder über 
Eingabe der Koordinaten im auf geocaching.com üblichen Format (Grad und Minuten) oder aus einer Url (Google-Maps oder geocaching.com/map) erfolgt
* Öffnen von https://www.google.de/maps bzw. https://www.geocaching.com/map, um z.B. ein direktes Kopieren der Url für die Abstandsberechnung zu ermöglichen 
* Anzeigen der vollständigen Beschreibung eines Caches sowie Möglichkeit, direkt zur aktuellen Version der Beschreibung im Browser zu wechseln - wird von dort aus eine neue Version der 
GPX-Datei heruntergeladen, kann diese mittels "Geocaches aktualisieren" in das Program eingebunden werden, ohne es neu zu starten
* Amzeigen der Position eines Caches auf https://www.google.de/maps oder https://www.geocaching.com/map
* Durchsuchen der Caches (Name, Beschreibung, Cachetyp, D- und T-Wertung, Größe, Download-Datum, Verfügbarkeit, Atttribute, Abstand zu einer bestimmten Position)
* Löschen eines oder mehrerer Caches
* Auslesen der als gefunden markierten Caches und Löschen dieser Caches mitsamt der Log-Information, nachdem diese auf der Fieldnote-Seite von geocaching.com geloggt wurden





