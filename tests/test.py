import sys

import test_ownfunctions
import test_geocache
import test_user_io
import test_main

saved_stdout = sys.stdout # save standard output

verbosity = input("Verbosity (1 oder 2): ")

a = test_ownfunctions.main(verbosity)
b = test_geocache.main(verbosity)
c = test_user_io.main(verbosity)
d = test_main.main(verbosity)

sys.stdout = saved_stdout # print output to display
print "\nTesten beendet. Zusammenfassung:"
print "{} Tests in ownfunctions.py, davon {} erfolgreich und {} fehlgeschlagen".format(a[0], a[0]-a[1], a[1])
print "{} Tests in geocache.py, davon {} erfolgreich und {} fehlgeschlagen".format(b[0], b[0]-b[1], b[1])
print "{} Tests in user_io.py, davon {} erfolgreich und {} fehlgeschlagen".format(c[0], c[0]-c[1], c[1])
print "{} Tests in geohelper.py, davon {} erfolgreich und {} fehlgeschlagen".format(d[0], d[0]-d[1], d[1])
print "Gesamt: {} Tests, davon {} erfolgreich und {} fehlgeschlagen".format(a[0]+b[0]+c[0]+d[0], a[0]-a[1] + b[0]-b[1] + c[0]-c[1] + d[0]-d[1], a[1]+b[1]+c[1]+d[1])