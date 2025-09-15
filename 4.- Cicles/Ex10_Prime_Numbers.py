# Ask for a number and show if it's prime or not

print("")
number = int(input("Write a number higher than 2: "))
print("")

for i in range(2,number+1):
    if number % i == 0:
        break

print("Prime") if i == number else print("No Prime")