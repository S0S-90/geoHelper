#!/usr/bin/python
# -*- coding: utf-8 -*-

"""This file contains some functions that can be used everywhere in the program."""

import math
import datetime
from html.parser import HTMLParser
import unicodedata
import urllib.request

import user_io

MONTHS = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
          "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12,
          "Mrz": 3, "Okt": 10, "Dez": 12}


def get_key(value, dictionary):
    """
    searches a dictionary for a certain value and returns the corresponding key
    """
    for key, val in dictionary.items():
        if value == val:
            return key
    raise KeyError("Error! Value", value, "not in", MONTHS)


def connected(website):
    """prueft, ob Internetverbindung vorhanden"""
    try:
        urllib.request.urlopen(website)
    except IOError:
        return False
    else:
        return True


class MyHTMLParser(HTMLParser):
    """parser to read all data that is in a table (tags <td> / </td)
    
    Attributes:
    -----------
    read: bool
        if true data is read, if false no data is read
        
    data: list
        container for data that is read
        
    
    Methods:
    ---------
    return_data(): return list data
    """

    def error(self, message):
        """automatically added function by PyCharm"""
        pass

    def __init__(self):
        HTMLParser.__init__(self)
        self.data = []
        self.read = False

    def handle_starttag(self, tag, attr):
        """find the tag where reading data should start"""
        if tag == "td":
            self.read = True

    def handle_endtag(self, tag):
        """find the tag where reading data should end"""
        if tag == "td":
            self.read = False

    def handle_data(self, data):
        """saves data that was read into self.data"""
        if self.read:
            self.data.append(data)

    def return_data(self):
        """returns data"""
        return self.data


def find_cp1252():
    """parses website about codepage 1252 and gives back a list with unicode descriptions"""
    
    current_folder = "/".join(__file__.split('/')[:-1])  # folder of current file (ownfunctions.py)
    with open("{}/cp1252.htm".format(current_folder)) as codingfile:  # read website www.cp1252.com (downloaded on 15.06.2017)
        x = codingfile.read()

    parser = MyHTMLParser()  # parse website
    parser.feed(x)
    cpdata = parser.return_data()  # content of table in cpdata

    cp1252 = []  # find unicode-descriptions in cpdata and save them in cp1252
    for i, d in enumerate(cpdata):
        if i % 4 == 3 and i > 6:
            cp1252.append(d)
    return cp1252


ALLOWED_SIGNS = find_cp1252()  # define allowed signs (codepage 1252) once 


def replace_signs(string):
    """replaces signs in inputstring that cannot represented correctly on screen (not in ALLOWED_SIGNS)
    returns the new string without the 'forbidden' signs"""

    newstring = ""
    for i, c in enumerate(string):
        if c == "\n" or c == "\t" or c == "\v":  # Newline, Tab (horizonal or vertical)
            newstring += c
        else:
            try:
                unic = unicodedata.name(c)
            except ValueError:  # if sign not in unicode
                newstring += "\u001a"
            else:
                if unic in ALLOWED_SIGNS:  # allowed signs
                    newstring += c
                elif c == "\u263a":  # smiley
                    newstring += ":-)"
                elif c == "\u2211":  # sign for sum
                    newstring += "sum"
                elif c == "\u221a":  # sign for square root
                    newstring += "sqrt"
                else:  # unknown sign
                    newstring += u"\u001a"
    return newstring


def show_xml(xml_tree):
    """shows tags, attributes and test of xml-tree (only for information)"""
    for x in xml_tree.iter():
        t = ""
        if x.text:
            t = x.text
        user_io.general_output("{} {} {}".format(x.tag, str(x.attrib), t))


def validate_coordinates(coordlist):
    """run this on a pair of coordinates [lon, lat]
    function throws an error of the coordinates are not valid"""

    if type(coordlist) != list or len(coordlist) != 2:
        raise TypeError("Bad input.")
    north = coordlist[0]
    east = coordlist[1]
    if (type(north) != float or type(east) != float) and (type(north) != int or type(east) != int) and (
                    type(north) != float or type(east) != int) and (type(north) != int or type(east) != float):
        raise TypeError("One of the coordinates is not a number.")
    if north > 90 or east > 180 or north < -90 or east < -180:
        raise ValueError("These coordinates do not exist on earth.")


