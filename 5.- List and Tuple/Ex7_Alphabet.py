# Remove all the letters are multiple of 3 from the alphabet

print("")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
rest = []

for i in range(len(alphabet),1,-1):
    if i % 3 == 0:
        rest.append(alphabet[i-1])
        alphabet.pop(i-1)

for i in range(len(alphabet)):
    print(alphabet[i],end=", ")
print("\n")

rest.reverse()

for i in range(len(rest)):
    print(rest[i], end=", ")
print("")