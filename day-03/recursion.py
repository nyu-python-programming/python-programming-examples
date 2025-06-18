"""
An example of a stack overflow
The function foo calls itself, which calls itself, which calls itself, etc.
Eventually, your computer would run out of memory and produce a
Stack Overflow Error!
"""


def foo():
    """
    An example of a recursive function....
    A function that calls itself.
    """
    print("Hello!")
    foo()


def main():
    """
    The main starting point of the program
    """
    foo()


# only call main if we are running this file directly
if __name__ == "__main__":
    main()