def coords_decimal_to_minutes(coordlist):
    """converts decimal coordinates (e.g. from gpx-file) to degrees and minutes (e.g. like on geocaching.com)
    
    input: list of floats [lat, lon]
    return: string 'X XX°XX.XXX, X XXX°XX.XXX'
    """

    validate_coordinates(coordlist)
    north = coordlist[0]
    east = coordlist[1]
    north_degree = int(north)
    east_degree = int(east)
    north_minutes = round(60 * (north - north_degree), 3)
    east_minutes = round(60 * (east - east_degree), 3)
    if north_degree >= 0:
        north_sign = "N"
    else:
        north_sign = "S"
        north_degree = -north_degree
        north_minutes = -north_minutes
    if east_degree >= 0:
        east_sign = "E"
    else:
        east_sign = "W"
        east_degree = -east_degree
        east_minutes = -east_minutes
    return "{} {:02}°{:06.3f}, {} {:03}°{:06.3f}".format(north_sign, north_degree, north_minutes, east_sign, east_degree,
                                                         east_minutes)


def coords_minutes_to_decimal(coordstring):
    """converts coordinates given in degrees and minutes (e.g. like on geocaching.com)
    to decimal degrees (e.g. like from gpx-file)
    which is format in which calculations can be done
    
    input: string 'X XX°XX.XXX, X XXX°XX.XXX'
    return: list of floats [lat, lon]
    """

    if type(coordstring) != str:
        raise TypeError("Wrong input type: {}".format(type(coordstring)))
    if len(coordstring) != 25:
        raise ValueError("Bad Input.")
    if coordstring[4] != "°" or coordstring[18] != "°" or coordstring[7] != "." or coordstring[21] != ".":
        raise ValueError("Bad Input.")
    north_degree = int(coordstring[2:4])
    east_degree = int(coordstring[15:18])
    north_minutes = float(coordstring[5:11])
    east_minutes = float(coordstring[19:25])
    north = north_degree + north_minutes / 60
    east = east_degree + east_minutes / 60
    if north > 90 or east > 180:
        user_io.general_output("These coordinates do not exist on earth.")
        return None
    if coordstring[0] == "S":
        north = -north
    elif coordstring[0] != "N":
        user_io.general_output("Wrong input format.")
        return None
    if coordstring[13] == "W":
        east = -east
    elif coordstring[13] != "E":
        user_io.general_output("Wrong input format.")
        return None
    return [north, east]


def coords_minutes_to_seconds(coordstring):
    """converts coordinates given in degrees and minutes (e.g. like on geocaching.com)
    to degrees, minutes and seconds (e.g. for google maps input)
    input and return value is a string"""

    if type(coordstring) != str:
        raise TypeError("Wrong input type: {}".format(type(coordstring)))
    if len(coordstring) != 25:
        return None
    if coordstring[4] != "°" or coordstring[18] != "°" or coordstring[7] != "." or coordstring[21] != ".":
        return None
    north_sign = coordstring[0]
    east_sign = coordstring[13]
    if (north_sign != "N" and north_sign != "S") or (east_sign != "E" and east_sign != "W"):
        user_io.general_output("Wrong input format.")
        return None
    north_degree = int(coordstring[2:4])
    east_degree = int(coordstring[15:18])
    if north_degree > 90 or east_degree > 180:
        user_io.general_output("These coordinates do not exist on earth.")
        return None
    north_minutes_exact = float(coordstring[5:11])
    east_minutes_exact = float(coordstring[19:25])
    if (north_degree == 90 and north_minutes_exact) > 0 or (east_degree == 180 and east_minutes_exact > 0):
        user_io.general_output("These coordinates do not exist on earth.")
        return None
    north_minutes_rounded = int(north_minutes_exact)
    east_minutes_rounded = int(east_minutes_exact)
    north_seconds = round((north_minutes_exact - north_minutes_rounded) * 60, 1)
    east_seconds = round((east_minutes_exact - east_minutes_rounded) * 60, 1)
    return "{}°{}'{}\"{}+{}°{}'{}\"{}".format(north_degree, north_minutes_rounded, north_seconds, north_sign, east_degree,
                                              east_minutes_rounded, east_seconds, east_sign)


def coords_url_to_decimal(url):
    """reads coordinates from a url (google maps or geocaching.com/map) and returns them as decimal degrees
    input: string
    return: list of floats [lat, lon]"""

    if type(url) != str:
        raise TypeError("Wrong input type: {}".format(type(url)))
    if url[:31] == "https://www.geocaching.com/map/":  # geocaching.com/map
        indices = [index for index, char in enumerate(url) if char == "&"]
        end = indices[-1]
        start = False
        for i in range(-5, -100, -1):
            if url[i] == "=":
                start = i + 1
                break
        coordlist = url[start:end].split(",")
        north = float(coordlist[0])
        east = float(coordlist[1])
    elif url[:27] == "https://www.google.de/maps/":  # Google Maps
        start_north = 0
        start_east = 0
        end_north = False
        end_east = False
        for i, z in enumerate(url):
            if z == "@":
                start_north = i + 1
            elif z == "," and start_north > 0 and start_east == 0:
                end_north = i
                start_east = i + 1
            elif z == "," and start_east > 0:
                end_east = i
                break
        north = float(url[start_north:end_north])
        east = float(url[start_east:end_east])
    else:
        raise ValueError("Bad input.")
    return [north, east]


