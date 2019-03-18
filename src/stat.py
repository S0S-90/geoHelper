#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This file contains the functionality to read found caches from geocaching.com
by using the python module 'pycaching' (https://github.com/tomasbedrich/pycaching)
"""

import os
import getpass

import pycaching
import ownfunctions


def login():
    """function that performs login on geocaching.com

    if file .gc_credentiols exists it uses the data from there,
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
        
    found_caches = geocaching.my_finds()

    with open("found_caches.csv", "w") as foundfile:
        foundfile.write("GC-Code,Name,Location,Difficulty,Terrain,Size,Type,Availibility\n")

    with open("found_caches.csv", "a") as foundfile:
        counter = 0
        while True:
            counter += 1
            try:
                c = next(found_caches)
            except pycaching.errors.PMOnlyException:    # premium member cache
                print("Trying to write cache", counter, ".Can't get information about premium member cache.")
                pass
            except StopIteration:                       # generator finished
                break
            else:                                       # everything okay
                print("Writing cache", counter, ":", c.name)
                c.load_quick()             # necessary to get state
                foundfile.write("{},{},{},{},{},{},{},{}\n".format(c.wp, c.name.replace(",", ""),
                                                                   ownfunctions.coords_decimal_to_minutes(
                                                                       [c.location.latitude, c.location.longitude]).
                                                                   replace(",", ""),
                                                                   c.difficulty, c.terrain, c.size, c.type, c.state))


if __name__ == "__main__":
    ans = input("Do you want to read all your found caches again? <y/n> ")
    if ans == "y":
        write_finds_into_csv()
    else:
        print("At the moment this program can do nothing else.")
