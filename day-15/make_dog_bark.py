"""
An example of using objects in object-oriented programming.
In this case, two Dog objects are created and have a conversation.
We use OpenAI's API to generate the meat of the conversation, using the Python openai module to help.
The results of the conversation are saved into a text file for future reference.

In order to run this code, you will need to install the openai module, with "pip install openai" in your Terminal.

You will also need to have an OpenAI API key, which you can get from the Developer Portal's Dashboard:
https://platform.openai.com/api-keys
"""

from dog import Dog
from openai import OpenAI
import csv
import datetime

# create an OpenAI object from the OpenAI class
client = OpenAI(
    # put your own OpenAI API key here... get one from the Developer Portal's Dashboard.
    # https://platform.openai.com/api-keys
    api_key="your_openai_api_key_here",  # replace with your OpenAI API key
)


def save_to_transcript(csv_writer, from_name, to_name, message):
    """
    Save a message from one dog to another into our transcript data file for future reference.

    Args:
        csv_writer: The CSV writer object to write the message to the file.
        from_name: The name of the dog sending the message.
        to_name: The name of the dog receiving the message.
        message: The message text to save.
    """
    csv_writer.writerow(
        {
            "from": from_name,  # the name of the dog the message is from
            "to": to_name,  # the name of the dog the message is to
            "message": message,  # the message text
            "timestamp": datetime.datetime.now().isoformat(),  # the current time & date
        }
    )


def main():
    # open a file where we will save the dog dialogues.  Open it in write mode.
    f = open("dog_conversation_transcript.csv", mode="w", encoding="utf-8")

    # set up the csv module so we can easily write lines in CSV format to the file later
    writer = csv.DictWriter(f, fieldnames=["from", "to", "message", "timestamp"])
    writer.writeheader()  # write the header line to the file

    # make two Dog "objects" (also known as "instances")... from our custom Dog class
    dog1 = Dog(
        name="Spot",
        style_instructions=f"You are a newly formed object-oriented instance of Dog called Spot responding to another Dog object called Tobik.  You live inside an Intro to Programming program written in Python.  Use old-fashioned boomer jokes, where appropriate. Respond with 1-2 sentences.",
    )

    # make a second dog object
    dog2 = Dog(
        name="Tobik",
        style_instructions=f"You are a newly formed object-oriented instance of Dog called Tobik speaking to another Dog object called Spot.  You believe yourself to be fancy and object-oriented when in fact you are procedural.  Use zoomer slang and saracastic humor, where appropriate. Respond with 1-2 sentences.",
    )  # make another instance/object from the Dog class

    # Spot, the first dog barks
    message = dog1.bark("Hello world!")  # returns the message that was barked
    # save this message to the transcript
    save_to_transcript(writer, dog1.name, "", message)  # from dog1 to the world!

    # Tobik, the second dog barks back
    message = dog2.bark(f"Hey there, {dog1.name}!")
    # save this message to the transcript
    save_to_transcript(writer, dog2.name, dog1.name, message)  # from dog2 to dog1

    # make some random openAI generated dialog between the dogs
    i = 0  # initialize the counter

    # iterate 10 times... until the counter i becomes 10, at which point stop
    while i < 10:

        # generate a response from the first dog to the second dog
        response = client.responses.create(
            model="gpt-4o",
            instructions=dog1.style_instructions,  # use the style instructions from dog1
            input=message,  # the input to respond to is the last message from dog2
        )
        message = response.output_text  # get the response from the OpenAI data
        dog1.bark(message)  # bark it out!
        # save this message to the transcript
        save_to_transcript(writer, dog1.name, dog2.name, message)

        response = client.responses.create(
            model="gpt-4o",
            instructions=dog2.style_instructions,  # use the style instructions from dog1
            input=message,  # the input to respond to is the last message from dog1
        )
        message = response.output_text  # get the response from the OpenAI data
        dog2.bark(message)  # bark it out!
        # save this message to the transcript
        save_to_transcript(writer, dog2.name, dog1.name, message)

        # cause the loop to stop at some point by incrementing i each iteration
        i = i + 1  # increment i

    # it's a dog eat dog world!
    message = dog1.eat(dog2)  # the second dog should no longer be alive after this...
    # save this message to the transcript
    save_to_transcript(writer, dog1.name, dog2.name, message)

    # this should not output the desired message since dog2 is no longer alive
    message = dog2.bark("I'm alive!")  # no, it's not
    # save this message to the transcript, even though dog2 is not alive
    save_to_transcript(writer, dog2.name, dog1.name, message)

    # after completing all writing to a file, you should always close it
    f.close()  # close the file to finalize the data saved

    print("\nDog conversation transcript saved to 'dog_conversation_transcript.csv'.")


if __name__ == "__main__":
    main()
