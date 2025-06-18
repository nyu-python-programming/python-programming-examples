'''
Various techniques for defining strings in Python.
'''

def main():
        
    # examples of defining a string
    vegetable = 'arugula'
    vegetable = "arugula"
    vegetable = '''arugula'''
    vegetable = """arugula"""

    # two_lines = 'Line one
    # Line two'
    two_lines = '''Line one
    Line two'''

    # phrase = 'I'm hungry!'
    phrase = "I'm hungry!"

    # sentence = "She said, "I'm hungry!"."
    # sentence = 'She said, "I'm hungry!".'
    sentence = '''She said, "I'm hungry!".'''

    # instruction = "The instructor said, "It's ok to use three single quotes, i.e. ''', to delimit a string."."
    # instruction = 'The instructor said, "It's ok to use three single quotes, i.e. ''', to delimit a string.".'
    # instruction = '''The instructor said, "It's ok to use three single quotes, i.e. ''', to delimit a string.".'''
    instruction = """The instructor said, "It's ok to use three single quotes, i.e. ''', to delimit a string."."""

    print(instruction)

# run the main function if this file is being run directly
if __name__ == '__main__':
    main()