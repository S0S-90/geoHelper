[![Build Status](https://travis-ci.com/S0S-90/geocachingTooly.svg?branch=master)](https://travis-ci.com/S0S-90/geocachingTooly)

This is a program that helps you organize your geocaches on your GPS device. Currently it's only available in a German language version.


# Voraussetzungen
* Python 3 mit Modulen: sys, glob, webbrowser, os, time, math, datetime, urllib.request, html.parser, unicodedata, xml.etree.ElementTree, subprocess (alle in Standardbibliothek vorhanden)
* Die gpx-Dateien können entweder über geocaching.com selbst heruntergeladen werden oder über das Firefox Addon "Geocaching.com GPX Downloader" erzeugt werden.
* Die Fieldnotes-Datei "geocache_visits.txt" sowie die Logdatei "geocache_logs.xml" müssen direkt im angegebenen Ordner für das GPS-Gerät liegen, 
die gpx-Dateien in einem Unterordner mit Namen "GPX". (Dies sollte bei Garmin-Geräten automatisch der Fall sein.)


# Download und Start des Programms
* Falls Python(3) nicht bereits auf dem System vorhanden: Download von Python 3, z.B. [hier](https://www.python.org/downloads/)
* Download und Entpacken des Archivs "geoHelper_vX.X.zip" auf [Release Page](https://github.com/S0S-90/geocachingTooly/releases) 
* Doppelklick auf "winstarter.bat"
* [Alternativ kann das Programm "main.py" auch direkt (aus der Konsole) geöffnet werden. Dazu muss jedoch vorher die Codierung der Konsole auf Codepage 1252 eingestellt werden.
So sollte das Programm auch auf Nicht-Windows-Rechnern laufen, was allerdings nicht getestet wurde.]


# Funktionen
* Anzeigen aller Caches und Wegpunkte auf dem GPS-Gerät mit den wichtigsten Informationen (GC-Code, Koordinaten, Cachetyp, D- und T-Wertung, Größe, Verfügbarkeit, Download-Datum, Name) 
* Sortieren der Caches nach einer bestimmten Eigenschaft (GC-Code, Name, Cachetyp, D- und T-Wertung, Groesse, Download-Datum, Verfügbarkeit)
* Berechnung der Entfernung der Caches zu einer bestimmten Position und Sortieren der Caches nach dieser Entfernung. Das Einlesen der Position erfolgt dabei entweder über 
Eingabe der Koordinaten im auf geocaching.com üblichen Format (Grad und Minuten) oder aus einer Url (Google-Maps oder geocaching.com/map), wobei diese Internetseiten auch aus dem 
Programm heraus geöffnet werden können.
* Anzeigen der vollständigen Beschreibung eines Caches sowie Möglichkeit, direkt zur aktuellen Version der Beschreibung im Browser zu wechseln - wird von dort aus eine neue Version der 
GPX-Datei heruntergeladen, kann diese mittels "Geocaches aktualisieren" in das Program eingebunden werden, ohne es neu zu starten
* Anzeigen der Position eines Caches auf https://www.google.de/maps oder https://www.geocaching.com/map
* Anzeigen aller Caches und Wegpunkte oder einer Auswahl auf der Karte https://www.mapcustomizer.com
* Durchsuchen der Caches (Name, Beschreibung, Cachetyp, D- und T-Wertung, Größe, Download-Datum, Verfügbarkeit, Atttribute, Abstand zu einer bestimmten Position)
* Löschen eines oder mehrerer Caches, z.B. aller als gefunden markieren Caches
* Loggen der gefundenen Caches auf der Fieldnotes-/Draftsseite von geocaching.com
* Wegpunkte erstellen, zu Caches zuordnen und löschen

**Achtung!** Falls Wegpunkte, die bereits durch das Herunterladen zum Cache gehören (z.B. Parkplatz-Koordinaten), vom GPS-Gerät aus gelöscht werden, kann geocachingTooly das gpx-File 
möglicherweise nicht mehr lesen, da das GPS-Gerät den Dateinamen verändert.


# Testen des Programms (nur für Entwickler)
* Die Beispieldateien aus "examples.rar" in einen Ordner "tests\examples" entpacken. (Sie werden für die Tests der Klassen benötigt.)
* In Konsole "py -3 test.py" (im Ordner tests) ausführen. Als Argument kann die Verbosity eingegeben werden, d.h. wie viele Informationen während der Testdurchläufe ausgegeben werden.
Die Standardeinstellung ist 1 (niedrigste Verbosity).
* Anstatt mittels "test.py" alle Tests gleichzeitig auszuführen, kann auch nur eine einzelne Quelldatei getestet werden, indem die entsprechende "test_*.py"-Datei ausgeführt wird.
Auch hier kann die Verbosity durch Eingabe eines Arguments bestimmt werden.




