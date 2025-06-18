"""
Exploration of the range() function.
"""


def inspect_range():
    """
    We prefer to think of ranges as lists.... but they are actually their own data type.
    That data type is not of direct interest to us.
    """
    numbers = range(10)  # equivalent to range(0, 10)
    type_of_data = type(numbers)  # the range data type IS NOT of direct interest to us
    print(f"The type of data returned by the range function is {type_of_data}.")
    print(f"The values returned by range(10) are {numbers}")


def inspect_list_from_range():
    """
    Our preferred way to use a range is to think of it (or convert it) as a list.
    """
    numbers = range(10)  # equivalent to range(0, 10)
    numbers = list(numbers)  # convert range to regular list
    type_of_data = type(numbers)  # the list data type IS of direct interest to us
    print(f"The type of data after converting a range to a list is {type_of_data}.")
    print(f"The values in the list derived from range(10) are {numbers}.")


def skip_every_other_value():
    """
    Create a list-like range of numbers from 0 thru 10, not including 10, skipping by 2ss
    """
    numbers = range(0, 10, 2)  # e.g. [0, 2, 4, 6, 8]
    numbers = list(numbers)  # convert range to regular list
    print(f"The values in the list derived from range(0, 10, 2) are {numbers}.")


def skip_every_other_value_starting_from_2():
    """
    Create a list-like range of numbers from 2 thru 10, not including 10, skipping by 2ss
    """
    numbers = range(2, 10, 2)  # e.g. [2, 4, 6, 8]
    numbers = list(numbers)  # convert range to regular list
    print(f"The values in the list derived from range(2, 10, 2) are {numbers}.")


def go_in_reverse():
    """
    Create a list-like range of numbers from 9 thru 0, in reverse order
    """
    numbers = range(9, -1, -1)  # e.g. [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    numbers = list(numbers)  # convert range to regular list
    print(f"The values in the list derived from range(9, 0, -1) are {numbers}.")


def go_in_reverse_skipping_by_2s():
    """
    Create a list-like range of numbers from 9 thru 0, in reverse order, skipping by 2
    """
    numbers = range(9, -1, -2)  # e.g. [9, 7, 5, 3, 1]
    numbers = list(numbers)  # convert range to regular list
    print(f"The values in the list derived from range(9, -1, -2) are {numbers}.")


def main():
    # inspect_range()
    # inspect_list_from_range()
    # skip_every_other_value()
    # skip_every_other_value_starting_from_2()
    # go_in_reverse()
    go_in_reverse_skipping_by_2s()


# run the main function if running this file directly
if __name__ == "__main__":
    main()
