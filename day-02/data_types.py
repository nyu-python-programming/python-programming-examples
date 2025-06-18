def the_hard_way():
    human_age = input("What is your age?")
    # print(type(human_age)) # debugging to see what data type human_age stores
    human_age = int(human_age)
    # print(type(human_age))
    dog_age = human_age * 7
    message = "Your age in dog years is " + str(dog_age) + "."
    print(message)


def the_easier_way():
    print("Your age in dog years is " + str(int(input("What is your age: ")) * 7) + ".")


the_hard_way()
the_easier_way()
