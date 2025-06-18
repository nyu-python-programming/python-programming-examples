import format_example
import practice_problem_2
import practice_problem_3
import practice_problem_5
import random


def main():
    """
    Call one of the functions in our other files.
    Which function gets called is pseudo-random.
    """
    num = random.randint(1, 5)  # pseudo-random number between 1-5, inclusive

    print(f"{'':-^30}")  # print separator

    # decide which function to run based on that pseduo-random number
    if num == 1:
        print("Running the main function in format_example...")
        format_example.main()
    elif num == 2:
        print("Running the main function in practice_problem_2...")
        practice_problem_2.main()
    elif num == 3:
        print("Running the main function in practice_problem_3...")
        practice_problem_3.main()
    elif num == 4:
        print("Unlucky number!  Not doing anything ...")
    elif num == 5:
        print("Running the main function in practice_problem_5...")
        practice_problem_5.main()

    print(f"{'':-^30}")  # print separator


# if running this file directly, call the main function
if __name__ == "__main__":
    main()
