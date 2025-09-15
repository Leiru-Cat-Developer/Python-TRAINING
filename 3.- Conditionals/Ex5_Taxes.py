# To pay taxes you need to be 16 years old, and you need
# a 1000 or higher salary per month. Ask for user age and
# month salary and show if the user needs to pay taxes or not
age = int(input("Write your age: "))
salary = float(input("Write your salary: "))

print("You're allowed to pay taxes") if age >= 16 and salary >= 1000 else print("You're not allowed to pay taxes")