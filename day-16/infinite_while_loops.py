"""
Inifinite loops are loops that never stop iterating.
Usually, this is not desireable, but sometimes it is.
"""

# infinite loop
# True is always True, so the loop will never stop iterating
while True:
    print("hello")

keep_going = True
while keep_going:
    print("hello")

# infinite loop....
# i < 10 is never False so the loop never stops iterating
i = 0
while i < 10:
    print("hello!")
    # oops... forgot to increment i!
