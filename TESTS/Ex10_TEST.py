# Your input is a compressed string of the format number[string] and the decompressed output
# form should be the string written number times. For example:
# The input: 3[abc]4[ab]c
# Would be output as: abcabcabcababababc
# Other rules:
# - Numbers can have more than one digit. For example, 10[a] is allowed, and just means: aaaaaaaaaa
# One repetition can occur inside another. For example, 2[3[a]b] decompresses into aaabaaab
# Characters allowed as input include digits, small English letters and brackets [].
# Digits are only to represent the amount of repetitions.
# Letters are just letters.
# Brackets are only part of the syntax of writing repeated substring.
# Input is always valid, so no need to check its validity.

def decompressed(compressed: str) -> str:
    pile = []
    currentString = ""
    currentNumber = 0

    for char in compressed.lower():
        if char.isdigit():
            currentNumber = currentNumber * 10 + int(char)
        elif char == "[":
            pile.append((currentString,currentNumber))
            print(pile)
            currentString = ""
            currentNumber = 0
        elif char == "]":
            p, n = pile.pop()
            print(f"P: {p} current: {currentString} n: {n}")
            currentString = p + currentString * n
            print(f"P: {p} current: {currentString}")
        else:
            currentString += char

    return currentString

string = input("\nWrite a sentence: \n -> ")
print(f"\nThe result is: {decompressed(string)}\n\n")