# Ask for age clients, depends the age is the condition you need to apply:
# 4 years old = don't pay
# between 4 and 18 years old = pay $5
# 18 and over = $10

print("")
age = int(input("What is your age?: "))
print("")

if age >= 0 and age <= 4:
    print("You don't pay")
elif age < 18:
    print("You pay $5")
elif age >= 18:
    print("You pay $10")
else:
    print("Sorry, try again . . .")