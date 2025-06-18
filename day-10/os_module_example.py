"""
Example of using the python standard distribution's os module.
"""

import os
from datetime import datetime


def main():
    # Get the current working directory where the current code file is located:
    current_directory = os.getcwd()
    print(f"The current working directory is: {current_directory}")

    # Get a list of names of files in the current working directory:
    list_of_files = os.listdir(current_directory)  # returns a list

    # loop through the list of files and print them out
    print("The files and folders in the current working directory are:")
    for filename in list_of_files:
        # each file is stored in filename, one at a time, and the following code is repeated for each

        # get the size of the file with this name
        filesize = os.stat(filename).st_size  # the file size in bytes

        # the unix timestamp when the file was last modified
        file_last_modified = os.stat(filename).st_mtime  # as unix timestamp (float)

        # convert to datetime object (a custom datatype)
        datetime_object = datetime.fromtimestamp(
            file_last_modified
        )  # as datetime object
        # convert to a "regular" date and time string format
        regular_datetime = datetime_object.strftime("%Y-%m-%d %H:%M:%S")  # as string
        # print out the metadata for this file
        print(f"- {filename} ({filesize}) ({regular_datetime})")

    # Find out if a file exists already:
    filename = "import_styles.py"
    file_exists = os.path.isfile(filename)  # returns a boolean
    if file_exists:
        print(f"The file named {filename} exists!")
    else:
        print(f"The file named {filename} does not exist!")


# run the main function, if this file is being run directly
if __name__ == "__main__":
    main()
