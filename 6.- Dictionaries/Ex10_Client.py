# Write a program to manage a company's customer database. 
# Customers will be stored in a dictionary where the key for each 
# customer will be their NIF (Tax ID Number), and the value will 
# be another dictionary containing the customer's data 
# (name, address, phone number, email, preferred), 
# where preferred will have the value True if the customer 
# is a preferred customer. The program should prompt the user 
# for an option from the following menu: 
# (1) Add customer
# (2) Delete customer
# (3) Show customer
# (4) List all customers
# (5) List preferred customers
# (6) Finish. 
# Depending on the option chosen, the program will do the following:
# 1.- Request customer data, create a dictionary with the data, and add it to the database.
# 2.- Request the customer's NIF (Tax ID Number) and delete their data from the database.
# 3.- Request the customer's NIF (Tax ID Number) and display their data.
# 4.- Display a list of all customers in the database with their NIF (Tax ID Number) and name.
# 5.- Display the list of preferred customers from the database, along with their ID number and name.
# 6.- Terminate the program.

import os
print("")
os.system("cls")

customer = {12345:{"name":"Uriel",
                   "address":"STREET 6A",
                   "phone":"5533557138",
                   "email":"imagine@gmail.com",
                   "preferred":"S"}}
end_program = 'N'

while end_program == 'N':
    print("\t\tCUSTOMERS\n")

    print("CHOICE AN OPTION: \n" +
           "1.- Add customer\n" +
           "2.- Delete customer\n" +
           "3.- Show customer\n" +
           "4.- List all customers\n" +
           "5.- List preferred customers\n" +
           "6.- Finish\n")
    option = int(input("-> "))
    print("")

    if option == 1:
        nif = int(input("What is the customer's NIF?: "))
        name = input("What is customer's name?: ")
        address = input("What is customer's address?: ")
        phone = input("What is customer's phone number?: ")
        email = input("What is customer's email?: ")
        preferred = input("Is customer preferred [S/N]?: ")
        customer[nif] = {'name':name,
                         'address':address,
                         'phone':phone,
                         'email':email,
                         'preferred':preferred}

    if option == 2:
        nif = int(input("What is the customer nif you want to delete?: "))
        print("")
        if nif in customer:
            del customer[nif]
            print("Customer successfully deleted . . .")
        else:
            print("The customer doesn't exists . . .")

    if option == 3:
        nif = int(input("What is the customer nif you want to search for?: "))
        print("")
        if nif in customer:
            values = customer[nif]
            print("NIF: " + str(nif) 
                + ", NAME: " + values["name"] 
                + ", ADDRESS: " + values["address"] 
                + ", PHONE: " + values["phone"]
                + ", EMAIL: " + values["email"]
                + ", PREFERRED: " + str(values["preferred"]))
        else:
            print("\nThe customer doesn't exists . . .")

    if option == 4:
        for nif, values in customer.items():
            print("NIF: " + str(nif) 
                  + ", NAME: " + values["name"] 
                  + ", ADDRESS: " + values["address"] 
                  + ", PHONE: " + values["phone"]
                  + ", EMAIL: " + values["email"]
                  + ", PREFERRED: " + str(values["preferred"]))

    if option == 5:
        for nif, values in customer.items():
            if values["preferred"] == 'S':
                print("NIF: " + str(nif) 
                    + ", NAME: " + values["name"] 
                    + ", ADDRESS: " + values["address"] 
                    + ", PHONE: " + values["phone"]
                    + ", EMAIL: " + values["email"]
                    + ", PREFERRED: " + values["preferred"] )
    if option == 6:
        end_program = input("Are you sure do you want to leave? [Y/N]: ")

    print("")
    os.system("pause")
    os.system("cls")