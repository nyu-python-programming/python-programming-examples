'''
Determine what day it is today and print out an appropriate message.
This example uses the datetime module to determine the day today.
'''

# datetime is one of the many default modules included with the Python language
import datetime

def main():
    '''
    The main logic of the program.
    '''

    # determine the day today
    # day of the week as an integer, starting from 0 for Monday
    day_today = datetime.datetime.today().weekday() 
    print(f"The day today (in int form) is {day_today}.")

    # do different actions each day
    if day_today == 0:
        print("Today is Monday!")
    elif day_today == 1:
        print("Today is Tuesday.")
    elif day_today == 2:
        print("Today is Wednesday.")
    else:
        print("Today is later than Wednesday....")

    # check if today is a weekday
    # if day_today == 0 or day_today == 1 or day_today == 2 or day_today == 3 or day_today == 4: # the hard way
    # if day_today >= 0 and day_today < 5: # unnecessary to check for >=0... the weekday function always provides a number >=0
    if day_today < 5: # the easy way
        # this will print on any weekday
        print("Today is a weekday!")

    # check if today is a weekend
    if day_today == 5 or day_today == 6:
        # this will print on Saturdays and Sundays
        print("Today is a weekend!")

    # check if today is both tuesday and wednesday
    if day_today == 1 and day_today == 2:
        # this will never be printed out, because the logical expression is never True
        print("Today is both Tuesday and Wednesday... it's magic!")

    # another example showing the non-exlclusive nature of the or operator
    is_intro_course = True
    is_nyu_course = True

    # the 'or' operator is non-exclusive... 
    # ... meaning if both operands are True, the entire expression will still be true
    if is_intro_course or is_nyu_course:
        print("This is an intro course OR an NYU course.... or both.")

    print("Done!")


# run the main function, if this file is being run directly
if __name__ == '__main__':
    main()
