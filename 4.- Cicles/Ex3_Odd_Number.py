# Ask for an int number and display the odd numbers in the range

print("")
times = 0
while times <= 0:
    times = int(input("Write the range: "))
print("")

for i in range(times):
    if i % 2 != 0:
        print(i,end=", ")
print("")