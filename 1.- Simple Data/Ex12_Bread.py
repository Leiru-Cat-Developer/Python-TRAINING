# A bakery sells pieces of bread for $3.49 each. The un-fresh bread has a 60% discount. 
# Read the pieces of un-fresh bread sold and display the normal cost, 
# the discount amount for un-fresh bread, and the total cost
discount = 0.60

pieces = int(input("Enter the number of pieces of un-fresh bread sold: "))
total = pieces * 3.49 * (1 - discount)


print("Normal cost: $3.49")
print(f"Discount amount: {discount * 100}%")
print(f"Total cost: ${total:.2f}")