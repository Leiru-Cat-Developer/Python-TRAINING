# Write a program that creates a Spanish-English translation dictionary. 
# The user will enter the Spanish and English words separated by colons, 
# and each <word>:<translation> pair separated by commas. The program should 
# create a dictionary with the words and their translations. It will then ask 
# for a Spanish sentence and use the dictionary to translate it word by word. 
# If a word isn't in the dictionary, it should be left untranslated.

print("")
translate_dictionary = {}

words = input("\nWrite the words you want to translate [word:translation]: ")
print("")

for i in words.split(","):
    id, value = i.split(":")
    translate_dictionary[id] = value

phrase = input("Write a phrase you want to translate: ")
print("\n\n\t\tTRANSLATION\n\n")

for i in phrase.split():
    if i in translate_dictionary:
        print(translate_dictionary[i], end=" ")
    else:
        print(i, end=" ")
print("")