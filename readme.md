This is a program that helps you organize your geocaches on your GPS device. Currently it's only available in a German language version.


# Voraussetzungen
* Python 2.7 mit Modulen: sys, glob, webbrowser, os, time, math, datetime, urllib, HTMLParser, unicodedata, xml.etree.ElementTree, subprocess (alle in Standardbibliothek vorhanden)

* Die gpx-Dateien sollten in dem Format vorliegen, das vom Firefox-Addon "Geocaching.com GPX Downloader" (https://addons.mozilla.org/de/firefox/addon/geocachingcom-gpx-downloader/) 
verwendet wird.
* Die Fieldnotes-Datei "geocache_visits.txt" sowie die Logdatei "geocache_logs.xml" müssen direkt im angegebenen Ordner für das GPS-Gerät liegen, 
die gpx-Dateien in einem Unterordner mit Namen "GPX". (Dies sollte bei Garmin-Geräten automatisch der Fall sein.)


# Download und Start des Programms
* Falls Python nicht bereits auf dem System vorhanden: Download von Python 2.7, z.B. [hier](https://www.python.org/downloads/)
* Download und Entpacken des Archivs "geoHelper_v2.0.3.zip" auf [Release Page](https://github.com/S0S-90/geocachingTooly/releases) 
* Doppelklick auf "winstarter.bat"
* [Alternativ kann das Programm "main.py" auch direkt (aus der Konsole) geöffnet werden. Dazu muss jedoch vorher die Codierung der Konsole auf Codepage 1252 eingestellt werden.
So sollte das Programm auch auf Nicht-Windows-Rechnern laufen, was allerdings nicht getestet wurde.]


# Funktionen
* Anzeigen aller Caches auf dem GPS-Gerät mit den wichtigsten Informationen (GC-Code, Koordinaten, Cachetyp, D- und T-Wertung, Größe, Verfügbarkeit, Download-Datum, Name) 
* Sortieren der Caches nach einer bestimmten Eigenschaft (GC-Code, Name, Cachetyp, D- und T-Wertung, Groesse, Download-Datum, Verfügbarkeit)
* Berechnung der Entfernung der Caches zu einer bestimmten Position und Sortieren der Caches nach dieser Entfernung. Das Einlesen der Position erfolgt dabei entweder über 
Eingabe der Koordinaten im auf geocaching.com üblichen Format (Grad und Minuten) oder aus einer Url (Google-Maps oder geocaching.com/map), wobei diese Internetseiten auch aus dem 
Programm heraus geöffnet werden können.
* Anzeigen der vollständigen Beschreibung eines Caches sowie Möglichkeit, direkt zur aktuellen Version der Beschreibung im Browser zu wechseln - wird von dort aus eine neue Version der 
GPX-Datei heruntergeladen, kann diese mittels "Geocaches aktualisieren" in das Program eingebunden werden, ohne es neu zu starten
* Anzeigen der Position eines Caches auf https://www.google.de/maps oder https://www.geocaching.com/map
* Anzeigen aller Caches oder einer Auswahl auf der Karte https://www.mapcustomizer.com
* Durchsuchen der Caches (Name, Beschreibung, Cachetyp, D- und T-Wertung, Größe, Download-Datum, Verfügbarkeit, Atttribute, Abstand zu einer bestimmten Position)
* Löschen eines oder mehrerer Caches, z.B. aller als gefunden markieren Caches
* Loggen der gefundenen Caches auf der Fieldnotes-/Draftsseite von geocaching.com


# Testen des Programms (nur für Entwickler)
* Zusätzlich zur Python-Standardinstallation muss das Package mock installiert werden. Für die Installation über pip in den Ordner C:\Python27\Scripts gehen, eine Konsole öffnen
und "pip install mock" eingeben.
* Die Beispieldateien aus "examples.rar" in einen Ordner "tests/examples" entpacken. (Sie werden für die Tests der Klassen benötigt.)
* In Konsole "test.py" (im Ordner tests) ausführen. Als Argument kann die Verbosity eingegeben werden, d.h. wie viele Informationen während der Testdurchläufe ausgegeben werden.
Die Standardeinstellung ist 1 (niedrigste Verbosity).
* Anstatt mittels "test.py" alle Tests gleichzeitig auszuführen, kann auch nur eine einzelne Quelldatei getestet werden, indem die entsprechende "test_*.py"-Datei ausgeführt wird.
Auch hier kann die Verbosity durch Eingabe eines Arguments bestimmt werden.




