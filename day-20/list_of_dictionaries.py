"""
Showing the "list of dictionaries" data structure.
This is a common data structure for dealing with real-world data.
"""

from pathlib import Path
import csv


def get_some_cats_from_data_file():
    """
    Return a list of cats from a data file.

    Returns:
        list: A list of cats (where each cat is a Dictionary)
    """
    # open the data file
    filepath = "data/cats.csv"  # our data file
    filepath = Path(filepath).resolve()  # get a platform-agnostic version of the path
    f = open(filepath, mode="r", encoding="utf-8")  # open the data file

    # make a DictReader, which makes it easy to fetch the data from the file
    # each line of data in the file is converted to a Dictionary automatically
    reader = csv.DictReader(f)

    cats = []  # start off with a blank list of cats
    # iterate through every Dictionary in our DictReader
    for cat in reader:
        # add this Dictionary to our list of cats
        cats.append(cat)
    # return the list of cats.
    return cats


def get_some_cats_from_hardcoded():
    """
    Makes a list of dictionaries, where each dictionary represents a cat.

    Returns:
        list: A list of cats (where each cat is a Dictionary)
    """

    cats = []
    cats.append(
        {
            "id": 100,
            "breed": "sphynx",
            "color": "gray",
            "age": 14,
            "name": "susha",
        }
    )
    cats.append(
        {
            "id": 8,
            "breed": "calico",
            "color": "orange and black",
            "age": 4,
            "name": "norman",
        }
    )
    cats.append(
        {"id": 29, "breed": "mao", "color": "speckled gray", "age": 7, "name": "arya"}
    )
    cats.append(
        {"id": 984, "breed": "tiger", "color": "orange", "age": 88, "name": "tony"}
    )
    cats.append(
        {"id": 7, "breed": "himalayan", "color": "white", "age": 10, "name": "thiksey"}
    )
    cats.append(
        {
            "id": 914,
            "breed": "short-haired",
            "color": "green",
            "age": 2,
            "name": "munchkin",
        }
    )

    # return the list of dictionaries
    return cats


def main():
    # v1
    # get a list of cats from a hard-coded list
    cats_list_1 = get_some_cats_from_hardcoded()  # a list of dictionaries
    # iterate through the list
    print("\nCat names from the hardcoded list:")
    for cat in cats_list_1:
        # every value in the list is a Dictionary
        print(f"- {cat["name"].title()}")

    # v2
    # get a second list of cats from a data file (CSV)
    cats_list_2 = get_some_cats_from_data_file()  # a list of dictionaries
    # iterate through the list
    print("\nCat names from the data file:")
    for cat in cats_list_2:
        # every value in the list is a Dictionary
        print(f"- {cat["name"].title()}")

    # merge the two lists of cats together... why not?!
    # add whats in cats_list_2 to the end of cats_lsit_1
    cats_list_1.extend(cats_list_2)

    # simply the variable name going forward
    cats = cats_list_1
    # print(cats)

    # filter the list by some attribute...

    # e.g. get a list of just the sphynx cats
    sphynxes = []  # start off a list of sphynxes blank
    # iterate through all cat dictionaries
    for cat in cats:
        # if this cat is a sphynx...
        if cat["breed"].lower() == "sphynx":
            sphynxes.append(cat)  # add this cat to our list of sphynxes

    # output the filtered list
    print("\nSphynx cat names:")
    for sphynx in sphynxes:
        print(f"- {sphynx['name'].title()}")


# run the main function if running this file directly
if __name__ == "__main__":
    main()
