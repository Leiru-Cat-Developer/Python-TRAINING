# Ask the user for a word and write each of the letters

print("")
word = input("Write a word: ")
print("")

for i in range(len(word)-1, -1, -1):
    print(word[i])