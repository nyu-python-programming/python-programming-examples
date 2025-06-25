"""
An example of using dictionaries to store countries and their capital cities
compared with storing the same data as two lists: one for countries and a second for capitals.
"""


def lookup_value_in_dictionary(country):
    """
    Look up a specific value in a Dictionary by using its key.

    Args
        country(str): The country of interest.

    Returns
        str: The capital city of the specified country, if any.  None otherwise.
    """
    capitals = {
        # key: value
        "Russia": "Moscow",
        "Ukraine": "Kyiv",
        "Germany": "Berlin",
        "Greece": "Athens",
        "Kazakhstan": "Astana",
        "Japan": "Tokyo",
        "Morocco": "Rabat",
        "Canada": "Ottowa",
    }

    # retrieve the value associated with a given key from a dictionary
    if country in capitals.keys():
        # country found
        city = capitals[country]  # get the capital city of this country
        return city
    else:
        # no country found
        return None


def lookup_value_in_lists(country):
    """
    Look up a specific value in a list of countries, get its index position,
    and return a value at the same position in another list of capital cities.

    Args
        country(str): The country of interest.

    Returns
        str: The capital city of the specified country, if any.  None otherwise.
    """

    countries = [
        "Russia",
        "Ukraine",
        "Germany",
        "Greece",
        "Kazakhstan",
        "Japan",
        "Morocco",
        "Canada",
    ]

    cities = [
        "Moscow",
        "Kyiv",
        "Berlin",
        "Athens",
        "Astana",
        "Tokyo",
        "Rabat",
        "Ottowa",
    ]

    # validate that the given country is indeed in the list of countries
    if country in countries:
        # found the country
        # get the position of this country in the list of countries
        position = countries.index(country)
        # get the city at the same position in the list of cities
        city = cities[position]
        # return that city value, if it exists, or None otherwise
        return city
    else:
        # no country found
        return None


def main():
    # our country of interest today
    country = input("What country would you like to investigate? ")
    capital = lookup_value_in_dictionary(country)
    if capital != None:
        print(f"The capital of {country} is {capital}!")
    else:
        print(f"Sorry, I don't know what the capital of {country} is!")

    # the same thing, but using lists instead of dictionaries (much more complicated)
    capital = lookup_value_in_lists(country)
    if capital != None:
        print(f"The capital of {country} is {capital}!")
    else:
        print(f"Sorry, I don't know what the capital of {country} is!")


# run the main function if running this file directly
if __name__ == "__main__":
    main()
