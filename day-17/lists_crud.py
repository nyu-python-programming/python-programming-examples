"""
Examples of CRUD operations using lists.
- Create
- Read
- Update
- Delete
"""


def main():
    # CREATE
    my_list = []  # create empty list
    # technically, the following are updates, but I'm using them to initialize the list here for example.
    my_list.append("foo")  # add a new value at the end ['foo']
    my_list.append("baz")  # add another value at the end ['foo', 'baz']
    my_list.insert(1, "bar")  # inject a new value at position 1 ['foo', 'bar', 'baz']
    print(my_list)

    # READ
    first_value = my_list[0]  # "read out" the first value in the list
    last_value = my_list[-1]  # "read out" the last value in the lsit
    print(f"The first value is '{first_value}' and the last value is '{last_value}'.")

    # determine whether a value exists in the list
    is_there = "bar" in my_list
    print(f"The value 'bar' is in the list? {is_there}.")

    # determine the length of the list
    num_values = len(my_list)  # number of values in the list
    print(f"There are {num_values} values in the list.")

    # slice a subset of the values
    first_two = my_list[0:2]  # slice the first two values from the list
    print(f"The first two values in the list are {first_two}.")
    last_two = my_list[-2:]  # slice off the last two values from the list
    print(f"The last two values in the list are {last_two}.")

    # UPDATE

    # note that lists are mutable and some list functions modify it

    # sort the list (either numerically if int or float, or character code order if string)
    my_list.sort()  # modify the list and sort it
    print(f"The sorted list is: {my_list}.")

    # reverse the order
    my_list.reverse()  # lists are mutable!  Their contents can be changed or modified.
    print(f"The reversed list is: {my_list}.")

    # DELETE

    # by default, pop() removes the last value from the list
    removed_value = my_list.pop()
    print(f"The last value ('{removed_value}') has been popped off: {my_list}.")

    # pop can also be supplied an index position of the value to remove
    removed_value = my_list.pop(1)  # remove the value at position 1
    print(
        f"The value at index position 1 ('{removed_value}') has been popped off: {my_list}."
    )

    # remove() removes a value by its value, not by its index position
    my_list.remove("foo")  # remove the value 'foo' from the list
    print(f"The value 'foo' has been removed from the list: {my_list}.")

    # if you have multiple occurrences of a value and want to remove them all...
    my_list = ["foo", "bar", "foo", "foo", "baz", "foo"]
    while "foo" in my_list:
        my_list.remove("foo")
    print(f'The list with all "foo" removed: {my_list}.')


# if running this file directly, call the main function.
if __name__ == "__main__":
    main()
