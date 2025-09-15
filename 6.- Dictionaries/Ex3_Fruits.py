# Save some fruits into a dictionary and ask for the fruit and display the
# total price on screen based on kg the user wants, if the fruit doesn't
# exists you need to notify

print("")
fruitDictionary = {'Banana':1.35, 'Apple':0.80, 'Pear':0.85, 'Orange':0.70}

choice = input("Which fruit do you want to buy?: ")
quantity = int(input("How many KG do you want?: "))
print("")

if choice in fruitDictionary:
    print(f"The total for {quantity} KG is: {quantity * fruitDictionary[choice]}")
else:
    print("The fruit doesn't exists")