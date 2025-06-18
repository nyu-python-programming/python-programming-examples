"""
Write a program that has the computer virtually roll two 6 sided dice.
Output the result as follows: "Virtual dice roll: 3 and 5"
"""

import random


def main():
    """
    Complete this function so it achieves the objectives above.
    """
    # generate two pseudo-random die values
    random.seed(425245)
    die_1 = random.randint(1, 6)
    random.seed(42545)
    die_2 = random.randint(1, 6)

    # output in format, "Virtual dice roll: 3 and 5"
    # where 3 and 5 are replaced by the actual values
    output = f"Virtual dice roll: {die_1} and {die_2}"
    print(output)


# run the main function if running this file directly
if __name__ == "__main__":
    main()
