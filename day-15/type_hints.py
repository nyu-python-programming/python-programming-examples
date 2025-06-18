"""
An example of using type hints in Python.
Nothing useful in this example, just focusing on type hint syntax.
"""

# a variable can store any type of data in Python
# ... it's a loosely-typed language
x: bool = True
x: int = 4
x: str = "Hello"

x: int = "hello"
y: str = "3"
z: int = x + y  # oops!


def foo(bar: str) -> int:
    """
    A function that shows type hints in Python.
    Note that the argument is expected to be a string and the return type is an integer.
    """
    print(int(bar))  # what if it can't be converted to an int?
    return 4  # return an int, as expected


# call the method with a few different data types

# this is a string and can be converted to an int... it works as expected
foo("4")

# this is an int, not as expected in the type hints of the function...
# when using type hints, you can set the interpreter to warn you about this or fail on this
foo(4)
