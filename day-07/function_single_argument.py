"""
Exhibiting how to define functions that accept an argument into a parameter variable.
"""


def foo(some_value):
    """
    A function that accepts any kind of data into its parameter variable.

    Args
        some_value (any type): any value of any type
    """

    # decide what data type the value is
    if isinstance(some_value, bool):
        data_type = "boolean"
    elif isinstance(some_value, int):
        data_type = "integer"
    elif isinstance(some_value, str):
        data_type = "string"
    else:
        data_type = "type of"

    print(f"Thank you for giving me the {data_type} value {some_value}!")


# pass various kinds of arguments to our custom function
foo(10)  # pass an int value
foo(20)  # pass an int value
foo("Hello world!")  # pass a string value
foo(True)  # pass a boolean value
foo(None)  # pass a NoneType value
