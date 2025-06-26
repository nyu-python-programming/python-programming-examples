"""
Showing how to do basic CRUD on a dictionary.
Create, Read, Update, Delete.
"""


def main():
    # CREATE

    # create a dictionary
    cat = {"breed": "sphynx", "color": "grey", "age": 14, "name": "susha"}

    # add an item to the dictionary
    cat["sheds"] = False

    # READ

    # read a value from the dictionary by its key
    if cat["sheds"]:
        print(f"{cat['name']} the {cat['breed']} sheds!")
    else:
        print(f"{cat['name']} is a {cat['breed']}, which is not a shedding breed!")

    # read an item that does not exist in the dictionary
    if "num toes" in cat.keys():
        # the key exists in the dictionary
        print(f"{cat['name']} has {cat['num toes']} toes.")
    else:
        # the key does not exist in the dictionary
        print(f"{cat['name']} has an undetermined number of toes.")

    # another way to protect against keys that do not exist in the dictionary
    # get the value if it exists, otherwise use the default
    num_toes = cat.get("num toes", 18)
    print(f"{cat['name']} has {num_toes} toes.")

    # UPDATE

    # update a value in the dictionary
    old_name = cat["name"]  # store the old name for future reference
    cat["name"] = "spot"  # reassign a key to point to a new value
    print(f"{old_name} is now called {cat['name']}.")

    # DELETE

    # delete an item from a dictionary
    cat.pop("age")  # remove the age key/value pair
    # the following will crash the program, since 'age' is no longer a key
    # print(f"{cat['name']} is {cat['age']} years old.")

    # delete item based on its value
    # the .items function returns a list-like data structure containing all the key/value pairs as items
    # each item is represented as a tuple, i.e. (key,value)
    new_cat = {}  # create a new dictionary we will copy items to
    for item in cat.items():
        key = item[0]
        value = item[1]

        # remove the item that has the value 'grey'
        # if value == "grey":
        #     cat.pop(key)  # don't do this!
        # do it this way... copy items to a new dictionary and don't include those you don't want
        if value != "grey":
            new_cat[key] = value
    cat = new_cat  # reassign the variable to point to the new dictionary
    print(
        f"{cat['name']} the {cat['breed']} cat has color {cat.get('color', 'unknown')}"
    )

    # add back a color
    cat["color"] = "pink"

    # an alternative way to remove an item by its value
    key_to_remove = None
    for item in cat.items():
        key = item[0]
        value = item[1]
        # look for a specific value of an item we want to remove
        if value == "pink":
            key_to_remove = key  # remember this key name so we can remove it later
    # now that the loop is over... go and remove an item by this key
    if key_to_remove != None:
        cat.pop(key)  # remove item by key
    print(
        f"{cat['name']} the {cat['breed']} cat has color {cat.get('color', 'unknown')}"
    )


# if running this file direclty, run the main function
if __name__ == "__main__":
    main()
