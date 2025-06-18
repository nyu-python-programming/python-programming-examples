"""
Showing the special *args keyword as a parameter variable.
DO NOT USE *args in your own function definitions for any exercises or exams.
Be specific in how many arguments you want your functions to accept and give the parameter variables intuitive names.
"""


def foo(*args):
    """
    Accept all arguments into a single tuple (i.e. list-like) variable.

    Args:
        *args (tuple): All arguments bundled up together into a single tuple.
    """
    print(f"Thank you for the arguments: args={args}")


def bar(x, y, *args):
    """
    Separate two arguments but bundle up any remaining into a single tuple (i.e. list-like) variable.

    Args:
        x (any type): The first argument, of any type.  DO NOT NAME YOUR VARIABLES 'x'... use descriptive names.
        y (any type): The second argument, of any type.  DO NOT NAME YOUR VARIABLES 'y'... use descriptive names.
        *args (tuple): All arguments bundled up together into a single tuple.  DO NOT DO THIS AT HOME!
    """
    print(f"Thank you for the arguments: x='{x}', y='{y}', and args={args}.")


foo("hello", "world", "goodbye", "universe", 10, 20, 30)
bar("hello", "world", "goodbye", "universe", 10, 20, 30)

# reminder that print allows an unlimited number of arguments
# so print must use the *args technique internally in its function definition
# print(
#     "foo",
#     "bar",
#     "baz",
#     "bum",
#     "a",
#     "b",
#     "c",
#     "foo",
#     "bar",
#     "baz",
#     "bum",
#     "a",
#     "b",
#     "c",
#     "foo",
#     "bar",
#     "baz",
#     "bum",
#     "a",
#     "b",
#     "c",
#     "foo",
#     "bar",
#     "baz",
#     "bum",
#     "a",
#     "b",
#     "c",
# )
