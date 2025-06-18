def foo(x="hello", y="world"):
    print(f"Thank you for these values, x='{x}' and y='{y}'.")


def main():
    foo()  # this will use the default values for x and y
    foo(10)  # this will set x=10 and the default for y
    foo(10, 20)  # this will set x=10 and y=20

    # THIS IS FINE... THE ARGUMENT ORDER IS THE SAME AS THE PARAMETER VARIABLE ORDER
    foo(x=10, y=20)  # this will set x=10 and y=20 as you can see

    # DO NOT DO THIS AT HOME!  USE ARGUMENTS IN THE SAME ORDER AS THE PARAMETER VARIABLES
    foo(y=10, x=20)

    # reminder that print can be called with a few special named arguments
    print("hello", "world", sep="-", end="?\n")
    print("hello world", end="?\n")


# call the main function if running this file directly
if __name__ == "__main__":
    main()
