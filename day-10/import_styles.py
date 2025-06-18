"""
Showing the two different ways of importing modules...
"""

# option 1... recommended in most cases... avoids any possibility of a naming conflict
import math
import random
import datetime

x = math.pow(10, 2)
y = random.randint(10, 100)
z = datetime.datetime.weekday(datetime.datetime.today())
print(x, y, z, sep=",")

# option 2... recommended if looking for ultimate convenience and there are no name conflicts
# from math import pow
# from random import randint
# from datetime import datetime

# x = pow(10, 2)
# y = randint(10, 100)
# z = datetime.weekday(datetime.today())
# print(x, y, z, sep=",")
