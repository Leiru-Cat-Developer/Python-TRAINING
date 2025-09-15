# Count from top to behind, but first ask the user for a limit

print("")
number = 0
while number <= 0:
    number = int(input("Write a positive number: "))
print("")

for i in range(number, 0, -1):
    print(i)