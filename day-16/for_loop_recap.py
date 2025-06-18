"""
Recap of what we have discussed regarding for loops.
Generally, use for loops instead of while loops when iterating through a
predetermined finite sequence of values.
"""

from pathlib import Path

# make this path work on all computer operating systems.
filepath = Path("data/Voting_Poll_Sites_20250618.csv").resolve()

# various SEQUENCE data types can be iterated through with a for loop
w = "hello world!"  # string
x = [1, 2, 3, None, True, "hello"]  # list
y = ("hello", "world")  # tuple (like a list)
z = range(1, 10, 2)  # range (like a list)
f = open(filepath, mode="r", encoding="utf-8")  # TextIOWrapper (i.e. a file)

# iterate through the characters in a string
for c in w:
    print(c)

# iterate through the values in a list
for val in x:
    print(val)

# iterate through the words in a tuple
for word in y:
    print(word)

# iterate through the numbers in a range
for num in z:
    print(num)

# iterate through the lines of a file
for line in f:
    line = line.strip()  # remove line break at end of each line
    print(line)
