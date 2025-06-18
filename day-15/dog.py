"""
A preview of what object-oriented programming looks like.
This file contains a class representing a Dog.
Instances/objects, which represent specific dogs, can be made from this class.
A class itself is a template or blueprint from which objects/instances can be created.
"""


class Dog:
    """
    A class representing a Dog.
    """

    def __init__(self, name, style_instructions):
        """
        This function is called automatically every time a new Dog object is created.
        The 'self' variable always refers to the specific object that this function is being called on.

        Args:
            name (str): The name of the dog.
        """
        self.is_alive = True  # whether this dog is alive or not... start out yet
        self.name = name  # specify a name
        # instructions to follow when generating the dog's messages with openAI
        self.style_instructions = style_instructions

    def bark(self, message="Woof!"):
        """
        Bark a message out!

        Args:
            message (str): The message to bark. Defaults to "Woof!".
        Returns:
            str: The message that was barked.
        """

        if self.is_alive:
            print(f"{self.name} says '{message}'")
        else:
            print(f'{self.name} says "Sorry, I can\'t bark anymore."')
        return message

    def eat(self, other_dog):
        """
        Eat another dog!

        Args:
            other_dog (Dog): The dog to be eaten.

        Returns:
            str: A message indicating the outcome of the eating action.
        """
        message = ""
        if self.is_alive:
            message = f"Yum.... {other_dog.name} is tasty!"
            self.bark(message)
            other_dog.is_alive = False  # the other dog has left us... it's eaten
        else:
            message = f'{self.name} says "Sorry, I\'m not hungry anymore."'

        print(message)
        return message
