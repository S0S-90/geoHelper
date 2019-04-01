#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This file contains the functionality to read found caches from geocaching.com
by using the python module 'pycaching' (https://github.com/tomasbedrich/pycaching)
and to write them into a file 'found_caches.csv'

'found_caches.csv' is also filled by marking caches as found in the 'main program' gpscontent.py.

Furthermore the file 'found_caches.csv' is read in and information about the caches is shown.
"""

import os
import getpass
import itertools

import pycaching
import ownfunctions
from geocache import Geocache, SIZE_LIST

# dictionary to map geocache types from pycaching to those of TYPE_LIST in geocache.py
TYPE_DICT = {"traditional": "Traditional Cache",
             "multicache": "Multi-cache",
             "earthcache": "EarthCache",
             "letterbox": "Letterbox Hybrid",
             "event": "Event Cache",
             "wherigo": "Wherigo Cache",
             "mystery": "Mystery Cache",
             "unknown": "Unknown Type"}


def login():
    """function that performs login on geocaching.com

    if file .gc_credentials exists it uses the data from there,
    otherwise it asks for username and password"""
    geocaching = None
    if os.path.isfile(".gc_credentials"):
        geocaching = pycaching.login()
    else:
        for i in range(3):
            username = input("Please give username: ")
            password = getpass.getpass("Please give password: ")
            try:
                geocaching = pycaching.login(username, password)
            except pycaching.errors.LoginFailedException:
                if i < 2:
                    print("Error! Your username and/or password are invalid! Try it again...")
                else:
                    print("Login failed!")
                    return "Error"
            else:
                break
    return geocaching


def write_finds_into_csv():
    """writes all found caches of a user into a csv-file 'found_caches'"""

    geocaching = login()
    if geocaching == "Error":
        exit()

    found_caches = itertools.chain(geocaching.my_logs(10), geocaching.my_finds())  # get found and attended caches

    with open("found_caches.csv", "w") as foundfile:
        foundfile.write("GC-Code,Name,Location,Difficulty,Terrain,Size,Type,Availibility,Date\n")

    with open("found_caches.csv", "a") as foundfile:
        counter = 0
        for cd in found_caches:
            counter += 1

            c = cd[0]  # cache
            date_string = "{:02} {} {}".format(int(cd[1].day), ownfunctions.get_month(int(cd[1].month)), cd[1].year)
            c.load_quick()  # necessary to get state and to get information of PMonly caches
            print("Writing cache", counter, ":", c.name)
            try:
                c.location  # if this fails it's a PMonly cache
            except pycaching.errors.LoadError:
                foundfile.write("{},{},{},{},{},{},{},{},{}\n".format(c.wp,
                                                                      ownfunctions.replace_signs(c.name.replace(",", "")),
                                                                      "not available", c.difficulty, c.terrain, c.size,
                                                                      c.type, c.state, date_string))
            else:
                foundfile.write("{},{},{},{},{},{},{},{},{}\n".format(c.wp,
                                                                      ownfunctions.replace_signs(c.name.replace(",", "")),
                                                                      ownfunctions.coords_decimal_to_minutes(
                                                                          [c.location.latitude, c.location.longitude]).
                                                                      replace(",", ""), c.difficulty, c.terrain, c.size,
                                                                      c.type, c.state, date_string))


def add_cache_to_file(cache):
    """add new cache to file 'found_caches.csv'"""
    if not os.path.isfile("found_caches.csv"):
        with open("found_caches.csv", "w") as foundfile:
            foundfile.write("GC-Code,Name,Location,Difficulty,Terrain,Size,Type,Availibility,Date\n")
    with open("found_caches.csv", "a") as foundfile:
        foundfile.write("{},{},{},{},{},{},{},{},{}\n".format(cache.gccode,
                                                              ownfunctions.replace_signs(cache.name.replace(",", "")),
                                                              cache.coordinates_string.replace(",", ""),
                                                              cache.difficulty, cache.terrain,
                                                              "Size.{}".format(cache.size_string),
                                                              "Type.{}".format(ownfunctions.get_key(cache.type, TYPE_DICT)),
                                                              cache.available, cache.date_string))


def read_cache_from_line(line):
    """get information about a geocache from one line of the file 'found_caches.csv'
    returns Geocache"""

    linelist = line.split(',')
    gc = Geocache()
    gc.gccode = linelist[0]
    gc.name = linelist[1]

    gc.coordinates_string = linelist[2]
    if gc.coordinates_string != "not available":
        coords_as_list = list(gc.coordinates_string)
        coords_as_list.insert(11, ',')
        gc.coordinates_string = "".join(coords_as_list)
        gc.coordinates = ownfunctions.coords_minutes_to_decimal(gc.coordinates_string)

    gc.difficulty = float(linelist[3])
    gc.terrain = float(linelist[4])

    gc.size_string = linelist[5][5:]  # remove "Size."
    if gc.size_string not in SIZE_LIST:
        gc.size_string = "other"
    gc.size = SIZE_LIST.index(gc.size_string)

    gc.longtype = linelist[6][5:]  # remove "Type"
    try:
        gc.type = TYPE_DICT[gc.longtype]
    except KeyError:
        gc.type = "Unknown Type"

    avail_string = linelist[7]
    gc.available = None
    if avail_string == "True":
        gc.available = True
    elif avail_string == "False":
        gc.available = False

    gc.date_string = linelist[8][:-1]  # cut '\n'
    gc.date = ownfunctions.string_to_date(gc.date_string)

    return gc


def read_in_founds_from_file():
    """function that reads in all caches from file 'found_caches.csv'
    returns list of geocaches"""

    with open("found_caches.csv") as infile:
        lines = infile.readlines()

    founds = []
    for i, line in enumerate(lines):
        if i > 0:  # first line is heading
            founds.append(read_cache_from_line(line))
    return founds


if __name__ == "__main__":
    ans = input("Do you want to read all your found caches again? <y/n> ")
    if ans == "y":
        write_finds_into_csv()

    found_geocaches = read_in_founds_from_file()
    for f in found_geocaches:
        print(f.shortinfo())
