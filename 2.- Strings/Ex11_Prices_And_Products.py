# Ask for product info, and display the info as follows:
# Unity Price, 6 int digits and 2 decimals
# Unities, 3 int digits
# Total, 8 int digits and 2 decimal
nameProduct = input("Write the product name: ")
priceProduct = float(input("Write the price: $"))
unityProduct = int(input("Write the unities: "))

print(f"\nProduct Name: {nameProduct}",
       f"\nPrice: ${priceProduct:09.2f}", 
       f"\nUnity(ies): {unityProduct:3d}",
       f"\nTotal: ${(priceProduct * unityProduct):011.2f}\n")