"""
Example showing the concept of the call stack.
"""


def function_1():
    print("Function 1 start.")
    function_2()
    print("Function 1 end.")


def function_2():
    print("Function 2 start.")
    function_3()
    print("Function 2 end.")


def function_3():
    print("Function 3 start.")
    print("Function 3 end.")


def main():
    print("Main start")
    function_1()  # call 'function_1'
    function_2()  # call 'function_2'
    print("Main end")


# start the program by calling main
# only call main if we are running this file directly
if __name__ == "__main__":
    main()
