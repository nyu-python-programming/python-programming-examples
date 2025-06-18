"""
An example of the world-famous "accumulator" pattern, using while loops.
"""


def main():
    """
    Count iterations of a loop and stop after a specified number of iterations.
    """

    i = 0  # intial value of a accumulator/counter variable
    # keep iterating in a loop until i becomes the value 5
    while i < 5:
        print("hello")
        i = i + 1  # increment i with every cycle

    print("Done!")


if __name__ == "__main__":
    main()
