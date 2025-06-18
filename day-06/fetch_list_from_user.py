'''
Ask the user to enter a list of values.... rather we ask them to enter a set of values with a separator.
Then we slice or split the input by that separator to create a list.
using the .split() function that exists in all strings.
'''

# foo = ' beet '
# foo = foo.strip() # 'beet'

def main():
    # get the vegetables the user likes
    response = input("Enter a list of vegetables you like made into soup (separated by commas): ")

    # split the repsonse into a list
    user_vegetables = response.split(",") # the split function chops up the string into a list by the separator you indicate

    # remove the leading or trailing whitespaces from each value in the list
    # DO NOT DO THIS ON AN EXAM!  THIS "LIST COMPREHENSION" TECHNIQUE IS BEYOND THE SCOPE OR INTEREST OF THIS COURSE!
    user_vegetables = [x.strip() for x in user_vegetables]

    print(user_vegetables)

def alternative_way():
    '''
    An alternative way to create a list from multiple user inputs.
    This only works for a finite number of inputs pre-determined in the code.
    '''
    # ask the user to enter multiple inputs... this is good for finite inputs
    input1 = input("Enter a vegetables you like made into soup: ")
    input2 = input("Enter a vegetables you like made into soup: ")
    input3 = input("Enter a vegetables you like made into soup: ")
    input4 = input("Enter a vegetables you like made into soup: ")
    input5 = input("Enter a vegetables you like made into soup: ")

    # group those together into a list
    user_vegetables = [input1, input2, input3, input4, input5]
    print(user_vegetables)


# call the main function
if __name__ == '__main__':
    main()


