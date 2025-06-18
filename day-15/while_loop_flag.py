"""
An example of the world-famous "flag" pattern, using while loops.
"""

import random


def main():

    # intialize a "flag" variable, i.e. a variable that stores true or false
    keep_going = True

    # keep iterating in a loop until the flag has a False value
    while keep_going:
        print("hello")

        # randomly decide whether to continue
        # we have a 1 in 10 chance of stopping after any iteration
        num = random.randint(1, 10)

        # if the pseudo-random number is a 7, set the flag to False to cause the loop to stop iterating
        if num == 7:
            keep_going = False

    print("Done!")


if __name__ == "__main__":
    main()
