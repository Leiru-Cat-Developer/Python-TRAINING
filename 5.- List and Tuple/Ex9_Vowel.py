# List the quantity vowels of a word

print("")
a = 0
e = 0
i = 0
o = 0
u = 0

word = input("Write a word: ")
word = word.lower()
print("")

for z in range(len(word)):
    if word[z] == 'a': a += 1
    if word[z] == 'e': e += 1
    if word[z] == 'i': i += 1
    if word[z] == 'o': o += 1
    if word[z] == 'u': u += 1
print("")

print("VOWELS QUANTITY\n")
print(f"A: {a}")
print(f"E: {e}")
print(f"I: {i}")
print(f"O: {o}")
print(f"U: {u}")
print("")