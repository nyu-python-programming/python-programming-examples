"""
A warning about declaring a variable inside a conditional block.
Avoid doing so.
"""

import random

num = random.randint(1, 10)

# declare the keep_going variable only if the num is 7... BAD IDEA!
if num == 7:
    keep_going = False

# this will crash on average 9 out of 10 times you run the program
# since keep_going will not have been declared or assigned a value
print(keep_going)
