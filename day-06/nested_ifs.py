''''
Exhibition of nested if/elif/else logical blocks.
'''

def simple_version():
    '''
    Ask the user for a number in a specific range... and do some appropriate output.
    '''
    # ask the user to enter a number in a specific range
    response = input("Enter a number between 1 and 100: ")

    # check whether what the user entered is even a number
    if response.isnumeric():

        # convert it to a number.... so we can later do numeric comparisons
        num = int(response) # this is safe to do, since we know the string is numeric

        # check it is a number in the correct range
        if num >= 1 and num <= 100:
            print("Good input...") # yes, it's in the correct range

            # check whether it is between 1 and 50 inclusive
            # if num >= 1 and num <= 50: # checking >= 1 is redundant
            if num <= 50:
                # the user entered a number <= 50
                print(f"You entered {num}, which is a number below 51.")
            else:
                # the user entered a number > 50
                print(f"You entered {num}, which is a number over 50!")
        else:
            # the user entered a number outside of our desired range
            print(f"Sorry, the number {num} is not in the desired ranfge.")
    else:
        # the user entered somethign non-numeric
        print("You messed up... you entered something non-numeric! Bye!")



def compressed_version():
    '''
    A second version showing how to reduce the levels of nested if/elif/else logic.
    Same output.
    '''
    # ask the user to enter a number in a specific range
    response = input("Enter a number between 1 and 100: ")

    # a shortcut version
    # do the numeric checks all in one if statement
    if response.isnumeric() and int(response) >= 1 and int(response) <= 100:
            print("Good input...") # yes, it's in the correct range

            # convert it to a number.... so we can later do numeric comparisons
            num = int(response) # this is safe to do, since we know the string is numeric

            # check whether it is between 1 and 50 inclusive
            # if num >= 1 and num <= 50: # checking >= 1 is redundant
            if num <= 50:
                # the user entered a number <= 50
                print(f"You entered {num}, which is a number below 51.")
            else:
                # the user entered a number > 50
                print(f"You entered {num}, which is a number over 50!")

    else:
        # the user entered somethign non-numeric
        print("You messed up... you entered something non-numeric! Bye!")


def main():
    # run both versions
    simple_version()
    compressed_version()

# run the main function
if __name__ == '__main__':
    main()
