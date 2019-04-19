# TODO

### Bugfixes

* keine Bugs bekannt :-D

### Neue Features

* Statistiken über bereits gefundene und geloggte Caches anzeigen [gerade in Arbeit]

* Möglichkeit, Koordinaten von Geocaches zu ändern (z. B. nützlich für Rätselcaches)

* Anzeigen von Wegpunkten, die in den GPX-Dateien gespeichert sind

### Restrukturierung

* Wegpunkte, die manuell zu Caches zugeordnet werden, nicht in Wegpunkt-Dateien, sondern als Wegpunkt in der entsprechenden Geocache-Datei speichern
* Tests so gestalten, dass sie nur Verhalten der getesteten Funktion, nicht das des Betriebssystems testen [sinnvoll, da dann die Tests ohne if-else-Abfragen auf allen Betriebssystemen laufen, aber nicht konkret in Planung]
* Programm so umgestalten, dass Hauptschleife im Benutzerinterface *user_io.py* ist und von dort aus die eigentliche Funktionalität aus der Datei *gps_content.py* aufgerufen wird [sinnvoll, um evtl. irgendwann eine GUI einzusetzen, aber nicht konkret in Planung]

## Gerade in Arbeit

Testen

* founds.py komplett -> scheint aber alles zu gehen
* gpscontent.py -> scheint alles zu gehen
  * show_founds schreibt Caches in found_caches.csv, wenn sie auf geocaching.com geloggt wurden 

Was dann noch fehlt:
 - Zugriff auf die Optionen für gefundene Caches aus Hauptprogramm
 - Gefundene Caches sortieren und anzeigen nach unterschiedlichen Kriterien
 - Readme ergänzen (**WICHTIG!** Es funktioniert nur mit meiner privaten Version von pycaching, Branch get_logdate)

