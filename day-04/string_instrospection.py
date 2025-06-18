'''
Analyzing the contents of a string
'''


def main():

    # get a string from the user
    vegetable = input("Enter your favorite vegetable: ")

    # determine what type of data this variable refers to
    data_type = type(vegetable) # use the built-in type function to determine data type
    print(f"The value, '{vegetable}' is of the data type: {data_type}.")

    # determine how many characters are in the string
    length = len(vegetable) # use the built-in len function to determine the number of characters in the string
    print(f"The string, '{vegetable}' has {length} characters.")

    if length < 7:
        # the vegetable name is less than 7 characters
        print("Thanks for the nice short vegetable name.")
    else:
        # the vegetable name is 7 or more characters long
        print("Sorry, that vegetable name is too long!")

    # check for alphabetic characters
    is_alphabetic = vegetable.isalpha()
    if is_alphabetic:
        # the vegetable name is all alphabetic characters
        print(f"The string, '{vegetable}', is all alphabetic.")
    else:
        # the vegetable name is not all alphabetic characters
        print(f"Sorry, no!  That string, '{vegetable}', is not all alphabetic.")


    # check for capitalization
    is_lower = vegetable.islower() # returns True or False, whether or not the given string is all lowercase
    if is_lower:
        # yes, the string is all lowercase!
        print(f"Yes, the string '{vegetable}' is all lowercase!")
    else:
        # no, the string is not all lowercase!
        print(f"No.  I'm so sorry.  The string, '{vegetable}', is not all lowercase!")

    # check for title case
    is_title = vegetable.istitle()
    if is_title:
        # yes, the string is in title case!
        print(f"Yes, the string '{vegetable}' is in title case!")
    else:
        # no, the string is not in title case
        print(f"No.  I'm so sorry.  The string, '{vegetable}', is not in title case!")

    # check for numbers
    is_number = vegetable.isnumeric()
    if is_number:
        # yes, the string is numeric
        print(f"Yes, the string '{vegetable}' is a number!")
    else:
        # no, the string is not numeric
        print(f"No.  I'm so sorry.  The string, '{vegetable}', is not a number!")

# if running this file directly, call the main method
if __name__ == '__main__':
    main()