# Write a function which you assign a string "name" and display
# on screen the greeting "HELLO <name>"

def greeting(name):
    print("Hello " + name)
    return

print("")
name = input("What is your name?: ")
print("")

greeting(name)