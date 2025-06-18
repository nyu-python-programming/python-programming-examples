"""
A collection of functions useful for dealing with ordinal suffixes.
Ok.... we actually only have one function... for now.
"""


def generate_ordinal_suffix(i):
    """
    Generates the appropriate ordinal suffix for any integer.

    Args:
        i (int) The number whose ordinal suffix we wish to generate.

    Returns:
        (str) The ordinal suffix for the given integer
    """

    suffix = "th"
    last_character = str(i)[-1]  # slice the last character in the string
    last_two_characters = str(i)[-2:]  # slice the last two characters in the string

    if (
        last_two_characters == "11"
        or last_two_characters == "12"
        or last_two_characters == "13"
    ):
        suffix = "th"
    elif last_character == "1":
        suffix = "st"
    elif last_character == "2":
        suffix = "nd"
    elif last_character == "3":
        suffix = "rd"

    return suffix
