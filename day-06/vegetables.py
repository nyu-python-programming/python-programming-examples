'''
A simple exhibition of if/elif/else decision-making
'''

def do_veggie_stuff():
    '''
    Decide what to do, based on user input.
    Following the logic diagrammed at https://knowledge.kitchen/content/courses/intro-to-programming/flow-charts/
    '''

    # start

    # ask user for favorite vegetable
    veg = input("What's your favorite vegetable? ")

    # convert what the user typed to lowercase to make comparisons case insensitive
    veg = veg.lower()

    # check whether it is a "beet"
    # if veg == 'beet' or veg == 'Beet' or veg == 'BEET': # this is not a great solution
    # if veg == 'beet': # good, but only works for exact matches
    # if veg.count('beet') >= 1: # fine
    if veg.find('beet') >= 0: # another fine solution
        # if so, do some beet-specific output
        print("You can make borsh... it's delicious!")

    # if not, check whether it is a "carrot"
    # elif veg == 'carrot' or veg == 'Carrot' or veg == 'CARROT':
    # elif veg == 'carrot':
    elif veg.find('carrot') >= 0:
        # if so, do some carrot-specific output
        print("You can make carrot cake... my favorite cake!")

    # if not, check whether it is 'arugula', a.k.a. 'rocket'
    # this was not in the diagram originally, but we've added it to show that you can have 
    # multiple elif blocks if you wish
    # elif veg == 'arugula' or veg == 'Arugula' or veg == 'ARUGULA':
    # elif veg == 'arugula':
    elif veg.find('arugula') >= 0:
        # if so, do something rocket-specific
        print("This is certainly bitter...")

    # this will be evaluated before we evaluate the search for 'potato'
    # treat 'sweet potato' the same as 'yam'
    elif veg.find('sweet potato') >= 0 or veg.find("yam") >= 0:
        print("Sweet potato or yams make a great soup.")

    # this will match 'potato', 'potatoes', and (possibly incorrectly) 'sweet potato'
    elif veg.find('potato') >= 0:
        print("Fry them up!")

    # if not, do some default vegetable output
    else:
        # by default print something
        print("I don't know what you can do with that!")

    # check the length of the vegetable name
    # this is an independent check... disconnected to any earlier decision-making
    # this is not in the flow diagram this code is based on, but we're adding it for educational purposes
    if len(veg) < 10:
        print("That's a short vegetable name!!!!")

    # print end message
    print("Thank you.  Bye!")

    # done!

def main():
    do_veggie_stuff()


# call the main function, if running this file directly
if __name__ == '__main__':
    main()