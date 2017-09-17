#!/usr/bin/python
# -*- coding: utf-8 -*-

"""This file opens the main menu."""

import sys
import os

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
        elif task == "map-menu":
            gps.show_map_menu()
        elif task == "show_one":
            gps.show_one()
        elif task == "search":
            results = gps.search()
            gps.actions_after_search(results)
        elif task == "show_founds":
            gps.show_founds()
        elif task == "exit":
            sys.exit()
         
if __name__ == "__main__":
    while True:
        PATH = user_io.ask_for_path()   # path to gps-device
        gpx_found = False
        if PATH == "default":
            for path in user_io.PATH:
                if os.path.exists(path):
                    new = GPSContent(path)
                    show_main_menu(new)
                    gpx_found = True
                    break
        else:
            if os.path.exists(PATH):
                new = GPSContent(PATH)
                show_main_menu(new)
                gpx_found = True
                break
        if not gpx_found:
            inp = user_io.general_input("\nERROR: {}: '{}'. {}".format(user_io.GPS_NOT_FOUND,
                                                                       PATH, user_io.LEAVE_PROGRAMME))
            if inp == "y":
                break
