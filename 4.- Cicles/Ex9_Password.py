# Save password in a variable and ask the user for the password til is correct

print("")
passwordOriginal = "password123"
passwordTyped = ""

while passwordTyped != passwordOriginal:
    passwordTyped = input("Write the password: ")
    if passwordTyped == passwordOriginal:
        print("\nWelcome . . .\n")