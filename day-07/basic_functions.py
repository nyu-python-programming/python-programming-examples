"""
Show how to call a random function a random number of times.
"""

import random


# function definition with the name 'main'
def foo():
    """
    Print out some nonsense text, 'Foo!'
    """
    print("Foo!")


def bar():
    """
    Print out some nonsense text, 'Bar!'
    """
    print("Bar!")


def baz():
    """
    Print out some nonsense text, 'Baz!'.
    """
    print("Baz!")


def main():
    # generate a pseudo-random number between 1-3, inclusive
    function_num = random.randint(1, 3)

    # generate a pseudo-random number between 1-10 inclusive
    repetition_num = random.randint(1, 10)

    print(f"Calling function #{function_num} {repetition_num} times...")

    if function_num == 1:
        # call the 'foo' function the number of times in repetition_num
        for i in range(repetition_num):  # we will discuss this line of code LATER
            foo()
    elif function_num == 2:
        # call the 'bar' function the number of times in repetition_num
        for i in range(repetition_num):  # we will discuss this line of code LATER
            bar()
    elif function_num == 3:
        # call the 'baz' function the number of times in repetition_num
        for i in range(repetition_num):  # we will discuss this line of code LATER
            baz()


# if this file is being run directly, run the main function
if __name__ == "__main__":
    main()
