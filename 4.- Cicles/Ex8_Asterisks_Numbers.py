# Ask for a number "n" and print in console an asterisks pyramid
# centered with no spaces on the left

# Now instead of asterisks, it's going to be numbers

print("")
n = 0
while n <= 0:
    n = int(input("What is the height?: "))
print("")

if n % 2 == 0:
    n -= 1

for i in range(1, n + 1, 2):
    spaces = (n - i) // 2
    print(" " * spaces, end="")

    # Left side
    for j in range(i, 0, -2):
        print(j, end="")

    # Right side
    for j in range(3, i + 1, 2):
        print(j, end="")

    print("")
