# Write a function that applies a price discount, another that applies TAX
# Write a third function that receives a dictionary with the prices and
# percentages from a shopping cart, and one of the last functions, and uses
# the last function to apply discounts or TAX to the shopping cart and return
# the final price

def discount(price,percentage):
    """
        Applies a simple discount
            -> price (float)
            -> percentage (float)
    """
    return price - (price * (percentage/100))

def tax(price,percentage):
    """
        Applies a simple tax
            -> price (float)
            -> percentage (float)
    """
    return price + (price * (percentage/100))

def cart(dictionary,function):
    """
        Applies the function to each of the products
            -> dictionary may content:
                - prices
                - percentages
                - function (discount / tax)
    """
    for price, percentage in dictionary.items():
        print(f"-> ${price}, {percentage}%, ${function(price,percentage)} final price")

productsIVA = {100:16,150:16,500:16}
productsDIS = {500.50:30,6580.99:10,3490.53:50}

print("\nThe prices with TAXES are: \n")
cart(productsIVA,tax)
print("\nThe prices with DISCOUNT are: \n")
cart(productsDIS,discount)