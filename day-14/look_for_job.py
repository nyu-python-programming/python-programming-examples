"""
Find the distance between each university and college in NYC to a reference point in Greenland.

Raw data on NYC Universities & Colleges sourced from NYC Open Data portal:
- NYC Government Job Postings: https://data.cityofnewyork.us/City-Government/Jobs-NYC-Postings/kpav-sd4t/about_data=
"""

from pathlib import Path  # useful module for dealing with file paths


def get_file(filepath):
    """
    Returns the open file at the specified file path, ready to read.

    Args:
        filepath (str): The path to the file to be opened.

    Returns:
        file object: An open file object (i.e. a TextIOWrapper object) for reading the specified file.
    """

    # THIS IS A VERY BAD FILE PATH.... NEVER USE ONE THAT LOOKS LIKE THIS!!!
    # this is an absolute file path that only works on one person's computer!
    # f = open("/Users/foobarstein/Desktop/py_day_14/data/Jobs_NYC_Postings_20250616.csv", mode="r", encoding="utf-8")

    # THIS IS A SOMEWHAT GOOD FILE PATH... IT IS NOT INCORRECT ON ANYONE'S COMPUTER
    # this is a relative file path that will work on anyone's computer who has your code
    # however, Windows uses \ as a directory separator, whereas UNIX/Linux/Mac use / instead
    # so this is likely to fail on some windows computers
    # f = open("data/Jobs_NYC_Postings_20250616.csv", mode="r", encoding="utf-8")

    # open up the data file in a platform-agnostic fashion.
    # THIS IS THE BEST FILE PATH SOLUTION... IT WILL BE CONVERTED TO THE APPROPRIATE PATH FOR WHOEVER'S COMPUTER RUNS IT
    # use the pathlib's Path object - https://docs.python.org/3/library/pathlib.html#module-pathlib
    filepath = Path(filepath).resolve()  # clean up path for platform-agnosticism
    f = open(filepath, mode="r", encoding="utf-8")  # open it in read mode
    return f  # return the file


def get_lines_of_file_as_list(filepath):
    """
    Return a list of the lines in the specified file/

    Args:
        filepath (str): The path to the file to be read.

    Returns:
        list: A list of strings, where each string is a line from the file.
    """

    f = get_file(filepath)  # get the file object using our specialized function

    # read the entire contents of the file and store into a variable
    total_file_contents = f.read()  # the entire contents as a string
    list_of_lines = total_file_contents.split("\n")  # split by line break
    return list_of_lines  # return the list of lines


def get_keyword_from_user():
    """
    Ask the user for a keyword to search jobs for.

    Returns:
        str: The lowercase form of whatever the user typed.
    """
    keyword = input("What keyword would you like to search for? ")
    return keyword.lower()


def main():
    """
    The main logic of the program.
    """

    filepath = "data/Jobs_NYC_Postings_20250616.csv"

    # get a list of lines from the file
    list_of_lines = get_lines_of_file_as_list(filepath)

    # print out the number of jobs (i.e. # of lines in the file)
    print(f"There are {len(list_of_lines)-1} jobs in NYC government right now!\n")

    # ask the user what keyword to look for in this business title
    keyword = get_keyword_from_user()

    # initialize a counter of how many matching jobs we found that match the keyword
    counter = 0

    # iterate through the list of lines
    for line in list_of_lines:

        # chop each line up by comma
        list_of_values_in_this_line = line.split(",")  # get a list of values

        # ignore any lines that have fewer than 5 comma-separated values
        if len(list_of_values_in_this_line) < 5:
            # skip to the next iteration of the loop
            continue

        # get the fifth value... this is the Business Title of the job
        business_title = list_of_values_in_this_line[4]

        # print(business_title)

        # True/False whether we found the keyword in the business title
        has_keyword = business_title.lower().find(keyword) >= 0
        if has_keyword:
            # increment our counter every time we find a matching job
            counter = counter + 1

            # this job's business title has the desired keyword... do something
            agency = list_of_values_in_this_line[1]  # grab the agency for this line

            # remove any quotes within the agency or job title
            agency = agency.replace('"', "")
            business_title = business_title.replace('"', "")

            # print out the job title and the agency it is in
            print(
                f"- The job '{business_title}' is in the NYC gov't agency, '{agency}'."
            )

    # the loop is complete... move on

    print(f"\nWe found {counter} of jobs with the keyword, '{keyword}'.")


# run the main function, if running this file directly
if __name__ == "__main__":
    main()
