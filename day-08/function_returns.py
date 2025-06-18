def foo():
    print("foo: Hello world!")
    # return None by default


def bar():
    return "bar: Hello world!"


def baz():
    print("baz: Hello world!")
    return "baz: Hello world!"


def main():
    print("\nCalling each function...")
    # call each function
    foo()
    bar()
    baz()

    print("\nCalling each function and printing its return value...")
    # call each function, and print its returned value
    x = foo()
    print(f"foo returned '{x}'")

    y = bar()
    print(f"bar returned '{y}'")

    z = baz()
    print(f"baz returned '{z}'")


# call the main function if running this file directly
if __name__ == "__main__":
    main()
