# Ask for a word and display if it's a palindrome or not

print("")
original_word = input("Write a phrase: ")
original_word.lower()
print("")

copy_word = original_word

original_word = list(original_word)
copy_word = list(copy_word)

copy_word.reverse()

if original_word == copy_word:
    print("It's a palindrome")
else:
    print("Is not a palindrome")