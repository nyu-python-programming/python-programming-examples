"""
An example of some use of some functions in some modules.
"""

import math


def main():
    """
    Do some example code.
    """
    # all programs auto-import all the functions in the __main__ module,
    # e.g. print(), input(), int(), type(), isinstance(), round(), pow(), etc. etc. etc. etc.

    # multiple ways to check the type of a value
    if type(5) == int:
        print("it's an int!")

    if isinstance(5, int):
        print("it's an int!")

    # multiple ways to do exponents
    y = 3**2  # do not do this... ** is a python-specific operator
    y = math.pow(3, 2)
    y = pow(3, 2)

    z = round(10.2)  # rounding
    z = math.floor(10.2)  # rounding down
    z = math.ceil(10.2)  # rounding up


if __name__ == "__main__":
    main()
