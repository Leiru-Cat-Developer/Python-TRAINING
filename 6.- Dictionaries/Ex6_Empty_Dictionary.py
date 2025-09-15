# Write a program that creates an empty dictionary and fills it with
# information about a person (e.g., name, age, sex, phone number, 
# email address, etc.) that the user requests. Each time new 
# information is added, the contents of the dictionary should be printed.

print("")
dictionary = {}
program = 'Y'

while program == 'Y':
    id = input("What information do you want to add?: ")
    value = input(id + " : ")
    dictionary[id] = value
    print(dictionary)
    program = input("Do you want to continue adding? [Y/N]: ")