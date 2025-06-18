"""
Analyze the distance between each NYC University and Greenland.

Raw data on NYC Universities & Colleges sourced from NYC Open Data portal:
- Colleges & Universities: https://data.cityofnewyork.us/Education/Colleges-and-Universities/4kym-4xw5
"""

import csv  # one of the standard distritution modules
from pathlib import Path  # one of the standard distritution modules

# an add-on module we downloaded with 'pip install geopy'
# ... you will have to run that command from Terminal in order to use it
# see https://geopy.readthedocs.io/en/stable/#module-geopy.distance
from geopy.distance import geodesic

# compare all university locations to sermersooq municipality, greenland
# order is (latitude, longitude)
reference_point = (62.197770, -49.341847)  # a tuple!... i.e. immutable list


def get_file(filepath):
    """
    Returns the open file at the specified file path, ready to read.

    Args:
        filepath (str): The path to the file to be opened.

    Returns:
        file object: An open file object (i.e. a TextIOWrapper object) for reading the specified file.
    """

    # open up the data file in a platform-agnostic fashion.
    filepath = Path(filepath).resolve()  # clean up path for platform-agnosticism
    f = open(filepath, mode="r", encoding="utf-8")  # open it in read mode
    return f  # return the file


def extract_geo_location(point):
    """
    Extract the geolocation from a data point representing an NYC university or college.
    We strip away all but the numeric data and return it as a tuple.

    Args:
        point (str): The raw geo data string from the CSV file, e.g. "POINT (-73.99465215457163 40.73519616365903)".

    Returns:
        tuple: A tuple containing the latitude and longitude in the order (latitude, longitude).
    """
    # extract the geospatial latitude, longitude from the geo data
    # note that this is ordered (longitude, latitude)... the opposite order we need for geopy
    parts = point.split(" ")  # split by space
    uni_longitude = parts[1].strip()  # get the first part
    uni_longitude = uni_longitude.replace("(", "")  # remove parentheses
    uni_latitude = parts[2].strip()  # get the second part
    uni_latitude = uni_latitude.replace(")", "")  # remove parentheses

    # create a tuple with order (latitude, longitude)
    uni_point = (uni_latitude, uni_longitude)
    return uni_point  # return it!


def main():
    """
    The main logic of the program.
    """

    # parse the data file using the csv module's DictReader
    # this converts every line of the text file to a python Dictionary
    f = get_file("data/COLLEGE_UNIVERSITY_20250616.csv")
    reader = csv.DictReader(f)

    # iterate through every line
    for line in reader:
        # each line is a Dictionary with fields from the column heading from the CSV
        geo_point = line["the_geom"]  # get the geom value for this line

        # extract a tuple (latitude, longitude) with just the geo data
        uni_point = extract_geo_location(geo_point)

        # calculate distance between greenland (our reference point) and this uni
        miles = geodesic(reference_point, uni_point).miles  # distance calculator
        miles = round(miles)  # remove decimal place

        # get the name of the university from the line
        name = line["NAME"]  # get the name for this university

        # print out nicely formatted string
        print(f"{name} is {miles:,} away from Sermersooq Municipality, Greenland!")


# run the main function, if running this file directly
if __name__ == "__main__":
    main()
