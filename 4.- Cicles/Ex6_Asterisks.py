# Ask for a number "n" and print in console an asterisks pyramid
# centered with no spaces on the left

print("")
n = 0
while n <= 0:
    n = int(input("What is the pyramid hight?: "))
print("")

space = n - 1
asterisk = 1

for i in range(0,n):
    for j in range(0,space):
        print(" ",end="")
    for k in range(0,asterisk):
        print("*",end="")
    print("")
    space -= 1
    asterisk += 2