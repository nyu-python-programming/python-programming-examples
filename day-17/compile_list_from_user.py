"""
Asks the user to enter a new word over and over again.
If the user says 'stop', we stop asking and print out the list of words.
"""


def main():
    words = []  # start with an empty list.

    # set a flag's initial value to True so the loop starts iterating
    keep_going = True
    while keep_going:
        # ask the user to enter a word
        word = input("Enter a word: ")
        # if the user enters the word 'stop', we change the flag value so the loop will quit
        if word.lower().strip() == "stop":
            keep_going = False  # change flag value
        else:
            # the user entered a valid word, so add it to the list
            words.append(word)  # add it to the list!

    print(f"The words you entered are: {words}.")


# call the main function if running this file directly.
if __name__ == "__main__":
    main()
