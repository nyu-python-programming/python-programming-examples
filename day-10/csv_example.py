import csv  # helps parse CSV files

# the pathlib module helps overcome differences in file paths on different operating systems
# for example, on Mac OS and UNIX/Linux the data file path is data/students.csv
# on Windows the same file path would be data\students.csv

from pathlib import Path

# generate a valid file path for your operating system
filepath = Path("data/students.csv").resolve()

# open the file in read mode
f = open(filepath, mode="r", encoding="utf-8")

# parse (i.e. break down into usable form) the file and convert each row to a Dictionary
reader = csv.DictReader(f)

# loop through every row in the file
print("\nStudents and their exam average scores:")
for row in reader:
    # for every row, print out the full name, followed by the exam average score
    full_name = f"{row['First']} {row['Last']}"
    print(f"- {full_name}: {row['Exam Average']}")
