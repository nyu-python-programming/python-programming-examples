"""
A student grade management system, intended to explore some uses of Python lists.
"""

from pathlib import Path


def remove_line_breaks_from_list_of_strings(list_of_strings):
    """
    Remove line breaks from every value in a list of strings.

    Args:
        list_of_strings(list): A list of strings
    Returns:
        list: The same set of values, with line breaks removed from each.
    """

    i = 0  # initialize counter
    for string_value in list_of_strings:
        # reassign the student variable to point to something different
        string_value = string_value.strip()
        list_of_strings[i] = string_value  # store the new value in the list
        i = i + 1  # increment the counter
    # the loop is done
    return list_of_strings  # return updated list


def open_file_correctly(filepath, mode="r"):
    """
    Open any file in a platform-agnostic manner.

    Args:
        filepath(str): The file path to open, in either Windows or Mac/Unix/Linux form.
        mode(str): The mode, either 'r', 'w', or 'a'.

    Returns:
        TextIOWrapper: The opened file in read mode with utf-8 encoding.
    """
    # platform-agnostic file paths that work on any system
    filepath = Path(filepath).resolve()
    file_object = open(filepath, mode=mode, encoding="utf-8")
    return file_object


def write_student_data_to_files(students, grades):
    """
    Writes student names and grades to the correct data files.

    Args:
        students(list): A list of student names.
        grades(list): A list of student grades.
    """

    # save the changes to files
    # open the files in read mode first
    students_file = open_file_correctly("data/students.txt", mode="w")
    grades_file = open_file_correctly("data/grades.txt", mode="w")

    # save the student list to the file
    for student in students:
        students_file.write(student + "\n")
    students_file.close()  # be polite, close your file when done

    # save the grades list to the file
    for grade in grades:
        grades_file.write(grade + "\n")
    grades_file.close()  # be polite, close your file when done


def print_menu():
    """
    Prints a menu of options for the user.

    Returns:
        int: The menu option the user picked or -1 if the user said to 'stop'.
    """

    print(
        """
Welcome to the student management application.
          
Please select from the following options (enter 'stop' to quit the program):
1. Look up a student's grade.
2. Remove a student from the course
3. Add a student.
"""
    )

    keep_going = True
    while keep_going:
        # ask for the user's choice
        response = input("Which option would you like? ")
        if response.isnumeric() and int(response) >= 1 and int(response) <= 3:
            # they entered a valid menu choice
            keep_going = False
            choice = int(response)
        elif response == "stop":
            # they want to quit
            keep_going = False
            choice = -1  # hard-coded stop indicator
    # we must have a good integer now
    return choice


def lookup_grade(students, grades):
    """
    Get a student's grade by their name.

    Args:
        students(list): A list of student names.
        grades(list): A list of student grades.

    Returns:
        str: The grade for the given student.
    """

    keep_going = True  # the flag that controls our loop
    stop_word = "stop"  # this is the word the user can enter to stop iterating
    annoyance_level = 0  # start off not annoyed at all!  good advice.

    # iterate until the flag becomes False
    while keep_going:
        # ask the user to enter a student's name
        name = input("Which student's grade would you like to see? ")

        # validate the name...
        if name in students:
            # the name exists in the list, continue...

            # get the index position of the given name in the students list
            position = students.index(name)  # should be called "find"!
            # get the grade at the same position in the grades list
            grade = grades[position]

            # print out the grade for this student
            print(f"The student, {name}, scored a {grade}.")
        elif name.lower() == stop_word:
            # the user wants to stop iterating
            print("Ok... stopping...")
            # set the flag to False so the loop quits before next iteration
            keep_going = False
        else:
            # the name does not exist in the list....
            if annoyance_level == 0:
                print(f"Sorry, the name, {name}, is not known to us!")
            elif annoyance_level > 0 and annoyance_level < 3:
                print(f"Sorry, once again, the name, {name}, is not known to us!")
            elif annoyance_level >= 3:
                print(
                    f"For the {annoyance_level}th time, the name, {name}, is not in our class!  Use better names!"
                )

            annoyance_level = annoyance_level + 1  # increasingly annoyed


def remove_student(students, grades):
    """
    Remove a student from our roster (and the corresponding grade)

    Args:
        students(list): A list of student names.
        grades(list): A list of student grades.

    """
    # ask the user for a student name
    name = input("Which student would you like to remove? ")

    # validate the name
    if name in students:
        # find the position of that name in the list of names
        # the position at which the name occurs in the list
        position = students.index(name)
        students.remove(name)  # remove the name from the students list
        grades.pop(position)  # remove the respective grade from the grades list
        # print(students, grades)

        # save the changes to files
        write_student_data_to_files(students, grades)

    else:
        # the name does not exist in our list
        print("Sorry, I don't recognize that name.")


def add_student(students, grades):
    """
    Add a student to our roster (and a corresponding grade)

    Args:
        students(list): A list of student names.
        grades(list): A list of student grades.
    """
    # ask the user for a student name
    name = input("What is the name of the student you would like to add? ")
    grade = input(f"What is {name}'s grade? ")

    # update the lists
    students.append(name)  # add the new name to the students list
    grades.append(grade)  # add the new grade to the students list

    # save the changes to files
    write_student_data_to_files(students, grades)


def main():
    # platform-agnostic file paths that work on any system
    students_file = open_file_correctly("data/students.txt")
    grades_file = open_file_correctly("data/grades.txt")

    # the .readlines function includes line breaks at the end of every string in the list
    students = students_file.readlines()  # get a list of students from the file
    grades = grades_file.readlines()  # get a list of grades from the file

    # remove line breaks from each string in the lists
    students = remove_line_breaks_from_list_of_strings(students)
    grades = remove_line_breaks_from_list_of_strings(grades)

    # repeatedly ask the user to do something
    keep_going = True  # a flag
    # loop as long as the flag is True
    while keep_going:
        # ask the user what they would like to do
        choice = print_menu()

        if choice == 1:
            # they want to look up a student's grade
            lookup_grade(students, grades)
        elif choice == 2:
            remove_student(students, grades)
        elif choice == 3:
            add_student(students, grades)
        # the print_menu function returns -1 if the user entered 'stop'
        elif choice == -1:
            # the user wants to quit
            keep_going = False  # change the flag value

    print("Bye!")


# run the main function if running this file directly
if __name__ == "__main__":
    main()
