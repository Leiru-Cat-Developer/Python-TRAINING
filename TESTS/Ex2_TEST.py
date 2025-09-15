# Create a function that detects an isogram which completes the next rules:
# - Empty array is an isogram
# - If array it's far than one word is False by default
def isIsogram(phrase: str) -> bool:
    # If it's empty
    if phrase == []:
        return True

    # If there's more than a word
    if len(phrase.split(" ")) > 1:
        return False

    wordArray = list(phrase.upper())

    for i in range(len(wordArray)):
        for j in range(len(wordArray)):
            if i == j:
                continue
            elif wordArray[i] == wordArray[j]:
                return False
    return True

phrase = input("\nGive me a word: ")
print("\nIs an Isogram") if isIsogram(phrase) else print("\nIs not an Isogram")