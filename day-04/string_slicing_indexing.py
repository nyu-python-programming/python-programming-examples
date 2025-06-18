'''
An example showing indexing and slicing and maybe some other stuff.
'''

def main():

    # The Raven, by Edgar Allen Poe
    poem = '''
    ONCE upon a midnight dreary, while I pondered, weak and weary,
    Over many a quaint and curious volume of forgotten lore,
    While I nodded, nearly napping, suddenly there came a tapping,
    As of some one gently rapping, rapping at my chamber door.
    "'Tis some visiter," I muttered, "tapping at my chamber door--
    Only this, and nothing more."
    Ah, distinctly I remember it was in the bleak December,
    And each separate dying ember wrought its ghost upon the floor.
    Eagerly I wished the morrow;--vainly I had sought to borrow
    From my books surcease of sorrow--sorrow
    '''

    # indexing... accessing a specific character in the string by its position, starting from zero
    twelvth_character = poem[11] # get the 12th character
    print(twelvth_character)

    # slicing... retrieving a subset of the characters by positional range
    twelvth_thru_sixteenth_characters = poem[11:17]
    print(twelvth_thru_sixteenth_characters)

    # this variable name is too long... you can do better!
    twelvth_thru_sixteenth_characters_skipping_by_twos = poem[11:17:2]
    print(twelvth_thru_sixteenth_characters_skipping_by_twos)

    # get a subset in reverse
    sixteenth_thru_twelvth = poem[16:11:-1]
    print(sixteenth_thru_twelvth)

    # the whole thing, backwards!
    print(poem[::-1])

# if running this file directly, run the main function
if __name__ == '__main__':
    main()