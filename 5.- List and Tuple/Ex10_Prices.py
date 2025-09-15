# Save the next values on an array and display the major one and the minor one

print("")
numbers = [50, 75, 46, 22, 80, 65, 8]

min = 999
max = 0

for i in range(len(numbers)):
    if numbers[i] > max:
        max = numbers[i]
    if numbers[i] < min:
        min = numbers[i]

print(f"\nThe max number is: {max}")
print(f"The min number is: {min}\n")