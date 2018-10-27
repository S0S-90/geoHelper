[![Build Status](https://travis-ci.com/S0S-90/geocachingTooly.svg?branch=master)](https://travis-ci.com/S0S-90/geocachingTooly) [![Coverage Status](https://coveralls.io/repos/github/S0S-90/geocachingTooly/badge.svg?branch=master)](https://coveralls.io/github/S0S-90/geocachingTooly?branch=master)

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
in Konsole (im Ordner "geocachingTooly"):

````bash
# Vorbereitung
cd tests                 # in Ordner gehen
tar -xzf "examples.tar"  # Beispieldateien entpacken

# alle Tests laufen lassen
py -3 test.py       # on Windows
python3 test.py     # on Linux

# oder (für mehr Informationen während Tests -> Angabe einer zusätzlichen Verbosity)
py -3 test.py 2      # on Windows
python3 test.py 2    # on Linux

# nur eine bestimmte Quelldatei testen (auch Verbosity als Argument möglich)
py -3 test_*.py       # on Windows
python3 test_*.py     # on Linux
````




