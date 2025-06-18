"""
A example file showing various built-in data types in the
Python programming language and a few tricks we can use
to investigate what kind of data a given value is.
"""


def main():
    # string
    result = "4" + "2"
    data_type = type(result)
    print(f"The value {result} is of the type {data_type}.")
    if isinstance(result, str):
        print("It's a string!")

    # int
    result = 4 + 2
    data_type = type(result)
    print(f"The value {result} is of the type {data_type}.")
    if isinstance(result, int):
        print("It's a int!")

    # float
    result = 2.0 * 1
    data_type = type(result)
    print(f"The value {result} is of the type {data_type}.")
    if isinstance(result, float):
        print("It's a float!")

    # boolean
    result = True or False
    data_type = type(result)
    print(f"The value {result} is of the type {data_type}.")
    if isinstance(result, bool):
        print("It's a bool!")

    # list
    result = [1, 2, "buckle", "my", "shoe"]
    data_type = type(result)
    print(f"The value {result} is of the type {data_type}.")
    if isinstance(result, list):
        print("It's a list!")

    # dictionary
    result = {"hello": "a greeting", "hey": "an informal version of hello"}
    data_type = type(result)
    print(f"The value {result} is of the type {data_type}.")
    if isinstance(result, dict):
        print("It's a dictionary!")


# call the main function
main()
