"""
Pseudo-randomly generates one line of a Mad Lib and
either prints it out or saves it to a file, depending
on the day of the week.
"""

import random
import datetime


def generate_mad_lib():
    """
    Function definition... no parameter variables, returns a Mad Lib string.

    Returns:
        str: A line from a Mad Lib generated psuedo-randomly.
    """
    # a randomish number
    num = random.randint(1, 100)

    adjectives = [
        "pretty",
        "pink",
        "awesome",
        "smart",
        "funny",
        "beautiful",
        "sly",
        "iconic",
        "slippery",
    ]
    # calculate the number of values in the list
    num_items_in_list = len(adjectives)
    # a randomish index for a value in the list
    index_num = random.randint(0, num_items_in_list - 1)
    # pick that value from the list using the index
    adj = adjectives[index_num]

    # a bunch of nouns in singular form
    nouns = [
        "skate",
        "legend",
        "cat",
        "diva",
        "blockchain",
        "bitcoin",
        "fish",
        "calculator",
        "iPhone",
        "programmer",
        "access",
        "pass",
    ]
    # calculate the number of values in the list
    num_items_in_list = len(nouns)
    # a randomish index for a value in the list
    index_num = random.randint(0, num_items_in_list - 1)
    # pick that value from the list using the index
    noun = nouns[index_num]

    # make the noun plural, if necessary
    if num > 1:
        if noun == "fish" or noun == "bitcoin":
            # handle the exception for bitcoin
            noun = noun  # keep as-is... singular form
        elif noun.endswith("sh"):
            noun = noun + "es"  # exception for words ending in 'sh'
        elif noun.endswith("s"):
            noun = noun + "es"
        else:
            # apply the general rule
            noun = noun + "s"

    mad_lib = f"{num} {adj} {noun} walked into a bar..."
    return mad_lib


def main():
    # get the date and time right now...
    date_today = datetime.datetime.today()
    # convert the date to an int representing the current day of the week (0 for Monday, 1 for Tuesday, etc)
    day_num = datetime.datetime.weekday(date_today)

    # generate a line of a "mad lib"
    mad_lib = generate_mad_lib()  # get a Mad Lib from the function

    # determine what to do next, based on the day of the week
    if day_num == 0 or day_num > 3:
        # on Mondays and Friday thru Sunday, print the mad lib text
        print(mad_lib)  # print it out
    else:
        # on Tuesdays, Wednesdays, Thursdays, save the mad lib text to a file
        f = open("mad_libs.txt", mode="a")  # open a file in append mode
        f.write(mad_lib + "\n")  # write a new line at the end of the file
        f.close()  # close the file to tell python you're done with it


# run main if running this file directly
if __name__ == "__main__":
    main()
