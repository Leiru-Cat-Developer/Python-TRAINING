# Write a program to manage a company's outstanding invoices. Invoices will
# be stored in a dictionary where the key for each invoice will be 
# the invoice number and the value will be the invoice cost. The program 
# should prompt the user if they want to add a new invoice, pay an existing one,
# or terminate. If they want to add a new invoice, they will be asked for the 
# invoice number and its cost, and the invoice will be added to the dictionary. 
# If they want to pay an invoice, they will be asked for the invoice number and 
# the invoice will be removed from the dictionary. After each operation, 
# the program should display the amount collected so far and the amount pending 
# collection on the screen.

import os

print("")
invoices = {1575:9000.50}
end_program = 'N'
total_payed = 0.0
os.system('cls')

while end_program == 'N':
    option = 0
    total_pending = 0.0
    print("\t\tINVOICES\n")

    for id, cost in invoices.items():
        print("CODE: " + str(id) + ", PRICE: $" + str(cost))
        total_pending += cost
    
    print("\nTOTAL PENDING: $" + str(total_pending))
    print("TOTAL PAYED: $" + str(total_payed))
    
    print("\nCHOICE AN ACTION:\n")
    print("1.-ADD" + 
          "\n2.-PAY" + 
          "\n3.-END PROGRAM\n")
    option = int(input("-> "))
    print("")

    if option == 1:
        id = int(input("What is the id of the invoice?: "))
        cost = float(input("What is the price of the invoice?: $"))
        invoices[id] = cost
    if option == 2:
        id = int(input("What is the invoice id?: "))
        cost = invoices.pop(id,0)
        total_payed += cost
        total_pending -= cost
    if option == 3:
        end_program = input("Are you sure do you want to leave? [Y/N]: ")
    os.system('cls')