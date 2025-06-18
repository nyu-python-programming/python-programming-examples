"""
A little bit about the built-in __name__ variable in Python.
You don't make it yourself or assign it a value yourself.
It is automatically assigned the value '__main__' if this file is being run directly.
"""

print(
    __name__
)  # will either print '__main__' or 'the_name_variable', depending on whether this file is being run directly or not

# check whether this file is being run directly
if __name__ == "__main__":
    # print 'Hoorah!' if this file is being run directly
    print("Hoorah!")
