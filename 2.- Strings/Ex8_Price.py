# Ask for euro price with 2 decimal, and show the euro number and the cents number
price = input("Enter the price in euros: ")
print(f"Price in euros: {price[:-3]}")
print(f"Price in cents: {price[-2:]}")