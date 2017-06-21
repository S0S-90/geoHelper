import os
import glob
import webbrowser
import subprocess

from geocache import TYPE_LIST, SIZE_LIST  
from geocache import Geocache   
import user_io      
import ownfunctions 


class GPS_content(object):
    """
    An object of this class contains all relevant information from the gps-device (or from another user-defined place)
    
    
    Attributes:
    ----------
    path: string
        path to gps-device (or other place where the information should be read from)
        
    geocaches: list
        list with all geocaches
        
    existing_attributes: list
        list with all attributes existing in the geocaches
        
    found_exists: bool
        is True, if caches are marked as found on gps-device
    
    found_caches: list
        list of all geocaches marked as found (if found_exists)
        
    warning: bool
        is True, if there are other caches beside the found ones in logfile (e.g. as not found, needs maintainance, ...) 
    
    
    Methods:
    ---------
    __init__(path): creates a GPS_content-object from path to gps-device
    
    show_all(): returns a string with most important infos for each cache, each cache in one line
    
    show_all_dist(): returns a string with most important infos (+ distances) for each cache, each cache in one line
    
    show_gc_selection(cachelist): returns a string with most important information of all caches in cachelist, each cache in one line
    
    show_gc_selection_dist(cachelist): returns a string with most important information (+ distances) of all caches in cachelist, each cache in one line
    
    sort_and_show_caches(): sorts all caches by criterion that is defined by the user and shows them"
    
    show_one(): shows detailed information about one cache and performs another actions with it if desired
    
    delete(cachelist): deletes all caches in cachelist from gps-device
    
    show_founds(): shows all caches that are marked as found and performs actions with them if desired
    
    search(): searches caches for desired criterion and returns list of geocaches that match to search
    
    actions_after_search(search_results): performs different actions with search results
    
    show_all_on_map(cachelist): "provides the possiblitly to show all caches in cachelist on a map (uses webservice 'www.mapcustomizer.com')

    """

    
    def __init__(self, path):
        """reads geocaches and logfile from gps-device"""
        
        self.path = path              
        self.found_exists = False     
        self.warning = False          
        self.existing_attributes = [] 
        
        self.geocaches = []               # read all caches from GC*.gpx-files in path\GPX and save in list 'geocaches'
        gpx_path = os.path.join(self.path, "GPX")
        for file in glob.glob(os.path.join(gpx_path,"GC*.gpx")):
            try:
                self.geocaches.append(Geocache(file))
            except:
                user_io.general_output("{}: {}".format(user_io.WARNING_BROKEN_FILE, os.path.basename(file)))
        user_io.general_output("\n{} {}".format(len(self.geocaches), user_io.GEOCACHES_ON_DEVICE))
            
        for g in self.geocaches:      # read existing attributes from geocaches
            for a in g.attributes:
                if a not in self.existing_attributes and a != "No attributes specified by the author":
                    self.existing_attributes.append(a)
        self.existing_attributes.sort()
              
        if os.path.isfile(os.path.join(self.path, "geocache_visits.txt")):    # save all found caches from logfile in found_caches (if logfile is present) 
            [logged_caches, self.found_caches] = self._get_logged_and_found_caches()
            if len(self.found_caches) > 0:
                self.found_exists = True
            if len(self.found_caches) < len(logged_caches): # warning, if caches in logfile that are not marked as found but as something different
                self.warning = True
            else:
                self.warning = False

    def _get_logged_and_found_caches(self):
        """reads logged and found caches from logfile 'geocache_visits.txt' (ignores those that are not saved on device as gpx-files), part of __init__
        
        return: list of two elements which are also lists
            first element: logged caches (not as Geocache-objects but as list [gc-code, date-and-time, logtype])
            second element: list of found caches as Geocache-objects"""

        logged_caches_raw = []           
        with open(os.path.join(self.path, "geocache_visits.txt")) as visits:
            visits = visits.read().decode("utf-16")
            visits_lines = visits.split("\n")
            for line in visits_lines:
                logged_caches_raw.append(line)
        logged_caches = []           
        for lcr in logged_caches_raw:
            lcr = lcr.split(",")
            lcr.remove(lcr[-1])
            if len(lcr) > 0:
                logged_caches.append(lcr)  
        found_caches = []
        logged_caches_new = []
        for lc in logged_caches:
            if lc[-1] == "Found it":
                try:
                    found_caches.append(Geocache(os.path.join(self.path,"GPX",lc[0]+".gpx")))
                    logged_caches_new.append(lc)
                except IOError:
                    user_io.general_output("\nWARNUNG! Der Geocache {} befindet sich nicht auf dem Geraet. Er wird daher im Folgenden nicht mehr beruecksichtigt.".format(lc[0])) 
            else:
                try:
                    Geocache(os.path.join(self.path,"GPX",lc[0]+".gpx"))
                    logged_caches_new.append(lc)
                except IOError:
                    user_io.general_output("\nWARNUNG! Der Geocache {} befindet sich nicht auf dem Geraet. Er wird daher im Folgenden nicht mehr beruecksichtigt.".format(lc[0])) 
        return [logged_caches_new, found_caches]

    def sort_and_show_caches(self):
        """sorts all caches by criterion that is defined by the user and shows them"""
        
        [criterion, rev] = user_io.sort_caches()
        if criterion == "distance":   # read coordinates from user input
            coords_str = user_io.coordinates_input()
            coords = ownfunctions.coords_string_to_decimal(coords_str)
            
            if coords:             # if reading coordinates successful
                for g in self.geocaches:
                    g.distance = ownfunctions.calculate_distance(g.coordinates, coords)  # calculate distance
                self.geocaches = sorted(self.geocaches, key = lambda geocache: getattr(geocache, criterion), reverse = rev)
                user_io.general_output(self.show_all_dist())
            else:
                user_io.general_output(user_io.INVALID_INPUT)
            
        elif criterion == "name":    # criterions for which capitalization doesn't matter
            self.geocaches = sorted(self.geocaches, key = lambda geocache: getattr(geocache, criterion).lower(), reverse = rev)
            user_io.general_output(self.show_all())
        else:                    # criterions for which capitalization matters
            self.geocaches = sorted(self.geocaches, key = lambda geocache: getattr(geocache, criterion), reverse = rev)
            user_io.general_output(self.show_all())
        
    def show_all(self):
        """returns a string with most important infos for each cache, each cache in one line"""
        text = ""
        for c in self.geocaches:
            text = text + c.shortinfo() + "\n"
        if len(self.geocaches) == 0:
            return user_io.NO_CACHES_ON_DEVICE
        return text
        
    def show_all_dist(self):
        """returns a string with most important infos (+ distances) for each cache, each cache in one line"""
        text = ""
        for c in self.geocaches:
            newline = u"{:7}km | {}\n".format(round(c.distance,1), c.shortinfo())
            text = text + newline
        if len(self.geocaches) == 0:
            return user_io.NO_CACHES_ON_DEVICE
        return text
        
    def show_one(self):
        """shows detailed information about one cache and performs another actions with it if desired"""
        
        gc = user_io.general_input(user_io.INPUT_GCCODE)
        cache = None
        for c in self.geocaches:
            if gc == c.gccode:
                cache = c
                break        
        if not cache:
            user_io.general_output(user_io.GC_DOES_NOT_EXIST)
        else:
            user_io.general_output(cache.longinfo())
        
            while True:
                task = user_io.show_one()
                if task == "delete":
                    self.delete([cache])
                    break
                elif task == "gc.com":
                    webbrowser.open_new_tab(cache.url)
                elif task == "dist":
                    koords_str = user_io.coordinates_input()
                    koords = ownfunctions.coords_string_to_decimal(coords_str)
                    if koords:
                        d = ownfunctions.calculate_distance(coords,cache.coordinates)
                        user_io.general_output("Abstand: {} Kilometer".format(round(d,1)))
                elif task == "gc-map":
                    url = "https://www.geocaching.com/map/#?ll={},{}&z=16".format(cache.coordinates[0], cache.coordinates[1])
                    webbrowser.open_new_tab(url)
                elif task == "googlemaps":
                    coords_sec = ownfunctions.coords_minutes_to_seconds(cache.coordinates_string)
                    url = u"https://www.google.de/maps/place/{}".format(coords_sec)
                    webbrowser.open_new_tab(url)
                else:
                    break
        
    def show_gc_selection(self, cachelist):
        """returns a string with most important information of all caches in cachelist, each cache in one line
        
        input: list of caches (as Geocache-objects) that are found on gps-device
        return: string with informations about these caches"""
        
        text = ""
        for c in cachelist:
            if type(c) != Geocache:
                raise TypeError("An Element of the selection is not a Geocache!")
            text = text + c.shortinfo() + "\n"
        return text
        
    def show_gc_selection_dist(self, cachelist):
        """returns a string with most important information (+ distances) of all caches in cachelist, each cache in one line
        
        input: list of caches (as Geocache-objects) that are found on gps-device
        return: string with informations about these caches"""
        
        text = ""
        for c in cachelist:
            if type(c) != Geocache:
                raise TypeError("An Element of the selection is not a Geocache!")
            newline = u"{:7}km | {}\n".format(round(c.distance,1), c.shortinfo())
            text = text + newline
        return text
        
    def search(self):
        """searches caches for desired criterion and returns list of geocaches that match to search"""
        
        search_results = []
        criterion = user_io.search()
        if criterion == "name" or criterion == "description":    # search for name or description
            keyword = user_io.input_decode(user_io.SEARCH_FOR)
            for c in self.geocaches:
                if keyword in getattr(c, criterion):
                    search_results.append(c)
        elif criterion == "difficulty" or criterion == "terrain":  # search for difficulty or terrain value
            input_str = user_io.general_input("{}: ".format(user_io.MIN_MAX_SEPERATED_BY_KOMMA)) 
            input = input_str.split(",")
            if len(input) != 2:
                user_io.general_output(user_io.INVALID_INPUT) 
            else:
                try:
                    min = float(input[0])
                    max = float(input[1])
                except ValueError:
                    user_io.general_output(user_io.INVALID_INPUT)
                else:
                    if min <= max and min >= 1 and min <=5 and max >=1 and max <=5: # all values need to be between 1 and 5
                        for c in self.geocaches:
                            if getattr(c, criterion) >= min and getattr(c, criterion) <= max:
                                search_results.append(c)
                    else:
                        user_io.general_output(user_io.INVALID_INPUT)
        elif criterion == "size":                                           # search by size
            input_str = user_io.general_input("{}. {}: other, micro, small, regular, large\n>>".format(user_io.MIN_MAX_SEPERATED_BY_KOMMA, user_io.POSSIBLE_SIZES))
            input = input_str.split(",")
            if len(input) != 2:
                user_io.general_output(user_io.INVALID_INPUT)
            else:
                try:
                    if input[1][0] == " ":
                        max_str = input[1][1:]
                    else:
                        max_str = input[1]
                    min = SIZE_LIST.index(input[0])
                    max = SIZE_LIST.index(max_str)
                except ValueError:
                    user_io.general_output(user_io.INVALID_INPUT)
                else:
                    if max < min:
                        user_io.general_output(user_io.INVALID_INPUT)
                    else:
                        for c in self.geocaches:
                            if c.size >= min and c.size <= max:
                                search_results.append(c)
        elif criterion == "downloaddate":                               # search by downloaddate
            input_str = user_io.general_input("{}\n>>".format(user_io.DATE_SEPERATED_BY_KOMMA))
            input = input_str.split(",")
            if len(input) != 2:
                user_io.general_output(user_io.INVALID_INPUT)
            else:
                first = input[0]
                if input[1][0] == " ":
                    last = input[1][1:]
                else:
                    last = input[1]
                try:
                    first_date = ownfunctions.string_to_date(first)
                    last_date = ownfunctions.string_to_date(last)
                except ValueError:
                    user_io.general_output(user_io.INVALID_INPUT)
                else:
                    if first_date > last_date:
                        user_io.general_output(user_io.INVALID_INPUT)
                    else:
                        for c in self.geocaches:
                            if c.downloaddate >= first_date and c.downloaddate <= last_date:
                                search_results.append(c) 
        elif criterion == "available":                # search by availibility
            input_str = user_io.general_input(user_io.CACHES_AVAILABLE_OR_NOT)
            if input_str == "n":
                for c in self.geocaches:
                    if c.available == False:
                        search_results.append(c)
            else:      # if invalid input: show available caches
                for c in self.geocaches:
                    if c.available == True:
                        search_results.append(c)
        elif criterion == "type":                    # search by cachetype
            input = user_io.search_type()
            if input not in TYPE_LIST:
                user_io.general_output(user_io.INVALID_INPUT)
            else:
                for c in self.geocaches:
                    if c.type == input:
                        search_results.append(c)
        elif criterion == "attribute":              # search by attribute
            input = user_io.search_attribute(self.existing_attributes)
            if input not in self.existing_attributes:
                user_io.general_output(user_io.INVALID_INPUT)
            else:
                for c in self.geocaches:
                    if input in c.attributes:
                        search_results.append(c)
        elif criterion == "distance":                # search by distance to a given point
            coords_str = user_io.coordinates_input()
            coords = ownfunctions.coords_string_to_decimal(coords_str)
            if coords:
                input_str = user_io.general_input(user_io.DIST_SEPERATED_BY_KOMMA) 
                input = input_str.split(",")
                if len(input) != 2:
                    user_io.general_output(user_io.INVALID_INPUT) 
                else:
                    try:
                        min = float(input[0])
                        max = float(input[1])
                    except ValueError:
                        user_io.general_output(user_io.INVALID_INPUT)
                    else:
                        for c in self.geocaches:
                            c.distance = ownfunctions.calculate_distance(coords,c.coordinates)
                            if c.distance >= min and c.distance <= max:
                                search_results.append(c)
            else:
                user_io.general_output(user_io.INVALID_INPUT)
        
        if len(search_results) == 0:                        # print search results
            user_io.general_output(user_io.NO_CACHES_FOUND)
        else:
            if criterion == "distance":
                user_io.general_output(self.show_gc_selection_dist(search_results))  
            else:
                user_io.general_output(self.show_gc_selection(search_results))
        return search_results
    
    def actions_after_search(self, search_results): 
        """performs different actions with search results
        input: output from function search()"""    

        if len(search_results) != 0:                        
            while True:
                task = user_io.actions_after_search()
                if task == "show_again":
                    user_io.general_output(self.show_gc_selection(search_results))
                elif task == "delete":
                    self.delete(search_results)
                elif task == "show_on_map":
                    self.show_all_on_map(search_results)
                elif task == "show_one":
                    self.show_one()
                elif task == "back":
                    break
        
    def show_founds(self):
        """shows all caches that are marked as found and performs actions with them if desired"""
        
        if not self.found_exists:
            raise ValueError("ERROR: no found caches")
        user_io.general_output(self.show_gc_selection(self.found_caches))
        while True:
            task = user_io.actions_with_founds()
            if task == "log":
                webbrowser.open_new_tab("https://www.geocaching.com/my/uploadfieldnotes.aspx")
            elif task == "delete":
                if self.warning:
                    user_io.general_output(user_io.WARNING_LOG_INFO)
                delete = self.delete(self.found_caches)
                if delete:
                    self.found_exists = False
                    os.remove(os.path.join(self.path,"geocache_visits.txt"))
                    os.remove(os.path.join(self.path,"geocache_logs.xml"))
                    break
            elif task == "exit":
                break
           
    def delete(self, cachelist):
        """deletes all caches in cachelist from gps-device
        
        input: list of caches that are to be deleted
        return: bool that is True if caches are deleted and False if not"""

        delete = user_io.confirm_deletion()
        if delete:
            for c in cachelist:
                os.remove(c.filename_path)
            removelist = []
            for c1 in self.geocaches:
                for c2 in cachelist:
                    if c1 == c2:
                        removelist.append(c1)
            self.geocaches = [c for c in self.geocaches if c not in removelist]
        return delete
        
    def show_all_on_map(self, cachelist):
        """provides the possiblitly to show all caches in cachelist on a map (uses webservice 'www.mapcustomizer.com')"""
    
        editor = user_io.show_all_on_map_start()
        with open("mapinfo.txt","w") as mapinfo:
            for i,g in enumerate(cachelist):
                if g.type == "Traditional Cache":
                    color = "green"
                elif g.type == "Multi-cache":
                    color = "default"
                elif g.type == "EarthCache":
                    color = "tan"
                elif g.type == "Letterbox Hybrid" or g.type == "Geocaching HQ":
                    color = "gray"
                elif g.type == "Event Cache" or g.type == "Wherigo Cache":
                    color = "yellow"
                elif g.type == "Mystery Cache":
                    color = "blue"
                else:                        # cache of unknown type
                    color = "pink"
                mapinfo.write("{},{} {{{}}} <{}>\n".format(g.coordinates[0], g.coordinates[1], g.name.encode(user_io.CODING), color))
        subprocess.Popen([editor,"mapinfo.txt"]) 
        webbrowser.open_new_tab("https://www.mapcustomizer.com/#bulkEntryModal") 
        user_io.show_all_on_map_end()
        os.remove("mapinfo.txt")        
            
 