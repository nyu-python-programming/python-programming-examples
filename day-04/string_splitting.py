'''
An example showing how to break up a string into a list.
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

    # clean up a little first so we can analyze it more easily
    revised_poem = poem.replace('\n', ' ')
    revised_poem = revised_poem.replace('--', ' ')
    revised_poem = revised_poem.replace(';', '')
    revised_poem = revised_poem.replace('.', '')
    revised_poem = revised_poem.replace('?', '')
    revised_poem = revised_poem.replace(',', '')
    revised_poem = revised_poem.lower()


    # split by space to separate the words
    word_list = revised_poem.split(' ')

    # the tenth word in the separated version
    tenth = word_list[9]
    print(f"The tenth word in the poem is '{tenth}'.")

    print() # blank line
    print(word_list)

# if running this file directly, run the main function
if __name__ == '__main__':
    main()