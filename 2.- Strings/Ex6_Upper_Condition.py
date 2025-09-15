# Ask for a phrase and a vowel, then print the phrase with the vowel in uppercase.
phrase = input("Enter a phrase: ")
vowel = input("Enter a vowel to uppercase: ")
modified_phrase = phrase.replace(vowel, vowel.upper())
print(modified_phrase)