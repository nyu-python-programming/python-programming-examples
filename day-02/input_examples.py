def print_hard_coded_value():
    x = 5  # a variable named x with a hard-coded value 5
    print(x)  # print what's in the variable named x


def print_user_input_value():
    y = input("What is your favorite number? ")
    # print("You responded with " + y + ".")
    # print("You responded with ", y, ".", sep="")
    print(
        f"You responded with {y}."
    )  # formatted string inserts a variable into the string


print_hard_coded_value()
print_user_input_value()
