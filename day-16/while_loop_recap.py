"""
Recap of what we have discussed regarding while loops.
Generally, DO NOT USE while loops when iterating through a
predetermined finite sequence of values, use for loops instead.
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
i = 0
while i < len(w):
    c = w[i]  # grab the character at position i from the string
    print(c)
    i = i + 1  # increment i

# iterate through the values in a list
i = 0
while i < len(x):
    val = x[i]  # grab the value at position i from the list
    print(val)
    i = i + 1  # increment i

# iterate through the words in a tuple
i = 0
while i < len(y):
    word = y[i]  # grab the value at position i from the tuple
    print(word)
    i = i + 1  # increment i

# iterate through the numbers in a range
i = 0
while i < len(z):
    num = z[i]  # grab the value at position i from the range
    print(num)
    i = i + 1  # increment i

# iterate through the lines of a file
lines = f.readlines()  # get a list of lines from the file
i = 0
while i < len(lines):
    line = lines[i]  # grab the value at position i from the list
    line = line.strip()  # remove line break at end of each line
    print(line)
    i = i + 1
