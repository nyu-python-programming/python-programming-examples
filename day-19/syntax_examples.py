"""
An example of storing student quiz scores in a dictionary and doing some computation on them.
Each student's quiz scores are stored as a list.
"""

# make a list
# foo = ["foo", "bar", "baz"]
# x = foo[1]  # retrieve the value at the index position 1
# print(x)

# make a dictionary with integers as its keys
# foo = {0: "foo", 2: "baz", 1: "bar"}
# x = foo[1]  # retrieve the value with the key 1... not necessarily the position 1
# print(x)


def drop_lowest_score(scores):
    """
    Drop the lowest value from a list.

    Args:
        scores(list): A list of quiz scores for a single student.

    Returns:
        list: The same list with the lowest value removed.
    """
    lowest_score = min(scores)  # get the lowest score
    scores.remove(lowest_score)  # remove that value
    return scores


def get_class_average(quiz_scores):
    """
    Calculate the overall average performance of all students on all quizzes.

    Args:
        quiz_scores(dict): A dictionary, where every value is a list of a single student's scores on the quizzes.

    Returns:
        int: The average score of all student across all quizzes, rounded.
    """

    # make a dictionary with lists as its values
    # get all the values from the dictionary, ignoring the keys
    all_scores = quiz_scores.values()
    # the data structure of all_scores is like a two-dimensional list
    # [
    #     [80, 99, 72, 58],
    #     [99, 97, 99, 50],
    #     [12, 22, 99, 99],
    #     [75, 75, 75, 2],
    # ]

    overall_total = 0
    student_counter = 0

    # iterating through each student's scores
    for score in all_scores:
        # drop the lowest score by removing it from the list
        score = drop_lowest_score(score)

        # each score is a list, e.g. [80, 99, 72, 58]
        total = sum(score)  # add all scores for this student
        num = len(score)  # get the number of scores for this student
        average_score = round(total / num)  # the average score for this student

        # add this average to the overall total
        student_counter = student_counter + 1  # increment our student counter
        overall_total = overall_total + average_score

    # compute the overall average
    overall_average_score = round(overall_total / student_counter)
    return overall_average_score


def get_average_score(student, quiz_scores):
    """
    Look up a student's average score on quizzes.

    Args:
        student(str): Their name.
        quiz_scores(dict): A dictionary of students, where each value is a list of a student's quiz scores.

    Returns:
        int: The rounded average quiz score for this student.
    """

    # get a list of Heidi's quiz scores
    heidi_quiz_scores = quiz_scores[student]

    # drop the lowest score by removing it from the list
    heidi_quiz_scores = drop_lowest_score(heidi_quiz_scores)

    # alternative way to drop the lowest score in the list
    # get the position of the lowest score in the list
    # position = heidi_quiz_scores.index(lowest_score)
    # remove that value at that position
    # heidi_quiz_scores.pop(position)

    total = sum(heidi_quiz_scores)  # the sum of the values in the list
    num = len(heidi_quiz_scores)  # the number of quiz scores
    average_score = round(total / num)  # a float
    return average_score


def main():
    # make a dictionary with lists as its values
    quiz_scores = {
        "Sheila": [80, 99, 72, 58],
        "Heidi": [99, 97, 99, 50],
        "Jimmy": [12, 22, 99, 99],
        "Johnny": [75, 75, 75, 2],
    }

    # print out a specific student's average score
    student = input("Which student's scores would you like to see? ")
    student_average = get_average_score(student, quiz_scores)
    print(f"The student, {student}, has an average quiz score of {student_average}.")

    # print out the class average score
    class_average = get_class_average(quiz_scores)
    print(f"The class average on all quizzes is {class_average}.")


# run the main function if running this file directly
if __name__ == "__main__":
    main()
