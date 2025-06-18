"""
Comparison of manually repeating some code versus automatically repeating it.
Automatically repeating allows you more easy maintenance of your code and less risk of typos, mistakes, and wasted time (and money)
"""


def what_not_to_do():
    """
    Repeat a task by simply writing the same code n number of times.
    DO NOT DO THIS!
    """
    print("\nManually repeating the same code 15 times...")
    print("hello world!")
    print("hello world!")
    print("hello world!")
    print("hello world!")
    print("hello world!")
    print("hello world!")
    print("hello world!")
    print("hello world!")
    print("hello world!")
    print("hello world!")
    print("hello world!")
    print("hello world!")
    print("hello world!")
    print("hello world!")
    print("hello world!")


def what_to_do_instead():
    """
    Repeat a task by instructing the program to repeat it.
    DO THIS INSTEAD!
    """
    print("\nAutomatically repeating the same code 15 times...")
    for i in range(15):
        print("hello world!")


if __name__ == "__main__":
    what_not_to_do()
    what_to_do_instead()
