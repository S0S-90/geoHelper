import sys
import os
import webbrowser

from gps_content import GPS_content 
import user_io                      

def show_main_menu(gps):    
    """start main menu
    input: path to gps-device"""

    while True:                                        
        task = user_io.main_menu(gps.found_exists)
        if task == "update":
            new = GPS_content(PATH)
            show_main_menu(new)
        elif task == "show_all":
            gps.sort_and_show_caches()
        elif task == "show_all_on_map":
            gps.show_all_on_map()
        elif task == "show_one":
            gps.show_one()
        elif task == "search":
            results = gps.search()
            gps.actions_after_search(results)
        elif task == "show_founds":
            gps.show_founds()
        elif task == "google-maps":
            webbrowser.open_new_tab("https://www.google.de/maps")
        elif task == "gc-maps":
            webbrowser.open_new_tab("https://www.geocaching.com/map")
        elif task == "exit":
            sys.exit()
         
if __name__ == "__main__":
    PATH = user_io.ask_for_path()   # path to gps-device
    if os.path.exists(PATH):
        new = GPS_content(PATH)
        show_main_menu(new)
    else:
        user_io.general_output("\nERROR: {}: '{}'".format(user_io.GPS_NOT_FOUND, PATH))