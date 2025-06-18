def foo():
    print("Hello world without a line break", end="")
    print(
        "Hello",
        "world",
        "with",
        "a",
        "custom",
        "separator",
        "and",
        "a",
        "question",
        "mark at the end",
        sep="-",
        end="?\n",
    )
    print("Hello world!")  # prints "Hello world!" with a line break attached at the end
    print("\n" in "Hello world!")  # line break is not in "Hello world!"
    print("Hello world!", end="")


# define a function called 'main'
def main():
    print("Hello world!")
    print("Hello", "world!")
    print("Hel", "lo", " ", "wo", "rld!", sep="")
    print("Hello\nworld!")
    print("Hello\tworld!")


# call the main function
# main()
foo()