def coords_string_to_decimal(coordstring):
    """reads coordinates from a string (X XX°XX.XXX, X XXX°XX.XXX or url) and returns them as decimal degrees
    return: list of floats [lat, lon]"""

    try:  # coordinates in geocaching.com format
        coords = coords_minutes_to_decimal(coordstring)
    except ValueError:
        try:  # url
            coords = coords_url_to_decimal(coordstring)
        except ValueError:
            return None
    return coords


def calculate_distance(point1, point2):
    """calculates distance between point1 and point2 in kilometers
    for the formula see: https://www.kompf.de/gps/distcalc.html)
    
    input: point1, point2 = list [lat, lon] with lat, lon in decimal degrees
    return: distance as float (int)"""

    if type(point1) != list or len(point1) != 2 or type(point2) != list or len(point2) != 2:  # see if input is ok
        raise TypeError("Bad input.")

    if (type(point1[0]) != float or type(point1[1]) != float) and (type(point1[0]) != int or type(point1[1]) != int) and (
                    type(point1[0]) != float or type(point1[1]) != int) and (
                    type(point1[0]) != int or type(point1[1]) != float):
        raise TypeError("One of the coordinates is not a number.")
    if (type(point2[0]) != float or type(point2[1]) != float) and (type(point2[0]) != int or type(point2[1]) != int) and (
                    type(point2[0]) != float or type(point2[1]) != int) and (
                    type(point2[0]) != int or type(point2[1]) != float):
        raise TypeError("One of the coordinates is not a number.")
    if point1[0] > 90 or point1[1] > 180 or point1[0] < -90 or point1[1] < -180 or point2[0] > 90 or point2[1] > 180 or \
            point2[0] < -90 or point2[1] < -180:
        raise ValueError("These coordinates do not exist on earth.")

    lat1 = point1[0] * (math.pi / 180)  # start of the calculation
    lon1 = point1[1] * (math.pi / 180)
    lat2 = point2[0] * (math.pi / 180)
    lon2 = point2[1] * (math.pi / 180)

    cos_g = math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon2 - lon1)
    g = math.acos(cos_g) * 6368  # radius of the earth
    return g


def get_year_without_century(year):
    """removes the century from a year, e.g. 1017 -> 17"""
    if type(year) != int:
        raise TypeError("ERROR: not a valid year")
    year_str = str(year)
    return int(year_str[-2:])


def get_month_number(string):
    """
    input: month as three letter string
    return: number of this month in the year
    """
    if string not in MONTHS.keys():
        raise KeyError("Unvalid month!")
    return MONTHS[string]


def get_month(number):
    """
    input: number of this month in the year
    return: month as three letter string
    """
    return get_key(number, MONTHS)


def string_to_date(string):
    """converts string 'DD.MM.YYYY' or 'DD MMM YYYY' or 'YYYY-MM-DD' to datetime.date objekt
    
    input: date as string
    return: date as datetime.date"""

    if len(string) == 10:
        try:
            day = int(string[0:2])     # DD.MM.YYYY
            month = int(string[3:5])
            year = int(string[6:10])
        except ValueError:
            try:
                year = int(string[0:4])   # YYYY-MM-DD
                month = int(string[5:7])
                day = int(string[8:10])
            except ValueError:
                raise ValueError("String for Date not correctly formated: {}".format(string))
        return datetime.date(year, month, day)

    elif len(string) == 11:
        try:
            day = int(string[0:2])        # DD MMM YYYY
            month = int(get_month_number(string[3:6]))
            year = int(string[7:11])
        except ValueError:
            raise ValueError("String for Date not correctly formated: {}".format(string))
        return datetime.date(year, month, day)

    else:
        raise ValueError


def remove_spaces(string):
    """removes unnecessary spaces from a string
    
    input: string
    return: string without the unnecessary spaces"""

    newstring = ""
    for i, a in enumerate(string):
        if i == 0 and a == " ":  # spaces at the beginning
            pass
        elif a == " " and i == len(string) - 1:  # spaces at the end
            return remove_spaces(newstring)
        elif a == " " and string[i - 1] == " ":  # two spaces back to back
            pass
        else:
            newstring = newstring + a
    return newstring


def string_is_int(string):
    """returns true if string can be converted into int
    returns false if string cannot be converted into int"""
    try:
        int(string)
    except ValueError:
        return False
    return True


if __name__ == "__main__":
    pass  # ROOM FOR DEVELOPMENT TESTING
