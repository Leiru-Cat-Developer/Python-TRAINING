# Write a program, ask the user name, age, direction and phone, and save it into a dictionary
# After, you show on screen the message:
# <NAME> is <AGE> years old, live in <DIRECTION> and the phone number is <PHONE>

print("")
name = input("What is your name?: ")
age = int(input("How old are you?: "))
direction = input("What is your address?: ")
phone = int(input("What is your phone?: "))
print("")

userDictionary = {'Name':name, 'Age':age, 'Direction':direction, 'Phone':phone}

print(userDictionary["Name"],
      "is",userDictionary["Age"], 
      "years old, live in",
      userDictionary["Direction"],
      "and the phone number is",
      userDictionary["Phone"])