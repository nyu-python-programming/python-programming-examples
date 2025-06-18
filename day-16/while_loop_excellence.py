"""
Recap of what we have discussed regarding while loops.
Generally, use while loops when iterating an indeterminate unknown
number of times.
"""

import random

# keep iterating until the user gives in and says, 'hello'!
response = ""
while response != "hello":
    response = input("Say 'hello'! ")

# same thing, but using a flag to control the loop
is_good = False  # start the flag variable as False
while not is_good:
    response = input("Say 'hello'! ")
    if response == "hello":
        is_good = True  # set the flag to True if the response is good

# same thing with reverse logic
is_bad = True  # start the flag variable as True
while is_bad:
    response = input("Say 'hello'! ")
    if response == "hello":
        is_bad = False  # set the flag to False if the response is good

# keep iterating until a pseudo-random number is a 7
num = 0
while num != 7:
    num = random.randint(1, 10)
