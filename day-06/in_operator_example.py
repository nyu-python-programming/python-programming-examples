'''
Example of checking user input against values in a list.
'''

def main():
    # make a list of acceptable responses from the user
    acceptable_foods = ['beet', 'beets', 'sweet potato', 'sweet potatoes', 'yam', 'yams'] # list of values

    # get input from the user
    veg = input("What's your favorite food? ")

    # convert the user's input to lowercase
    veg = veg.lower()

    # check whether what the user typed is one of the values in the list
    # no easy way to accommodate plural forms or variations of the values in the list
    if veg in acceptable_foods:
        # the value the user entered is in our list!
        print("You can make a great soup from that!")
    else:
        # the value the user entered is not in our list
        print("That's not good for soup!")

# run the main function, if running this file directly
if __name__ == '__main__':
    main()

