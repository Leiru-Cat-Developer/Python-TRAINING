# VEGAN PIZZA INGREDIENTS: PEPPER, TOFU
# NON VEGAN PIZZA INGREDIENTS: PEPERONI, HAM, SALMON
# Ask if someone wants a vegan or non vegan pizza,
# show the proper ingredients based on the first choice
# and display the final order at the end

print("")
option = input("Do you want a vegan pizza? [Y/N]: ")
print("")

vegan_pepper = "PEPPER"
vegan_tofu = "TOFU"

normal_peperoni = "PEPERONI"
normal_ham = "HAM"
normal_salmon = "SALMON"

if option == "Y" or option == "y":
    print("Write the ingredient you want: ")
    print("1.- Pepper")
    print("2.- Tofu")
    opt = int(input("-> "))
    if opt == 1:
        print(f"You choice a {vegan_pepper} pizza")
    elif opt == 2:
        print(f"You choice a {vegan_tofu} pizza")
    else:
        print("Try everything again . . .")
elif option == "N" or option == "n":
    print("Write the ingredient you want: ")
    print("1.- Peperoni")
    print("2.- Ham")
    print("3.- Salmon")
    opt = int(input("-> "))
    if opt == 1:
        print(f"You choice a {normal_peperoni} pizza")
    elif opt == 2:
        print(f"You choice a {normal_ham} pizza")
    elif opt == 3:
        print(f"You choice a {normal_salmon} pizza")
    else:
        print("Try everything again . . .")
else:
    print("Try again . . .")