# Check if a password is correct or not, in lower case
key = "password"

password = input("Write the password: ")

if password.lower() == key: 
    print("\nPass\n")
else:
    print("\nBlocked\n")