# Write a function that receives a string and returns a dictionary
# with each word and frequency. Write another function that receives
# the generated dictionary with the last function and returns a
# tuple with the most repeated word and frequency

def generateDictionary(phrase):
    """
        Returns a dictionary with the
        words counted of a phrase
    """
    dictionary = {}
    phrase = phrase.split(" ")
    for i in range(0,len(phrase),1):
        if phrase[i] in dictionary:
            dictionary[phrase[i]] += 1
        else:
            dictionary[phrase[i]] = 1

    return dictionary

def mostFrequentedWord(dictionary):
    """
        Returns a tuple with the most
        repeated word
    """
    major = 0
    for word, repeat in dictionary.items():
        if repeat > major:
            repeated = (word,repeat)
            major = repeat

    return repeated

phrase = input("\nWrite something" +
               "\n\t-> ")

dictionary = generateDictionary(phrase)

print(f"\n {dictionary}")

print(f"\nThe most repeated word is: {mostFrequentedWord(dictionary)}")