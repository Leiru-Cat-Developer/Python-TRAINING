import os

def createFile(file: str) -> str:
    if os.path.isfile(file):
        answer = input("\nThe file already exists, do you want to create it again? [Y/N]: ")
        if answer == 'N' or answer == 'n':
            return "\nThe directory already exists"
    f = open(file,'w')
    f.close()
    return "\nDirectory created successfully"

def searchContact(file: str, contact: str):
    try:
        f = open(file,'r')
    except FileNotFoundError:
        return "\nThe file doesn't exists . . ."
    else:
        lines = f.readlines()
        f.close()
        lines = dict([tuple(i.split(",")) for i in lines])
        if contact in lines:
            return lines[contact]
        else:
            return "\nThe contact doesn't match . . ."

def addContact(file: str, name: str, phone: str):
    try:
        f = open(file,'a')
    except FileNotFoundError:
        return "\nThe file couldn't be opened . . ."
    else:
        f.write(name + "," + phone + "\n")
        f.close()
        return "\nContact added successfully"

def delContact(file: str, contact: str):
    try:
        f = open(file,'r')
    except FileNotFoundError:
        return "\nThe file doesn't exists . . ."
    else:
        lines = f.readlines()
        f.close()
        lines = dict([tuple(i.split(",")) for i in lines])
        if contact in lines:
            del lines[contact]
            f = open(file,'w')
            for n, p in lines.items():
                f.write(n + "," + p)
            f.close()
            return "\nThe contact was deleted successfully"
        else:
            return "\nThe contact doesn't match . . ."

file = "list.txt"
os.system('cls')

while True:
    print("Choose an option:\n\n" +
          "1.- Create file\n"+
          "2.- Search contact\n"+
          "3.- Add contact\n"+
          "4.- Del contact\n"+
          "5.- Exit\n")
    option = int(input("-> "))

    if option == 1:
        print(createFile(file))
    elif option == 2:
        contact = input("\nWrite the contact name you are searching for: ")
        print(f"\n{searchContact(file,contact)}")
    elif option == 3:
        name = input("\nWrite contact's name: ")
        phone = input("Write phone contact's name: ")
        print(addContact(file,name,phone))
    elif option == 4:
        contact = input("\nWrite the contact name you want to delete: ")
        print(delContact(file,contact))
    else:
        print("\nLeaving . . .")
        break

    input("\nPress a key to continue . . .")
    os.system('cls')
