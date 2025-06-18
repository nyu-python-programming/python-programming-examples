import csv
from pathlib import Path


def main():

    # make this path work on all computer operating systems.
    filepath = Path("data/Voting_Poll_Sites_20250618.csv").resolve()
    f = open(filepath, mode="r", encoding="utf-8")

    # create a list of the lines in the file where each line is converted to a Python dictionary
    reader = csv.DictReader(f)

    # populations of each borough
    # pulled from wikipedia: https://en.wikipedia.org/wiki/Boroughs_of_New_York_City
    bronx_population = 1472654
    brooklyn_population = 2736074
    staten_island_population = 495747
    queens_population = 2405464
    manhattan_population = 1694251

    # counters for each borough
    bronx_count = 0
    brooklyn_count = 0
    staten_island_count = 0
    queens_count = 0
    manhattan_count = 0

    # iterate line by line through the file
    for line in reader:
        # get the borough from the Dictionary that represents this line
        borough = line["BOROUGH"]

        # determine which counter to increment, based on the borough in this line
        if borough.lower() == "bronx":
            bronx_count = bronx_count + 1  # increment it!
        elif borough.lower() == "brooklyn":
            brooklyn_count = brooklyn_count + 1  # increment it!
        elif borough.lower() == "staten is":
            staten_island_count = staten_island_count + 1  # increment it!
        elif borough.lower() == "queens":
            queens_count = queens_count + 1  # increment it!
        elif borough.lower() == "manhattan":
            manhattan_count = manhattan_count + 1  # increment it!

    # compute the ratio of population to voting sites
    bronx_ratio = bronx_population / bronx_count
    brooklyn_ratio = brooklyn_population / brooklyn_count
    staten_island_ratio = staten_island_population / staten_island_count
    queens_ratio = queens_population / queens_count
    manhattan_ratio = manhattan_population / manhattan_count

    # we're done iterating through the lines of the file
    # print out the results
    print("The number of polling sites in each borough: \n")
    print(f"- bronx: {bronx_count} voting sites ({bronx_ratio:,.1f} people per site)")
    print(
        f"- brooklyn: {brooklyn_count} voting sites ({brooklyn_ratio:,.1f} people per site)"
    )
    print(
        f"- staten island: {staten_island_count} voting sites ({staten_island_ratio:,.1f} people per site)"
    )
    print(
        f"- queens: {queens_count} voting sites ({queens_ratio:,.1f} people per site)"
    )
    print(
        f"- manhattan: {manhattan_count} voting sites ({manhattan_ratio:,.1f} people per site)"
    )


# run the main function if running this file directly
if __name__ == "__main__":
    main()
