# Write a program that creates a dictionary simulating a shopping cart. 
# The program should ask for the item and its price and add the pair to
# the dictionary until the user decides to finish. The shopping list 
# and the total cost should then be displayed on the screen

print("")
products = {}
total = 0.0

end_program = "Y"

while end_program == "Y":
    item = input("What's the name of the product?: ")
    price = float(input("What is the price of the product " + item + " : $"))
    products[item] = price
    total += price
    end_program = input("\nDo you want to add more products? [Y/N]: ")
    print("")

for item, price in products.items():
    print(item,'\t',"$" + str(price))
print("-------------------------------------")
print("Total = " + "$" + str(total))