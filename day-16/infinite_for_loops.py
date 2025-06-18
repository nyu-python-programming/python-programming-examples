"""
Yes, it is possible to create an infinite loop
using the for loop technique.
"""

# an infinite loop using the for keyword
# it's easier to create an infinite loop with the while keyword
values = [1, 2, 3]  # a list to start with
for i in values:
    print("hello")
    values.append(i + 1)  # add a new value to the end of the list
