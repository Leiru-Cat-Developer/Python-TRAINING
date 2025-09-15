# Ask for products separated by commas and display it in different lines
products = input("Write your products: ")
cart = products.replace(',', '\n')
print(f"\n{cart}\n")