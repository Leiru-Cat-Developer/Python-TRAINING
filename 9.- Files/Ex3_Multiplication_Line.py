# Write a function that asks for n and m values, numbers from 1 - 10, the function
# opens the "table-n.txt" file since "n" is a number and "m" search for an
# specific line in the file, if the line doesn't exists you need to display it

def searching(n: int, m: int):
    file_name = "table-" + str(n) + ".txt"
    try:
        with open(file_name,'r') as file:
            lines = file.readlines()
        print(f"\n{lines[m-1]}")
    except:
        print(f"The file with '{file_name}' name and line {m} doesn't exists")

n = 0
m = 0

while (n<=0 or n>10) or (m<=0 or m>10):
    n = int(input("\nWrite a number between 1-10: "))
    m = int(input("Write the line between 1-10: "))

searching(n,m)