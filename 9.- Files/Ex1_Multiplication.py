# Write a function that asks for an int number between 1 - 10 and save the
# multiplication table into a file called "table-n.txt" sine "n" is
# the input value

def multiplication(n: int):
    file_name = "table-" + str(n) + ".txt"
    file = open(file_name,'w')
    for i in range(10):
        file.write(str(i+1) + " * " + str(n) + " = " + str((i+1) * n) + "\n")
    file.close()
    print(f"Watch the file: {file_name}, to see the results . . .")

n = 0
while n<=0 or n>10:
    n = int(input("\nWrite a number between 1 - 10: "))

print("")
multiplication(n)