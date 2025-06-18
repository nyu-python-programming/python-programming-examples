"""
A recap of what we know about functions so far.
"""

# import any modules we use in our code


def foo():
    """
    Function definition... no parameter variables, no return value.
    """
    message = "Welcome back to class!"
    print(message)


def bar(adj, noun, num):
    """
    Function definition... three parameter variables, no return value.

    Args:
        adj (string): An adjective.
        noun (string): A noun.
        num (int): A number.
    """

    mad_lib = f"{num} {adj} {noun} walked into a bar..."
    print(mad_lib)


def main():
    # function call
    foo()
    bar("pretty", "skates", 10)


# run the main function, if running this file directly
if __name__ == "__main__":
    main()
