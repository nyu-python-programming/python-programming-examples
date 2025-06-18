"""
Example showing how one file can import code from another file.
This is a preview of stuff we will get deeper into later
in our discussion of 'modules'.
"""

import functions_recap  # import the code from the other file


# define a main function
def main():
    """
    The main function that we run.
    """
    # call one of the functions defined in the other file
    functions_recap.say_hello()
    # functions_recap.say_goodbye()
    print("Hello world from another file!")


# only call main if we are running this file directly
if __name__ == "__main__":
    main()
