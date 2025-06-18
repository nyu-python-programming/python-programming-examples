'''
Introducing the boolean data type!
The function main is called.  The main function then calls the check_types function.
The check_type function then prints out some messages showing the type of two boolean values.
'''

def check_types():
    '''
    Create two variables, each referring to boolean values.
    Print out the values and their data type.
    '''

    x = True
    y = False
    print(f"The data type of {x} is {type(x)}")
    print(f"The data type of {y} is {type(y)}")

def main():
    '''
    Call the check_types function.
    '''
    check_types()

# if we are running this file directly, call the main function
print(f"hello, the __name__ variable in truthy.py has the value '{__name__}'.")
if __name__ == '__main__':
    main()
