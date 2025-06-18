'''
Recap of some boolean basics.
'''

def boolean_examples():
    ''' 
    Using the and, or, not, ==, and != operators.
    '''

    print("\nBoolean comparisons:\n")
    # boolean basic operators
    x = True
    y = False

    print(x and y) # False
    print(x or y) # True
    print(x == y) # False
    print(x != y) # True
    print(not x) # False
    print(not y) # True

def numeric_examples():
    '''
    Using the <, <=, >, >= operators.
    '''

    print("\nNumeric comparisons:\n")
    # numeric comparisons operators
    x = 5
    y = 10

    print( x == y ) # False
    print( x != y ) # True
    print( x < y ) # True
    print( x <= y ) # True
    print( x > y ) # False
    print( x >= y ) # False

def main():
    '''
    The main logic of the program... simply calling the two other functions.
    '''
    boolean_examples()
    numeric_examples()

# if this file is being run direclty, run the main function
if __name__ == '__main__':
    main()
