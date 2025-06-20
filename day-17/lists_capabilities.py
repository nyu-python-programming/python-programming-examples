"""
A few example functions that show list capabilities.
"""


def define_list_literal():
    """
    Shows how to define a list literal.
    """
    # literal syntax
    my_list = [1, 2, "buckle", "my", "shoe"]  # a list literal
    print(my_list)


def derive_list_from_string(the_string: str, separator: str):
    """
    Shows how to split a string into a list with a specific separator.

    Args:
        the_string (str): The string to split into a list.
        separator (str): The separator to use for splitting.

    Returns:
        list: The values that have been chopped up from the string
    """
    the_list = the_string.split(separator)  # split string by separator
    return the_list  # return the list


def convert_numeric_values_to_int_v1(the_list):
    """
    Replace numeric strings with ints.

    Args:
        the_list (list): The list to iterate through.

    Returns:
        list: The list with numeric string values replaced with integers.
    """
    # iterate through each value in the list
    # convert any numeric values to int
    # using a for loop
    i = 0  # initialize counter at 0
    for value in the_list:
        if isinstance(value, str) and value.isnumeric():
            value = int(value)  # get int equivalent
            the_list[i] = value  # reassign the value in the list
            print(f"The value {value} is of the type {type(value)}")
        i = i + 1  # increment i

    return the_list  # return the updated list


def convert_numeric_values_to_int_v2(the_list):
    """
    Replace numeric strings with ints.

    Args:
        the_list (list): The list to iterate through.

    Returns:
        list: The list with numeric string values replaced with integers.
    """
    # iterate through each value in the list
    # convert any numeric values to int
    # using a while loop this time
    i = 0
    while i < len(the_list):
        value = the_list[i]  # get one value from the list
        if isinstance(value, str) and value.isnumeric():
            value = int(value)  # get int equivalent
            the_list[i] = value  # reassign the value in the list
            print(f"The value {value} is of the type {type(value)}")
        i = i + 1  # increment i

    return the_list  # return the updated list


def main():

    # create a simple list and print it out
    define_list_literal()

    # split a string into a list
    the_list = derive_list_from_string("1,2,buckle,my,shoe", ",")
    print(f"first list: {the_list}")

    # send the list into one of our functions that swaps numeric strings for ints
    updated_list_v1 = convert_numeric_values_to_int_v1(the_list)
    print(f"second list: {updated_list_v1}")

    # send the list into one of our functions that swaps numeric strings for ints
    updated_list_v2 = convert_numeric_values_to_int_v2(the_list)
    print(f"third list: {updated_list_v2}")


# call the main function if this file is being run directly
if __name__ == "__main__":
    main()
