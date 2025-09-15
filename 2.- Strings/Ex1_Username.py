# Ask for the user's name and print it the n times the user specifies
name = input("Enter your username: ")
n = int(input("Enter a number: "))

for i in range(n):
    print(f"{i + 1} - {name}")