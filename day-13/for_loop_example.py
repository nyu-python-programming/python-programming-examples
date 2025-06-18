"""
Examples of for loops either using or not using the value of the variable
assigned automatically by the for loop.
"""

from suffix_generator import generate_ordinal_suffix


def iterate_and_ignore_value(start, stop, step):
    """
    Iterate a specific number of times and perform
    the exact same action or outcome each time.
    """
    for i in range(start, stop, step):
        print("hello world!")  # action!


def iterate_and_use_value(start, stop, step):
    """
    Iterate a specific number of times and perform
    slight variations of the same action or outcome each time.
    """
    for i in range(start, stop, step):
        suffix = generate_ordinal_suffix(i)
        print(f"hello world for the {i}{suffix} time!")


def main():
    print("\nIterate not using the value of the variable: ")
    iterate_and_ignore_value(0, 10, 2)

    print("\nIterate and use the value of the assigned variable: ")
    iterate_and_use_value(1, 10, 1)


if __name__ == "__main__":
    main()
