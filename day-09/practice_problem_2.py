"""
Write a program that asks the user to supply two words.
Sort the words in size order and print them back to the user.
"""


def main():
    """
    Complete this function so the program achieves the goals above
    """

    word1 = input("Give a word: ")
    word2 = input("Give another word: ")
    word1_length = len(word1)
    word2_length = len(word2)

    # determine which word is shorter
    if word1_length < word2_length:
        # print word 1 first, since it's shorter
        print(word1)
        print(word2)
    elif word1_length == word2_length:
        # they are the same length... sort alphabetically
        if word1 < word2:
            print(word1)
            print(word2)
        else:
            print(word2)
            print(word1)
    else:
        # print word 2 first, since it's shorter
        print(word2)
        print(word1)


# if running this file directly, call the function
if __name__ == "__main__":
    main()
