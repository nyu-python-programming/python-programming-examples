"""
Example of using default parameter values.
"""


def foo(some_value_1="Hello", some_value_2="world!"):
    """
    Example of a function that accepts multiple arguments with default values.

    Args:
        some_value_1 (any type): any value of any type... defaults to 'Hello'.
        some_value_2 (any type): any value of any type... defaults 'world!'.

    """
    print(f"Thank you for these two values, '{some_value_1}' and '{some_value_2}'.")


# provide no arguments... the defaults will be used, if any
foo()

# provide one argument... the second parameter variable will be default value
foo("Goodbye")

# provide two arguments... both parameter variables are customized
foo("Goodbye", "universe!")
