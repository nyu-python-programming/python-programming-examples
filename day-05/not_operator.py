'''
Showing a bit more about boolean operators and expressions, including the != and not operators.
'''

def main():
    '''
    The main logic of the program.
    '''

    name = input("What's your name? ")

    if name == 'Bob':
        print('Hello, Bob!')

    if name == 'Sheila':
        print("Hey, Sheila!")

    # check if the name is NOT Bob
    if name != 'Bob':
        print("You're not Bob!")

    # check if the name is NOT Sheila
    if name != 'Sheila':
        print("Wait... you're not Sheila!")

    # check if the name is NOT in a list of names
    if name not in ['John', "Jane", 'Herbert', 'Herberta']:
        print("Who are you?!")

    if name in ['Bob', 'Sheila', 'Iris']:
        print("I know you!")


# if running this file directly, call the main function
if __name__ == '__main__':
    main()
