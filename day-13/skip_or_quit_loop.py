"""
Showing the 'break' and 'continue' keywords available within any loop.
"""


def main():
    # using the 'break' keyword in a loop
    # is almost always (but not always) a sign of bad code
    # try to design the loop to iterate the number
    # of times you want, so you don't need it
    for i in range(10):
        print(i)
        if i == 7:
            break  # stop iterating
    print("Done!")

    # using 'continue' keyword in a loop
    # is also usually not necessary but can be in some circumstances....
    # just use a custom step in a range to avoid certain numbers
    # if possible... in some cases 'continue' is useful.
    for i in range(0, 10):
        if i == 7 or i == 8:
            continue  # skip to the next value of i
        print(i)

    print("Done!")


# run the main function if running this file directly
if __name__ == "__main__":
    main()
