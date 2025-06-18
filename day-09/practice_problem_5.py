"""
Write a program that qualfies the user for a particular credit card.
Users must meet the following criteria:
    - Make at least $30,000 per year
    - Their rent payment must not be more than 5% of their total salary per month
    (i.e. 1,500 is the max rent that they can pay while making 30,000 per year)
    - However, if they own their home you do not need to take their monthly house
    payment into account

Here is a sample running of the program:

    Credit card qualifier
    How much do you make per year? 30000
    Do you own your home? (y/n) y
    You qualify!

    Credit card qualifier
    How much do you make per year? 35000
    Do you own your home? (y/n) n
    How much do you pay in rent per month? 1000
    You qualify!

    Credit card qualifier
    How much do you make per year? 50000
    Do you own your home? (y/n) n
    How much do you pay in rent per month? 5000
    Sorry, you don't qualify. Your rent is too high
"""


def main():
    """
    Complete this function so it solves the problem described above.
    """
    # solve the problem here

    # solicit input from the user
    print("Credit card qualifier")
    salary = input("How much do you make per year? ")
    home_owner = input("Do you own your home? (y/n) ")
    if home_owner.lower() == "n":
        monthly_rent = input("How much do you pay in rent per month? ")

        # cleanup the data first before we can do comparisons
        monthly_rent = monthly_rent.replace("$", "")
        monthly_rent = monthly_rent.replace(",", "")

        # remove decimal place to make it easy to compare
        if "." in monthly_rent:
            position = monthly_rent.find(".")
            # get the slices up to but not including the dot
            monthly_rent = monthly_rent[0:position]

    # cleanup the data first before we can do comparisons
    salary = salary.replace("$", "")
    salary = salary.replace(",", "")

    # remove decimal place to make it easy to compare
    if "." in salary:
        position = salary.find(".")
        salary = salary[0:position]  # get the slices up to but not including the dot

    # convert to int... somewhat confidently
    salary = int(salary)

    # determine whether the user qualifies for the credit card or not
    if salary < 30000:
        # too low salary
        print("Sorry, you don't qualify. Your salary is too low.")
    elif home_owner.lower() == "n":
        # they are not homeowners... check their monthly rent
        monthly_salary = salary / 12  # monthly salary computation
        cutoff = monthly_salary * 0.05  # get cutoff for acceptable monthly salary
        if monthly_salary < cutoff:
            print("Sorry, you don't qualify. Your rent is too high")
    else:
        print("You qualify!")


if __name__ == "__main__":
    main()
