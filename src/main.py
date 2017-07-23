#!/usr/bin/python
# -*- coding: utf-8 -*-

"""This file opens the main menu."""

import sys
import os
import webbrowser

from gpscontent import GPSContent
import user_io                      


def show_main_menu(gps):
    """start main menu
    input: path to gps-device"""

    while True:                                        
        task = user_io.main_menu(gps.found_exists)
        if task == "update":
            new_content = GPSContent(PATH)
            show_main_menu(new_content)
        elif task == "show_all":
            gps.sort_and_show_caches()
        elif task == "show_waypoints":
            gps.show_waypoints()
        elif task == "show_on_map":
            gps.show_on_map(gps.geocaches, True)
        elif task == "show_one":
            gps.show_one()
        elif task == "show_one_gc.com":
            gps.show_one_gccom()
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
    while True:
        PATH = user_io.ask_for_path()   # path to gps-device
        if os.path.exists(PATH):
            new = GPSContent(PATH)
            show_main_menu(new)
            break
        else:
            user_io.general_output("\nERROR: {}: '{}'".format(user_io.GPS_NOT_FOUND, PATH))
