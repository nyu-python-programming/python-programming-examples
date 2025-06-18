"""
Show how to define a function that accepts multiple arguments into multiple parameter variables.
"""


def foo(x, y):
    """
    An example of a function that accepts mutliple arguments.

    Args:
        x (any type): any value of any type
        y (any type): any value of any type
    """

    if isinstance(x, str) and isinstance(y, str):
        print(f"Thank you for sharing these two strings: x='{x}' and y='{y}'.")
    elif isinstance(x, int) and isinstance(y, int):
        print(f"Thank you for sharing the integers: x={x} and y={y}.")
    elif type(x) != type(y):
        print(f"Thank you for sharing these two types of values: x='{x}' and y='{y}'.")
    else:
        print(f"Thank you for these two wonderful values, x='{x}' and y='{y}'.")


def main():
    foo("Hello", "world")  # provide 2 arguments to the function
    foo(10, 20)
    foo(True, None)
    foo(10.2, 4.1)


# call the main function if running this file directly
if __name__ == "__main__":
    main()
