'''
This file contains some examples that review and recap what we 
have covered in previous lectures.
'''

def say_hello():
    '''
    Prints out a welcome message!
    '''
    # print to the command line a greeting
    message = "Hello world!"
    print(message)

def say_goodbye():
    '''
    Prints a warm parting message.
    '''
    message = "It's so good to have seen you.  Bye!"
    print(message)

def main():
    '''
    This is the "entry-point" function...
    in other words, the first function that is called in this program.
    '''
    # call (also known as "invoke" or "run") the functions
    say_goodbye()
    say_hello()

# check what's in the built-in variable named __name__
print(f"The __name__ built-in variable has the value '{__name__}'.")
# only call main if we are running this file directly
if __name__ == '__main__':
    main()