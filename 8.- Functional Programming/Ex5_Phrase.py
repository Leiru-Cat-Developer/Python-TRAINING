# Write a function that receives a phrase and returns a dictionary
# with the words and the longitude

def frequency(phrase):
    """
        Receives a phrase and returns a dictionary
            -> phrase (string)
    """
    dictionary = {}
    phrase = phrase.split(" ")

    for i in range(len(phrase)):
        dictionary[phrase[i]] = len(phrase[i])

    return dictionary

phrase = input("\nWrite a phrase\n\t -> ")

print(f"\nResult: {frequency(phrase)}")