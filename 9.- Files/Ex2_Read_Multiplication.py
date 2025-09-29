# Write a function that asks for a number between 1-10 and read the file table-n.txt
# with the multiplication table of that number. "n" is the input number and you need
# to display it on screen. If the file doesn't exists display it too

def find_multiplication(n: int):
    file_name = "table-" + str(n) + ".txt"
    try:
        file = open(file_name,'r')
    except FileNotFoundError:
        print(f"\nThe file with '{file_name}' name doesn't exists . . .")
    else:
        print(f"\n{file.read()}")
        file.close()

n = 0
while n<=0 or n>10:
    n = int(input("\nWrite a number between 1-10: "))

find_multiplication(n)