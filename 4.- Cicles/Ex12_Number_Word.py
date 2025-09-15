# Ask for a phrase and a letter, and display the number of letters contained in the phrase

print("")
phrase = input("Write a phrase: ")
letter = input("Write a letter: ")
print("")

lowerCasePhrase = phrase.lower()
lowerCaseLetter = letter.lower()
letterCounter = 0

for i in range(0, len(lowerCasePhrase), 1):
    if lowerCasePhrase[i] == lowerCaseLetter:
        letterCounter += 1

print(f"The number of '{lowerCaseLetter}' letters is: {letterCounter}")