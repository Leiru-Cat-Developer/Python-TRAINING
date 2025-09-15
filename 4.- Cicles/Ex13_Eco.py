# Repeat each word introduced til the user type 'Stop'

print("")
words = ""
while words != "Stop":
    words = input("Write: ")
    if words != "Stop":
        print("Eco: " + words)